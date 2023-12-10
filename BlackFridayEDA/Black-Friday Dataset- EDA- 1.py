#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# importing the dataset from local
# its e-com data - people who bought the product
#build a model


# a retail company "ABC Private Limited" wants to understand te  customer purchase behaviour (specifically, purchase amount) against various products of different categories. they have shared purchase summary of various customers for selected high volume products from last month. the  data set also contain customers demographics(age, gender, maritial status, city_type, stay_in_current_city), procucts details(products id and product category) and total purchase amount from last month
# 
# now they want tot build a model to predict the purchaase amount of customer against varisous products which will help them to create personalized offer for customers against different products

# In[3]:


df_train = pd.read_csv('train.csv')
df_train.head()


# In[4]:


#load test dataset
df_test = pd.read_csv('test.csv')
df_test.head()


# In[5]:


# merge both train and test data if you have 2 datasets
df = df_train.append(df_test)


# In[6]:


df.head()


# In[7]:


## basic
df.info()


# In[8]:


df.dtypes


# In[9]:


df.describe(include='all')


# In[10]:


# as we seen, userid is not any independent variable
df.drop(['User_ID'],axis=1, inplace=True)

#df1 =df.drop(['User_ID'],axis=1) if use df= then nno need inplace


# In[11]:


df.head()


# In[13]:


# lets focus on age and gender
# df['Gender']=pd.get_dummies(df['Gender'],drop_first=1) you may use this


# In[14]:


# use map because we have only 2 feature , male and female, 
# so we can use map
df['Gender'] =df['Gender'].map({'F':0,'M':1})


# In[15]:


df.head()


# In[16]:


# Lets talk about age
df['Age'].unique()


# In[18]:





# In[19]:


#here also you can use one hot encoding and increase columns
#lets give some rank to age rather than dummee
# you can also use lable encoding here
# so we can use map
df['Age'] =df['Age'].map({'0-17':1,'18-25':1, '26-35':3,'36-45':4,'46-50':5, '51-55':6,'55+':7})


# In[20]:


df.head()


# In[21]:


df['City_Category'].unique()


# In[22]:


df['City_Category'] =df['City_Category'].map({'A':1,'B':2, 'C':3})


# In[23]:


df.head()


# In[24]:


df['Product_Category_1'].unique()


# In[25]:


#Check Missing Values
df.isnull().sum()


# In[26]:


# purchase have null , because we append test data also,
# we we focus on replacing purchasing missing value


# In[27]:


df['Product_Category_2'].unique()


# # we have descrete feature here so replace the NaN value
# # bset way to replace missing value with MODE

# In[28]:


df['Product_Category_2'].value_counts()


# In[29]:


df['Product_Category_2'].mode()


# In[30]:


df['Product_Category_2'].mode()[0]


# In[31]:


df['Product_Category_2']=df['Product_Category_2'].fillna(df['Product_Category_2'].mode()[0])


# In[32]:


df['Product_Category_2'].isnull().sum()


# In[33]:


df['Product_Category_3']=df['Product_Category_3'].fillna(df['Product_Category_3'].mode()[0])


# In[34]:


df['Product_Category_3'].isnull().sum()


# In[35]:


df.head()


# In[36]:


df['Stay_In_Current_City_Years'].unique()


# In[37]:


#you can map like this also for 4+
#df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].map({'2':2, '4+':4, '1':1,'0':0})


# In[38]:


# or only replace +
df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].str.replace('+','')


# In[39]:


df.head()


# In[40]:


df['Stay_In_Current_City_Years'].unique()


# In[41]:


df.info()


# In[42]:


# as we seen Stay-in city showing object
# so convert obj into int

df['Stay_In_Current_City_Years']=df['Stay_In_Current_City_Years'].astype(int)


# In[43]:


df.info()


# In[44]:


##visualisation 

sns.pairplot(df)
plt.show()


# In[46]:


sns.barplot(data=df, x= 'Age',
    y='Purchase',
    hue='Gender')


# In[47]:


df.to_csv('final-black-friday.csv')


# In[48]:


sns.barplot(data=df, x= 'Age',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[ ]:




