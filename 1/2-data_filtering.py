#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

# In[35]:


students_perfomance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')

# In[36]:


students_perfomance.dtypes

# In[25]:


students_perfomance.head()

# In[28]:


students_perfomance.iloc[0:3, 0:5]

# In[29]:


students_perfomance.iloc[[0, 3], [0, 5]]

# In[32]:


students_perfomance.loc[:7]

# In[33]:


students_perfomance.iloc[:7]

# In[34]:


students_perfomance.loc[0:7]
students_perfomance.loc[0:7]

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

# In[46]:


titanic.loc(titanic.lunch == 'free/reduced').mean()

# In[47]:


titanic

# In[49]:


students_perfomance.loc(students_perfomance.lunch == 'free/reduced').mean()

# In[50]:


students_perfomance.lunch.type()

# In[51]:


students_perfomance.lunch.type

# In[52]:


students_perfomance.dtypes

# In[53]:


students_perfomance.loc(students_perfomance.lunch == free / reduced).mean()

# In[54]:


students_perfomance.loc(students_perfomance.lunch == 'free/reduced').mean()

# In[56]:


len(t.index)

# In[57]:


t = students_perfomance.loc[students_perfomance.lunch == 'free/reduced']

# In[58]:


len(t.index)

# In[60]:


len(t) / len(students_perfomance)

# In[61]:


len(t)

# In[62]:


len(students_perfomance)

# In[63]:


t = students_perfomance.loc[students_perfomance.lunch == 'free/reduced']

# In[64]:


len(t)

# In[65]:


len(t) / len(students_perfomance)

# In[66]:


students_perfomance

# In[67]:


students_perfomance.head(20)

# In[68]:


ce.loc[students_perfomance.lunch == 'free/reduced'].mean()

# In[73]:


t = students_perfomance.loc[students_perfomance.lunch == 'free/reduced']

# In[74]:


t.mean()

# In[75]:


t.var()

# In[76]:


t1 = students_perfomance.loc[students_perfomance.lunch == 'standard']

# In[77]:


t1.mean()

# In[79]:


t1.var()

# In[4]:


students_perfomance

# In[5]:


students_perfomance.head()

# In[7]:


students_perfomance = students_perfomance.rename(columns=
                                                 {'parental level of education': 'parental_level_of_education',
                                                  'test preparation course': 'test_preparation_course',
                                                  'math score': 'math_score',
                                                  'reading score': 'reading_score',
                                                  'writing score': 'writing_score'})

# In[8]:


students_perfomance.head()

# In[34]:


students_perfomance[['math_score', 'reading_score']].head()

# In[15]:


students_perfomance[col].head()

# In[38]:


students_perfomance1 = students_perfomance
columns = list(students_perfomance1)
score_columns = [column for column in columns if 'score' in column]

# In[40]:


students_perfomance[score_columns].head()

# In[ ]:
