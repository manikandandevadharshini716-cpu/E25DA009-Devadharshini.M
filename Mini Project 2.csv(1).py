#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = { 
         "ID":[1,2,3,4,5],"Name":["Arun","Meena","Vijay","Anu","Rohit"],
          "Age":[21,24,28,26,22],"Department":["IT","EEE","CSE","MECH","ECE"],
          "Marks":[82,79,88,95,89]
}
df = pd.DataFrame(data)
print(df)
df.to_csv("Mini Project 2.csv",index = False)
print("✅ Data saved to sample_data.csv")


# In[ ]:




