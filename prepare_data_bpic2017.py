import matplotlib.pyplot as plt
import pandas as pd
from sys import argv
#import pickle5 as pickle
import pickle

# In[2]:


# read data and add label
file = "./data/bpic2017/bpic2017.csv"

def read_data(file):
    # read original data
    df = pd.read_csv(file, sep =';')
    #with open(file, "rb") as fh:
    #    df = pickle.load(fh)

    #df = pd.read_pickle(file)
    # delte old label
    del df['label']    
    return df



def add_label(file):    
    # function to cheack if a case contains A_Pending activity or not
    def check_A_Pending(gr):
        df = pd.DataFrame(gr)
        if  "A_Pending" in list(df['Activity']):
            df['label'] = "regular" 
        else:
            df['label'] = "deviant" 
        return df
    
    # read data and del old label
    df = read_data(file)
    
    # add new label for each case based on A_Pending
    df = df.groupby('Case ID').apply(check_A_Pending)
    df = df.reset_index(drop=True)
    return df

# fn to add #offers column to the original data based on "O_Created" Activity
def add_No_Of_Offers(df):
    # get all observations with O_Created activity
    tmp_df = df[df['Activity'] == "O_Created"]  # to count offers
    
    # count numbe rof offers for each case
    tmp_df2 = pd.DataFrame(tmp_df.groupby(['Case ID'])['Activity'].count()).reset_index()
    tmp_df2.columns = ['Case ID', 'NumberOfOffers']
    df = pd.merge(tmp_df2, df, on='Case ID')
    return df 
    
# function to add treatment based on the number of offers
def add_treatment(df):
    
    # function to cheack if a case contains A_Pending activity or not
    def check_NoOfOffers(gr):
        df = pd.DataFrame(gr)
        
        # case should be not treated if it receives more than one offer
        if  list(df['NumberOfOffers'])[0] <= 1:
            df['treatment'] = "treat"  # T=1
        else:
            df['treatment'] = "noTreat" # T=0
        return df
    

    # add new treatment for each case based on number of offers
    # cases with only one offer should be treated
    df = df.groupby('Case ID').apply(check_NoOfOffers)
    df = df.reset_index(drop=True)
    return df

df = add_label(file)
df = add_No_Of_Offers(df)
df = add_treatment(df)



# In[6]:

results_dir = "prepared_data"
import os
if not os.path.exists(os.path.join(results_dir)):
    os.makedirs(os.path.join(results_dir))

df.to_csv(results_dir + '/prepared_treatment_outcome_bpic2017.csv', index=False, sep=';')

# Save the prepared log for predicitve and prescriptive models
#df.to_csv('./prepare_data/prepared_treatment_outcome_bpic2017.csv', index=False, sep=';')
#import pickle5 as pickle
#with open("prepared_bpic2017.pkl", "rb") as fh:
#df.to_pickle("./prepare_data/prepared_bpic2017.pkl")
