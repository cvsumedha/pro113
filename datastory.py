import pandas as pd
import statistics as st
import plotly.express as px

df=pd.read_csv("savings_data_final.csv")


fig=px.scatter(df,x="age" , y="quant_saved" , color="rem_any")
fig.show()

import csv
import plotly.graph_objects as go
with open("savings_data_final.csv",newline="" ) as f:
  file1=csv.reader(f)
  data1=list(file1)
  
data1.pop(0)
print(data1)
total_people=len(data1)
reminder_people=0
for i in data1:
  if(int(i[3])==1):
    reminder_people=reminder_people+1

fig=go.Figure(go.Bar(x=["reminded","not reminded"] , y=[reminder_people,(total_people-reminder_people)]))
fig.show()

savings=[]
for i in data1:
  savings.append(float(i[0]))
print("mean:",st.mean(savings))
print("median:",st.median(savings))
print("mode:",st.mode(savings))

rem_sav=[]
not_rem_sav=[]
for i in data1:
  if int(i[3])==1:
    rem_sav.append(float(i[0]))
  else:
    not_rem_sav.append(float(i[0]))

print("mean:",st.mean(rem_sav))
print("median:",st.median(rem_sav))
print("mode:",st.mode(rem_sav))

print("\n\n")

print("mean:",st.mean(not_rem_sav))
print("median:",st.median(not_rem_sav))
print("mode:",st.mode(not_rem_sav))

print("std all:",st.stdev(savings))
print("std reminded people:",st.stdev(rem_sav))
print("mod:",st.stdev(not_rem_sav))

q1=df['quant_saved'].quantile(0.25)
q3=df['quant_saved'].quantile(0.75)
iqr=q3-q1
lw=q1-1.5*iqr
uw=q3+1.5*iqr
newdf=df[df['quant_saved']<uw]
print (len(newdf))
print (len(df))

savings=newdf['quant_saved'].tolist()
print("mean: ",st.mean(savings))
print("median: ",st.median(savings))
print("mode: ",st.mode(savings))
print("stdev: ",st.stdev(savings))

import random
samples=[]
for i in range(1000):
  temp_list=[]
  for j in range(100):
    temp_list.append(random.choice(savings))
  samples.append(st.mean(temp_list))
final_mean=st.mean(samples)
final_std=st.stdev(samples)
print("Final mean: ",final_mean)
print("Final stdev: ",final_std)
