#!/usr/bin/env python
# coding: utf-8

# In[1]:


r=float(input(("Enter radius: ")))
a=(22/7)*r*r
print("The area of the circle with radius 1.1 is: ",a)


# In[2]:


file=input("Enter filename: ")
file_ext=file.split(".")
a=file_ext[-1]
if a=="py":
    print("The extension of the file is: 'Python'")

