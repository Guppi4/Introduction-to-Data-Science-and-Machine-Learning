#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas   as pd
import numpy as np


import matplotlib.pyplot as plt
import seaborn as sns

# In[9]:


data = {'type': ['A', 'A', 'B', 'B'], 'value': [10, 14, 12, 23]}

# In[10]:


my_data = pd.DataFrame.from_dict(data)

# In[11]:


my_data.head()

# In[12]:


my_data.dtypes

# In[14]:


df = pd.read_csv('https://stepik.org/media/attachments/course/4852/my_stat.csv')

# In[16]:


df.head()

# In[28]:


subset_1 = df.iloc[:10, [0, 2]]

# In[25]:


df.dtypes

# In[29]:


subset_1

# In[35]:


subset_3 = df.drop([0, 4])

# In[33]:




# In[34]:


subset_2 = subset_3.iloc[:, [1, 3]]

# In[39]:


subset_11 = df[(df['V1'] > 0) & (df['V3'] == 'A')]

# In[40]:


subset_11

# In[57]:


V5 = df[['V1', 'V4']].sum(axis=1)

#

# In[51]:


V5.dtype

# In[50]:


V6 = np.log([8, np.e, np.e ** 2, 0])

# ######

# In[49]:


V6

# In[58]:


V5

# In[59]:


V5.to_frame()

# In[60]:


V5

# In[61]:


V5 = V5.to_frame()

# In[62]:


V5

# In[230]:


my_stat = pd.read_csv('https://stepik.org/media/attachments/course/4852/my_stat_1.csv')

# In[231]:


my_stat.head()

# In[228]:


my_stat['session_value'] = my_stat['session_value'].fillna(0)

# In[202]:


m = my_stat.loc[my_stat['n_users'] >= 0, 'n_users'].median()

# In[229]:


my_stat

# m

# In[192]:


m

# In[147]:


my_stat[my_stat['n_users'] <= 0] = my_stat[my_stat['n_users'] >= 0].median().astype('int')

# In[170]:


m

# In[199]:


my_stat[my_stat['n_users'] <= 0] = m

# In[200]:


my_stat

# In[232]:


my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename(index=str, columns={
    'session_value': 'mean_session_value'})

# In[233]:


mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename(index=str,
                                                                                                         columns={
                                                                                                             'session_value': 'mean_session_value'})

# In[234]:


mean_session_value_data

# In[237]:


mean_session_value_data = my_stat.groupby('group', as_index=False).agg({'session_value': 'mean'}).rename(index=str,
                                                                                                         columns={
                                                                                                             'session_value': 'mean_session_value'})

# In[ ]:



