
import pandas as pd
import numpy as np


# In[1]:


import pandas as pd
import numpy as np

# In[20]:


students_performance = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')

# In[7]:


students_performance.groupby('gender').aggregate({
    'math score': 'mean',
    'reading score': 'mean'})

# In[5]:


students_performance.head()

# In[9]:


students_performance.groupby('gender', as_index=false).aggregate({
    'math score': 'mean',
    'reading score': 'mean'})

# In[12]:


students_performance.groupby('gender', as_index=False).aggregate({'math score': 'mean', 'reading score': 'mean'})

# In[21]:


students_performance.sort_values(['math_score', 'gender'], ascending=False).groupby('gender').head(5)

# In[22]:


students_performance.head(5)

# In[23]:


students_perfomance = students_perfomance.rename(columns=
                                                 {'parental level of education': 'parental_level_of_education',
                                                  'test preparation course': 'test_preparation_course',
                                                  'math score': 'math_score',
                                                  'reading score': 'reading_score',
                                                  'writing score': 'writing_score'})

# In[26]:


students_performance = students_perfomance.rename(columns=
                                                  {'parental level of education': 'parental_level_of_education',
                                                   'test preparation course': 'test_preparation_course',
                                                   'math score': 'math_score',
                                                   'reading score': 'reading_score',
                                                   'writing score': 'writing_score'})

# In[27]:


students_performance.sort_values(['math_score', 'gender'], ascending=False).groupby('gender').head(5)

# In[28]:


students_performance.sort_values(['gender', 'math_score'], ascending=False).groupby('gender').head(5)

# In[30]:


students_performance.sort_values(['gender', 'math_score'], ascending=False).head(10)

# In[32]:


students_performance.sort_values(['gender', 'math_score'], ascending=False).head(10)

# In[36]:


students_performance1 = pd.read_json('https://api.opendota.com/api/heroes')

# In[42]:


df = pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')

# In[44]:


df.head(10)

# In[47]:


df.groupby('attack_type').head(10)

# In[57]:


df.sort_values(['legs']).groupby('legs').agg({'id': 'count'})

# In[58]:


df1 = pd.read_csv('C:\\Users\kiril\Downloads/accountancy.csv')

# In[59]:


df1.head()

# In[71]:


df1.groupby(['Executor', 'Type']).agg({'Salary': 'mean'}).head(25)

# In[74]:


df.groupby(['attack_type', 'primary_attr']).head()

# In[77]:


df.groupby(['attack_type', 'primary_attr']).u

# In[78]:


df.groupby(['attack_type', 'primary_attr']).agg({'count'}).head(25)

# In[79]:


concentrations = pd.read_csv('http://stepik.org/media/attachments/course/4852/algae.csv')

# In[80]:


concentrations.head()

# In[109]:


concentrations = concentrations.groupby(['group'])

# In[83]:


concentrations.head()

# In[84]:


concentrations.aggregate({
    'sucrose': 'mean',
    'alanin': 'mean', 'citrate': 'mean', 'glucose': 'mean', 'oleic_acid': 'mean'})

# In[85]:


mean_concentrations = concentrations.groupby(['genus']).aggregate({
    'sucrose': 'mean',
    'alanin': 'mean', 'citrate': 'mean', 'glucose': 'mean', 'oleic_acid': 'mean'})

# In[86]:


mean_concentrations

# In[87]:


mean_concentrations = concentrations.mean()

# In[88]:


mean_concentrations

# In[103]:


concentrations.aggregate({

    'alanin': ['min', 'mean', 'max']})

# In[101]:


concentrations.aggregate({'alanin': ['min', 'mean', 'max']}).loc[['Fucus']].round(2)

# In[106]:


mean_concentrations = concentrations.agg({'group': 'count'})

# In[107]:


mean_concentrations

# In[110]:


concentrations1 = pd.read_csv('http://stepik.org/media/attachments/course/4852/algae.csv')

# In[113]:


concentrations1.groupby(['group']).agg({'genus': 'count'})

# In[ ]:





