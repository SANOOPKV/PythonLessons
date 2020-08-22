#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hi Welcome")


# In[2]:


#Immutable
a = 10
b = 12.1
c = 10+5j
print(a,b,c)
print(type(a),type(b),type(c))


# In[3]:


#Immutable
a = "Good"
b = "Morning"
c = """Students
    From Sanoop !"""
print(a,b,c)


# In[18]:


#Immutable
tuple_01 = (1,2,"Sanoop",1,4,2,5)
print("1 : ",tuple_01)
print("2 : ",tuple_01[0])
print("3 : ",tuple_01[-1])
print("4 : ",tuple_01[:])
print("5 : ",tuple_01[::-1])
print("6 : ",tuple_01[:-1])
print("7 : ",tuple_01[:-8])
print("8 : ",tuple_01[:8])
print("9 : ",tuple_01[-8])
print("10 : ",tuple_01[8])


# In[28]:


print(type(tuple_01))
print(tuple_01.__doc__)
dir(tuple_01)


# In[36]:


#Mutable
list_01 = [1,2,"Sanoop",1,4,2,5]
print("1 : ",list_01)
print("2 : ",list_01[0])
print("3 : ",list_01[-1])
print("4 : ",list_01[:])
print("5 : ",list_01[::-1])
print("6 : ",list_01[:-1])
print("7 : ",list_01[:-8])
print("8 : ",list_01[:8])
print("9 : ",list_01[-8])
print("10 : ",list_01[8])


# In[31]:


print(type(list_01))
print(list_01.__doc__)
dir(list_01)


# In[32]:


help(list_01)


# In[35]:


help(list_01.extend)
help(list_01.append)


# In[5]:


for i in range(2):
    print("PrintFuntion01","PrintFuntion02",sep="_",end="**")


# In[22]:


#Mutable
disctionary_01 = {"Kerala":56000,"Karnataka":120000,"Goa":1122}
print(disctionary_01)
disctionary_01.update({"Tamilnadu":12121122})
disctionary_01.setdefault("Maharashtra",22323233)
print(disctionary_01.get("Kerala"))
print(disctionary_01.items())
print(disctionary_01.keys())
print(disctionary_01.values())
dir(disctionary_01)
help(disctionary_01.setdefault)


# In[23]:


set_01 = {12,43,565,121,12,6767,43}
print(set_01)
print(type(set_01))


# In[ ]:




