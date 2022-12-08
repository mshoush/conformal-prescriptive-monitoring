import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from DatasetManager import DatasetManager

class conformal_prediction:

    def __init__(self, prediction_cal, prediction_test, y_true_cal, y_true_test, alpha):

        self.prediction_cal = prediction_cal
        self.prediction_test = prediction_test
        self.y_true_cal = y_true_cal
        self.y_true_test = y_true_test
        self.alpha = alpha
        pass
        # self.alpha=alpha

    ############################Naive method#####################################

    # compute q-hat based on the Inverse probability nonconformity score
    def get_qhat_naive(self, alpha):
        self.alpha = alpha

        """Inverse probability nonconformity score returns :math:`1 - p`, where :math:`p` is the probability
    assigned to the actual class by the underlying classification model (:py:attr:`ClassModelNC.model`)."""
        #         self.predictions_cal=predictions_cal
        #         self.y_cal=y_cal
        #         self.alpha=alpha
        N = self.prediction_cal.shape[0]
        scores = np.zeros(N)  # non-conformity scores

        for i in range(N):
            true_class_proba = self.prediction_cal[i][
                self.y_true_cal[i]]  # predicted proba of the true class, y_cal[i]: to get the true class
            # InverseProbabilityErrFunc - non-conformity scores
            scores[i] = 1 - true_class_proba  # probs of the opposite class, s1, s2, .., sn

        q_yhat = np.quantile(scores, np.ceil((N + 1) * (1 - self.alpha)) / N)  # quantile of the non-conformity scores
        return q_yhat

    # function to get predict sets: Naive method
    def get_pred_set_naive(self, q_yhat):
        self.q_yhat = q_yhat
        #         self.predictions_test=predictions_test
        #         self.y_test=y_test
        # self.model=model

        softmax_outputs = self.prediction_test  # probs for test set
        N = softmax_outputs.shape[0]  # how many rows in the test set

        pred_sets = []  # pred set

        for i in range(N):  # for each row
            aux = []
            for j in range(softmax_outputs.shape[1]):  # loop over the number of classes
                if softmax_outputs[i][j] >= 1 - self.q_yhat:  # pred_proba[class_0 | 1] >
                    aux.append(j)
            pred_sets.append(aux)

        return pred_sets
        ############################Naive method#####################################

    ############################Adaptive method#####################################

    # alpha=0.1
    # y_pred = model.predict(X_cal)
    # y_classes = [np.argmax(element) for element in y_pred]
    # N=X_cal.shape[0]

    def get_ind(self, y_pred_i, y_test_i):
        self.y_pred_i = y_pred_i
        self.y_test_i = y_test_i
        return np.where(np.sort(self.y_pred_i)[::-1] == self.y_pred_i[self.y_test_i])[0][0]

    def get_qhat_adaptive(self, alpha):
        #         self.prediction_cal = prediction_cal
        #         self.y_cal = y_cal
        self.alpha = alpha

        y_pred = self.prediction_cal
        sums_density = []
        N = self.y_true_cal.shape[0]

        for i in range(N):
            sum_density = 0
            ind = self.get_ind(y_pred[i], self.y_true_cal[i])
            sums_density.append(np.sum(np.sort(y_pred[i])[::-1][0:ind + 1]))

        q_yhat = np.quantile(sums_density, np.ceil((N + 1) * (1 - self.alpha)) / N)

        return q_yhat

    def get_pred_set_adaptive(self, q_yhat):
        self.q_yhat = q_yhat
        y_pred = self.prediction_test

        conf_sets = []

        for i in range(y_pred.shape[0]):
            #             print(y_pred[i])
            #             print(np.where(np.cumsum(np.sort(y_pred[i])[::-1])>self.q_yhat)[0])
            a = np.where(np.cumsum(np.sort(y_pred[i])[::-1]) > self.q_yhat)[0][0]

            classes = []

            for j in range(a + 1):
                ind = np.where(y_pred == np.sort(y_pred[i])[::-1][j])[1][0]
                classes.append(ind)

            conf_sets.append(classes)

        return conf_sets

    ############################Adaptive method#####################################

    ############################Class_balanced method############################################

    def get_qhat_crossBalance(self, alpha):

        self.alpha = alpha

        y_pred = self.prediction_cal
        # N=self.X_cal.shape[0]
        N = self.y_true_cal.shape[0]
        d_alpha = {}
        d_alpha_q_yhats = {}
        conf_pred = []

        for i in range(N):
            real_class = self.y_true_cal[i]
            prob = 1 - y_pred[i][real_class]

            if real_class not in d_alpha:
                d_alpha[real_class] = [prob]
            else:
                d_alpha[real_class].append(prob)

        for i, (k, v) in enumerate(d_alpha.items()):
            N = len(v)
            d_alpha_q_yhats[k] = np.quantile(v, np.ceil((N + 1) * (1 - alpha)) / N)

        return d_alpha_q_yhats

    def get_pred_set_crossBalance(self, d_alpha_q_yhats):
        #         self.prediction_test = prediction_test
        self.d_alpha_q_yhats = d_alpha_q_yhats

        conf_sets = []
        y_pred = self.prediction_test  # model.predict(X_val)

        for i in range(y_pred.shape[0]):
            conf = []
            for j in range(y_pred.shape[1]):
                if 1 - y_pred[i][j] < self.d_alpha_q_yhats[j]:
                    conf.append(j)
            conf_sets.append(conf)

        return conf_sets

    ##############################Class_balanced method##########################################

    def get_pred_set_size(self, alpha, pred_sets):
        self.alpha = alpha
        self.pred_sets = pred_sets

        my_dict = {}
        my_dict_alpha = {}
        import pandas as pd

        for a in self.alpha:
            my_dict = {}
            print(f"Alpha: {a}")
            for i in range(len(pd.Series(self.pred_sets[a]).value_counts().index[:].to_list())):
                # print(i)
                my_dict[str(pd.Series(self.pred_sets[a]).value_counts().index[:].to_list()[i])] = \
                pd.Series(self.pred_sets[a]).value_counts().to_list()[i]
                # break
            my_dict_alpha[a] = my_dict
        return my_dict_alpha

    # function to evaluate coverage
    def calculate_coverage(self, pred_sets, y_true):
        s = 0

        for i in range(len(pred_sets)):
            if y_true[i] in pred_sets[i]:
                s += 1

        return s / len(y_true)

    def plot_pred_sets(self, alpha, pred_sets_size):
        # creating the dataset
        # data = data
        pred_set = list(pred_sets_size.keys())
        values = list(pred_sets_size.values())

        colors = {"#1f77b4", "#ff7f0e", "#2ca02c", }
        fig, ax = plt.subplots()

        # creating the bar plot
        ax.bar(pred_set, values, color=colors,
               width=0.4)

        for bar in ax.patches:
            ax.annotate(text=bar.get_height(),
                        xy=(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2),
                        ha='center',
                        va='center',
                        size=15,
                        xytext=(0, 8),
                        textcoords='offset points')

        # plt.axhline(y=0.9, color='r', linestyle='--')
        plt.xlabel("Prediction sets")
        plt.ylabel(f"No. of instances")
        plt.title(f"Cases in different prediction sets: alpha={alpha}")
        plt.grid()
        plt.tight_layout()
        plt.show()

    def plot_covarage(self, alpha, pred_sets, y_test):
        self.alpha = alpha
        self.pred_sets = pred_sets
        self.y_test = y_test
        colors = {"#1f77b4", "#ff7f0e", "#2ca02c", }

        for a in self.alpha:

            d1 = np.zeros(10)
            d2 = np.zeros(10)

            for i in range(len(self.pred_sets[a])):
                d2[y_test[i]] += 1

                if y_test[i] in self.pred_sets[a][i]:
                    d1[y_test[i]] += 1

            plt.bar([i for i in range(10)], d1 / d2, color=colors)
            plt.axhline(y=0.9, color='r', linestyle='--')
            plt.title(f'Naive method coverage: {a}')
            # plt.legend()
            plt.xlabel('Class')
            plt.ylabel('Coverage')
            plt.grid()
            plt.tight_layout()
            plt.show()
            plt.show()

def main(dataset_name, pred_test, pred_train, pred_cal, dt_test_prefixes, dataset_manager):
    

    def split_data_strict(data, train_ratio, split="temporal"):
        timestamp_col= "timestamp"
        activity_col = "activity"
        case_id_col = "case_id"
        sorting_cols = [timestamp_col, activity_col]
        # split into train and test using temporal split and discard events that overlap the periods
        data = data.sort_values(sorting_cols, ascending=True, kind='mergesort')
        grouped = data.groupby(case_id_col)
        start_timestamps = grouped[timestamp_col].min().reset_index()
        start_timestamps = start_timestamps.sort_values(timestamp_col, ascending=True, kind='mergesort')
        train_ids = list(start_timestamps[case_id_col])[:int(train_ratio*len(start_timestamps))]
        train = data[data[case_id_col].isin(train_ids)].sort_values(sorting_cols, ascending=True, kind='mergesort')
        test = data[~data[case_id_col].isin(train_ids)].sort_values(sorting_cols, ascending=True, kind='mergesort')
        split_ts = test[timestamp_col].min()
        train = train[train[timestamp_col] < split_ts]
        return (train, test)


    y_test = np.array([pred_test['actual']])[0]
    prediction_test = np.column_stack((pred_test['predicted_proba_0'], pred_test['predicted_proba_1']))
    print(f"length of y: {len(y_test)}, and prediction shape: {prediction_test.shape}")

    y_train = np.array([pred_train['actual']])[0]
    prediction_train = np.column_stack((pred_train['predicted_proba_0'], pred_train['predicted_proba_1']))
    print(f"length of y: {len(y_train)}, and prediction shape: {prediction_train.shape}")

    y_cal = np.array([pred_cal['actual']])[0]
    prediction_cal = np.column_stack((pred_cal['predicted_proba_0'], pred_cal['predicted_proba_1']))
    print(f"length of y: {len(y_cal)}, and prediction shape: {prediction_cal.shape}")

    # conformal prediction object
    alpha = np.round(np.arange(0.1, 1.0, 0.1), 1)

    #  prediction_cal, X_cal, y_cal, alpha
    cp = conformal_prediction(prediction_cal=prediction_cal,
                              prediction_test=prediction_test,
                              y_true_cal=y_cal,
                              y_true_test=y_test,
                              alpha=alpha)

    # Naive
    qhat_naive = {a: cp.get_qhat_naive(a) for a in alpha}  # {alhp: q_hat}
    pred_sets_naive = {alpha: cp.get_pred_set_naive(qhat) for alpha, qhat in qhat_naive.items()}
    pred_sets_size_naive = cp.get_pred_set_size(alpha, pred_sets_naive)


    # classbalance
    qhat_classBalance = {a: cp.get_qhat_crossBalance(a) for a in alpha}  # {alhp: q_hat}
    pred_sets_classBalance = {alpha: cp.get_pred_set_crossBalance(qhat) for alpha, qhat in qhat_classBalance.items()}
    pred_sets_size_classBalance = cp.get_pred_set_size(alpha, pred_sets_classBalance)


    # Adaptive
    qhat_adaptive ={}
    qhat_adaptive_old = {a: cp.get_qhat_adaptive(a) for a in alpha}  # {alhp: q_hat}
    [qhat_adaptive_old[alpha] if np.round(qhat, 2) == 1.0 else qhat_adaptive.update({alpha: qhat}) for alpha, qhat in
     qhat_adaptive_old.items()]
    # Get pred sets
    pred_sets_adaptive = {alpha: cp.get_pred_set_adaptive(qhat) for alpha, qhat in qhat_adaptive.items()}
    pred_sets_size_adaptive = cp.get_pred_set_size(list(pred_sets_adaptive.keys()), pred_sets_adaptive)
    #pred_sets_size_adaptive = {alpha: cp.get_pred_set_size(alph, pred_sets_adaptive) for alpha, qhat in qhat_adaptive.items()}
    #cp.get_pred_set_size(alph, pred_sets_adaptive)

    df_test_result = pred_test
    # Predictive part
    df_test_result["prefix_nr"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).first()["prefix_nr"])
    df_test_result["case_id"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).first()["orig_case_id"])
    df_test_result["activity"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).last()["Activity"])
    df_test_result["timestamp"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).last()[dataset_manager.timestamp_col])
    df_test_result = df_test_result.sort_values(by=["timestamp"]).reset_index(drop=True)

    def get_df_with_pred_sets(df, alpha, pred_set):
        df = df.copy(deep=True)
        for a in alpha:
            #print(a)
            df["alpha=" + str(a)] = pred_set[a]
        return df

    print("Naive")
    df_naive = get_df_with_pred_sets(df_test_result, list(pred_sets_naive.keys()), pred_sets_naive)

    print("class")
    df_class = get_df_with_pred_sets(df_test_result, list(pred_sets_classBalance.keys()), pred_sets_classBalance)

    print("Adaptive")
    df_adaptive = get_df_with_pred_sets(df_test_result, list(pred_sets_adaptive.keys()), pred_sets_adaptive)
    
    print("Read ORF DATA...")
    if dataset_name=="bpic2012":
        orf_data = pd.read_csv('./results_orf/bpic2012/bpic2012_df_results_orf_test_new2.csv', sep=';')
    else:
        orf_data = pd.read_csv(
            './results_orf/bpic2017/bpic2017_df_results_orf_test_new2.csv',
            sep=';')
    # Predictive part
    orf_data["prefix_nr"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).first()["prefix_nr"])
    orf_data["case_id"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).first()["orig_case_id"])
    orf_data["activity"] = list(dt_test_prefixes.groupby(dataset_manager.case_id_col).last()["Activity"])
    orf_data["timestamp"] = list(
        dt_test_prefixes.groupby(dataset_manager.case_id_col).last()[dataset_manager.timestamp_col])
    orf_data = orf_data.sort_values(by=["timestamp"]).reset_index(drop=True)
    orf_data.rename(columns={'Treatment Effects': 'CATE'}, inplace=True)
    try:
         orf_data = orf_data[['Outcome', 'te_lower', 'te_upper', 'Interval Length','NumberOfOffers','prefix_nr', 'case_id', 'CATE', 'Treatment', 'activity', 'timestamp']]
    except:
        orf_data = orf_data[['Outcome', 'NumberOfOffers','prefix_nr', 'case_id', 'CATE', 'Treatment', 'activity', 'timestamp']]
    cols_to_use = df_naive.columns.difference(orf_data.columns)
    #df_final_adaptive = pd.merge(orf_data, df_adaptive[cols_to_use], left_index=True, right_index=True,
    #                             how='outer')
    df_final_crossBalanced = pd.merge(orf_data, df_class[cols_to_use], left_index=True,
                                      right_index=True, how='outer')
    df_final_naive = pd.merge(orf_data, df_naive[cols_to_use], left_index=True, right_index=True,
                              how='outer')
    
    #print(cols_to_use)
    cols_to_use = ['actual','confidence', 'data_uncer', 'knowledge_uncer', 'predicted',
                                 'predicted_proba_0', 'predicted_proba_1', 'total_uncer'] + ["alpha=%s"%str(a) for a in list(pred_sets_adaptive.keys())]
    #print(cols_to_use)
    df_final_adaptive = pd.merge(orf_data, df_adaptive[cols_to_use], left_index=True, right_index=True, how='outer')

    if dataset_name=="bpic2017":
        train_adaptive, df_final_adaptive = split_data_strict(df_final_adaptive, 0.84)
        train_class, df_final_crossBalanced = split_data_strict(df_final_crossBalanced, 0.84)
        train_naive, df_final_naive = split_data_strict(df_final_naive, 0.84)
    

    result_df_naive = pd.DataFrame(pred_sets_size_naive).reset_index()
    result_df_naive.name = "Naive"

    result_df_class= pd.DataFrame(pred_sets_size_classBalance).reset_index()
    result_df_class.name = "classBalance"

    result_df_adaptive= pd.DataFrame(pred_sets_size_adaptive).reset_index()
    result_df_adaptive.name = "Adaptive"

    all_df = pd.DataFrame()
    all_df = pd.DataFrame()
    all_df = all_df.append(result_df_naive.loc[result_df_naive['index']=='[1]'])
    all_df = all_df.append(result_df_class.loc[result_df_class['index']=='[1]'])
    all_df = all_df.append(result_df_adaptive.loc[result_df_adaptive['index']=='[1]'])
    #all_df['index'] = ["Naive", "ClassBalance", "Adaptive"]
    #all_df = all_df.reset_index(drop=True)
    all_df['index'] = ["Naive", "Outcome-balanced", "Adaptive"]
    all_df = all_df.reset_index(drop=True)



    return df_final_naive, df_final_crossBalanced, df_final_adaptive, all_df

    #return df_naive, df_class, df_adaptive

    #pass


    #pass

