# -*- coding: utf-8 -*-
"""CGPA Calculation.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wxPN8wUtZPntTknM97web7Ep2xUnqQWH
"""

import pandas as pd
import numpy as np

# Load your dataset into a Pandas DataFrame
df = pd.read_csv('/content/Grades - Sheet1.csv')
# Assuming 'GPA' and 'Term Credits' columns are present
# If not, replace with your actual column names

# Calculate 'Term Grade Points' for each term
df['Term Grade Points'] = df['GPA'] * df['Term Credits']

# Calculate CGPA
total_term_grade_points = df['Term Grade Points'].sum()
total_term_credits = df['Term Credits'].sum()
cgpa = total_term_grade_points / total_term_credits

print(f'Total Term Credits: {total_term_credits}')
print(f'CGPA: {cgpa}')