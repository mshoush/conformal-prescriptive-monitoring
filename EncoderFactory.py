from transformers.StaticTransformer import StaticTransformer
from transformers.LastStateTransformer import LastStateTransformer
from transformers.AggregateTransformer import AggregateTransformer
from transformers.IndexBasedTransformer import IndexBasedTransformer
from transformers.PreviousStateTransformer import PreviousStateTransformer
        
def get_encoder(method, model="catboost", case_id_col=None, static_cat_cols=None, static_num_cols=None, dynamic_cat_cols=None, dynamic_num_cols=None, fillna=True, max_events=None, dataset_name=None,):

    if method == "static":
        return StaticTransformer(dataset_name, model=model, case_id_col=case_id_col, cat_cols=static_cat_cols, num_cols=static_num_cols, fillna=fillna)

    elif method == "last":
        return LastStateTransformer(dataset_name, case_id_col=case_id_col, cat_cols=dynamic_cat_cols, num_cols=dynamic_num_cols, fillna=fillna)

    elif method == "prev":
        return PreviousStateTransformer(dataset_name, case_id_col=case_id_col, cat_cols=dynamic_cat_cols, num_cols=dynamic_num_cols, fillna=fillna)

    elif method == "agg":
        return AggregateTransformer(dataset_name, model=model, case_id_col=case_id_col, cat_cols=dynamic_cat_cols, num_cols=dynamic_num_cols, boolean=False, fillna=fillna)

    elif method == "bool":
        return AggregateTransformer(case_id_col=case_id_col, cat_cols=dynamic_cat_cols, num_cols=dynamic_num_cols, boolean=True, fillna=fillna)
    
    elif method == "index":
        return IndexBasedTransformer(case_id_col=case_id_col, cat_cols=dynamic_cat_cols, num_cols=dynamic_num_cols, max_events=max_events, fillna=fillna)

    else:
        print("Invalid encoder type")
        return None
