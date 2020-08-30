#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set


# In[2]:


list=[1,2,4,5,6,7,4,5,3]
set1 = set(list)


# In[3]:


print(set1)


# In[9]:


A = {1,2,3,4,5}
B = {4,5,6,7,8}
#Union
C = A|B
C = A.union(B)
print(C)


# In[11]:


#Intersection
print(A&B)
print(A.intersection(B))


# In[15]:


#Difference
print(A-B)
print(A.difference(B))


# In[18]:


print(B.issubset(A))


# In[19]:


print(5 in set1)


# In[20]:


print(5 not in set1)


# In[ ]:




