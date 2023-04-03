#!/usr/bin/env python
# coding: utf-8

# # Adults Income
# Sources:
# 
# - https://www.kaggle.com/datasets/wenruliu/adult-income-dataset. 
# 
# - http://www.cs.toronto.edu/~delve/data/adult/adultDetail.html . 
# 
# An annual income results to various factors, some of them are the education level, the age, the gender, the race and etc. We decided to visualize demographic factors on that time that afected on the anual income on that time and visualize them to determine if there are notable differences to influence on the income or not. After getting the data I had some questions:
# 
# - Does the age matters? Should we expect more anual income after 35 year old?
# - Does the educational level influence the age rate getting more income?
# - Does the educational level matters? How big are the differences between the income on different educational levels?
# - Does race matters? On the 90's (1994), How spread out the income was for the different races?
# - Last but nor least, It is known that in the 90's (1994) the salary gap was important between genders, is this true? does it really matters?
# ### Conditions 
# We have to note that the Data was taken from a census made on USA on 1994 and they took some conditions of the people to make the data more practic. There are the conditions they made bellow:
# 
# ##### ((AAGE>16) && (AGI>100) && (AFNLWGT>1)&& (HRSWK>0)):
# - Individual Age > 16.
# - Individual's adjusted gross income > 100.
# - An individual's final weight (AFNLWGT)>1. 
# - Individual's hours worked per week >1.
# 
# They used 14 columns on the dataset, but today, our target will be on 5 of them:
# - ###### 'income', 'age', 'education', 'race', 'gender'
# 

# In[638]:


import io
import gzip
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[526]:


df = pd.read_csv('/Users/ez/Desktop/Bootcamp/adult.csv')


# In[527]:


df.info()


# In[528]:


df=df.dropna()


# In[529]:


df.head()


# In[530]:



df[df['workclass'] == '?']


# In[531]:


df.drop(df.index[(df["workclass"] == "?")],axis=0,inplace=True)


# In[532]:


df[df['education'] == '10th']


# In[533]:


df.drop(df.index[(df["occupation"] == "?")],axis=0,inplace=True)


# In[534]:


df[df['occupation']== '?']


# In[535]:


df[df['native-country']=='?']


# In[536]:


df.drop(df.index[(df["native-country"] == "?")],axis=0,inplace=True)


# In[537]:


df[df['native-country']=='?']


# In[538]:


df.describe()


# In[539]:


df.head()


# In[ ]:





# In[540]:


df['education'].unique()


# In[541]:


uphighschool = ['Assoc-acdm', 'Some-college', 'Prof-school' , 'Bachelors', 'Assoc-voc', 'Doctorate']
lowhighschool= ['HS-grad','12th','11th', '10th' ,'9th','7th-8th', '5th-6th', '1st-4th', 'Preschool']
upHS = df[df['education'].isin(uphighschool)]
lowHS= df[df['education'].isin(lowhighschool)]


# ## Visualization
# 
# ### Here we can begin to ask the questions described above.
# 
# 
# #### - Does the age matters? Should we expect more anual income after 35 year old?
# 

# In[633]:


colors = {'<=50K': 'r', '>50K': 'b'}
sns.catplot(data=df,x='income', y='age', kind= 'box', aspect=1, palette= colors)
plt.title('Relationship between Income and Age')
plt.show()


# ##### From the above chart we can infer that:
# - Most of the people having income less than or equal to 50K are between age 25-45.
# - Most of the people having income more than 50K are between age 35-50.
# - We can expect an income higher than 50K between age 40-45.

# #### -Does the educational level influence the age rate getting more income?
# 

# In[620]:





colors = {'<=50K': 'r', '>50K': 'b'}


sns.catplot(data=lowHS, x='income', y='age', kind='box', aspect=1, hue='income', palette=colors)
plt.title('Relationship between Income and Age with people graduated on High School or less')
plt.show()


sns.catplot(data=upHS, x='income', y='age', kind='box', aspect=1, hue='income', palette=colors, order=['<=50K', '>50K'])
plt.title('Relationship between Income and Age with people graduated on higher education than High school')
plt.show()


# - With the charts above, we found that most of the people with an higher education level than a High School degree get younger more income than 50K. 
# - No notable differences between people with High School degree or lower education level and people with higher education leve that have an income lower than 50K

# In[621]:


df_less_50k = df[df['income'] == '<=50K']
df_more_50k = df[df['income'] == '>50K']

fig, ax = plt.subplots()
ax.hist(df_less_50k['age'], color='r', alpha=0.5, bins=20, label='Income <=50K')
ax.hist(df_more_50k['age'], color='b', alpha=0.5, bins=20, label='Income >50K')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.legend(loc='upper right')
plt.show()


# - We can see the tendence of young people to get an income lower than 50K and the actual difference of incomes on a young age

# ### - Does the educational level matters? 
# ### - How big are the differences between the income on different educational levels?
# 

# In[630]:


sns.displot(color= 'g', x= df['education'], aspect= 3.5)
plt.title('Education Level & Number of People')
plt.show()


# Here three notable group of education levels between people with an income:
# ###### (note that the Dataset is just for people with a current income the dataset doesnt count people without a job).
# - High School degree.
# - Some-College degree.
# - Bachelor degree.

# In[554]:


counts = df['income'].value_counts()

counts_by_other = df.groupby([df['education'], 'income']).size().unstack()

fig, ax = plt.subplots(1, 2, figsize=(15, 4))
counts.plot(kind='bar', ax=ax[0], color=['b', 'r'])
counts_by_other.plot(kind='bar', ax=ax[1], color=['b', 'r'])

ax[0].set_xlabel('Income')
ax[1].set_xlabel('Education Level')
ax[0].set_ylabel('Amount of people')
ax[1].set_ylabel('Amount of people')
ax[0].set_xticklabels(['Income < 50K', 'Income >= 50K'], rotation=0)
ax[1].set_xticklabels(ax[1].get_xticklabels(), rotation=90)
ax[0].set_title('Income per Amount of people')
ax[1].set_title('Relation between the Eduucation Level and the amount of people per income')

plt.show()


# Difference of Incomes, here we can infer that is important to get at least a high school degree to get better jobs, however, make a College and stop there is not that good, people should keep studying and get a Bachelor Degree because with High School degree is less likely to get an income higher than 50K. 

# #### - Does race matters? 
# #### - On the 90's (1994), How spread out the income was for the different races?

# In[608]:


grouped = df.groupby(['race', 'income']).size()

pivot_table = grouped.unstack()

fig, axes = plt.subplots(nrows=pivot_table.shape[0], ncols=1, figsize=(4, 20))

colors = ['r', 'b']
for i, education_level in enumerate(pivot_table.index):
    row = pivot_table.loc[education_level]
    row.plot(kind='pie', ax=axes[i], colors=colors, autopct='%1.1f%%', startangle=90)
    axes[i].set_title(education_level)

fig.suptitle('Income by Race', fontsize=16)
fig.text(0.5, 0.04, 'Race', ha='center')
fig.text(0.04, 0.5, 'Count', va='center', rotation='vertical')

fig.tight_layout()
plt.show()


# There are no notable differences of income related to Race, with just little different percentage with the Asian-Pac-Islander race on incomes percentage

# In[600]:


grouped = df[df['income'] == '<=50K'].groupby(['race']).size()

colors = ['lightblue', 'pink', 'lightgreen', 'yellow', 'orange', 'purple']
labels = grouped.index

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(grouped, labels=labels, colors=colors, autopct='%1.1f%%', startangle=500, textprops={'fontsize': 14})

ax.set_title('Distribution of Races with Income <=50K', fontsize=16)
ax.legend(loc='best')




grouped = df[df['income'] == '>50K'].groupby(['race']).size()

colors = ['lightblue', 'pink', 'lightgreen', 'yellow', 'orange', 'purple']
labels = grouped.index

fig, ax = plt.subplots(figsize=(8,8))
ax.pie(grouped, labels=labels, colors=colors, autopct='%1.1f%%', startangle=500, textprops={'fontsize': 14})

ax.set_title('Distribution of Races with Income >50K', fontsize=16)
ax.legend(loc='best')

plt.show()


# There is a high percentage of White race on the data, nonetheless, there are a higher percentage on White race and Asian-Pac-Islander with an income higher than 50K, with notable decreases of Black and Amer-Indian-Eskimo percentages between  an income lower than 50K and higher than 50K.

# ### - It is known that in the 90's (1994) the salary gap was important between genders, is this true? does it really matters?

# In[636]:



grouped = df.groupby(['gender', 'income']).size()

pivot_table = grouped.unstack()

fig, axes = plt.subplots(nrows=pivot_table.shape[0], ncols=1, figsize=(4, 8))

colors = ['r', 'b']
for i, (gender, row) in enumerate(pivot_table.iterrows()):
    row.plot(kind='bar', ax=axes[i], color=[colors[j] for j in range(len(row.index))])
    axes[i].set_title(gender)

fig.suptitle('Income by Gender', fontsize=16)

fig.text(0.04, 0.5, 'Count', va='center')

fig.tight_layout()


# In[637]:


grouped = df.groupby(['gender', 'income']).size()

pivot_table = grouped.unstack()

fig, axes = plt.subplots(nrows=pivot_table.shape[0], ncols=1, figsize=(4, 8))

for i, (gender, row) in enumerate(pivot_table.iterrows()):
    row.plot(kind='pie', ax=axes[i], colors=colors, autopct='%1.1f%%')
    axes[i].set_title(gender)

fig.suptitle('Income by Gender', fontsize=16)

fig.tight_layout()


# Differences between the percentages of income are notable by Gender, with a higher percentage of an income higher of 50K on the Male gender than Female gender, showing the wage gap of the time

# ## Conclusion:
# After visualize the data and the different factors than can ifluence the anual income to be higher or lower than 50K we can conclude that on 1994, the **age** rate was the biggest factor of influence to get an income higher than 50K. However, we found also big influence on the **educational level**, being the bachelor's degree the educational level with the most income above 50k, the differences between **genders** were notable and could be the result of gender inequality at the time, while no evidence of **racial** differences in annual income was found.
