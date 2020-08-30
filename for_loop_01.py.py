#!/usr/bin/env python
# coding: utf-8

# In[2]:


#For Loop
temp = {"Kerala":2456,"Tamil Nadu":23334,"Karnataka":121221}
for key in temp.keys():
    print(f"Covid Active cases in {key} is {temp.get(key)}")


# In[3]:


for i in range(10):
    print(i)


# In[10]:


n = int(input())
for i in range(1,n+2):
    for j in range(1,i):
        print(j,end=" ")
    print()


# In[13]:


list = [1,2,3,4,5,6,7,8]
listNew = [x**2 for x in list]
print(listNew)
listNew = [x**2 for x in list if x%2==0]
print(listNew)


# In[4]:





# In[ ]:




