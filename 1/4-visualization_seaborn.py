#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas   as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


sp = pd.read_csv('https://stepik.org/media/attachments/course/4852/StudentsPerformance.csv')


# In[4]:


sp.head()


# In[5]:


sp= sp                                    .rename(columns=
                                            {'parental level of education': 'parental_level_of_education',
                                            'test preparation course': 'test_preparation_course',
                                            'math score': 'math_score',
                                            'reading score': 'reading_score',
                                            'writing score': 'writing_score'})
sp


# In[6]:


sp.math_score.hist()


# In[7]:


sp.plot.scatter(x='math_score',y='reading_score')


# In[11]:


sns.lmplot(x='math_score', y='reading_score',hue='gender', data=sp)


# In[12]:


sns.lmplot(x='math_score', y='reading_score',hue='gender', data=sp,fit_reg=False)


# In[18]:


plt=sns.lmplot(x='math_score', y='reading_score',hue='gender', data=sp,fit_reg=False)
plt.set_xlabels('Math score')
plt.set_ylabels('Reading score')


# In[15]:


plt.set_xlabels('Math score')
plt.set_ylabels('Reading score')


# In[16]:


plt


# In[17]:


plt.show()


# In[19]:


df = pd.read_csv('https://stepik.org/media/attachments/course/4852/income.csv')


# In[20]:


df.head()


# In[21]:



sns.lineplot(data=df)


# In[22]:



df.income.plot()


# In[23]:



df.income.plot()


# In[24]:



df['income'].plot()


# In[25]:



df['income'].plot()


# In[26]:



df.plot(kind='line')


# In[27]:


sns.lineplot(x=df.index, y=df.income)


# In[28]:


f = pd.read_csv(https://stepik.org/api/attempts/441797315/file)


# In[29]:


df = pd.read_csv("dataset_209770_6.txt", sep=" ")


# In[31]:


import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

path = 'C:\\Users\kiril\Desktop\g'
file = [_ for _ in os.listdir(path) if 'txt' in _][0]
df = pd.read_csv(os.path.join(path, file), sep=" ")
f1, f2 = df.columns
df.plot.scatter(f1, f2)
plt.show()


# In[32]:


import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

path = 'C:\\Users\kiril\Desktop\g'
file = [_ for _ in os.listdir(path) if 'txt' in _][0]
df = pd.read_csv(os.path.join(path, file), sep=" ")
f1, f2 = df.columns
df.plot.scatter(f1, f2)
plt.show()


# In[33]:


import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

path = 'C:\\Users\kiril\Desktop\g'
file = [_ for _ in os.listdir(path) if 'txt' in _][0]
df = pd.read_csv(os.path.join(path, file), sep=" ")
f1, f2 = df.columns
df.plot.scatter(f1, f2)
plt.show()


# In[34]:


import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

path = 'C:\\Users\kiril\Desktop\g'
file = [_ for _ in os.listdir(path) if 'txt' in _][0]
df = pd.read_csv(os.path.join(path, file), sep=" ")
f1, f2 = df.columns
df.plot.scatter(f1, f2)
plt.show()


# In[35]:


import os
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

path = 'C:\\Users\kiril\Desktop\g'
file = [_ for _ in os.listdir(path) if 'txt' in _][0]
df = pd.read_csv(os.path.join(path, file), sep=" ")
f1, f2 = df.columns
df.plot.scatter(f1, f2)
plt.show()


# In[36]:


import numpy as np
import pandas as pd
df = pd.read_csv("dataset_209770_6.txt", sep = ' ')
df.plot.scatter(x = 'x', y = 'y')


# In[38]:


df = pd.read_csv('C:\\Users\kiril\Desktop\g\dataset_209770_6.txt', sep = ' ')

sns.scatterplot(df.x, df.y)


# In[47]:


df1= pd.read_csv('https://stepik.org/media/attachments/course/4852/genome_matrix.csv',index_col=0)


# In[48]:



g = sns.heatmap(df1, center=0, cmap="viridis")
g.xaxis.set_ticks_position('top')
g.xaxis.set_tick_params(rotation=90)


# In[57]:


df2= pd.read_csv('https://stepik.org/media/attachments/course/4852/dota_hero_stats.csv')


# In[58]:


df2.head()


# In[59]:


lenths = [len(r.split(',')) for r in df2.roles]


# In[60]:


df2['Lenths']=lenths


# In[61]:


df2.head()


# In[64]:


df2.Lenths.mean()


# In[92]:


df3= pd.read_csv('https://stepik.org/media/attachments/course/4852/iris.csv',index_col=0)


# In[78]:


df3.head()


# In[95]:


df3= df3                                    .rename(columns=
                                            {'sepal length': 'sepal_length',
                                            'sepal width': 'sepal_width',
                                            'sepal width': 'sepal_width',
                                            'petal width': 'petal_width',
                                             'petal length': 'petal_length',
                                            })


# In[96]:


df3.head()


# In[101]:


sns.distplot(df3.sepal_length)


# In[84]:


sns.distplot(df3.sepal_width)


# In[86]:


sns.distplot(df3.petal_length)


# In[98]:


sns.distplot(df3.petal_width)


# In[99]:


sns.distplot(df3.species)


# In[102]:


sns.kdeplot(data=df3)


# In[103]:


sns.set_theme(style="whitegrid")


# In[104]:


ax = sns.violinplot(x=df3.petal_length)


# In[105]:


sns.pairplot(df3)


# In[ ]:

