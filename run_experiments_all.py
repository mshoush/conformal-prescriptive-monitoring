import pandas as pd
from sys import argv
import numpy as np
import random
import os
import sys
import datetime
# Resource allocator
import time
import threading
import random

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

from FilterCases import FilterCases
from ResourceAllocator import allocateRes, block_and_release_res
from estimateFutureScores import estimateFutureScores


from tqdm import tqdm


resources = int(argv[1])#10  # argv[3]
cost_t0 = int(argv[2])#20
cost_t1 = int(argv[3])#1
t_dist = argv[4]#"fixed", "normal"
condition = argv[5]#"proba", "ic", "uncer", "cate"
proba_thre = float(argv[6])#0.5
t_dur = float(argv[7]) # seconds

mode = argv[8]# [naive, crossBalance, adaptive]

data_name = argv[9]# [naive, crossBalance, adaptive]
alha_col_val = argv[10]

data_name2 = argv[11] #["bpic2012", "bpic2017"]
uncer_thre = float(argv[12])

#t_dist = dist
if t_dist == "normal":
    treatment_duration = int(random.uniform(1, t_dur))
elif t_dist == "fixed":
    treatment_duration = t_dur  # int(np.random.exponential(60, size=1))
else:
    treatment_duration = int(np.random.exponential(t_dur, size=1))



if data_name =="naive":
    data = pd.read_csv("./results_conformal/%s/df_final_naive_all.csv"%data_name2, sep=';')
    pass
elif data_name == "classBalanced":
    data = pd.read_csv("./results_conformal/%s/df_final_classBalanced_all.csv"%data_name2, sep=';')
    pass
elif data_name == "adaptive":
    data = pd.read_csv("./results_conformal/%s/df_final_adaptive_all.csv"%data_name2, sep=';')
    pass
else:
    print("No Valid Data")

data.rename(columns={alha_col_val:'alpha_col'}, inplace=True)


alpha_dict = dict(enumerate(data['alpha_col'].astype('category').cat.categories))
alpha_condition_val = list(alpha_dict.keys())[list(alpha_dict.values()).index("[1]")]

data['alpha_col'] = data['alpha_col'].astype('category').cat.codes#.astype(np.float64)
data_dict = data.to_dict("record")

# t_dist = dist
if t_dist == "normal":
    folder = "results_normal/%s/%s/"%(data_name2, data_name)
elif t_dist == "fixed":
    folder = "results_fixed/%s/%s/"%(data_name2, data_name)
else:
    folder = "results_exp/%s/%s/"%(data_name2, data_name)


results_dir = "./results_runtime/" + folder + mode +"_"+condition+"_"+alha_col_val+"_" + str(cost_t1)+"/"+str(uncer_thre)+"/"
if not os.path.exists(os.path.join(results_dir)):
    os.makedirs(os.path.join(results_dir))


filter_obj = FilterCases()
estimate_future = estimateFutureScores()

pre_rows_dict = []
Future_state = False
candidate_cases = {}
gain_dicts = {}
gain_dicts_conformal = {}
treated_cases = {}

nr_res = list(range(1, resources+1, 1))

start_time = time.time()

for row in tqdm(data_dict):
    if row['case_id'] not in treated_cases.keys():

        # filter cases based on a certain condition
        if filter_obj.filter_cases(row, condition, cost_t0, cost_t1, proba_thre, alpha_condition_val,uncer_thre):
            cur_row_dict = []
            cur_row_dict.append(row)

            if mode == "predictive":
                gain = row['CATE']
                candidate_cases[row['case_id']] = [row['case_id'], gain, row['prefix_nr'],
                                                   row['activity']]  # delta_uncer]#
                gain_dicts[row['case_id']] = candidate_cases[row['case_id']][1]

                # best case with the highest CATE
                best_Case = max(gain_dicts, key=gain_dicts.get)
                if candidate_cases[best_Case][1] > 0 and nr_res:
                    selceted_res = nr_res[0]
                    nr_res.remove(nr_res[0])
                    treated_cases[best_Case] = candidate_cases[best_Case]
                    del candidate_cases[best_Case]
                    allocateRes(selceted_res, t_dist, nr_res, treatment_duration)
                    del gain_dicts[best_Case]


            elif mode == "current":
                gain = np.subtract(np.multiply(row['CATE'], cost_t0), cost_t1)
                candidate_cases[row['case_id']] = [row['case_id'], gain, row['prefix_nr'],
                                                   row['activity']]
                gain_dicts[row['case_id']] = candidate_cases[row['case_id']][1]
                best_case = max(gain_dicts, key=gain_dicts.get)

                if candidate_cases[best_case][1] > 0 and nr_res:
                    selceted_res = nr_res[0]
                    nr_res.remove(nr_res[0])
                    treated_cases[best_case] = candidate_cases[best_case]
                    del candidate_cases[best_case]
                    allocateRes(selceted_res, t_dist, nr_res, treatment_duration)
                    del gain_dicts[best_case]


            elif mode == "future":
                gain = np.subtract(np.multiply(row['CATE'], cost_t0), cost_t1)
                try:
                    e_gain, e_cate, e_alpha = estimate_future.estimate_future_scores(pre_rows_dict, cur_row_dict,
                                                                                     cost_t0, cost_t1)
                    adjusted_gain = np.subtract(np.multiply(gain, 2), e_gain)  # gain - opp_cost
                    candidate_cases[row['case_id']] = [row['case_id'], adjusted_gain, row['prefix_nr'], row['activity'],
                                                       gain, e_gain]  # delta_uncer]#
                    gain_dicts[row['case_id']] = candidate_cases[row['case_id']][1]

                    # Case with the highest adjusted gain and future gain < current gain and gain>0
                    best_Case_for_future = max(gain_dicts, key=gain_dicts.get)

                    # if max gain > 0, and egain<gain, and nr_resour, and gain>0
                    if candidate_cases[best_Case_for_future][1] > 0 \
                            and candidate_cases[best_Case_for_future][-1] < candidate_cases[best_Case_for_future][-2] \
                            and nr_res \
                            and candidate_cases[best_Case_for_future][-2] > 0:
                        selceted_res = nr_res[0]
                        nr_res.remove(nr_res[0])
                        treated_cases[best_Case_for_future] = candidate_cases[best_Case_for_future]
                        del candidate_cases[best_Case_for_future]
                        allocateRes(selceted_res, t_dist, nr_res, treatment_duration)
                        del gain_dicts[best_Case_for_future]
                except:
                    if row in pre_rows_dict:
                        pass
                    else:
                        pre_rows_dict.append(row)

            # Future with conformal
            elif mode == "future_conformal":
                gain = np.subtract(np.multiply(row['CATE'], cost_t0), cost_t1)
                try:
                    e_gain, e_cate, e_alpha = estimate_future.estimate_future_scores(pre_rows_dict, cur_row_dict,
                                                                                     cost_t0, cost_t1)
                    adjusted_gain = np.subtract(np.multiply(gain, 2), e_gain)  # gain - opp_cost
                    candidate_cases[row['case_id']] = [row['case_id'], adjusted_gain, row['prefix_nr'], row['activity'],
                                                       row['alpha_col'], e_alpha, gain, e_gain]  # delta_uncer]#

                    gain_dicts[row['case_id']] = candidate_cases[row['case_id']][1]

                    # if max gain > 0, and egain<gain, and nr_resour, and gain>0, and e_alpha==3
                    case_id_for_best_case = [k for k, v in gain_dicts.items() if
                                             v == max([v[1] for k, v in candidate_cases.items() if v[4] == v[5]])][0]

                    if candidate_cases[case_id_for_best_case][1] > 0 \
                            and candidate_cases[case_id_for_best_case][-1] < candidate_cases[case_id_for_best_case][-2] \
                            and nr_res \
                            and candidate_cases[case_id_for_best_case][-2] > 0:
                        selceted_res = nr_res[0]
                        nr_res.remove(nr_res[0])
                        treated_cases[case_id_for_best_case] = candidate_cases[case_id_for_best_case]
                        del candidate_cases[case_id_for_best_case]
                        allocateRes(selceted_res, t_dist, nr_res, treatment_duration)
                        del gain_dicts[case_id_for_best_case]
                except:
                    if row in pre_rows_dict:
                        pass
                    else:
                        pre_rows_dict.append(row)
            else:
                print("Not valid mode")
        else:
            if row in pre_rows_dict:
                pass
            else:
                pre_rows_dict.append(row)

treated_cases['wallTime-min'] = ((time.time() - start_time) / 60)
df = pd.DataFrame()

for k, v in treated_cases.items():
    print(k)
    print(v)
    df = df.append(pd.Series(v), ignore_index=True)

#df_gains_with_res_2_1.columns = ['case_id', 'gain', 'prefix_nr', 'Activity', ]
df.to_csv(results_dir + data_name + "_" + str(resources)+'.csv', index=False, sep=';')