import os
from sys import argv

if __name__ == "__main__":
    dataset = argv[1]
    datasets = [dataset]#["bpic2012","bpic2017"]
    results_pred = "results_pred"
    results_conformal = "results_conformal" + "/" + dataset + "/"

    
    # create results directory
    if not os.path.exists(os.path.join(results_conformal)):
        os.makedirs(os.path.join(results_conformal))



    for dataset_name in datasets:
        #print(f"Start with: {dataset_name}")
        dataset_manager = DatasetManager(dataset_name)
        print(f"start with: {dataset_name}...")
        test_file = "preds_test_%s.csv" % dataset_name
        train_file = "preds_train_%s.csv" % dataset_name
        cal_file = "preds_val_%s.csv" % dataset_name
        # test prefixes pkl
        test_pfx_pkl_file = "%s_dt_test_prefixes.pkl"% dataset_name

        print(results_pred)
        pred_test = pd.read_csv(os.path.join(results_pred, dataset_name, test_file), sep=';')
        pred_train = pd.read_csv(os.path.join(results_pred, dataset_name, train_file), sep=';')
        pred_cal = pd.read_csv(os.path.join(results_pred, dataset_name, cal_file), sep=';')

        with open(os.path.join(results_pred, dataset_name, test_pfx_pkl_file), "rb") as fh:
            dt_test_prefixes = pickle.load(fh)
        df_naive, df_classbalanced, df_adaptive, all_df = main(dataset_name, pred_test, pred_train, pred_cal, dt_test_prefixes, dataset_manager)

        if dataset_name =="bpic2017":
            print("bpic17")

        df_naive.to_csv(os.path.join(results_conformal, "df_final_naive_all.csv"), sep=";", index=False)
        df_classbalanced.to_csv(os.path.join(results_conformal, "df_final_classBalanced_all.csv"), sep=";", index=False)
        df_adaptive.to_csv(os.path.join(results_conformal,  "df_final_adaptive_all.csv"), sep=";", index=False)
        all_df.to_csv(os.path.join(results_conformal,  "all_df.csv"), sep=";", index=False)
        print(f"Done with: {dataset_name}...\n")

