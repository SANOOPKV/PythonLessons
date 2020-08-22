#!/usr/bin/env python
# coding: utf-8

# In[3]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x for x in list_x]
print(list_y)


# In[4]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x**2 for x in list_x]
print(list_y)


# In[5]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x+x for x in list_x]
print(list_y)


# In[6]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [2*x for x in list_x]
print(list_y)


# In[8]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x**2 for x in list_x if x%2==0]
print(list_y)


# In[9]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x**2 for x in list_x if x%2!=0]
print(list_y)


# In[20]:


#List Comprehension
list_x = [1,2,3,4,5,6]
list_y = [x**2 for x in list_x]
print(list_y)


# In[18]:


#Alternative map + filter
list_x = [1,2,3,4,5,6]
list_y = list(map(lambda x: x**2,list_x))
print(list_y)


# In[19]:


#Alternative map + filter
list_x = [1,2,3,4,5,6]
list_y = list(map(lambda x: x**2,filter(lambda x: x%2 == 0,list_x)))
print(list_y)


# In[21]:


#Alternative map + filter
list_x = [1,2,3,4,5,6]
list_y = list(filter(lambda x: x%2 == 0,list_x))
print(list_y)


# In[25]:


#Generator Comprehension, used when range is large
list_x = [1,2,3,4,5,6]
list_y = list((x**2 for x in list_x if x%2!=0))
print(list_y)


# In[ ]:




