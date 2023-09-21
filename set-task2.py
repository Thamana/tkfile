#!/usr/bin/env python
# coding: utf-8

# In[10]:


a={1,2,3,4,5,6,7,8}
b={2,4,6,8,10,12,16}
u=a.union(b) 
print("The Union of a & b =",u) #union


# In[11]:


i=a.intersection(b) 
print("The Intersection of a & b =",i) #intersection


# In[13]:


d=a.difference(b) 
print("The difference in set a - set b =",d) #a-b


# In[12]:


d1=b.difference(a) 
print("The difference in set b - set a =",d1) #b-a


# In[14]:


s = a.symmetric_difference(b)
print("The symmetric difference in set a - set b =",s)  #symmetric_difference


# In[ ]:




