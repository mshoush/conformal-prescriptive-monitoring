class FilterCases:

    def __init__(self, ):
        pass


    def filter_cases(self, row, condition, cost_t0, cost_t1, proba_thre, alpha_condition_val,uncer_thre):
        self.row = row
        self.condition = condition
        self.cost_t0 = cost_t0
        self.cost_t1 = cost_t1
        self.proba_thre = proba_thre
        self.alpha_condition_val = alpha_condition_val
        self.uncer_thre = uncer_thre

        predicted_proba_1 = self.row['predicted_proba_1']
        total_uncer = self.row['total_uncer']
        confidence = self.row['confidence']
        prefix_nr = self.row['prefix_nr']
        case_id = self.row['case_id']
        CATE = self.row['CATE']
        Activity = self.row['activity']
        # row_dict = self.row.to_dict()
        alpha_col = self.row['alpha_col']


        # proba
        if self.condition == "proba":
            if predicted_proba_1 > self.proba_thre:
                return self.row
            else:
                return None

            # proba_conformal
        elif self.condition == "cate":
            if CATE >  0:
                return self.row
            else:
                return None

            # proba_conformal
        elif self.condition == "conformal":
            if alpha_col == self.alpha_condition_val:
                return self.row
            else:
                return None
        
        elif self.condition == "proba_conformal":
            if predicted_proba_1 > self.proba_thre and alpha_col == self.alpha_condition_val:
                return self.row
            else:
                return None

        elif self.condition == "proba_uncer":
            if predicted_proba_1 > self.proba_thre and total_uncer < self.uncer_thre:
                return self.row
            else:
                return None

        # proba_cate
        elif self.condition == "proba_cate":
            if predicted_proba_1 > self.proba_thre and CATE >  0:
                return self.row
            else:
                return None
        
        # proba_cate_unce
        elif self.condition == "proba_cate_uncer":
            if predicted_proba_1 > self.proba_thre and CATE >  0 and total_uncer < self.uncer_thre:
                return self.row
            else:
                return None

        # proba_cate_conformal
        elif self.condition == "conformal_cate":
            if CATE > 0 and alpha_col == self.alpha_condition_val:
                return self.row
            else:
                return None

        elif self.condition == "proba_cate_conformal":
            if predicted_proba_1 > self.proba_thre and CATE >  0 and alpha_col == self.alpha_condition_val:
                return self.row
            else:
                return None
        else:
            print("No valid condition")




        # # proba_conformal
        # elif self.condition == "proba_conformal":
        #     if predicted_proba_1 > self.proba_thre and alpha_col == 3:
        #         return self.row
        #     else:
        #         return None

        #
        # # CATA
        # elif self.condition == "cate":
        #     if CATE > 0:
        #         return self.row
        #     else:
        #         return None
