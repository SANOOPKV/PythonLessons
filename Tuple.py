#!/usr/bin/env python
# coding: utf-8

# In[5]:


#Tuple
    #Faster execution
    #Fixed values


# In[6]:


tup = ("Mango","Orange","Apple")


# In[7]:


print(tup)


# In[11]:


print(len(tup))
print(max(tup))
print(min(tup))


# In[34]:


print(tup+tup)
print(2*tup)
print("Mango" in tup)
#print(sorted(tup))
print(tup[::])
print(tup[::-1])
#print(dir(tup))
print(tup)
tup = tup +(1,2)
print(tup[0])
print(tup)


# In[35]:


print(tup)


# In[38]:


num = (1,2,4,5,6,7,8)
num = num[:2]+(3,)+num[2:]
num = num + (9,)
print(num)


# In[4]:


list1 = [1,2,3,4,5,6,7,7]
print(list1)
tuple1 = tuple(list1)
print(tuple1)
set1 = set(tuple1)
print(set1)
set2 = set(list1)
print(set2)


# In[ ]:




