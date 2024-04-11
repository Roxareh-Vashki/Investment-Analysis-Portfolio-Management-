#!/usr/bin/env python
# coding: utf-8

# In[145]:


import pandas as pd
import numpy as np
# use the yahoo finance API
import yfinance
from scipy.stats import linregress


# In[146]:


data_aapl = yfinance.download("AAPL",
                         start = "2014-03-08",
                         end = "2024-03-08",       
                         period = "1w")


# In[147]:


data_aapl.head()


# In[148]:


df_aapl = data_aapl [[ 'Adj Close']]
df_aapl


# In[149]:


data_sp500 = yfinance.download("^GSPC",
                         start = "2014-03-08",
                         end = "2024-03-08",       
                         interval = "1d")


# In[150]:


data_sp500.head()


# In[151]:


df_sp500 = data_sp500 [[ 'Adj Close']]
df_sp500


# In[152]:


# Merge based on common values in columns 'Date' and 'Date'
df = pd.merge(df_aapl, df_sp500, left_on='Date', right_on='Date', how='left')
df


# In[153]:


new_col_names = ['r_company' , 'r_sp500']
df.columns = new_col_names
df.head()


# In[154]:


#calculating cov manually using function


def beta(df, company_price_col_name, sp500_price_col_name) :
    returns_df = df.pct_change(1)                 # returns
    returns_df.dropna(inplace = True)
    returns_df['company_deviations'] = returns_df['r_company'] - returns_df['r_company'].mean()         #deviations
    returns_df['sp500_deviations'] = returns_df['r_sp500'] - returns_df['r_sp500'].mean()      #deviations
    returns_df['product_deviations'] = returns_df['company_deviations'] * returns_df['sp500_deviations']          #product of deviations
    cov_company_sp500 = returns_df['product_deviations'].sum() / (len(returns_df['product_deviations']) - 1)      # cov
    
    # var
    returns_df['squared_deviations'] = returns_df['sp500_deviations'] ** 2
    sum_squared_deviations = np.sum(returns_df['squared_deviations'])
    var_sp500 = sum_squared_deviations / (len(returns_df['squared_deviations']) - 1)
    
    #beta
    beta_company = cov_company_sp500 / var_sp500
    return beta_company


# In[155]:


beta(df,'r_company', 'r_sp500')


# In[156]:


# calculating cov manually


# In[157]:


new_col_names = ['r_aapl' , 'r_sp500']
df.columns = new_col_names


# In[158]:


returns_df = df.pct_change(1).dropna()


# In[159]:


returns_df.head()


# In[160]:


#returns_df.dropna(inplace = True)


# In[161]:


returns_df['aapl_deviations'] = returns_df['r_aapl'] - returns_df['r_aapl'].mean()
returns_df['sp500_deviations'] = returns_df['r_sp500'] - returns_df['r_sp500'].mean()


# In[162]:


returns_df.head()


# In[163]:


returns_df['product_deviations'] = returns_df['aapl_deviations'] * returns_df['sp500_deviations']


# In[164]:


returns_df.head()


# In[165]:


cov_aapl_sp500 = returns_df['product_deviations'].sum() / (len(returns_df['product_deviations']) - 1)


# In[166]:


cov_aapl_sp500


# In[167]:


# using numby cov function
np.cov(returns_df['r_sp500'], returns_df['r_aapl'])[0][1]


# In[168]:


# var
returns_df['squared_deviations'] = returns_df['sp500_deviations'] ** 2
sum_squared_deviations = np.sum(returns_df['squared_deviations'])
var_sp500 = sum_squared_deviations / (len(returns_df['squared_deviations']) - 1)
var_sp500


# In[169]:


# beta
beta_aapl = cov_aapl_sp500 / var_sp500
beta_aapl


# In[170]:


#calculating beta using linregress

linregress(y = returns_df['r_aapl'], x = returns_df['r_sp500'])


# In[ ]:




