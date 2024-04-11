#!/usr/bin/env python
# coding: utf-8

# In[17]:


get_ipython().system('pip install yfinance')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
# use the yahoo finance API
import yfinance


# In[18]:


# download historical data of APPLE
data = yfinance.download("AAPL",
                         start = "2000-01-01",
                         end = "2017-12-31",       
                         period = "1w")   # weekly prices


# In[4]:


#data = pd.read_csv(r"C:\Users\rokhs\OneDrive\Courses\Investment Analysis & Portfolio Management with Python\assignment\14\AAPL.csv")


# In[20]:


data.head()


# In[21]:


def getExpectedReturn(df, price_col_name, annualised=True, annualise_method='sophisticated'):
    """
    Returns the expected return of a stock given price data.
    """
    
    # Calculate returns of prices
    returns = df[price_col_name].pct_change(1)
    
    # Calculate the expected return usind the meam method
    expected_return_weekly = returns.mean()
    
    if annualised:
        if annualise_method == 'sophisticated':
            expected_return_annual = ((1 + expected_return_weekly) ** 52) - 1
        elif annualise_method == 'crude':
            # Crude method
            expected_return_annual = expected_return_weekly * 52
            
        return expected_return_annual
    else:
        return expected_return_weekly


# In[22]:


# Annualised Expected Return (sophisticated method)
getExpectedReturn(data, 'Adj Close')


# In[23]:


# weekly expected return
getExpectedReturn(data, 'Adj Close', annualised=False)


# In[24]:


# Annualised Expected Return (crude method)
getExpectedReturn(data, 'Adj Close', annualise_method = 'crude')


# In[ ]:




