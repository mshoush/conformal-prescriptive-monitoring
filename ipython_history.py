 1/1: import econml
 1/2:
# Main imports
from econml.orf import DMLOrthoForest, DROrthoForest
from econml.dml import CausalForestDML
from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV

# Helper imports
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt
 2/1:
# Main imports
from econml.orf import DMLOrthoForest, DROrthoForest
from econml.dml import CausalForestDML
from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV

# Helper imports
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt
 3/1: %run ./orf.py
 3/2: import econml
 4/1: import econml
 5/1: import econml
 6/1: import econml
 6/2: from econml.orf import DMLOrthoForest, DROrthoForest
 6/3: from econml.dml import CausalForestDML
 6/4: from econml.orf import DMLOrthoForest, DROrthoForest
 6/5: from econml.dml import CausalForestDML
 6/6: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
 6/7:
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt
 6/8:
# Main imports
from econml.orf import DMLOrthoForest, DROrthoForest
from econml.dml import CausalForestDML##
from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV

# Helper imports
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt

#cd%matplotlib inline
 6/9:


# A few more imports
import os
import pandas as pd
import urllib.request
from sklearn.preprocessing import StandardScaler
6/10: oj_data = pd.read_csv("./../../data_from_vm/df_2017_full_encoded_with_colsNames.csv", sep=';')
 7/1:


# A few more imports
import os
import pandas as pd
import urllib.request
from sklearn.preprocessing import StandardScaler
 7/2:
# Main imports
from econml.orf import DMLOrthoForest, DROrthoForest
#from econml.dml import CausalForestDML##
from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV

# Helper imports
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt


#cd%matplotlib inline
 8/1: import econml
 9/1: import econml
 9/2: import econmlمم
10/1: import econml
11/1: import econml
11/2: from econml.orf import DMLOrthoForest, DROrthoForest
11/3: from econml.dml import CausalForestDML
11/4: from econml.sklearn_extensions.linear_model
11/5: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
11/6:
# Helper imports
import numpy as np
from itertools import product
from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
import matplotlib.pyplot as plt
12/1: import econml
12/2: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
12/3: from econml.dm1 import CausalForestDML##
12/4: from econml.dml import CausalForestDML
12/5: cython
13/1: import econml
13/2: from econml.orf import DMLOrthoForest, DROrthoForest
13/3: from econml.dml import CausalForestDML
13/4: _econml_ version
13/5: _econml_ --version
13/6: _numpy_ --version
13/7: import econml
13/8: _econml_ --version
13/9: !pip install econml -U
13/10: import econml
13/11: from econml.dm1 import CausalForestDML
13/12: from econml.dml import CausalForestDML
13/13: import sklearn
13/14: print('The scikit-learn version is {}.'.format(sklearn.__version__))
13/15: print('The scikit-learn version is {}.'.format(econml.__version__))
14/1: import causallitf
15/1: import econml
16/1: import econml
17/1: import econml
17/2: from econml.orf import DMLOrthoForest, DROrthoForest
17/3: from econml.dml import CausalForestDML
18/1: import econml
18/2: from econml.dml import CausalForestDML##
19/1: from econml.dml import CausalForestDML##
20/1: from econml.dml import CausalForestDML##
21/1: from econml.dml import CausalForestDML##
22/1: from econml.dml import CausalForestDML##
23/1: from econml.dml import CausalForestDML##
23/2: import econml
24/1: import econml
24/2: from econml.dml import CausalForestDML##
25/1: import econml
26/1: import econml
27/1: import econml
27/2: cd
28/1: import econml
28/2: from econml.orf import DMLOrthoForest, DROrthoForest
29/1: import econml
29/2: from econml.orf import DMLOrthoForest, DROrthoForest
30/1: import econml
30/2: from econml.orf import DMLOrthoForest, DROrthoForest
31/1: import econml
31/2: from econml.orf import DMLOrthoForest, DROrthoForest
31/3: from econml.dml import CausalForestDML##
32/1: from econml.dml import CausalForestDML##
32/2: from econml.orf import DMLOrthoForest, DROrthoForest
32/3: from econml.dml import CausalForestDML##
32/4: from econml.dml import CausalForestDML##
32/5: from econml.orf import DMLOrthoForest, DROrthoForest
32/6: # Main imports
32/7: from econml.orf import DMLOrthoForest, DROrthoForest
32/8: from econml.dml import CausalForestDML##
32/9: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
32/10: # Helper imports
32/11: import numpy as np
32/12: from itertools import product
32/13: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
32/14: import matplotlib.pyplot as plt
32/15: #cd%matplotlib inline
33/1: import econml
33/2: %run ./orf.py
34/1: import econml
34/2: from econml.dml import CausalForestDML##
34/3: from econml.dml import CausalForestDML##
34/4: from econml.dml import CausalForestDML##
34/5: %run ./orf.py
35/1: import econmlml
35/2: import econml
35/3: from econml.orf import DMLOrthoForest, DROrthoForest
35/4: from econml.orf import DMLOrthoForest, DROrthoForest
35/5: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
35/6: !pwd
36/1: import econml
36/2: from econml.orf import DMLOrthoForest, DROrthoForest
36/3: from econml.orf import DMLOrthoForest, DROrthoForestfrom econml.orf import DMLOrthoForest, DROrthoForest
36/4: from econml.orf import DMLOrthoForest, DROrthoForestfrom econml.orf
36/5: from econml.orf import DMLOrthoForest, DROrthoForest
36/6: from econml.dml import CausalForestDML
36/7: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
36/8: from IPython.utils import io
36/9: %run orf.py > outputORF.txt
38/1: import econml
38/2: from econml.dml import CausalForestDML##
38/3: from econml.dml import CausalForestDML##
38/4: from econml.dml import CausalForestDML##
38/5:
%%capture cap --no-stderr
%run orf.py
with open('ORF_output.txt', 'w') as f:
    f.write(cap.stdout)
39/1: from econml.dml import CausalForestDML##
39/2: from econml.dml import CausalForestDML##
39/3: %run orf.py
39/4: %run orf.py
40/1: import econml
40/2: from econml.dml import CausalForestDML##
41/1: import econml
42/1: import econml
42/2: from econml.orf import DMLOrthoForest, DROrthoForest
42/3: from econml.dml import CausalForestDML
42/4: # Main imports
42/5: from econml.orf import DMLOrthoForest, DROrthoForest
42/6: from econml.dml import CausalForestDML
42/7: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
42/8: # Helper imports
42/9: import numpy as np
42/10: from itertools import product
42/11: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
42/12: import matplotlib.pyplot as plt
43/1: import matplotlib.pyplot as plt
43/2: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
43/3: from itertools import product
43/4: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
43/5: from econml.orf import DMLOrthoForest, DROrthoForest
44/1: import numpy as np
44/2: np.__version__
46/1: df_full_2017 = pd.read_csv("df_2017_full.csv", sep=';')
47/1: # load packages
47/2: import numpy as np
47/3: import pandas as pd
47/4: from statsmodels.stats.proportion import proportions_ztest
47/5: import sklearn as sk
47/6: from sklearn.metrics import auc
47/7: import xgboost as xgb
47/8: import matplotlib as mpl
47/9: import matplotlib.pyplot as plt
47/10: df_full_2017 = pd.read_csv("df_2017_full.csv", sep=';')
47/11: df_out = pd.read_csv("./../../data_from_vm/causal_output/07_model_output/df.csv", sep=',')
47/12: df_out = pd.read_csv("/home/centos/phd/code/new_Mahmoud_PrescriptiveProcessMonitoring/old_py38_causal_output/07_model_output/df.csv", sep=',')
47/13:
cols = ['partition','NumberOfOffers', 'Outcome', 'Treatment','Propensity', 'Proba_if_Treated',
       'Proba_if_Untreated', 'CATE', 'Recommendation']
47/14: df_filtered = df_out[cols]
47/15: df_filtered
47/16:
cols = ['partition',
 'NumberOfOffers',
  'Outcome_actual',
   'Treatment_acyual',
    'Propensity',
     'Proba_if_Treated',
      'Proba_if_Untreated',
       'CATE',
        'Recommendation']
47/17: df_filtered.columns = cols
47/18: df_filtered
47/19: train_df = df_filtered.loc[df_filtered['partition'] == "train"].reset_index(drop=True)
47/20: train_df
47/21: test_df = df_filtered.loc[df_filtered['partition'] == "test"].reset_index(drop=True)
47/22: test_df
47/23: import numpy as np
47/24: from sklearn.model_selection import train_test_split
47/25: train_df_full, test_df_full = train_test_split(df, test_size=0.2, random_state=seed, stratify=df['Treatment'])
47/26: train_df_full, test_df_full = train_test_split(df_full_2017, test_size=0.2, random_state=seed, stratify=df['Treatment'])
47/27: train_df_full, test_df_full = train_test_split(df_full_2017, test_size=0.2, random_state=0, stratify=df['Treatment'])
47/28: train_df_full, test_df_full = train_test_split(df_full_2017, test_size=0.2, random_state=0, stratify=df_full_2017['Treatment'])
47/29: train_df_full, test_df_full = train_test_split(df_full_2017, test_size=0.2, random_state=0)
47/30:
dt_preds = pd.DataFrame({"predicted_proba": test_df['Proba_if_Treated'], "actual": test_df['Outcome_actual'],
                         "prefix_nr": test_df_full.groupby("Case ID").first()["prefix_nr"][0:225232],
                         "case_id": test_df_full.groupby("Case ID").first()["orig_case_id"]})
47/31:
dt_preds = pd.DataFrame({"predicted_proba": test_df['Proba_if_Treated'], "actual": test_df['Outcome_actual'],
                         "prefix_nr": test_df_full.groupby("Case ID").first()["prefix_nr"],
                         "case_id": test_df_full.groupby("Case ID").first()["orig_case_id"]})
47/32: dt_preds
47/33: len(test_df_full.groupby("Case ID").first()["prefix_nr"])
47/34: len(test_df['Proba_if_Treated'])
48/1: import econml
48/2: import econml
48/3: from econml.dml import CausalForestDML##
49/1: import econml
49/2: # Main imports
49/3: from econml.orf import DMLOrthoForest, DROrthoForest
49/4: from econml.dml import CausalForestDML##
49/5: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
49/6: # Helper imports
49/7: import numpy as np
49/8: from itertools import product
49/9: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
49/10: import matplotlib.pyplot as plt
49/11: #cd%matplotlib inline
49/12: # A few more imports
49/13: import os
49/14: import pandas as pd
49/15: import urllib.request
49/16: from sklearn.preprocessing import StandardScaler
49/17: train = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/train_df_causal.csv", sep=';')
49/18: valid = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/test_df_causal.csv", sep=';')
49/19: train = pd.read_csv("./results_dir/train_df_causal.csv", sep=';')
49/20: valid = pd.read_csv("./results_dir/test_df_causal.csv", sep=';')
49/21: # train = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/train_df_causal.csv", sep=';')
49/22: # valid = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/test_df_causal.csv", sep=';')
49/23: features = train.columns.tolist()[:-2]
49/24: X_train = train[features].values
49/25: y_train = train['Outcome']#.values.reshape(-1, 1)
49/26: X_test = valid[features].values
49/27: y_test = valid['Outcome']#.values.reshape(-1, 1)
49/28: t_train = train["Treatment"].values.reshape(-1, 1)
49/29: t_test = valid["Treatment"].values.reshape(-1, 1)
49/30: W_train = train["NumberOfOffers"].values.reshape(-1, 1)
49/31: W_test = valid["NumberOfOffers"].values.reshape(-1, 1)
49/32: # Define some parameters
49/33: n_trees = 1000
49/34: min_leaf_size = 50
49/35: max_depth = 20
49/36: subsample_ratio = 0.04
49/37:
est = DMLOrthoForest(n_jobs=2,
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
                subsample_ratio=subsample_ratio,
                        model_T=Lasso(alpha=0.1),
                                model_Y=Lasso(alpha=0.1),
                                        model_T_final=WeightedLassoCVWrapper(cv=3, n_jobs=1), 
                                                model_Y_final=WeightedLassoCVWrapper(cv=3, n_jobs=1)
                                                       )
49/38: est.fit(y_train, t_train, X=X_train, W=W_train, inference="blb")
49/39: # Calculate treatment effects
49/40: treatment_effects = est.effect(X_test)
49/41: print("\n==========Treatments effects starts====================\n")
49/42: print(treatment_effects)
49/43: print("\n==========Treatments effects finish====================\n")
49/44: # Calculate default (90%) confidence intervals for the test data
49/45: te_lower, te_upper = est.effect_interval(X_test, alpha=0.01)
49/46: print("\n==========te_lower, te_upper starts====================\n")
49/47: print(te_lower, te_upper)
49/48: print("\n==========te_lower, te_upper finish====================\n")
49/49: res = est.effect_inference(X_test)
49/50: print("\n==========res starts====================\n")
49/51: print(res)
49/52: print("\n==========res finish====================\n")
49/53: print(res.summary_frame().head())
49/54: res.summary_frame().to_csv("res.summary_frame.csv", sep=';')
49/55: print(res.population_summary())
49/56: res.population_summary().to_csv("res.population_summary.csv", sep=';')
49/57: import joblib
49/58: import sklearn
49/59: import numpy
49/60: import scipy
49/61: import joblib
49/62: import threadpoolctl
49/63: from platform import python_version
49/64: print('python:            ',python_version())
49/65: print('threadpoolctl:     ',threadpoolctl.__version__)
49/66: print('scipy:             ',scipy.__version__)
49/67: print('joblib:           ',joblib.__version__)
49/68: print('scikit-learn:     ',sklearn.__version__)
49/69: print('numpy:            ',numpy.__version__)
49/70: !pip install joblib==1.0.1
49/71: import sklearn
49/72: import numpy
49/73: import scipy
49/74: import joblib
49/75: import threadpoolctl
49/76: from platform import python_version
49/77: print('python:            ',python_version())
49/78: print('threadpoolctl:     ',threadpoolctl.__version__)
49/79: print('scipy:             ',scipy.__version__)
49/80: print('joblib:           ',joblib.__version__)
49/81: print('scikit-learn:     ',sklearn.__version__)
49/82: print('numpy:            ',numpy.__version__)
50/1: import sklearn
50/2: import numpy
50/3: import scipy
50/4: import joblib
50/5: import threadpoolctl
50/6: from platform import python_version
50/7: print('python:            ',python_version())
50/8: print('threadpoolctl:     ',threadpoolctl.__version__)
50/9: print('scipy:             ',scipy.__version__)
50/10: print('joblib:           ',joblib.__version__)
50/11: print('scikit-learn:     ',sklearn.__version__)
50/12: print('numpy:            ',numpy.__version__)
50/13: from econml.orf import DMLOrthoForest, DROrthoForest
50/14: import econml
50/15: # Main imports
50/16: from econml.orf import DMLOrthoForest, DROrthoForest
50/17: from econml.dml import CausalForestDML##
50/18: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
50/19: # Helper imports
50/20: import numpy as np
50/21: from itertools import product
50/22: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
50/23: import matplotlib.pyplot as plt
50/24: #cd%matplotlib inline
50/25: # A few more imports
50/26: import os
50/27: import pandas as pd
50/28: import urllib.request
50/29: from sklearn.preprocessing import StandardScaler
50/30: train = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/train_df_causal.csv", sep=';')
50/31: train = pd.read_csv("./results_dir/train_df_causal.csv", sep=';')
50/32: valid = pd.read_csv("./results_dir/test_df_causal.csv", sep=';')
50/33: # train = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/train_df_causal.csv", sep=';')
50/34: # valid = pd.read_csv("./../Mahmoud_PrescriptiveProcessMonitoring/results_dir/test_df_causal.csv", sep=';')
50/35: features = train.columns.tolist()[:-2]
50/36: X_train = train[features].values
50/37: y_train = train['Outcome']#.values.reshape(-1, 1)
50/38: X_test = valid[features].values
50/39: y_test = valid['Outcome']#.values.reshape(-1, 1)
50/40: t_train = train["Treatment"].values.reshape(-1, 1)
50/41: t_test = valid["Treatment"].values.reshape(-1, 1)
50/42: W_train = train["NumberOfOffers"].values.reshape(-1, 1)
50/43: W_test = valid["NumberOfOffers"].values.reshape(-1, 1)
50/44: # Define some parameters
50/45: n_trees = 1000
50/46: min_leaf_size = 50
50/47: max_depth = 20
50/48: subsample_ratio = 0.04
50/49:
est = DMLOrthoForest(n_jobs=2,
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
                subsample_ratio=subsample_ratio,
                        model_T=Lasso(alpha=0.1),
                                model_Y=Lasso(alpha=0.1),
                                        model_T_final=WeightedLassoCVWrapper(cv=3, n_jobs=1), 
                                                model_Y_final=WeightedLassoCVWrapper(cv=3, n_jobs=1)
                                                       )
50/50: est.fit(y_train, t_train, X=X_train, W=W_train, inference="blb")
51/1: # load packages
51/2: import numpy as np
51/3: import pandas as pd
51/4: from statsmodels.stats.proportion import proportions_ztest
51/5: import sklearn as sk
51/6: from sklearn.metrics import auc
51/7: import xgboost as xgb
51/8: import matplotlib as mpl
51/9: import matplotlib.pyplot as plt
51/10: %matplotlib inline
51/11: import pickle
51/12:
def read_prefixes(file):
        df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
            df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
51/13:     df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')
51/14:     train_prefix = pd.concat([df_train_prefix, df_val_prefix])
51/15:     return train_prefix, df_test_prefix
51/16:
def read_prefixes(file):
        df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
            df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
51/17:     df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')
51/18:     train_prefix = pd.concat([df_train_prefix, df_val_prefix])
51/19:
def read_prefixes(file):
    df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
    df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
        df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')
50/51: treatment_effects = est.effect(X_test)
50/52: treatment_effects = est.effect(X_test)
50/53: %env JOBLIB_TEMP_FOLDER=/tmp
50/54: import os
50/55: os.environ['JOBLIB_TEMP_FOLDER'] = '/tmp'
50/56: treatment_effects = est.effect(X_test)
50/57: treatment_effects = est.effect(X_test)
50/58: treatment_effects = est.effect(X_test)
50/59:
est = DMLOrthoForest(n_jobs=4,
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
                subsample_ratio=subsample_ratio,
                        model_T=Lasso(alpha=0.1),
                                model_Y=Lasso(alpha=0.1),backend='threading',
                                        model_T_final=WeightedLassoCVWrapper(cv=3, n_jobs=3), 
                                                model_Y_final=WeightedLassoCVWrapper(cv=3, n_jobs=3)                 
                                                       )
50/60: est.fit(y_train, t_train, X=X_train, W=W_train, inference="blb")
52/1: import econml
52/2: # Main imports
52/3: from econml.orf import DMLOrthoForest, DROrthoForest
52/4: from econml.dml import CausalForestDML##
52/5: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
52/6: # Helper imports
52/7: import numpy as np
52/8: from itertools import product
52/9: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
52/10: import matplotlib.pyplot as plt
52/11: #cd%matplotlib inline
52/12: # A few more imports
52/13: import os
52/14: import pandas as pd
52/15: import urllib.request
52/16: from sklearn.preprocessing import StandardScaler
52/17: train = pd.read_csv("./results_dir/train_df_causal.csv", sep=';')
52/18: valid = pd.read_csv("./results_dir/test_df_causal.csv", sep=';')
52/19: features = train.columns.tolist()[:-2]
52/20: X_train = train[features].values
52/21: y_train = train['Outcome']#.values.reshape(-1, 1)
52/22: X_test = valid[features].values
52/23: y_test = valid['Outcome']#.values.reshape(-1, 1)
52/24: t_train = train["Treatment"].values.reshape(-1, 1)
52/25: t_test = valid["Treatment"].values.reshape(-1, 1)
52/26: W_train = X_train
52/27: W_test = X_test
52/28: # Define some parameters
52/29: n_trees = 1000
52/30: min_leaf_size = 50
52/31: max_depth = 20
52/32: subsample_ratio = 0.04
52/33:
est = DMLOrthoForest(n_jobs=4,backend='threading',
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
                subsample_ratio=subsample_ratio,
                        model_T=Lasso(alpha=0.1, max_iter=1000),
                                model_Y=Lasso(alpha=0.1), max_iter=1000,
                                        model_T_final=WeightedLassoCVWrapper(cv=3, n_jobs=3), 
                                                model_Y_final=WeightedLassoCVWrapper(cv=3, n_jobs=3)
                                                       )
