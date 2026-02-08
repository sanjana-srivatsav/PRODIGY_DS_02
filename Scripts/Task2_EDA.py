-----------#Step1: Import Required Libraries--------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

-----------# Optional settings--------------
sns.set_style("whitegrid")

-----------#Step2: Load Dataset-----------
df = pd.read_csv(r"C:\Users\admin\Documents\Prodigy Infotech\Prodigy_DS_02\Titanic-Dataset.csv")

df.head()

-----------#Step3: Data Understanding / Initial Exploration
#Dataset Info
df.info()

#Statistical Summary
df.describe()

#Check Missing Values
df.isnull().sum()

-----------#Step4: Data Cleaning-------------
-----------#Handle Missing Values------------
# Fill Age with median
df['Age'] = df['Age'].fillna(df['Age'].median())

# Fill Embarked with mode
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

-----------#Check Again------------
df.isnull().sum()

------------#Step5: Exploratory Data Analysis (EDA)-----------
------------#Survival Distribution-----------
sns.countplot(x='Survived', data=df)
plt.title("Survival Count")
plt.show()

------------#Survival by Gender------------
sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

------------#Survival by Passenger Class----------
sns.countplot(x='Pclass', hue='Survived', data=df)
plt.title("Survival by Passenger Class")
plt.show()

------------#Age Distribution-------------
plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

------------#Correlation Heatmap-----------
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()




