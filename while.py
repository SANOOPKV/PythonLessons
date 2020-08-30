#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Loops
#While Loop - support else aswell
num = 10
while num < 20:
    print(num)
    num+=1
else:
    print("Completed")


# In[2]:


#Loops
#While Loop - support else aswell
num = 10
while num < 20:
    if num == 16:
        break
    print(num)
    num+=1
else:
    print("Completed")


# In[3]:


#Loops
#While Loop - support else aswell
num = 10
while num < 20:
    num+=1
    if num == 16:
        continue
    print(num)
else:
    print("Completed")


# In[ ]:


num = 0
correctNum = int(input())
while 