52/34:
est = DMLOrthoForest(n_jobs=4,backend='threading',
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
                subsample_ratio=subsample_ratio,
                        model_T=Lasso(alpha=0.1, max_iter=1000),
                                model_Y=Lasso(alpha=0.1, max_iter=1000),
                                        model_T_final=WeightedLassoCVWrapper(cv=3, n_jobs=3), 
                                                model_Y_final=WeightedLassoCVWrapper(cv=3, n_jobs=3)
                                                       )
52/35: est.fit(y_train, t_train, X=X_train, W=W_train, inference="blb")
52/36: treatment_effects = est.effect(X_test)
53/1: import numpy as np
53/2: import pandas as pd
53/3:
def read_prefixes(file):
        df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
            df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
53/4:     df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')
53/5:     train_prefix = pd.concat([df_train_prefix, df_val_prefix])
53/6:     return train_prefix, df_test_prefix
53/7:
def read_prefixes(file):
    df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
    df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
        df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')
53/8:
def read_prefixes(file):
    df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
    df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
    df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')   
        train_prefix = pd.concat([df_train_prefix, df_val_prefix])
53/9:
def read_prefixes(file):
    df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
    df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
    df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')   
    train_prefix = pd.concat([df_train_prefix, df_val_prefix])
53/10:
def read_prefixes(file):
    df_train_prefix = pd.read_csv(file+"dt_train_prefixes.csv", sep=';')
    df_test_prefix = pd.read_csv(file+"dt_test_prefixes.csv", sep=';')
    df_val_prefix = pd.read_csv(file+"dt_val_prefixes.csv", sep=';')   
    train_prefix = pd.concat([df_train_prefix, df_val_prefix])
    return train_prefix, df_test_prefix
53/11: dirr = "./results_dir/"
53/12: train_prefix, test_prefix = read_prefixes(dirr)
53/13: def # sort values by prefix
53/14:
def sort_values(gr):
        df = pd.DataFrame(gr)
            df = df.sort_values(by=['prefix_nr'])
53/15:     return df
53/16:
def sort_values(gr):
    df = pd.DataFrame(gr)
    df = df.sort_values(by=['prefix_nr'])
    return df
53/17:
def prepare_output(dirr, df_train_prefix, df_test_prefix):
        df_out = pd.read_csv(dirr+"df.csv", sep=',')
        train_out = df_out[df_out['partition']=='train']
            test_out = df_out[df_out['partition']=='test']
53/18:     test_out["prefix_nr"]= list(df_test_prefix.groupby("Case ID").first()["prefix_nr"])
53/19:     test_out["case_id"]= list(df_test_prefix.groupby("Case ID").first()["orig_case_id"])
53/20:     train_out["prefix_nr"]= list(df_train_prefix.groupby("Case ID").first()["prefix_nr"])
53/21:     train_out["case_id"]= list(df_train_prefix.groupby("Case ID").first()["orig_case_id"])
53/22:     train_out = train_out.groupby('case_id').apply(sort_values)
53/23:     train_out = train_out.reset_index(drop=True)
53/24:     test_out = test_out.groupby('case_id').apply(sort_values)
53/25:     test_out = test_out.reset_index(drop=True)
53/26:     return train_out, test_out
53/27:
def prepare_output(dirr, df_train_prefix, df_test_prefix):
        df_out = pd.read_csv(dirr+"df.csv", sep=',')
        train_out = df_out[df_out['partition']=='train']
        test_out = df_out[df_out['partition']=='test']
        test_out["prefix_nr"]= list(df_test_prefix.groupby("Case ID").first()["prefix_nr"])
            test_out["case_id"]= list(df_test_prefix.groupby("Case ID").first()["orig_case_id"])
53/28:
def prepare_output(dirr, df_train_prefix, df_test_prefix):
        df_out = pd.read_csv(dirr+"df.csv", sep=',')
        train_out = df_out[df_out['partition']=='train']
        test_out = df_out[df_out['partition']=='test']
        test_out["prefix_nr"]= list(df_test_prefix.groupby("Case ID").first()["prefix_nr"])
        test_out["case_id"]= list(df_test_prefix.groupby("Case ID").first()["orig_case_id"])
        train_out["prefix_nr"]= list(df_train_prefix.groupby("Case ID").first()["prefix_nr"])
        train_out["case_id"]= list(df_train_prefix.groupby("Case ID").first()["orig_case_id"])
        train_out = train_out.groupby('case_id').apply(sort_values)
        train_out = train_out.reset_index(drop=True)
        test_out = test_out.groupby('case_id').apply(sort_values)
        test_out = test_out.reset_index(drop=True)
        return train_out, test_out
53/29: dirr = "./py38_causal_output/07_model_output/"
53/30: train_out, test_out = prepare_output(dirr, train_prefix, test_prefix)
55/1: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
55/2: #from econml.causal_tree import CausalTree
55/3: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
55/4: from econml.cate_interpreter import SingleTreeCateInterpreter, SingleTreePolicyInterpreter
55/5: import graphviz
55/6: # Helper imports
55/7: import numpy as np
55/8: from itertools import product
55/9: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
55/10: import matplotlib.pyplot as plt
55/11: %matplotlib inline
55/12: # A few more imports
55/13: import os
55/14: import pandas as pd
55/15: import urllib.request
55/16: from sklearn.preprocessing import StandardScaler
55/17: from sklearn.model_selection import train_test_split
55/18: !pip install ipykernel
55/19: from matplotlib.backends.backend_agg import FigureCanvasAgg as fc
55/20: fig = Figure()
55/21: canvas = fc(fig)
55/22: ax = fig.add_subplot(1, 1, 1)
55/23: import matplotlib
55/24: import matplotlib.pyplot as plt
55/25: import numpy as np
55/26: # Data for plotting
55/27: t = np.arange(0.0, 2.0, 0.01)
55/28: s = 1 + np.sin(2 * np.pi * t)
55/29: fig, ax = plt.subplots()
55/30: ax.plot(t, s)
55/31:
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
55/32: ax.grid()
55/33: fig.savefig("test.png")
55/34: plt.show()
55/35: !pwd
55/36: !ls
55/37: %matplotlib inline
55/38: import matplotlib.pyplot as plt
55/39: plt.show()
55/40: t = np.arange(0.0, 2.0, 0.01)
55/41: s = 1 + np.sin(2 * np.pi * t)
55/42: fig, ax = plt.subplots()
55/43: ax.plot(t, s)
55/44:
ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
55/45: ax.grid()3
55/46: ax.grid()
55/47: plt.show()
55/48: import pandas as pd
55/49: import numpy as np
55/50: from numpy import savetxt
55/51: from tqdm import tqdm, tqdm_notebook
55/52: from sklearn.preprocessing import StandardScaler
55/53: pd.set_option('display.max_columns', None)
55/54: import itertools
55/55: import econml
55/56: import warnings
55/57: warnings.filterwarnings('ignore')
55/58: # Main imports
55/59: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
55/60: #from econml.causal_tree import CausalTree
55/61: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
55/62: from econml.cate_interpreter import SingleTreeCateInterpreter, SingleTreePolicyInterpreter
55/63: import graphviz
55/64: # Helper imports
55/65: import numpy as np
55/66: from itertools import product
55/67: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
55/68: import matplotlib.pyplot as plt
55/69: %matplotlib inline
55/70: # A few more imports
55/71: import os
55/72: import pandas as pd
55/73: import urllib.request
55/74: from sklearn.preprocessing import StandardScaler
55/75: from sklearn.model_selection import train_test_split
55/76: case_id_col = "Case ID"
55/77: activity_col = "Activity"
55/78: resource_col = "org:resource"
55/79: timestamp_col = "time:timestamp"
55/80: treatment = 'Treatment'
55/81: outcome = 'Outcome' # outcome: 1 or zero
55/82: df = pd.read_csv("./phd/code/new_Mahmoud_PrescriptiveProcessMonitoring/encoded_data/df_2017_full_encoded_with_colsNames.csv", sep=";")
55/83: # Prepare data for time of activity treatment
55/84: train, test = train_test_split(df, test_size=0.2, shuffle=False)
55/85: train, valid = train_test_split(train, test_size=0.2, shuffle=False)
55/86: features = train.drop([outcome, treatment], axis=1)
55/87: features_test = valid.drop([outcome, treatment], axis=1)
55/88: #cat_confound_cols = ['LoanGoal', 'ApplicationType']
55/89: #num_confound_cols = features.columns.difference(cat_confound_cols)
55/90: #cat_hetero_cols = ['LoanGoal', 'ApplicationType']
55/91: #num_hetero_cols = features.columns.difference(cat_hetero_cols)
55/92: #num_hetero_cols = ['RequestedAmount', 'CreditScore']
55/93: Y = train[outcome].to_numpy()
55/94: T = train[treatment].to_numpy()
55/95: scaler = StandardScaler()
55/96: W1 = scaler.fit_transform(features.to_numpy())
55/97: #W2 = pd.get_dummies(features[cat_confound_cols]).to_numpy()
55/98: W = W1#np.concatenate([W1, W2], axis=1)
55/99: X1 = scaler.fit_transform(features.to_numpy())
55/100: #X2 = pd.get_dummies(features[cat_hetero_cols]).to_numpy()
55/101: X = X1#np.concatenate([X1, X2], axis=1)
55/102: X1_test = scaler.fit_transform(features_test.to_numpy())
55/103: #X2_test = pd.get_dummies(features_test[cat_hetero_cols]).to_numpy()
55/104: X_test = X1_test#np.concatenate([X1_test, X2_test], axis=1)
55/105: N_trees = [200]
55/106: Min_leaf_size = [20]
55/107: Max_depth = [30]
55/108: Subsample_ratio = [0.4]
55/109: Lambda_reg = [0.01]
55/110:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
        print(i)
            n_trees = i[0]
55/111:     min_leaf_size = i[1]
55/112:     max_depth = i[2]
55/113:     subsample_ratio = i[3]
55/114:     lambda_reg = i[4]
55/115:
    est = DMLOrthoForest(n_jobs=-1,backend='threading',
        n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
            subsample_ratio=subsample_ratio, discrete_treatment=True,
                model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
                    model_Y=Lasso(alpha=lambda_reg),
                        model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
                            model_Y_final=WeightedLasso(alpha=lambda_reg),
                                random_state=106
                                   )
55/116:     ortho_model = est.fit(Y, T, X, W)
55/117:     batches = np.array_split(X_test, X_test.shape[0] / 100)
55/118:     treatment_effects = est.const_marginal_effect(batches[0])
55/119:     ii = 0
55/120:
    for batch in batches[1:]:
            estimates = est.const_marginal_effect(batch)
                treatment_effects = np.append(treatment_effects, estimates)
55/121:         ii += 1
55/122:     df_results = valid
55/123:     df_results['Treatment Effects'] = treatment_effects
55/124:     net_value = [0]
55/125:     net_value2 = [0]
55/126:     net_value3 = [0]
55/127:     percentages = [10,20,30,40,50,60,70,80,90,100]
55/128:
    for n in percentages:
            num = int(len(df_results)*(n/100))
                top_n = df_results.nsmallest(num,'Treatment Effects')
55/129:         n_treated = top_n[top_n['Treatment']==1].shape[0]
55/130:         n_control = top_n[top_n['Treatment']==0].shape[0]
55/131:         scale_factor = n_treated/n_control
55/132:         treated = top_n[top_n['treatment']==1]['duration'].sum()
55/133:         control = top_n[top_n['treatment']==0]['duration'].sum()
55/134:         reduction = (scale_factor*control) - treated
55/135:         net_value.append(reduction)
55/136:     plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
55/137:
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',
             linestyle='dashed')
55/138:     plt.xlabel('Proportion of cases targeted')
55/139:     plt.ylabel('Expected incremental reduction')
55/140:     plt.legend(loc='best')
55/141:     plt.title(i)
55/142:     #plt.savefig('Results/_Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
55/143:     plt.show()
55/144:     AUC = np.trapz(net_value, [0]+percentages)
55/145:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=-1,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
55/146:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=-1,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
55/147: N_trees = [1000]
55/148: Min_leaf_size = [50]
55/149: Max_depth = [20]
55/150: Subsample_ratio = [0.04]
55/151: Lambda_reg = [0.01]
55/152:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=-1,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
56/1:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
56/2: import pandas as pd
56/3: import numpy as np
56/4: from numpy import savetxt
56/5: from tqdm import tqdm, tqdm_notebook
56/6: from sklearn.preprocessing import StandardScaler
56/7: pd.set_option('display.max_columns', None)
56/8: import itertools
56/9: import econml
56/10: import warnings
56/11: warnings.filterwarnings('ignore')
56/12: # Main imports
56/13: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
56/14: #from econml.causal_tree import CausalTree
56/15: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
56/16: from econml.cate_interpreter import SingleTreeCateInterpreter, SingleTreePolicyInterpreter
56/17: import graphviz
56/18: # Helper imports
56/19: import numpy as np
56/20: from itertools import product
56/21: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
56/22: import matplotlib.pyplot as plt
56/23: %matplotlib inline
56/24: # A few more imports
56/25: import os
56/26: import pandas as pd
56/27: import urllib.request
56/28: from sklearn.preprocessing import StandardScaler
56/29: from sklearn.model_selection import train_test_split
56/30: case_id_col = "Case ID"
56/31: activity_col = "Activity"
56/32: resource_col = "org:resource"
56/33: timestamp_col = "time:timestamp"
56/34: treatment = 'Treatment'
56/35: outcome = 'Outcome' # outcome: 1 or zero
56/36: df = pd.read_csv("./phd/code/new_Mahmoud_PrescriptiveProcessMonitoring/encoded_data/df_2017_full_encoded_with_colsNames.csv", sep=";")
56/37: # Prepare data for time of activity treatment
56/38: train, test = train_test_split(df, test_size=0.2, shuffle=False)
56/39: train, valid = train_test_split(train, test_size=0.2, shuffle=False)
56/40: features = train.drop([outcome, treatment], axis=1)
56/41: features_test = valid.drop([outcome, treatment], axis=1)
56/42: #cat_confound_cols = ['LoanGoal', 'ApplicationType']
56/43: #num_confound_cols = features.columns.difference(cat_confound_cols)
56/44: #cat_hetero_cols = ['LoanGoal', 'ApplicationType']
56/45: #num_hetero_cols = features.columns.difference(cat_hetero_cols)
56/46: #num_hetero_cols = ['RequestedAmount', 'CreditScore']
56/47: Y = train[outcome].to_numpy()
56/48: T = train[treatment].to_numpy()
56/49: scaler = StandardScaler()
56/50: W1 = scaler.fit_transform(features.to_numpy())
56/51: #W2 = pd.get_dummies(features[cat_confound_cols]).to_numpy()
56/52: W = W1#np.concatenate([W1, W2], axis=1)
56/53: X1 = scaler.fit_transform(features.to_numpy())
56/54: #X2 = pd.get_dummies(features[cat_hetero_cols]).to_numpy()
56/55: X = X1#np.concatenate([X1, X2], axis=1)
56/56: X1_test = scaler.fit_transform(features_test.to_numpy())
56/57: #X2_test = pd.get_dummies(features_test[cat_hetero_cols]).to_numpy()
56/58: X_test = X1_test#np.concatenate([X1_test, X2_test], axis=1)
56/59: N_trees = [1000]
56/60: Min_leaf_size = [50]
56/61: Max_depth = [20]
56/62: Subsample_ratio = [0.04]
56/63: Lambda_reg = [0.01]
56/64:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
56/65:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
56/66:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',
    n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth, 
    subsample_ratio=subsample_ratio, discrete_treatment=True,
    model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),
    model_Y=Lasso(alpha=lambda_reg),
    model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'), 
    model_Y_final=WeightedLasso(alpha=lambda_reg),
    random_state=106
    )
    ortho_model = est.fit(Y, T, X, W)
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = valid
    df_results['Treatment Effects'] = treatment_effects
    df_results.to_csv('df_results.csv', index=False, sep=';')
    '''
    net_value = [0]
    net_value2 = [0]
    net_value3 = [0]
    percentages = [10,20,30,40,50,60,70,80,90,100]
    for n in percentages:
        num = int(len(df_results)*(n/100))
        top_n = df_results.nsmallest(num,'Treatment Effects')
        n_treated = top_n[top_n['Treatment']==1].shape[0]
        n_control = top_n[top_n['Treatment']==0].shape[0]
        scale_factor = n_treated/n_control
        treated = top_n[top_n['treatment']==1]['duration'].sum()
        control = top_n[top_n['treatment']==0]['duration'].sum()
        reduction = (scale_factor*control) - treated 
        net_value.append(reduction)
    plt.plot([0]+percentages, net_value, label="'Treatment Effect", marker="o")
    plt.plot([0,percentages[9]], [0,net_value[10]], label="'Random",  marker="o", color='Black',linestyle='dashed')
    plt.xlabel('Proportion of cases targeted')
    plt.ylabel('Expected incremental reduction')
    plt.legend(loc='best')
    plt.title(i)
    plt.savefig('Call_incomplete_files_valid_%s.png'%str(i), format='png', dpi=300)
    AUC = np.trapz(net_value, [0]+percentages)
    '''
56/67: df_results
56/68: df_results.to_csv('df_results_orf.csv', index=False, sep=';')
56/69: filename = 'est1_model.sav'
56/70: import pickle
56/71: pickle.dump(est, open(filename, 'wb'))
56/72: f_test = test.drop([outcome, treatment], axis=1)
56/73: X1_test = scaler.fit_transform(features_test.to_numpy())
56/74: X1_test = scaler.fit_transform(f_test.to_numpy())
56/75: X_test = X1_test
56/76: filename = 'Ortho_model.sav'
56/77: pickle.dump(ortho_model, open(filename, 'wb'))
56/78: batches = np.array_split(X_test, X_test.shape[0] / 100)
56/79:     ii = 0
56/80:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
56/81:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = test
    df_results['Treatment Effects'] = treatment_effects
    te_lower, te_upper = est.effect_interval(batches[0])
    ii=0
    for batch in batches[1:]:
        print(ii)
        lower, upper = est.effect_interval(batch)
        te_lower = np.append(te_lower, lower)
        te_upper = np.append(te_upper, upper)
        ii += 1
    df_results['te_lower'] = te_lower
    df_results['te_upper'] = te_upper
    df_results['Interval Length'] = df_results['te_upper'] - df_results['te_lower']
    df_results.to_csv('df_results_orf_test.csv', index=False, sep=';')
56/82: filename = 'est1_model.sav'
56/83: est = pickle.load(open(filename, 'rb'))
56/84:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = test
    df_results['Treatment Effects'] = treatment_effects
    te_lower, te_upper = est.effect_interval(batches[0])
    ii=0
    for batch in batches[1:]:
        print(ii)
        lower, upper = est.effect_interval(batch)
        te_lower = np.append(te_lower, lower)
        te_upper = np.append(te_upper, upper)
        ii += 1
    df_results['te_lower'] = te_lower
    df_results['te_upper'] = te_upper
    df_results['Interval Length'] = df_results['te_upper'] - df_results['te_lower']
    df_results.to_csv('df_results_orf_test.csv', index=False, sep=';')
56/85:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=12,backend='threading',n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth,subsample_ratio=subsample_ratio, discrete_treatment=True,model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y=Lasso(alpha=lambda_reg),model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y_final=WeightedLasso(alpha=lambda_reg),random_state=106)
    ortho_model = est.fit(Y, T, X, W)                            
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = test
    df_results['Treatment Effects'] = treatment_effects
    te_lower, te_upper = est.effect_interval(batches[0])
    ii=0
    for batch in batches[1:]:
        print(ii)
        lower, upper = est.effect_interval(batch)
        te_lower = np.append(te_lower, lower)
        te_upper = np.append(te_upper, upper)
        ii += 1
    df_results['te_lower'] = te_lower
    df_results['te_upper'] = te_upper
    df_results['Interval Length'] = df_results['te_upper'] - df_results['te_lower']
    df_results.to_csv('df_results_orf_test.csv', index=False, sep=';')
57/1:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth,subsample_ratio=subsample_ratio, discrete_treatment=True,model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y=Lasso(alpha=lambda_reg),model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y_final=WeightedLasso(alpha=lambda_reg),random_state=106)
    ortho_model = est.fit(Y, T, X, W)                            
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = test
    df_results['Treatment Effects'] = treatment_effects
    te_lower, te_upper = est.effect_interval(batches[0])
    ii=0
    for batch in batches[1:]:
        print(ii)
        lower, upper = est.effect_interval(batch)
        te_lower = np.append(te_lower, lower)
        te_upper = np.append(te_upper, upper)
        ii += 1
    df_results['te_lower'] = te_lower
    df_results['te_upper'] = te_upper
    df_results['Interval Length'] = df_results['te_upper'] - df_results['te_lower']
    df_results.to_csv('df_results_orf_test.csv', index=False, sep=';')
57/2: import pandas as pd
57/3: import numpy as np
57/4: from numpy import savetxt
57/5: from tqdm import tqdm, tqdm_notebook
57/6: from sklearn.preprocessing import StandardScaler
57/7: pd.set_option('display.max_columns', None)
57/8: import itertools
57/9: import econml
57/10: import warnings
57/11: warnings.filterwarnings('ignore')
57/12: # Main imports
57/13: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
57/14: #from econml.causal_tree import CausalTree
57/15: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
57/16: from econml.cate_interpreter import SingleTreeCateInterpreter, SingleTreePolicyInterpreter
57/17: import graphviz
57/18: # Helper imports
57/19: import numpy as np
57/20: from itertools import product
57/21: from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
57/22: import matplotlib.pyplot as plt
57/23: %matplotlib inline
57/24: # A few more imports
57/25: import os
57/26: import pandas as pd
57/27: import urllib.request
57/28: from sklearn.preprocessing import StandardScaler
57/29: from sklearn.model_selection import train_test_split
57/30: case_id_col = "Case ID"
57/31: activity_col = "Activity"
57/32: resource_col = "org:resource"
57/33: timestamp_col = "time:timestamp"
57/34: treatment = 'Treatment'
57/35: outcome = 'Outcome' # outcome: 1 or zero
57/36:
def read_data(file):
    #df = pd.read_csv(file,sep=';')
    df = pd.read_csv(file,sep=';',compression="zip")
    return df
57/37: data = '/home/mshoush/ut_cs_phd/phd/data_from_vm/df_2017_full_encoded_with_colsNames.zip'
57/38: df = read_data(data)
57/39: df = read_csv("/home/centos/phd/code/new_Mahmoud_PrescriptiveProcessMonitoring/encoded_data/df_2017_full_encoded_with_colsNames.csv", sep=';')
57/40: df = pd.read_csv("/home/centos/phd/code/new_Mahmoud_PrescriptiveProcessMonitoring/encoded_data/df_2017_full_encoded_with_colsNames.csv", sep=';')
57/41: # Prepare data for time of activity treatment
57/42: train, test = train_test_split(df, test_size=0.2, shuffle=False)
57/43: train, valid = train_test_split(train, test_size=0.2, shuffle=False)
57/44: features = train.drop([outcome, treatment], axis=1)
57/45: features_test = valid.drop([outcome, treatment], axis=1)
57/46: #cat_confound_cols = ['LoanGoal', 'ApplicationType']
57/47: #num_confound_cols = features.columns.difference(cat_confound_cols)
57/48: #cat_hetero_cols = ['LoanGoal', 'ApplicationType']
57/49: #num_hetero_cols = features.columns.difference(cat_hetero_cols)
57/50: #num_hetero_cols = ['RequestedAmount', 'CreditScore']
57/51: Y = train[outcome].to_numpy()
57/52: T = train[treatment].to_numpy()
57/53: scaler = StandardScaler()
57/54: W1 = scaler.fit_transform(features.to_numpy())
57/55: #W2 = pd.get_dummies(features[cat_confound_cols]).to_numpy()
57/56: W = W1#np.concatenate([W1, W2], axis=1)
57/57: X1 = scaler.fit_transform(features.to_numpy())
57/58: #X2 = pd.get_dummies(features[cat_hetero_cols]).to_numpy()
57/59: X = X1#np.concatenate([X1, X2], axis=1)
57/60: X1_test = scaler.fit_transform(features_test.to_numpy())
57/61: #X2_test = pd.get_dummies(features_test[cat_hetero_cols]).to_numpy()
57/62: X_test = X1_test#np.concatenate([X1_test, X2_test], axis=1)
57/63: N_trees = [1000]
57/64: Min_leaf_size = [50]
57/65: Max_depth = [20]
57/66: Subsample_ratio = [0.04]
57/67: Lambda_reg = [0.01]
57/68: # n_trees = 1000
57/69: # min_leaf_size = 50
57/70: # max_depth = 20
57/71: # subsample_ratio = 0.04
57/72: # preparing the test set
57/73: f_test = test.drop([outcome, treatment], axis=1)
57/74: X1_test = scaler.fit_transform(f_test.to_numpy())
57/75: #X2_test = pd.get_dummies(f_test[cat_hetero_cols]).to_numpy()
57/76: X_test = X1_test
57/77:
for i in itertools.product(N_trees, Min_leaf_size, Max_depth, Subsample_ratio, Lambda_reg):
    print(i)
    n_trees = i[0]
    min_leaf_size = i[1]
    max_depth = i[2]
    subsample_ratio = i[3]
    lambda_reg = i[4]
    est = DMLOrthoForest(n_jobs=8,backend='threading',n_trees=n_trees, min_leaf_size=min_leaf_size, max_depth=max_depth,subsample_ratio=subsample_ratio, discrete_treatment=True,model_T=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y=Lasso(alpha=lambda_reg),model_T_final=LogisticRegression(C=1/(X.shape[0]*lambda_reg), penalty='l1', solver='saga'),model_Y_final=WeightedLasso(alpha=lambda_reg),random_state=106)
    ortho_model = est.fit(Y, T, X, W)                            
    batches = np.array_split(X_test, X_test.shape[0] / 100)
    treatment_effects = est.const_marginal_effect(batches[0])
    ii = 0
    for batch in batches[1:]:
        estimates = est.const_marginal_effect(batch)
        treatment_effects = np.append(treatment_effects, estimates)
        ii += 1
    df_results = test
    df_results['Treatment Effects'] = treatment_effects
    te_lower, te_upper = est.effect_interval(batches[0])
    ii=0
    for batch in batches[1:]:
        print(ii)
        lower, upper = est.effect_interval(batch)
        te_lower = np.append(te_lower, lower)
        te_upper = np.append(te_upper, upper)
        ii += 1
    df_results['te_lower'] = te_lower
    df_results['te_upper'] = te_upper
    df_results['Interval Length'] = df_results['te_upper'] - df_results['te_lower']
    df_results.to_csv('df_results_orf_test.csv', index=False, sep=';')
58/1: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
58/2:
from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV

from sklearn.linear_model import Lasso, LassoCV, LogisticRegression, LogisticRegressionCV
from sklearn.preprocessing import StandardScaler

import EncoderFactory
from DatasetManager import DatasetManager
#from calibration_wrappers import LGBMCalibrationWrapper

import pandas as pd
import numpy as np
59/1: !pwd
59/2:
%load_ext autoreload
%autoreload 2
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
from sys import argv
59/3: !pip install pickle5
59/4: import econml
59/5: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
59/6: %run -i './predictive_and_prescriptive/optimize_params_xgboost.py' "prepared_bpic2017" "params_dir"
59/7: !pip install hyperopt
59/8: %run -i './predictive_and_prescriptive/optimize_params_xgboost.py' "prepared_bpic2017" "params_dir"
59/9: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
59/10:
%load_ext autoreload
%autoreload 2
%matplotlib inline
59/11: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
59/12:
%load_ext autoreload
%autoreload 2
%matplotlib inline
59/13: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/1: %load_ext autoreload
60/2: %autoreload 2
60/3: %matplotlib inline
60/4: import matplotlib.pyplot as plt
60/5: import pandas as pd
60/6: from sys import argv
60/7: # Run Predictive and ORF models.
60/8: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/9: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/10: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/11: %load_ext autoreload
60/12: %autoreload 2
60/13: %matplotlib inline
60/14: import matplotlib.pyplot as plt
60/15: import pandas as pd
60/16: from sys import argv
60/17: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/18: %load_ext autoreload
60/19: %autoreload 2
60/20: %matplotlib inline
60/21: import matplotlib.pyplot as plt
60/22: import pandas as pd
60/23: from sys import argv
60/24: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "results_dir"
60/25: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "params_dir" "optimal_params_xgboost_prepared_bpic2017.pickle"
60/26: %load_ext autoreload
60/27: %autoreload 2
60/28: %matplotlib inline
60/29: import matplotlib.pyplot as plt
60/30: import pandas as pd
60/31: from sys import argv
60/32: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "optimal_params_xgboost_prepared_bpic2017.pickle" "results_dir"
60/33: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./predictive_and_prescriptive/params_dir/optimal_params_xgboost_prepared_bpic2017.pickle" "results_dir"
60/34: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./predictive_and_prescriptive/params_dir/optimal_params_xgboost_prepared_bpic2017.pickle" "results_dir"
60/35: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./predictive_and_prescriptive/params_dir/optimal_params_xgboost_prepared_bpic2017_old.pickle" "results_dir"
60/36: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./params_dir/optimal_params_xgboost_prepared_bpic2017.pickle" "results_dir"
61/1: %load_ext autoreload
61/2: %autoreload 2
61/3: %matplotlib inline
61/4: import matplotlib.pyplot as plt
61/5: import pandas as pd
61/6: from sys import argv
61/7: !pwd
61/8: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./params_dir/optimal_params_xgboost_prepared_bpic2017.pickle" "results_dir"
61/9: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./params_dir/optimal_params_xgboost_bpic2017_accepted.pickle" "results_dir"
61/10: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./params_dir/optimal_params_xgboost_bpic2017_accepted.pickle" "results_dir"
62/1: %load_ext autoreload
62/2: %autoreload 2
62/3: %matplotlib inline
62/4: import matplotlib.pyplot as plt
62/5: import pandas as pd
62/6: from sys import argv
62/7: %run -i './predictive_and_prescriptive/orf-18-5-2021.py' "prepared_bpic2017" "./params_dir/optimal_params_xgboost_bpic2017_accepted.pickle" "results_dir"
63/1: %run run_experiments.ipynb
63/2: !pip install nbformat
63/3: %run run_experiments.ipynb
63/4: !pwd
63/5: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
63/6: %run run_experiments.ipynb
63/7: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
63/8: %load_ext autoreload
63/9: %autoreload 2
63/10: %matplotlib inline
63/11: import matplotlib.pyplot as plt
63/12: import pandas as pd
63/13: from sys import argv
63/14: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
63/15: !pwd
63/16: %load_ext autoreload
63/17: %autoreload 2
63/18: %matplotlib inline
63/19: import matplotlib.pyplot as plt
63/20: import pandas as pd
63/21: from sys import argv
63/22: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
63/23: %load_ext autoreload
63/24: %autoreload 2
63/25: %matplotlib inline
63/26: import matplotlib.pyplot as plt
63/27: import pandas as pd
63/28: from sys import argv
63/29: %run -i './prepare_data/BPIC2017_preparation_outcom_and_treatment.py' "./prepare_data/bpic2017.pkl"
63/30: %run -i './predictive_and_prescriptive/optimize_params_xgboost.py' "prepared_bpic2017" "params_dir"
63/31: %run -i './predictive_and_prescriptive/optimize_params_xgboost.py' "prepared_bpic2017" "params_dir"
63/32: %run -i "./predicitive_and_prescriptive/optimize_params_xgboost.py" "prepared_bpic2017" "params_dir"
64/1: import econml
64/2: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
64/3: from econml.sklearn_extensions.linear_model import WeightedLassoCVWrapper, WeightedLasso, WeightedLassoCV
64/4: from econml.ortho_forest import DMLOrthoForest, DROrthoForest
65/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
66/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
67/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
68/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
69/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
69/2: pwd
70/1:
from plotly.graph_objs.volume.caps import X

import EncoderFactory
from DatasetManager import DatasetManager

import pandas as pd
import numpy as np

from sklearn.metrics import roc_auc_score
from sklearn.pipeline import FeatureUnion

import time
import os
import sys
from sys import argv
import pickle

from catboost import Pool, CatBoostRegressor, CatBoostClassifier

from sklearn.pipeline import FeatureUnion

import time
import os
from sys import argv
import pickle

import xgboost as xgb

from catboost import Pool, CatBoostRegressor, CatBoostClassifier
70/2:

calibrate = False
split_type = "temporal"
oversample = False
calibration_method = "beta"

train_ratio = 0.8
val_ratio = 0.2
70/3: dataset_name = "prepared_bpic2017"
70/4: results_dir = "res_cp"
70/5: en_size = 50
70/6:
# create results directory
if not os.path.exists(os.path.join(results_dir)):
    os.makedirs(os.path.join(results_dir))
70/7:
print('Preparing data...')
start = time.time()
70/8:
# read the data
dataset_manager = DatasetManager(dataset_name)
data = dataset_manager.read_dataset()
70/9: dataset_name = "bpic2017_accepted"
70/10:
# read the data
dataset_manager = DatasetManager(dataset_name)
data = dataset_manager.read_dataset()
70/11:
%load_ext autoreload
%autoreload 2
70/12:
# read the data
dataset_manager = DatasetManager(dataset_name)
data = dataset_manager.read_dataset()
70/13:
%load_ext autoreload
%autoreload 2
70/14:
# read the data
dataset_manager = DatasetManager(dataset_name)
data = dataset_manager.read_dataset()
70/15:
min_prefix_length = 1
max_prefix_length = int(np.ceil(data.groupby(dataset_manager.case_id_col).size().quantile(0.9)))
70/16:

cls_encoder_args = {'case_id_col': dataset_manager.case_id_col,
                    'static_cat_cols': dataset_manager.static_cat_cols,
                    'static_num_cols': dataset_manager.static_num_cols,
                    'dynamic_cat_cols': dataset_manager.dynamic_cat_cols,
                    'dynamic_num_cols': dataset_manager.dynamic_num_cols,
                    'fillna': True}
70/17:
# split into training and test
if split_type == "temporal":
    train, test = dataset_manager.split_data_strict(data, train_ratio, split=split_type)
else:
    train, test = dataset_manager.split_data(data, train_ratio, split=split_type)

train, val = dataset_manager.split_val(train, val_ratio)
70/18: train['Case ID']
70/19: len(train['Case ID'])
70/20: np.where(train['Case ID'] == test['Case ID'])
70/21: train['Case ID'] == test['Case ID']
70/22: list(set(list(train['Case ID'])).intersection(list(test['Case ID'])))
70/23: list(set(list(train['Case ID'])).intersection(list(valid['Case ID'])))
70/24: list(set(list(train['Case ID'])).intersection(list(val['Case ID'])))
70/25: list(set(list(test['Case ID'])).intersection(list(val['Case ID'])))
70/26:
# generate data where each prefix is a separate instance
dt_train_prefixes = dataset_manager.generate_prefix_data(train, min_prefix_length, max_prefix_length)
dt_train_prefixes.to_pickle(os.path.join(results_dir, "dt_train_prefixes.pkl"))
70/27:
dt_test_prefixes = dataset_manager.generate_prefix_data(test, min_prefix_length, max_prefix_length)
dt_test_prefixes.to_pickle(os.path.join(results_dir, "dt_test_prefixes.pkl"))

dt_val_prefixes = dataset_manager.generate_prefix_data(val, min_prefix_length, max_prefix_length)
dt_val_prefixes.to_pickle(os.path.join(results_dir, "dt_val_prefixes.pkl"))
70/28:

# encode all prefixes
feature_combiner = FeatureUnion(
    [(method, EncoderFactory.get_encoder(method, **cls_encoder_args)) for method in ["static", "agg"]])
print("Start encoding...")

# train
X_train = feature_combiner.fit_transform(dt_train_prefixes)
y_train = dataset_manager.get_label_numeric(dt_train_prefixes)
train_data = pd.concat([pd.DataFrame(X_train), pd.DataFrame(y_train), ], axis=1)  # pd.DataFrame(X_val)])
70/29:

del X_test
del y_test

# Valid
X_val = feature_combiner.fit_transform(dt_val_prefixes)
y_val = dataset_manager.get_label_numeric(dt_val_prefixes)
valid_data = pd.concat([pd.DataFrame(X_val), pd.DataFrame(y_val)], axis=1)  # pd.DataFrame(X_val)])
70/30:

# Valid
X_val = feature_combiner.fit_transform(dt_val_prefixes)
y_val = dataset_manager.get_label_numeric(dt_val_prefixes)
valid_data = pd.concat([pd.DataFrame(X_val), pd.DataFrame(y_val)], axis=1)  # pd.DataFrame(X_val)])
70/31:
del X_val
del y_val

print("Read encoded data...")
df_agg = pd.read_csv('dt_transformed_agg.csv', sep=';')
df_static = pd.read_csv('dt_transformed_static.csv', sep=';')

static_agg_df = pd.concat([df_static, df_agg], axis=1)
cat_feat_idx = np.where(static_agg_df.dtypes != float)[0]

#  rename columns
train_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
test_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
valid_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
70/32:

# test
X_test = feature_combiner.fit_transform(dt_test_prefixes)
y_test = dataset_manager.get_label_numeric(dt_test_prefixes)
test_data = pd.concat([pd.DataFrame(X_test), pd.DataFrame(y_test)], axis=1)  # pd.DataFrame(X_val)])
70/33:

#  rename columns
train_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
test_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
valid_data.columns = list(static_agg_df.columns) + ["Outcome"]  # + ["Treatment"]
70/34: train_data.to_pickle(os.path.join(results_dir, "train_data.pkl"))
70/35: valid_data.to_pickle(os.path.join(results_dir, "valid_data.pkl"))
70/36: test_data.to_pickle(os.path.join(results_dir, "test_data.pkl"))
70/37:

y_train = train_data['Outcome']
X_train = train_data.drop(['Outcome', ], axis=1)

y_valid = valid_data['Outcome']
X_valid = valid_data.drop(['Outcome'], axis=1)

y_test = test_data['Outcome']
X_test = test_data.drop(['Outcome'], axis=1)
70/38:
print("Create modle...")
print(f"Cat_feat_idx: {cat_feat_idx}")
70/39:

# Ensemble of CatBoost
class Ensemble(object):

    def __init__(self, esize=10, iterations=1000, lr=0.1, random_strength=0, border_count=128, depth=6, seed=100, best_param=None):

        self.seed = seed
        self.esize = esize
        self.depth = depth
        self.iterations = iterations
        self.lr = lr  # from tunning
        self.random_strength = random_strength
        self.border_count = border_count
        self.best_param = best_param
        self.ensemble = []
        for e in range(self.esize):
            model = CatBoostClassifier(iterations=self.iterations,
                                       depth=self.depth,
                                       border_count=self.border_count,
                                       random_strength=self.random_strength,
                                       loss_function='Logloss',  # -ve likelihood
                                       verbose=False,
                                       bootstrap_type='Bernoulli',
                                       posterior_sampling=True,
                                       eval_metric='AUC',
                                       use_best_model=True,
                                       langevin=True,
                                       learning_rate=self.best_param['learning_rate'],
                                       subsample=self.best_param['subsample'],
                                       random_seed=self.seed + e)
            self.ensemble.append(model)

    def fit(self, X_train, y_train, cat_feat_idx, eval_set=None):
        for m in self.ensemble:
            print(f"\nFitting model...")
            m.fit(X_train, y=y_train, cat_features=cat_feat_idx,  eval_set=(X_valid, y_valid))
            print("best iter ", m.get_best_iteration())
            print("best score ", m.get_best_score())

    def predict_proba(self, x):
        probs = []
        for m in self.ensemble:
            prob = m.predict_proba(x)
            probs.append(prob)
        probs = np.stack(probs)
        return probs

    def predict(self, x):
        preds = []
        for m in self.ensemble:
            pred = m.predict(x)
            preds.append(pred)
        preds = np.stack(preds)
        return preds
70/40:

# Ensemble of CatBoost
class Ensemble(object):

    def __init__(self, esize=10, iterations=1000, lr=0.1, random_strength=0, border_count=128, depth=6, seed=100, best_param=None):

        self.seed = seed
        self.esize = esize
        self.depth = depth
        self.iterations = iterations
        self.lr = lr  # from tunning
        self.random_strength = random_strength
        self.border_count = border_count
        #self.best_param = best_param
        self.ensemble = []
        for e in range(self.esize):
            model = CatBoostClassifier(iterations=self.iterations,
                                       depth=self.depth,
                                       border_count=self.border_count,
                                       random_strength=self.random_strength,
                                       loss_function='Logloss',  # -ve likelihood
                                       verbose=False,
                                       bootstrap_type='Bernoulli',
                                       posterior_sampling=True,
                                       eval_metric='AUC',
                                       use_best_model=True,
                                       langevin=True,
                                       #learning_rate=self.best_param['learning_rate'],
                                       #subsample=self.best_param['subsample'],
                                       random_seed=self.seed + e)
            self.ensemble.append(model)

    def fit(self, X_train, y_train, cat_feat_idx, eval_set=None):
        for m in self.ensemble:
            print(f"\nFitting model...")
            m.fit(X_train, y=y_train, cat_features=cat_feat_idx,  eval_set=(X_valid, y_valid))
            print("best iter ", m.get_best_iteration())
            print("best score ", m.get_best_score())

    def predict_proba(self, x):
        probs = []
        for m in self.ensemble:
            prob = m.predict_proba(x)
            probs.append(prob)
        probs = np.stack(probs)
        return probs

    def predict(self, x):
        preds = []
        for m in self.ensemble:
            pred = m.predict(x)
            preds.append(pred)
        preds = np.stack(preds)
        return preds
70/41:

# eoe: Total uncer: entropy of the avg predictions
def entropy_of_expected(probs, epsilon=1e-10):
    mean_probs = np.mean(probs, axis=0)
    log_probs = -np.log(mean_probs + epsilon)
    return np.sum(mean_probs * log_probs, axis=1)


# Data uncer: avg(entropy of indviduals)
def expected_entropy(probs, epsilon=1e-10):
    log_probs = -np.log(probs + epsilon)

    return np.mean(np.sum(probs * log_probs, axis=2), axis=0)


# Knowledge uncer
def mutual_information(probs, epsilon):
    eoe = entropy_of_expected(probs, epsilon)
    exe = expected_entropy(probs, epsilon)
    return eoe - exe  # knowldge_ucer = total_uncer - data_uncer


def ensemble_uncertainties(probs, epsilon=1e-10):
    #print(f"Probs: {np.max(probs)}")
    print(f"Ensemble size: {len(probs)}\n")
    mean_probs = np.mean(probs, axis=0)  # avg ensamble prediction
    conf = np.max(mean_probs, axis=1)  # max avg ensamble prediction: predicted class

    eoe = entropy_of_expected(probs, epsilon)
    exe = expected_entropy(probs, epsilon)
    mutual_info = eoe - exe

    uncertainty = {'confidence': conf,
                   'entropy_of_expected': eoe,  # Total uncer: entropy of the avg predictions
                   'expected_entropy': exe,  # Data uncer: avg(entropy of indviduals)
                   'mutual_information': mutual_info,  # Knowledge uncer
                   }
    print(f"total_uncer: {eoe}")
    print(f"len total_uncer: {len(eoe)}\n")

    print(f"Data_uncer: {exe}")
    print(f"len Data_uncer: {len(exe)}\n")

    print(f"Knowldge_uncer: {mutual_info}")
    print(f"len Knowldge_uncer: {len(mutual_info)}\n")

    return uncertainty
70/42: ens = Ensemble(esize=en_size, iterations=1000, lr=0.1, depth=6, seed=2, random_strength = 100,)
70/43: ens.fit(X_train, y_train, cat_feat_idx,)
70/44:
import pickle
with open('my_trained_ensemble_model.pkl', 'wb') as f:
    pickle.dump(ens, f)
70/45:

probs_train = ens.predict_proba(X_train)
probs_test = ens.predict_proba(X_test)
probs_valid = ens.predict_proba(X_valid)

preds_train_e = ens.predict(X_train)
preds_test_e = ens.predict(X_test)
preds_valid_e = ens.predict(X_valid)


probs_train_mean = np.mean(ens.predict_proba(X_train), axis=0)
probs_test_mean = np.mean(ens.predict_proba(X_test), axis=0)
probs_valid_mean = np.mean(ens.predict_proba(X_valid), axis=0)

uncerts_train = ensemble_uncertainties(probs_train)
uncerts_test = ensemble_uncertainties(probs_test)
uncerts_valid = ensemble_uncertainties(probs_valid)


print("Predict train...")
preds_train_prob_1 = probs_train_mean[:, 1]
preds_train_prob_0 = probs_train_mean[:, 0]
preds_train = np.array(pd.DataFrame(preds_train_e).mode().iloc[0].astype(int))

#np.array(pd.DataFrame(preds).mode().iloc[0].astype(int))

print("Predict test...")
preds_test_prob_1 = probs_test_mean[:, 1]
preds_test_prob_0 = probs_test_mean[:, 0]
preds_test = np.array(pd.DataFrame(preds_test_e).mode().iloc[0].astype(int))

print("Predict valid")
preds_valid_prob_1 = probs_valid_mean[:, 1]
preds_valid_prob_0 = probs_valid_mean[:, 0]
preds_valid = np.array(pd.DataFrame(preds_valid_e).mode().iloc[0].astype(int))

print("Save results")
# write train set predictions
dt_preds_train = pd.DataFrame({"predicted_proba_0": preds_train_prob_0,
                               "predicted_proba_1": preds_train_prob_1,
                               "predicted": preds_train,
                               "actual": y_train,
                               "total_uncer": uncerts_train['entropy_of_expected'],
                              "data_uncer": uncerts_train['expected_entropy'],
                                "knowledge_uncer": uncerts_train["mutual_information"],
                                "confidence": uncerts_train["confidence"] })
dt_preds_train.to_pickle(os.path.join(results_dir, "preds_train_%s.pkl" % dataset_name))

# write test set predictions
dt_preds_test = pd.DataFrame({"predicted_proba_0": preds_test_prob_0,
                              "predicted_proba_1": preds_test_prob_1,
                              "predicted": preds_test,
                              "actual": y_test,
                               "total_uncer": uncerts_test['entropy_of_expected'],
                              "data_uncer": uncerts_test['expected_entropy'],
                                "knowledge_uncer": uncerts_test["mutual_information"],
                                "confidence": uncerts_test["confidence"] })
dt_preds_test.to_pickle(os.path.join(results_dir, "preds_test_%s.pkl" % dataset_name))

# write valid set predictions
dt_preds_valid = pd.DataFrame({"predicted_proba_0": preds_valid_prob_0,
                               "predicted_proba_1": preds_valid_prob_1,
                               "predicted": preds_valid,
                               "actual": y_valid,
                               "total_uncer": uncerts_valid['entropy_of_expected'],
                              "data_uncer": uncerts_valid['expected_entropy'],
                                "knowledge_uncer": uncerts_valid["mutual_information"],
                                "confidence": uncerts_valid["confidence"]})
dt_preds_valid.to_pickle(os.path.join(results_dir, "preds_valid_%s.pkl" % dataset_name))

print("write train-val set predictions CSV")
dt_preds_train.to_csv(os.path.join(results_dir, "preds_train_%s.csv" % dataset_name), sep=";", index=False)
dt_preds_valid.to_csv(os.path.join(results_dir, "preds_val_%s.csv" % dataset_name), sep=";", index=False)
dt_preds_test.to_csv(os.path.join(results_dir, "preds_test_%s.csv" % dataset_name), sep=";", index=False)
70/46:  probs_valid_mean
70/47:  preds_valid
70/48: np.max(probs_valid_mean, axis=1)
70/49: preds_valid_e
70/50: probs_valid_mean
70/51: np.max(probs_valid_mean, axis=1)
70/52: np.argmax(probs_valid_mean, axis=1)
70/53:  preds_valid
70/54: preds_valid
70/55: probs_valid_mean
70/56: y_valid
70/57: np.argmax(probs_valid_mean, axis=1)
70/58: np.max(probs_valid_mean, axis=1)
70/59: y_pred_valid = preds_valid
70/60: y_pred_proba_valid = probs_valid_mean
70/61: y_pred_proba_max_valid = np.max(probs_valid_mean, axis=1)
70/62:
alpha = np.round(np.arange(0.1, 1.0, 0.1), 1)
alpha
70/63:
#function to calculate q_yhat

def get_q_hat(pred_proba_cal, y_cal, alpha):
    N = pred_proba_cal.shape[0]
    scores = np.zeros(N) # non-conformity scores
    
    for i in range(N):
        true_class_proba = pred_proba_cal[i][y_cal[i]] # predicted proba of the true class, y_cal[i]: to get the true class
        # InverseProbabilityErrFunc - non-conformity scores
        scores[i] = 1 - true_class_proba # probs of the opposite class, s1, s2, .., sn
        
    q_yhat = np.quantile(scores, np.ceil((N + 1) * (1 - alpha)) / N) # quantile of the non-conformity scores
    #print(f"Scores: {scores}")
    return q_yhat
70/64:
# get q_hat for different alhpa

qhat_alpha = {a: get_q_hat(y_pred_proba_valid, y_valid, a) for a in alpha}# {alhp: q_hat}
qhat_alpha
70/65:
# Saving the objects:
with open('qhat.pkl', 'w') as f:  # Python 3: open(..., 'wb')
    pickle.dump([qhat_alpha], f)
70/66:
#function to get predict sets: Naive method

def get_pred_set_naive(model, X_val, y_val, q_yhat):
    softmax_outputs = model.predict_proba(X_val) # probs for test set
    N = softmax_outputs.shape[0] # how many rows in the test set
    
    pred_sets = [] # pred set
    
    for i in range(N): # for each row
        aux=[]
        for j in range(softmax_outputs.shape[1]): # loop over the number of classes
            if softmax_outputs[i][j] >= 1-q_yhat: # pred_proba[class_0 | 1] > 
                aux.append(j)
        pred_sets.append(aux)
        
    return pred_sets
70/67:
pred_sets = {alpha: get_pred_set_naive(xgbm,X_test,y_test,qhat) for alpha, qhat in qhat_alpha.items()}# {alhp: q_hat}
pred_sets
70/68:
pred_sets = {alpha: get_pred_set_naive(ens,X_test,y_test,qhat) for alpha, qhat in qhat_alpha.items()}# {alhp: q_hat}
pred_sets
70/69: softmax_outputs = ens.predict_proba(X_test)
70/70: softmax_outputs
70/71:
#function to get predict sets: Naive method

def get_pred_set_naive(model, X_val, y_val, q_yhat):
    #softmax_outputs = model.predict_proba(X_val) # probs for test set
    softmax_outputs = np.mean(model.predict_proba(X_val), axis=0)
    N = softmax_outputs.shape[0] # how many rows in the test set
    
    pred_sets = [] # pred set
    
    for i in range(N): # for each row
        aux=[]
        for j in range(softmax_outputs.shape[1]): # loop over the number of classes
            if softmax_outputs[i][j] >= 1-q_yhat: # pred_proba[class_0 | 1] > 
                aux.append(j)
        pred_sets.append(aux)
        
    return pred_sets
70/72:
pred_sets = {alpha: get_pred_set_naive(ens,X_test,y_test,qhat) for alpha, qhat in qhat_alpha.items()}# {alhp: q_hat}
pred_sets
70/73: len(pred_sets[0.1])
70/74: pred_sets[0.1]
70/75: df_test_result = pd.DataFrame(probs_test_mean, columns=['predicted_proba_0', 'predicted_proba_1'])
70/76: df_test['actual'] = y_test
70/77: df_test_result['actual'] = y_test
70/78: df_test_result['predicted'] = preds_test
70/79:
# Predictive part
df_test_result["prefix_nr"]= list(dt_test_prefixes.groupby("Case ID").first()["prefix_nr"])
df_test_result["case_id"]= list(dt_test_prefixes.groupby("Case ID").first()["orig_case_id"])
df_test_result["activity"]= list(dt_test_prefixes.groupby("Case ID").last()["Activity"])
df_test_result['time:timestamp'] = list(dt_test_prefixes.groupby("Case ID").last()["time:timestamp"])
df_test_result = df_test_result.sort_values(by=['time:timestamp']).reset_index(drop=True)
df_test_result
70/80:
for a in alpha:
    print(a)
    df_test_result["alpha="+str(a)]=pred_sets[a]
70/81:
# Size for each prediction set
my_dict={}
my_dict_alpha = {}
import pandas as pd
for a in alpha:
    my_dict={}
    print(f"Alpha: {a}")
    #print(len(pd.Series(pred_sets[a]).value_counts().index[:].to_list()))
    for i in range(len(pd.Series(pred_sets[a]).value_counts().index[:].to_list())):
        #print(i)
        my_dict[str(pd.Series(pred_sets[a]).value_counts().index[:].to_list()[i])]=pd.Series(pred_sets[a]).value_counts().to_list()[i]
        #break
    my_dict_alpha[a]=my_dict
    
    #print(pd.Series(pred_sets[a]).value_counts().index[:].to_list())
    #print(pd.Series(pred_sets[a]).value_counts().to_list()[:])
    #print("")
70/82: my_dict_alpha
70/83:
import matplotlib.pyplot as plt


def plot_pred_sets(alpha, data):
    # creating the dataset
    data = data
    courses = list(data.keys())
    values = list(data.values())


    colors = {"#1f77b4", "#ff7f0e", "#2ca02c",}
    fig, ax =  plt.subplots()

    # creating the bar plot
    ax.bar(courses, values, color =colors,
            width = 0.4)

    for bar in ax.patches:
        ax.annotate(text = bar.get_height(),
                      xy = (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      ha='center', 
                      va='center',
                      size=15,
                      xytext=(0, 8),
                      textcoords='offset points')



    plt.xlabel("Prediction sets")
    plt.ylabel(f"No. of instances")
    plt.title(f"Cases in different prediction sets: alpha={alpha}")
    plt.grid()
    plt.tight_layout()
    plt.show()

for key, ele in my_dict_alpha.items():
    print(f"Alpha: {key}")
    print(f"Pred_sets: {ele}")
    plot_pred_sets(key, ele)
70/84:
import matplotlib.pyplot as plt


def plot_pred_sets(alpha, data):
    # creating the dataset
    data = data
    courses = list(data.keys())
    values = list(data.values())


    colors = {"#1f77b4", "#ff7f0e", "#2ca02c",}
    fig, ax =  plt.subplots()

    # creating the bar plot
    ax.bar(courses, values, color =colors,
            width = 0.4)

    for bar in ax.patches:
        ax.annotate(text = bar.get_height(),
                      xy = (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      ha='center', 
                      va='center',
                      size=15,
                      xytext=(0, 8),
                      textcoords='offset points')



    plt.xlabel("Prediction sets")
    plt.ylabel(f"No. of instances")
    plt.title(f"Cases in different prediction sets: alpha={alpha}")
    plt.grid()
    plt.tight_layout()
    plt.savefig(f'x_{alpha}.png')
    plt.show()

for key, ele in my_dict_alpha.items():
    print(f"Alpha: {key}")
    print(f"Pred_sets: {ele}")
    plot_pred_sets(key, ele)
70/85:
for i in range(len(pred_sets)):
    print(f"true label is: {y_test[i]}")
    print(pred_sets[0.8][i])
    #break
    if y_test[i] in pred_sets[0.8][i]:
        print("true label in the prediction set\n")
70/86:
for i in range(len(pred_sets)):
    print(f"true label is: {y_test[i]}")
    print(pred_sets[0.1][i])
    #break
    if y_test[i] in pred_sets[0.1][i]:
        print("true label in the prediction set\n")
70/87:
#function to evaluate coverage
# compare true label with the prediction sets
# https://towardsdatascience.com/conformal-prediction-4775e78b47b6

def calculate_coverage(pred_sets, y_true): # pred_set and true test labels as input
    s=0    
    for i in range(len(pred_sets)):
        if y_true[i] in pred_sets[i]:
            s+=1
    
    return s/len(y_true)
70/88:
coverage_dict = {a: calculate_coverage(pred_sets[a],y_test) for a in alpha }
coverage_dict
70/89:
for a in alpha:
    #print(a)
    print(f"coverage with alpha: {a} is {calculate_coverage(pred_sets[a],y_test)}")
70/90:
for a in alpha:    
    sets_dim=[len(set_conf) for set_conf in pred_sets[a]]
    plt.bar(dict(pd.Series(sets_dim).value_counts()).keys(),dict(pd.Series(sets_dim).value_counts()).values())
    plt.xlabel('Set sizes')
    plt.ylabel('Frequency')
    plt.title(f'Naive method alpha={a}')
    plt.savefig(f'coverage_{a}.png')
    plt.show()
70/91:
for a in alpha:
    
    d1=np.zeros(10)
    d2=np.zeros(10)

    for i in range(len(pred_sets[a])):
        d2[y_test[i]]+=1

        if y_test[i] in pred_sets[a][i]:
            d1[y_test[i]]+=1




    plt.bar([i for i in range(10)],d1/d2)
    plt.axhline(y=0.9, color='r', linestyle='--')
    plt.title(f'Naive method coverage: {a}')
    #plt.legend()
    plt.xlabel('Class')
    plt.ylabel('Coverage')
    plt.savefig(f'coverage2_{a}.png')
    plt.show()
70/92: df_test_result
70/93: df_test_result.to_csv(os.path.join(results_dir, "df_results_tests.csv"), sep=";", index=False)
70/94: pred_sets
70/95:
f = open('pred_sets.pckl', 'wb')
pickle.dump(pred_sets, f)
f.close()
70/96:
f = open('qhat.pckl', 'wb')
pickle.dump(qhat_alpha, f)
f.close()
72/1: %history -g -f ipython_history
73/1: %history -g -f ipython_history.txt
   1: %history -g -f ipython_history.py
