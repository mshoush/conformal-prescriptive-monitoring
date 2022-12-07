import os

case_id_col = {}
activity_col = {}
resource_col = {}
timestamp_col = {}
label_col = {}
treatment_col = {}
pos_treatment = {}
neg_treatment = {}

pos_label = {}
neg_label = {}
dynamic_cat_cols = {}
static_cat_cols = {}
dynamic_num_cols = {}
static_num_cols = {}
filename = {}


logs_dir = "./prepared_data/"
# /home/mshoush/Desktop/uncertainity/uncer_2/CatBoost_uncer/data"
#logs_dir = "~/phd/code/Mahmoud_PrescriptiveProcessMonitoring/prepared_data"

#### BPIC2017 settings ####
#TODO change file name for pickle
bpic2017_dict = {"bpic2017": "prepared_treatment_outcome_bpic2017.csv"}

for dataset, fname in bpic2017_dict.items():
    filename[dataset] = os.path.join(logs_dir, fname)
    # min cols
    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = 'org:resource'
    timestamp_col[dataset] = 'time:timestamp'
    # label/outcome col
    label_col[dataset] = "label"
    neg_label[dataset] = "regular"  # negative outcome that we don't need to predict
    pos_label[dataset] = "deviant"  # positive outcome that will be predicted
    # treatment col
    treatment_col[dataset] = 'treatment'
    pos_treatment[dataset] = "treat"  # do treatment
    neg_treatment[dataset] = "noTreat"  # do not treat

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", 'org:resource', 'Action', 'EventOrigin', 'lifecycle:transition', "Accepted", "Selected"]
    static_cat_cols[dataset] = ['ApplicationType', 'LoanGoal']  #static attributes, no need for predicting in suffix predictions
    dynamic_num_cols[dataset] = ['FirstWithdrawalAmount', 'MonthlyCost', 'NumberOfTerms', 'OfferedAmount', 'CreditScore', "timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour","open_cases"]
    static_num_cols[dataset] = ['NumberOfOffers' ,'RequestedAmount',] #static attributes, no need for predicting in suffix predictions

    #cat_feat = ["Activity", 'org:resource', 'Action', 'EventOrigin', 'lifecycle:transition', "Accepted", "Selected", 'ApplicationType', 'LoanGoal']i


bpic2012_dict = {"bpic2012": "prepared_treatment_outcome_bpic2012.csv"}
#BPI012
for dataset, fname in bpic2012_dict.items():
    #logs_dir = "./data/" + dataset + "/"
    filename[dataset] = os.path.join(logs_dir, fname)
    #print(f"filename: {filename}")
    # min cols
    case_id_col[dataset] = "Case ID"
    activity_col[dataset] = "Activity"
    resource_col[dataset] = 'Resource'
    timestamp_col[dataset] = 'start_time'
    # label/outcome col
    label_col[dataset] = "label"
    neg_label[dataset] = "regular"  # negative outcome that we don't need to predict
    pos_label[dataset] = "deviant"  # positive outcome that will be predicted
    # treatment col
    treatment_col[dataset] = 'treatment'
    pos_treatment[dataset] = "treat"  # do treatment
    neg_treatment[dataset] = "noTreat"  # do not treat

    # features for classifier
    dynamic_cat_cols[dataset] = ["Activity", 'Resource',] #'Action', 'EventOrigin', 'lifecycle:transition', "Accepted", "Selected"]
    static_cat_cols[dataset] = []  #static attributes, no need for predicting in suffix predictions
    dynamic_num_cols[dataset] = ["timesincelastevent", "timesincecasestart", "timesincemidnight", "event_nr", "month", "weekday", "hour","open_cases"]
    static_num_cols[dataset] = ['NumberOfOffers', "AMOUNT_REQ",] #static attributes, no need for predicting in suffix predictions

