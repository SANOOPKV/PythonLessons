#!/usr/bin/env python
# coding: utf-8

# In[18]:


#String
name = "Sanoop"
print(name)
print(list(name))
print(set(name))
print(tuple(name))
print(name[::-1])
print(dir(name))
print(name.upper())
print(name.lower())
print(name.isupper())
print(name.islower())
print(name.isdigit())
print(name.isalpha())
print(name.isalnum())
print(name.casefold())


# In[19]:


print(2*name)


# In[20]:


print(name[:1])


# In[22]:


print("S" in name)
print("s" in name)


# In[23]:


print(name[:20])


# In[24]:


list = list(name)


# In[26]:


print(list[1:20])


# In[27]:


print("%s is a good student,should secure more than %d marks"%(name,90))


# In[28]:


print(f"{name} is a good student,should secure more than {90} marks")


# In[48]:


print(len(name))
print(name.upper())
print(name.lower())
print(name)
print(name.capitalize())
print(name.find("n"))
print(name.find("Z"))#Error safe
print(name.index("n"))
#print(name.index("Z"))#WIll throw error if not found


# In[54]:


print(name.replace("o","i",1))
print(name)
print(name.replace("o","i",1))
print(name.count("o"))


# In[ ]:




