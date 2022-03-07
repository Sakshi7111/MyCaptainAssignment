#!/usr/bin/env python
# coding: utf-8

# In[1]:


import operator
f=input("Please enter a string ")
def most_frequent(string=f): 
    d=dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
s=most_frequent()
sort_dict=dict(sorted(s.items(), key=operator.itemgetter(1),reverse=True))
print(sort_dict)

