# -*- coding: utf-8 -*-
"""mushroom_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uo45sj2tIpDlvRWKZTn5qXmUM7NxsNZl
"""

import pandas as pd #importing necessary modules
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv ('mushrooms (1).csv') #importing the dataset

df.head() #showing top 5 rows of the dataset

df.isnull().sum() #cgecking null values

df.shape

df.describe()

import warnings
warnings.filterwarnings("ignore") # removing warnings

# Defining colors
colors = ['pink', 'red']  # Mentioning the colors

# Chart for Class Distribution
plt.figure(figsize=(8, 5))
sns.countplot(x='class', data=df, palette=colors)
plt.title('Class Distribution')
plt.xlabel('Class (Edible or Poisonous)')
plt.ylabel('Count')
plt.show()

#  Pie Chart for cap-shape distribution
plt.figure(figsize=(8, 6))
df['cap-shape'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Proportion of Mushrooms by Cap Shape')
plt.ylabel('')
plt.show()

# Histogram for cap-color distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['cap-color'], bins=10, color='brown')
plt.title('Distribution of Mushrooms by Cap Color')
plt.xlabel('Cap Color')
plt.ylabel('Count')
plt.show()

from sklearn.preprocessing import LabelEncoder

# Applying LabelEncoder to all categorical columns
data = df.apply(LabelEncoder().fit_transform)

data.head()

"""# Logistic Regression"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Splitting data into features and the target variable
X = data.drop('class', axis=1)
y = data['class']

# Splitting the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Initializing and training the model
lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)

# Predictions
y_pred = lr_model.predict(X_test)

# Performance metrics
accuracy_lr = accuracy_score(y_test, y_pred)
report_lr = classification_report(y_test, y_pred)

print("Logistic Regression Accuracy:", accuracy_lr)
print("Classification Report for Logistic Regression:")
print(report_lr)

"""# Support Vector Machine (SVM)"""

from sklearn.svm import SVC

# Initializing and train the model
svm_model = SVC(kernel='linear', random_state=42)
svm_model.fit(X_train, y_train)

# Predictions
y_pred_svm = svm_model.predict(X_test)

# Performance metrics
accuracy_svm = accuracy_score(y_test, y_pred_svm)
report_svm = classification_report(y_test, y_pred_svm)

print("Support Vector Machine Accuracy:", accuracy_svm)
print("Classification Report for Support Vector Machine:")
print(report_svm)

