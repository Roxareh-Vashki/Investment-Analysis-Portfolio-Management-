#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np


# In[46]:


aapl = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\AAPL.csv")
aapl.head()


# In[47]:


googl = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\GOOGL.csv")
googl.head()


# In[48]:


meta = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\META.csv")
meta.head()


# In[49]:


amz = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\AMZ.csv")
amz.head()


# In[50]:


msft= pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\MSFT.csv")
msft.head()


# In[51]:


dell = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\DELL.csv")
dell.head()


# In[52]:


tsla = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\TSLA.csv")
tsla.head()


# In[58]:


ibm = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\IBM.csv")
ibm.head()


# In[59]:


gld = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\GLD.csv")
gld.head()


# In[60]:


nvda = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\28\NVDA.csv")
nvda.head()


# In[61]:


df1 = pd.merge(aapl, googl, left_on='Date', right_on='Date', how='left')
df1


# In[62]:


df2 = pd.merge(meta, amz, left_on='Date', right_on='Date', how='left')
df2


# In[63]:


df3 = pd.merge(msft, dell, left_on='Date', right_on='Date', how='left')
df3


# In[73]:


df4 = pd.merge(tsla, ibm, left_on='Date', right_on='Date', how='left')
df4


# In[74]:


df5 = pd.merge(gld, nvda, left_on='Date', right_on='Date', how='left')
df5


# In[75]:


df12 = pd.merge(df1, df2, left_on='Date', right_on='Date', how='left')
df12


# In[76]:


df34 = pd.merge(df3, df4, left_on='Date', right_on='Date', how='left')
df34


# In[77]:


df1234 = pd.merge(df12, df34, left_on='Date', right_on='Date', how='left')
df1234


# In[78]:


df = pd.merge(df1234, df5, left_on='Date', right_on='Date', how='left')
df


# In[79]:


df.set_index('Date', inplace = True)


# In[80]:


df.head()


# In[81]:


new_col_names = ['aapl' , 'googl', 'meta', 'amz', 'msft', 'dell', 'tsla', 'ibm', 'gld', 'nvda']
df.columns = new_col_names
df.head()


# In[82]:


returns_df = df.pct_change(1)


# In[83]:


returns_df.head()


# In[84]:


num_stocks = 10
weights = [1 / num_stocks] * num_stocks       #weight


# In[85]:


weights


# In[86]:


vcv_matrix = returns_df.cov()              #vcv matrix


# In[87]:


vcv_matrix


# In[88]:


var_p = np.dot(np.transpose(weights), np.dot(vcv_matrix, weights))


# In[89]:


var_p


# In[90]:


sd_p = np.sqrt(var_p) 


# In[91]:


sd_p


# In[92]:


sd_p_annual = sd_p * np.sqrt(250)


# In[93]:


sd_p_annual


# In[94]:


individual_risks = np.std(returns_df) * np.sqrt(250)


# In[96]:


individual_risks


# In[ ]:




