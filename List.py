#!/usr/bin/env python
# coding: utf-8

# In[68]:


#List
#No Random Access, Need Index based access
list=["Mango","Apple"]
print(list)
list.append("Orange")
print(list)
del(list[1])
print(list)


# In[5]:


dir(list)eibccckrihccrnhdnuvuvfcdjruhhkvffkirnerjfllf


# In[7]:


list.remove("Mango")


# In[11]:


print(list)


# In[12]:


print(list.pop())
print(list.pop(2))


# In[24]:


print(list)


# In[70]:


list.append("Grapes")


# In[69]:


list.extend(["Papaya","Kiwi"])


# In[23]:


list.remove("Kiwi")


# In[25]:


list[2:4]


# In[26]:


del list[2:4]


# In[27]:


print(list)


# In[28]:


print(type(list))


# In[29]:


list1 = [x*2 for x in list ]


# In[30]:


print(list1)


# In[31]:


list1 = [x*2 for x in list if x[0]=="M"]


# In[32]:


print(list1)


# In[33]:


list.insert(1,"Sanoop")


# In[34]:


print(list)


# In[35]:


print(sorted(list))


# In[44]:


list.sort()
print(list)


# In[58]:


print(list[-1:0:-1])


# In[59]:


print(list[::2])


# In[71]:


list.sort()
print(list)


# In[72]:


list.reverse()
print(list)


# In[82]:


#print(list.sum())
print(list.count("Orange"))


# In[ ]:




