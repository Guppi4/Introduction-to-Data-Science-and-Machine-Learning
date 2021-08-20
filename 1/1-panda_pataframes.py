#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np



# In[15]:


students_perfomance=pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')


# In[24]:


students_perfomance.dtypes


# In[25]:


students_perfomance.head()


# In[28]:


students_perfomance.iloc[0:3,0:5]


# In[29]:


students_perfomance.iloc[[0,3],[0,5]]


# In[32]:


students_perfomance.loc[:7]


# In[33]:


students_perfomance.iloc[:7]


# In[34]:


students_perfomance.loc[0:7]students_perfomance.loc[0:7]


# In[35]:


students_perfomance.iloc[:7]


# In[36]:


students_perfomance.head(7)


# In[37]:


students_perfomance.tail(7)


# In[38]:


students_perfomance.loc[:7]


# In[39]:


titanic = pd.read_csv('C:\Users\kiril\Downloads\TitaniC.csv')


# In[40]:


titanic = pd.read_csv('C:\Users\kiril\Downloads\titaniC.csv')


# In[41]:


titanic = pd.read_csv('C:\\Users\kiril\Downloads\TitaniC.csv')


# In[42]:


titanic.columns


# In[43]:


len(titanic.columns)


# In[44]:


titanic.shape


# In[45]:


titanic.dtypes.value_counts()


# In[ ]:


