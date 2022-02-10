#!/usr/bin/env python
# coding: utf-8

# In[1]:


num=int(input("Enter the terms: "))
f=0
s=1
if num<=0:
    print(f)
else:
    print(f,s,end=" ")
    for x in range(2,num):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next

