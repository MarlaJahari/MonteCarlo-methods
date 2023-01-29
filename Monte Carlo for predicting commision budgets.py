#!/usr/bin/env python
# coding: utf-8

# In[39]:


import pandas as pd
import numpy as np
import seaborn as sns
avg=1
sd=0.1
no=500
n=1000
ptt=np.random.normal(avg,sd,no)
def cr(x):
    if x<=0.9:
        return 0.2
    elif x<=0.99:
        return 0.3
    else:
        return 0.4
        
#for numpys random choice weve to assign probabilities for each values in an array and no: of samples required second
stv=[75_000,100_000,150_000,200_000,250_000, 300_000] 
prob=[0.5,0.2,0.1,0.1,0.05,0.05]
st=np.random.choice(stv,no,p=prob)
df=pd.DataFrame(index=range(no),data={'Actual pt to target':ptt,'sales target':st})
df.head()
df['Actual pt to target'].plot(kind='hist', title='Historical % to Target Distribution')
df['sales target'].plot(kind='hist', title='Historical Sales Target Distribution')
#df[] to add more columns
df['sales']=(df['Actual pt to target']*df['sales target']).round(2)
df['Commision rate']=df['Actual pt to target'].apply(cr)

df['Commision']=df['sales']*df['Commision rate']

df.head()
df.describe()
allstars=[]
for i in range(n):
 ptt=np.random.normal(avg,sd,no) 
 st=np.random.choice(stv,no,p=prob)
 df=pd.DataFrame(index=range(no),data={'Actual pt to target':ptt,'sales target':st})
 df['sales']=(df['Actual pt to target']*df['sales target']).round(2)
 df['Commision rate']=df['Actual pt to target'].apply(cr)
 df['Commision']=df['sales']*df['Commision rate']
 allstars.append([df['sales'].sum().round(1),df['Commision'].sum().round(1),df['sales target'].sum().round(1)])  
res=pd.DataFrame.from_records(allstars,columns=['Sales','Commision Amount','Sales Target'])
res.describe().round(0).style.format('{:,}')
#res['Commision Amount'].plot(kind='hist',title="Tot commision amt")
res['Sales'].plot(kind='hist',title="SALES")


# In[ ]:





# In[ ]:




