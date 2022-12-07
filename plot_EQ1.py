import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sys import argv


dataset = argv[1]

df = pd.read_csv("./results_conformal/"+dataset+"/all_df.csv", sep=';')
print(df)

Class = df['index'].values.tolist()#["Fisrt","Second","Third","Fourth","Fifth"]


df = df.iloc[:, 1:]

colors = ['#148f77',"#b03a2e",'#2980B9',    "#839192", "#2e4053", "#884ea0" ,
          "#641e16","#d4ac0d", "#0b5345", "#82e0aa", "#e59866",
           "#597EBA", "#283807", "#DE0100"]



t_12 = 21461

ax = df.plot(stacked=True, kind='bar',figsize=(5, 5),)#color=colors)
hh = []
for bar in ax.patches:
    height = np.round(bar.get_height()/t_12, 2)
    hh.append(height)
    #print(height)
    if height ==0.0 or height<0.09:
        continue
    width = bar.get_width()
    x = bar.get_x()
    y = bar.get_y()
    label_text = height
    label_x = x + width / 2
    label_y = y + height / 2
    ax.text(label_x, label_y, label_text,ha='center', #rotation=10,# ha='center',     
            va='bottom',fontsize=10,)
    
# Set Tick labels

# ax.legend(bbox_to_anchor=(0.9, 1.4),
#                   fancybox=True, shadow=True,title = "Significance levels  (alpha)" , ncol=5,title_fontsize=13,prop={'size': 12,},)
# ax.get_legend().remove()
ax.set_xticklabels(Class,rotation='horizontal')

# Display chart

plt.grid(True)
plt.show()
plt.title(dataset.upper())

plt.savefig('EQ1_'+dataset+'.pdf')  

