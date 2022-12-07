import pandas as pd
import numpy as np
from DatasetManager import DatasetManager

case_id_col = "Case ID"
activity_col = "Activity"
resource_col = "Resource"
timestamp_col = "start_time"
label_col = "label"
pos_label = "deviant"  # positive outcome that will be predicted
neg_label = "regular"  # negative outcome that we don't need to predict

dynamic_cat_cols = ["Activity",
                    'Resource', ]  # 'Action', 'EventOrigin', 'lifecycle:transition', "Accepted", "Selected"]
static_cat_cols = []  # static attributes, no need for predicting in suffix predictions
dynamic_num_cols = ["timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday",
                    "hour", "open_cases"]
static_num_cols = ['NumberOfOffers', "AMOUNT_REQ", ]

static_cols = static_cat_cols + static_num_cols + [case_id_col, label_col]
dynamic_cols = dynamic_cat_cols + dynamic_num_cols + [timestamp_col]
cat_cols = dynamic_cat_cols + static_cat_cols
freq_threshold = 10

import numpy as np


def extract_timestamp_features(group):
    group[timestamp_col] = pd.to_datetime(group[timestamp_col])

    group = group.sort_values(timestamp_col, ascending=False, kind='mergesort')

    tmp = group[timestamp_col] - group[timestamp_col].shift(-1)
    tmp = tmp.fillna(pd.Timedelta(seconds=0))
    group["timesincelastevent"] = tmp.apply(lambda x: float(x / np.timedelta64(1, 'm')))  # m is for minutes

    tmp = group[timestamp_col] - group[timestamp_col].iloc[-1]
    tmp = tmp.fillna(pd.Timedelta(seconds=0))
    group["timesincecasestart"] = tmp.apply(lambda x: float(x / np.timedelta64(1, 'm')))  # m is for minutes

    group = group.sort_values(timestamp_col, ascending=True, kind='mergesort')
    group["event_nr"] = range(1, len(group) + 1)

    return group


def get_open_cases(date, dt_first_last_timestamps):
    return sum((dt_first_last_timestamps["start_time"] <= date) & (dt_first_last_timestamps["end_time"] > date))


def add_label(df):
    # function to cheack if a case contains A_Pending activity or not
    def check_A_Pending(gr):
        df = pd.DataFrame(gr)
        if ' A_APPROVED' in list(df[activity_col]):
            df['label'] = neg_label
        else:
            df['label'] = pos_label
        return df

    # read data and del old label
    # df = file

    # add new label for each case based on A_Pending
    df = df.groupby(case_id_col).apply(check_A_Pending)
    df = df.reset_index(drop=True)
    return df


# fn to add #offers column to the original data based on "O_Created" Activity
def add_No_Of_Offers(df):
    # get all observations with O_Created activity
    tmp_df = df[df[activity_col] == ' O_CREATED']  # to count offers

    # count numbe rof offers for each case
    tmp_df2 = pd.DataFrame(tmp_df.groupby([case_id_col])[activity_col].count()).reset_index()
    tmp_df2.columns = [case_id_col, 'NumberOfOffers']
    df = pd.merge(tmp_df2, df, on=case_id_col)
    return df


# function to add treatment based on the number of offers
def add_treatment(df):
    # function to cheack if a case contains A_Pending activity or not
    def check_NoOfOffers(gr):
        df = pd.DataFrame(gr)

        # case should be not treated if it receives more than one offer
        if list(df['NumberOfOffers'])[0] <= 1:
            df['treatment'] = "treat"  # T=1 pos_treatment
        else:
            df['treatment'] = "noTreat"  # T=0 neg_treatment
        return df

    # add new treatment for each case based on number of offers
    # cases with only one offer should be treated
    df = df.groupby(case_id_col).apply(check_NoOfOffers)
    df = df.reset_index(drop=True)
    return df


def main(file):
    data = file  # pd.read_csv(file, sep=',', compression='gzip')

    data[timestamp_col] = pd.to_datetime(data[timestamp_col])
    data[resource_col] = data.sort_values(timestamp_col, ascending=True).groupby(case_id_col)[resource_col].transform(
        lambda grp: grp.fillna(method='ffill'))
    data.rename(columns=lambda x: x.replace('(case) ', ''), inplace=True)

    # add event duration
    data[timestamp_col] = pd.to_datetime(data[timestamp_col])
    data["timesincemidnight"] = data[timestamp_col].dt.hour * 60 + data[timestamp_col].dt.minute
    data["month"] = data[timestamp_col].dt.month
    data["weekday"] = data[timestamp_col].dt.weekday
    data["hour"] = data[timestamp_col].dt.hour

    print("Extracting timestamp features...")
    data = data.groupby(case_id_col).apply(extract_timestamp_features)

    print("Extracting open cases...")
    data = data.sort_values([timestamp_col], ascending=True, kind='mergesort').reset_index(drop = True)
    dt_first_last_timestamps = data.groupby(case_id_col)[timestamp_col].agg([min, max])
    dt_first_last_timestamps.columns = ["start_time", "end_time"]
    data["open_cases"] = data[timestamp_col].apply(lambda x: get_open_cases(x, dt_first_last_timestamps))
    print("Add labels...")
    data = add_label(data)

    print("Add No of Offers...")
    data = add_No_Of_Offers(data)

    print("Add Treatment...")
    data = add_treatment(data)

    # impute missing values
    print("impute missing values...")
    grouped = data.sort_values(timestamp_col, ascending=True, kind='mergesort').groupby(case_id_col)
    for col in static_cols + dynamic_cols:
        data[col] = grouped[col].transform(lambda grp: grp.fillna(method='ffill'))

    data[cat_cols] = data[cat_cols].fillna('missing')
    data = data.fillna(0)

    # set infrequent factor levels to "other"
    for col in cat_cols:
        counts = data[col].value_counts()
        mask = data[col].isin(counts[counts >= freq_threshold].index)
        data.loc[~mask, col] = "other"
    return data


if __name__ == "__main__":
    datasets = ["bpic2012"]
    for dataset_name in datasets:
        #dataset_manager = DatasetManager(dataset_name)
        #data = dataset_manager.read_dataset()
        data = pd.read_csv("./data/bpic2012/bpic2012.csv", sep=',')
        df = main(data)
        del df['end_time']
        print("Saving csv file...")
        results_dir = "prepared_data"
        import os
        if not os.path.exists(os.path.join(results_dir)):
            os.makedirs(os.path.join(results_dir))
        df.to_csv(results_dir + '/prepared_treatment_outcome_bpic2012.csv', index=False, sep=';')

