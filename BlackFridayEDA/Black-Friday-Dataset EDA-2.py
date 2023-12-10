#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[ ]:





# In[ ]:





# In[2]:


df=pd.read_csv('final-black-friday.csv', index_col=0)


# In[3]:


df.head()


# In[4]:


## Start visualisation Age vs Purchase


# In[5]:


sns.barplot(data=df, x= 'Age',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[6]:


# purchasing of products almost equal but from observation
#purchasing of men is high then women


# In[7]:


# visualisation of purchase with occupation
sns.barplot(data=df, x= 'Occupation',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[8]:


sns.barplot(data=df, x= 'Product_Category_1',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[9]:


sns.barplot(data=df, x= 'Product_Category_2',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[10]:


sns.barplot(data=df, x= 'Product_Category_3',
    y='Purchase',
    hue='Gender')
plt.legend(labels=['Female','Male'])


# In[11]:


# seprate the train data and test data
df_test=df[df['Purchase'].isnull()]


# In[12]:


df_train=df[~df['Purchase'].isnull()] #~ use for except null


# In[31]:


# feature scaling
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()


# In[14]:


from sklearn.model_selection import train_test_split


# In[25]:


X =df_train.drop('Purchase', axis=1)


# In[33]:


X =df_train.drop('Product_ID', axis=1)


# In[35]:


y=df_train['Purchase']


# In[36]:


X.shape


# In[37]:


y.shape


# In[38]:


df_train.head()


# In[39]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


# In[40]:


X_train= sc.fit_transform(X_train)


# In[42]:


X_test=sc.transform(X_test)


# In[43]:


# regression


# In[44]:


from sklearn.linear_model import LinearRegression


# In[45]:


reg=LinearRegression()


# In[46]:


reg.fit(X_train, y_train)


# In[47]:


yhat= reg.predict(X_train)


# In[48]:


plt.scatter(y_train, yhat)

plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.show()


# In[49]:


sns.kdeplot(y_train-yhat)


# In[50]:


reg.score(X_train, y_train) # Rsquare


# In[51]:


yhat_test = reg.predict(X_test)


# In[52]:


plt.scatter(y_test, yhat_test)


# In[ ]:




