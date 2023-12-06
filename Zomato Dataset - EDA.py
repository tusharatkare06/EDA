#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[5]:


# download dataset- and load dataset
df = pd.read_csv('zomato.csv', encoding= 'latin-1')
# Encoding to use for UTF when reading/writing


# In[6]:


df.head() #check dataset


# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.describe()


# ## In Data Analysis what all things we do
# #1 missing value
# #2. check about the numerical veriable
# #3. explore about catagerical veriable
# #4. finding relationship between feature

# In[10]:


# with the help of null value
df.isnull().sum()


# In[11]:


#with the help of list comperhension
[features for features in df.columns if df[features].isnull().sum()>0]


# In[12]:


#with the help of heatmap
import matplotlib
matplotlib.rcParams['figure.figsize'] = 12,6
sns.heatmap(df.isnull(), yticklabels=False, cbar= False, cmap='crest')


# In[13]:


df_country = pd.read_excel('Country-Code.xlsx')


# In[14]:


df_country.head()


# In[15]:


# combine two dataframe with same country code columns

final_df = pd.merge(df, df_country, on ='Country Code', how ='left')


# In[16]:


final_df.head(2)


# In[17]:


## To check datatype
final_df.dtypes


# In[18]:


final_df.columns


# In[19]:


final_df.Country.value_counts()


# In[20]:


final_df.Country.value_counts().index


# In[21]:


country_name = final_df.Country.value_counts().index


# In[22]:


country_val = final_df.Country.value_counts().values


# In[23]:


## pie chart
plt.pie(country_val , labels= country_name)
plt.show()


# In[24]:


## pie chart - top 3 country uses zomato
plt.pie(country_val[:3] , labels= country_name[:3],autopct= '%1.2f%%')
plt.show()


# Observation :- Zomato maximum records or transaction or orders are from India 94.39% then from US 4.73% and then UK 0.87% 

# In[25]:


# relationship with country

final_df.columns


# In[26]:


final_df.groupby(['Aggregate rating','Rating color', 'Rating text'])


# In[27]:


final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size()


# In[28]:


final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index()


# In[29]:


final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[30]:


rating = final_df.groupby(['Aggregate rating','Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating Count'})


# In[31]:


rating.head()


# Observation - whenever tha rating is from 4.5 to 4.9 indecates service is excelent
# 
# when the rating is 4.0 to 4.4 the service is very good
# 
# when the rating is 3.5 to 3.9 the service is  good
# 
# when the rating is 2.5 to 3.4 the service is Average
# 
# when the rating is 1.8 to 2.4 the service is poor
# 
# and 2148 people give rating zero for zomato service

# In[32]:


import matplotlib
matplotlib.rcParams['figure.figsize'] = 12,6
sns.barplot(x='Aggregate rating', y='Rating Count', data = rating)


# In[33]:


sns.barplot(x='Aggregate rating', y='Rating Count', hue='Rating color', data = rating)


# In[34]:


sns.barplot(x='Aggregate rating', y='Rating Count', hue='Rating color', data = rating, palette=['blue','red','orange','yellow','green','green'])


# Observation - 
# 1. not rated count is very high
# 2. maximun mmbers of rating are between 2.5 to 3.4
# 

# In[35]:


## countplot

sns.countplot(x='Rating color', data = rating, palette=['blue','red','orange','yellow','green','green'])


# In[36]:


##find the countries name that has given 0 rating


# In[37]:


final_df.columns


# In[38]:


final_df[final_df['Rating color']=='White'].groupby('Country').size().reset_index()


# In[39]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index()


# Observation
# maximum number of 0 rating from Indian customers
# 

# In[40]:


#which currency use by which country
final_df.groupby(['Country','Currency']).size().reset_index().rename(columns={0:'Currency Count'})


# In[41]:


final_df.groupby(['Country','Has Online delivery']).size().reset_index().rename(columns={0:'online delivery Count'})


# In[42]:


final_df.groupby(['Has Online delivery','Country']).size().reset_index().rename(columns={0:'online delivery Count'})


# Observation - online delivery is in India and UAE

# In[43]:


# create a pie chart for city distribution
City_index=final_df.City.value_counts().index
City_value=final_df.City.value_counts().values


# In[44]:


plt.pie(City_value[:5],labels=City_index[:5], autopct='%1.2f%%')
plt.show()


# In[47]:


final_df.Cuisines.value_counts()


# In[46]:


## top 10 cuisines

final_df.Cuisines.value_counts().index


# In[49]:


Cuisines_name = final_df.Cuisines.value_counts().index


# In[50]:


Cuisines_val = final_df.Cuisines.value_counts().values


# In[55]:


plt.pie(Cuisines_val[:5], labels=Cuisines_name[:5], autopct='%1.2f%%')
plt.show()


# In[56]:


final_df.groupby(['Has Online delivery','Cuisines']).size().reset_index().rename(columns={0:'online delivery Count'})


# In[61]:


final_df.groupby(['Country','Cuisines']).size().reset_index().rename(columns={0:'cusines Count'})


# In[ ]:





# In[68]:





# In[ ]:





# In[ ]:




