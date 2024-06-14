#!/usr/bin/env python
# coding: utf-8

# In[4]:


id=input("Enter your ID:")

if not id.startswith("AB"):
  print("the ID has to start with AB ")
elif len(id) != 7:
  print("ID has to be 7 digits")
elif not id[-4:].isdigit():
  print("ID has to end with 4 digits")
else:
  print("ID is valid")


# In[6]:


for i in range(1,11):
    for j in range (i,11):
        print(f"{i}x {j} =",i*j)
    print("................")


# In[ ]:





# In[ ]:




