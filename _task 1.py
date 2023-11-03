#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


data = pd.read_csv(r"C:\Users\ROHIT SONAWANE\Desktop\Untitled Folder\\diabetes.csv")


# In[3]:


data.head()


# In[4]:


data.tail()


# In[5]:


data.shape


# In[6]:


data.info


# In[7]:


data.describe()


# In[8]:


data.columns


# In[9]:


data.corr()


# In[11]:


#summary of datasets

summary_stats = data.describe()
print(summary_stats)


# In[12]:


#datatype of dataset

datatypes = data.dtypes
print(datatypes)


# In[13]:


#data visualization in histogram

data.hist(bins=10,figsize=(10,10))


# In[14]:


#data visualization in scatter plot

plt.figure(figsize=(20,6))
sns.scatterplot(data=data, x="Glucose", y="BMI", hue="Age", size="Age")


# In[15]:


sns.countplot('Outcome', data = data)


# In[ ]:




