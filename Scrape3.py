#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
from bs4 import BeautifulSoup


# In[3]:


response = requests.get('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')


# In[4]:


print(response)


# In[7]:


print(response.text)


# In[10]:


soup=BeautifulSoup(response.text, 'html.parser') #parsing html using bs


# In[11]:


print(soup.body)


# In[12]:


print(soup.title)


# In[13]:


print(soup.find_all('div'))


# In[15]:


print(soup.find_all('p')) # finding all the tags of p


# In[18]:


print(soup.select('.mw-body-content')) #select class with the name


# In[20]:


import pandas as pd


# In[21]:


data = pd.read_html('https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites')


# In[22]:


data


# In[23]:


df = data[0]


# In[24]:


df


# In[25]:


df['Popularity (unique visitors per month)[1]']


# In[27]:


df['Websites']


# In[ ]:





# In[29]:


df.drop(4)


# In[31]:


df.drop(5)


# In[32]:


df.drop(14)


# In[33]:


df = df.drop([4,5,7,14,15])


# In[34]:


df


# In[35]:


df['Popularity (unique visitors per month)[1]'].describe()


# In[36]:


df['Popularity (unique visitors per month)[1]']


# In[37]:


df.convert_dtypes()


# In[40]:


df['Popularity (unique visitors per month)[1]'] = pd.to_numeric(df['Popularity (unique visitors per month)[1]'])


# In[42]:


df['Popularity (unique visitors per month)[1]'].describe()


# In[43]:


import matplotlib.pyplot as plt


# In[51]:


websites = df['Websites']
df


# In[45]:


uniquevisitors = df['Popularity (unique visitors per month)[1]']


# In[63]:


exp = [0.2,0.2,0.2,0,0,0,0,0,0,0,0] #to give space b/w pies


# In[64]:


plt.pie(uniquevisitors,labels = websites , shadow = True , radius=2 , autopct = '%2.1f%%',explode = exp)
plt.show()


# In[ ]:




