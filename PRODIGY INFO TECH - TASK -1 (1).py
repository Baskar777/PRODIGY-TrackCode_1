#!/usr/bin/env python
# coding: utf-8

# # TASK 1:
      Create a barchart or histogram to visualize
      the distribution of categorical or continuous variable,
      such as the distribution the distribution of 
      ages or gender in a population

#  
#      The aim of this analysis is to investigate a range of health-related factors and their interconnections to classify diabetes accurately.These factors include aspects such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.
# This comprehensive examination will not only provide insights into the patterns and trends in diabetes risk but will also create a solid base for further research. 
# Specifically, research can be built on how these variables interact and influence diabetes occurrence and progression,
# crucial knowledge for improving patient care and outcomes in this increasingly critical area of healthcare.

# In[1]:


#load the dependans
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# this is for avoid the pink color warnings lol
import warnings
warnings.filterwarnings('ignore')


# In[3]:


#load the dataset 
diabetes_df = pd.read_csv('diabetes_prediction_dataset.csv.zip')
diabetes_df.head()


# In[4]:


#shape of dataset
diabetes_df.shape


# In[5]:


#columns in this dataset
diabetes_df.columns


# In[6]:


# this is large data so iam going to remove the duplicates
duplicate_rows_data = diabetes_df[diabetes_df.duplicated()]
print("number of duplicate rows: ", duplicate_rows_data.shape)


# In[7]:


#drop the duplicate
diabetes_df = diabetes_df.drop_duplicates()


# In[8]:


# Loop through each column and count the number of distinct values
for column in diabetes_df.columns:
    num_distinct_values = len(diabetes_df[column].unique())
    print(f"{column}: {num_distinct_values} distinct values")


# In[9]:


#describe fun for statistics
diabetes_df.describe().round(2)


# In[10]:


#target variable counts
diabetes_df['diabetes'].value_counts()
# this data is higgly imbalanced 


# In[11]:


#percentage of target variable
100*diabetes_df['diabetes'].value_counts()/ len(diabetes_df['diabetes'])


# In[12]:


#my task is do a EDA use bar and hist 
diabetes_df.isnull().sum()


# In[13]:


#information about the data types and null values
diabetes_df.info()


# In[14]:


#gender value 
diabetes_df['gender'].value_counts()


# In[15]:


diabetes_df.columns


# In[16]:


#univarient analysis
#gender distribution using countplot
sns.countplot(data=diabetes_df,x='gender')
plt.title('Gender distribution ')
plt.show()

female win this poll 😅  lol-- female data is higer than male data

# In[17]:


#age distribution useing hist
sns.histplot(data=diabetes_df,x='age',color='cornflowerblue',edgecolor='darkslateblue')
plt.title('Age distribution')
plt.show()


seniors on the top of the table and ages

# In[18]:


#bmi (boby mass index) useing distributionplot
sns.distplot(diabetes_df['bmi'],bins=40)
plt.title('distribution of bmi')


# In[19]:


#hypertention using countplot
sns.countplot(data=diabetes_df,x='hypertension')
plt.title('Distribution of Hypertension')


hypertension is low tension in this plot 

# In[20]:


#heart disease using countplot
sns.countplot(data=diabetes_df,x='heart_disease')
plt.title('Distribution of Heart disease')


# In[21]:


#diabetes in counts 1 = diabetes, 0 = no diabetes 
sns.countplot(data=diabetes_df,x='diabetes')
plt.title('distribution of diabetes')


# The diabetes data have low diabetes

# In[22]:


sns.violinplot(y=diabetes_df['blood_glucose_level'],x=diabetes_df['diabetes'])


# In[23]:


#I create a addtional information - age group
bins = [0,5,13,20,40,60,81]
labels = ['infant and toddler','child', 'teen ','adult','middle age', 'senior citizen']
diabetes_df['age_group'] = pd.cut(diabetes_df['age'], bins=bins,labels = labels, right=False)
diabetes_df.head(5)


# In[24]:


#age group using countplot
sns.countplot(data=diabetes_df, x='age_group',palette='dark')
plt.title('distribution of Age group')

this time middle age overtaken the senior , middle age pepoles data is higer compare to others# I create a age group based on the stages of life in helthcare 
0-4   --- infant and toddler
5-12  --- child
13-19 --- teen
20-39 --- adult
40-59 --- middle age
60 +  --- senior citizen
# In[25]:


#smoking history using countplot
sns.countplot(data=diabetes_df,x='smoking_history')
plt.title('Distribution of Smoking history')

the smocking history -- never is higher than no info it is good
# In[26]:


#bivariant analysis


# In[27]:


sns.barplot(data=diabetes_df,x='age_group',y='diabetes')
plt.title('age vs diabetes')


senior citizen is senior in diabetes  

# In[28]:


sns.barplot(data=diabetes_df,x='gender',y='hypertension')
plt.title('hypertension vs gender')

tension! tension! tension! so be calm mens
# In[29]:


sns.barplot(data=diabetes_df, x='diabetes', y='bmi')
plt.title('diabetes vs BMI ')

bmi (body mass index) is refer to your body fat % 
Excess body fat, particularly around the waist, can lead to insulin resistance and impair
the body's ability to regulate blood sugar levels.
# In[30]:


for i, predictor in enumerate(diabetes_df.drop(columns=['bmi','blood_glucose_level','age','HbA1c_level'])):
    plt.figure(i)
    sns.countplot(data=diabetes_df, x=predictor, hue='diabetes')


# In[31]:


#multivariant analysis
diabetes_df_1 = diabetes_df[diabetes_df['diabetes'] == 1]

diabetes_df_0 = diabetes_df[diabetes_df['diabetes'] == 0]
# i split the data to diabetes and no diabetes iam going to analize the diabetes data (diabetes_df_1)


# In[32]:


def uniplot(df,col,title,hue =None):
    
    sns.set_style('whitegrid')
    sns.set_context('talk')
    plt.rcParams["axes.labelsize"] = 14
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.titlepad'] = 20
    
    
    temp = pd.Series(data = hue)
    fig, ax = plt.subplots()
    width = len(df[col].unique()) + 4 + 4*len(temp.unique())
    fig.set_size_inches(width , 4)
    plt.xticks(rotation=45)
    #plt.yscale('log')
    plt.title(title)
    ax = sns.countplot(data = df, x= col, order=df[col].value_counts().index,hue = hue,palette='bright') 
    for p in ax.patches:
        ax.annotate('{:.1f}'.format(p.get_height()), (p.get_x()+0.25, p.get_height()+0.01))


        
    plt.show()


# In[33]:


uniplot(df=diabetes_df_1,col='smoking_history',title='diabetes and smoking history split by gender',hue='gender')


never smoked pepole have diabetes compare to others - female 2002 , male 1344

# In[34]:


uniplot(df=diabetes_df_1, col='heart_disease',title='diabetes and heart disease split  by gender', hue='gender')

female 526 -- heart disease and dieabetes
male 741 -- heart disease and dieabetes
# In[35]:


uniplot(df=diabetes_df_1, col='hypertension',title='hypertension and diabetes splited by gender', hue='gender')


# female hypertension metter higher than male

# In[36]:


uniplot(df=diabetes_df_1,col='diabetes',title='diabetes by gender',hue='gender')


# In[37]:


uniplot(df=diabetes_df_0, col='HbA1c_level',title='no diabetes HbA1c_level split by gender', hue='gender')


# no diabetes range of HbA1c_level -- 3.5 to 6.6

# In[38]:


uniplot(df=diabetes_df_1, col='HbA1c_level',title='diabetes HbA1c_level split by gender', hue='gender')


# diabetes range of HbA1c_level -- 5.7 to 9.0
 the insight of this plot was higer HbA1c_level leads to diabetes
# In[39]:


uniplot(df=diabetes_df_1, col='age_group',title='diabetes and age_group by gender', hue='gender')


# In[40]:


uniplot(df=diabetes_df_1, col='blood_glucose_level',title='heart disease by gender', hue='gender')


# the blood_glucose_level of diabetes pa range -- 126 to 300

# In[41]:


uniplot(df=diabetes_df_0, col='blood_glucose_level',title='heart disease by gender', hue='gender')


# the blood_glucose_level of no diabetes pa range -- 80 to 200
# 
# high in blood_glucose_level (sugar) leads to diabetes
# 

# In[42]:


dia_age = sns.histplot(diabetes_df_1['age'],kde=True)

dia_age.set_ylabel('counts')
dia_age.set_xlabel('age of diabetes pepole')
dia_age.set_title('distribution diabetes in age')


# higer age higer chance to get diabates

# insights:
# 1 . bmi (body mass index) is refer to your body fat percentage 
# Excess body fat, particularly around the waist, can lead to insulin resistance and impair
# the body's ability to regulate blood sugar levels.
# 2 . age 60+ pepole's have higher chance to get diabetes
# 3.  high in blood_glucose_level (sugar) leads to diabetes
# 4.  higer HbA1c_level leads to diabetes
# 

# # THE KNOWLEDGE I GAINED IN THIS DOMAIN

# #Age: Age is an important factor in predicting diabetes risk. As individuals get older, their risk of developing diabetes increases. This is partly due to factors such as reduced physical activity, changes in hormone levels, and a higher likelihood of developing other health conditions that can contribute to diabetes.
# 
# #Gender: Gender can play a role in diabetes risk, although the effect may vary. For example, women with a history of gestational diabetes (diabetes during pregnancy) have a higher risk of developing type 2 diabetes later in life. Additionally, some studies have suggested that men may have a slightly higher risk of diabetes compared to women.
# 
# #Body Mass Index (BMI): BMI is a measure of body fat based on a person's height and weight. It is commonly used as an indicator of overall weight status and can be helpful in predicting diabetes risk. Higher BMI is associated with a greater likelihood of developing type 2 diabetes. Excess body fat, particularly around the waist, can lead to insulin resistance and impair the body's ability to regulate blood sugar levels.
# 
# #Hypertension: Hypertension, or high blood pressure, is a condition that often coexists with diabetes. The two conditions share common risk factors and can contribute to each other's development. Having hypertension increases the risk of developing type 2 diabetes and vice versa. Both conditions can have detrimental effects on cardiovascular health.
# 
# #Heart Disease: Heart disease, including conditions such as coronary artery disease and heart failure, is associated with an increased risk of diabetes. The relationship between heart disease and diabetes is bidirectional, meaning that having one condition increases the risk of developing the other. This is because they share many common risk factors, such as obesity, h
# igh blood pressure, and high cholesterol.
# 
# #Smoking History: Smoking is a modifiable risk factor for diabetes. Cigarette smoking has been found to increase the risk of developing type 2 diabetes. Smoking can contribute to insulin resistance and impair glucose metabolism. Quitting smoking can significantly reduce the risk of developing diabetes and its complications.
# 
# #HbA1c Level: HbA1c (glycated hemoglobin) is a measure of the average blood glucose level over the past 2-3 months. It provides information about long-term blood sugar control. Higher HbA1c levels indicate poorer glycemic control and are associated with an increased risk of developing diabetes and its complications.
# 
# #Blood Glucose Level: Blood glucose level refers to the amount of glucose (sugar) present in the blood at a given time. Elevated blood glucose levels, particularly in the fasting state or after consuming carbohydrates, can indicate impaired glucose regulation and increase the risk of developing diabetes. Regular monitoring of blood glucose levels is important in the diagnosis and management of diabetes.

# 
#       my task is use barchart and hist to visualize the data distribution .i try my best in this dataset , give your 
# feed back if any mistake or suggestion pls let me know       
#     

# # THANK YOU

# In[ ]:




