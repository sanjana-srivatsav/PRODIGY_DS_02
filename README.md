# **📊 Prodigy Infotech Internship – Task 2**
# **Data Cleaning & Exploratory Data Analysis (EDA) using Python**

---

## **📌 Task Objective**

Perform data cleaning and exploratory data analysis (EDA) on a real-world dataset.
Explore relationships between variables and identify patterns and trends using visualizations.

---

## **📁 Dataset**

The dataset used in this task is the Titanic Dataset from Kaggle.
It contains information about passengers on the Titanic and whether they survived.

### Key Columns:

- **Survived – Survival status (0 = No, 1 = Yes)**

- **Pclass – Passenger class (1st, 2nd, 3rd)**

- **Name – Passenger name**

- **Sex – Gender**

- **Age – Passenger age**

- **SibSp – Number of siblings/spouses aboard**

- **Parch – Number of parents/children aboard**

- **Fare – Ticket fare**

- **Embarked – Port of embarkation (C, Q, S)**

---

## **🛠 Tools & Libraries**

- Python

- Pandas

- NumPy

- Matplotlib

- Seaborn

---

## **📊 Exploratory Data Analysis (EDA)**

### 1. Survival Distribution
Countplot showing how many passengers survived vs not survived.

**Insights:**
- More passengers did not survive.
- Survival was not evenly distributed.

---

### 2. Survival by Gender
Countplot of survival based on gender.

**Insights:**
- Females had a much higher survival rate.
- Males had a significantly lower chance of survival.

--- 

### 3. Survival by Passenger Class
Countplot of survival by Pclass.

**Insights:**
- 1st class passengers had the highest survival rate.
- 3rd class passengers had the lowest survival rate.

---

### 4. Age Distribution
Histogram of passenger ages.

**Insights:**
- Most passengers were between 20 and 40 years old.
- Very few elderly passengers.
- Age distribution is right-skewed.

---

### 5. Correlation Heatmap
Heatmap showing relationships between numerical variables.

**Insights:**
- Fare is positively correlated with survival.
- Pclass is negatively correlated with survival.
- Age has a weak correlation with survival.

---

## **📂 Project Structure**
Prodigy_DS_Task2/
│
├── Titanic-Dataset.csv
├── task2_eda.ipynb
└── task2_eda.py

---

## **▶ How to Run**

### **1. Install dependencies**
pip install pandas numpy matplotlib seaborn

### **2. Run the script or notebook**
- python task2_eda.py
or
- Open task2_eda.ipynb in Jupyter Notebook and run all cells.

---

## **📈 Conclusion**
- This task demonstrates how data cleaning and exploratory data analysis help uncover hidden patterns and trends.
- The Titanic dataset clearly shows that gender, passenger class, and fare played a major role in survival.

---

## **✨ Author**

**Sanjana S M**

**Prodigy Infotech**
**Data Science Intern**
