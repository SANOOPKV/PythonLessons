#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")


# In[ ]:


#Reading only in binary format
file = open("sanoop.txt","rb")


# In[ ]:


#For both Reading and Writing
file = open("sanoop.txt","r+")


# In[ ]:


#Open a file for Writing only, Overwrite the file if file exists and create a file for writing if the file not exists
file = open("sanoop.txt","w")


# In[ ]:


#Open a file for Writing only in binary format, Overwrite the file if file exists and create a file for writing if the file not exists
file = open("sanoop.txt","wb")


# In[ ]:


#Open file for Appending, if file does not exists the create a file, will not be overwritten
file = open("sanoop.txt","a")


# In[ ]:


#Open file for Appending in binary format, if file does not exists the create a file, will not be overwritten
file = open("sanoop.txt","ab")


# In[ ]:


#Open file for both appending and reading
file = open("sanoop.txt","a+")


# In[ ]:


#Open file for both appending and reading in binary format
file = open("sanoop.txt","ab+")


# In[ ]:


#Open file for both writing and reading, Overwrite the file if file exists and create a file for writing if the file not exists
file = open("sanoop.txt","w+")


# In[ ]:


#Open file for both writing and reading in binary format,Overwrite the file if file exists and create a file for writing if the file not exists
file = open("sanoop.txt","wb+")


# In[ ]:


file.write("Sanoop is good");


# In[ ]:


file.close()


# In[ ]:


print(file.read())


# In[ ]:


import os
os.rename("ditya.txt","sanoop.txt")


# In[ ]:


import subprocess
subprocess.check_output("ls")


# In[ ]:


import subprocess
subprocess.check_output("pwd")


# In[ ]:


dir(file)


# In[ ]:


help(file.read)


# In[ ]:


help(file.readline)


# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")
print("--------")
print(file.read())
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print(file.read())
print("--------")
print(file.read())
print("--------")
file.close()


# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print(file.read())
print("--------")
print(file.read())
print("--------")
file.close()


# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")
print("--------")
print(file.readline())
print("--------")
print(file.readline())
print("--------")
print("--------")
print(file.read())
print("--------")
print(file.read())
print("--------")
file.close()


# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")
print("--------")
print(file.readline(3))
print("--------")
print(file.readline(5))
print("--------")
print(file.readline(10))
print("--------")
print(file.readline(11))
print("--------")
print(file.read(20))
print("--------")
print(file.read(1000))
print("--------")
file.close()


# In[ ]:


#Default mode, reading only
file = open("sanoop.txt","r")
print("--------")
print(file.readline(3))
print("--------")
print(file.readline(5))
print("--------")
print(file.readline(10))
print("--------")
print(file.readline(11))
print("--------")
print(file.read(2011))
print("--------")
print(file.read(1000))
print("--------")
file.close()


# In[ ]:


file = open("sanoop.txt","r")
print(file.read())
file.close()


# In[ ]:


file = open("sanoop.txt","r")
print(file.readline(),end="")
print(file.readline(),end="")
print(file.readline(),end="")
file.close()


# In[ ]:


file = open("sanoop.txt","r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
else:
    print("Reading Completed")
file.close()


# In[1]:


file = open("sanoop.txt","r")
line = file.readline()
while line:
    print(line)
    line = file.readline()
else:
    print("Reading Completed")
file.close()


# In[2]:


print("Hi All")


# In[ ]:




