#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
import matplotlib.pyplot as plt

### Data Source ###
# https://www.cdc.gov/flu/prevent/vaccine-supply-historical.htm

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.set(ylabel='Flu Vaccinations in Millions',
       title='America Flu Vaccinations since 2008')
year = ["2008", "2009", "2010", "2011", "2012", "2013","2014","2015", "2016","2017","2018", "2019", "2020"]
fluVaccineCount = [110.9, 114, 155.1, 132, 134.9, 134.5, 147.8, 146.4, 145.9, 155.3, 169.1, 174.5, 189.5]
ax.bar(year,fluVaccineCount)
plt.show()


# In[20]:


labels = ['Not vaccinated', 'Vaccinated']
sizes = [142, 189]

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, )

ax1.axis('equal')
print('America Flu Vaccination Population Percentages')
plt.show()


# In[ ]:




