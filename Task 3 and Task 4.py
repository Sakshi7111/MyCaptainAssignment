#!/usr/bin/env python
# coding: utf-8

# In[1]:


list1=[12, -7, 5, 64, -14]
for i in list1:
    if i>0:
        if i==64:
            print(i)
        else:
            print(i,end=",")


# In[2]:


list2=[12, 14, -95, 3]
l=[]
for i in list2:
    if i>0:
        l.append(i)
print(l)

