#!/usr/bin/env python
# coding: utf-8

# In[5]:


#File methods
file = open("sanoop.txt","r")
for i in file.readlines():
    print(i,end="")
file.close()


# In[9]:


#File methods
file = open("sanoop.txt","r")
print(file.tell())
for i in file.readlines():
    print(i,end="")
    print(file.tell())
file.close()


# In[36]:


#tell() to get the current position in th efile
#seek(a,b) a - position, b - offset(0-start,1 current position, 2 end of file)
file = open("sanoop.txt","r")
position = file.tell()
line = file.readline()
count = 1;
while line:
    print(count,line,sep=" :: ",end=" ")
    print(position)
    file.seek(position)
    line = file.readline()
    print(count,line,sep=" :: ",end="")
    print(position)
    position = file.tell()
    line = file.readline()
    count+=1
file.close()


# In[ ]:




