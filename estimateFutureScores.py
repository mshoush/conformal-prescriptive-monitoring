import gower as gower
import pandas as pd
import numpy as np
#import datetime
import gower

class estimateFutureScores:

    def __init__(self, ):
        pass

    def estimate_future_scores(self, pre_rows_dict, cur_row_dict, cost_t0, cost_t1):
        self.pre_rows_dict=pre_rows_dict
        self.cur_row_dict=cur_row_dict
        self.cost_t0 = cost_t0
        self.cost_t1 = cost_t1

        self.pre_rows_dict = pd.DataFrame(self.pre_rows_dict)[
            pd.DataFrame(self.pre_rows_dict)['prefix_nr'] == (pd.DataFrame(self.cur_row_dict)['prefix_nr'][0] + 1)].to_dict("record")

        if not self.pre_rows_dict:
            return None
        else:
            # get frequency
            freq_activites = []
            [freq_activites.append(ls['activity']) for ls in self.pre_rows_dict]
            freq_activites_dict = dict(pd.Series(freq_activites).value_counts())

            w = [sum(x) for x in \
                 zip(list(gower.gower_matrix(pd.DataFrame(self.pre_rows_dict), pd.DataFrame(self.cur_row_dict)).flatten()), \
                     pd.DataFrame(self.pre_rows_dict)['activity'].apply(lambda x: freq_activites_dict.get(x)))]

            e_cate = np.ma.average(pd.DataFrame(self.pre_rows_dict).CATE, weights=w)

            data_alpha = pd.DataFrame(columns=['alpha_values', 'w'])
            alpha_values = pd.DataFrame(self.pre_rows_dict).alpha_col
            data_alpha['alpha_values'] = pd.Series(alpha_values).reset_index(drop=True)
            data_alpha['w'] = pd.Series(w).reset_index(drop=True)
            e_alpha = max(data_alpha.groupby("alpha_values")['w'].sum().to_dict(),
                          key=data_alpha.groupby("alpha_values")['w'].sum().to_dict().get)

            e_gain = np.subtract(np.multiply(e_cate, cost_t0), cost_t1)

            return e_gain, e_cate, e_alpha

