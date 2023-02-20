import csv
import statsmodels.api as sm
import numpy as np

# Load the data from the CSV file
with open('SurveyDataScored.csv') as f:
    data = [row for row in csv.DictReader(f, delimiter='|')]

# Convert the Cryptography_Score and BCDR_Score columns to numeric types
for row in data:
    row['Cryptography_Score'] = int(row['Cryptography_Score'])
    row['BCDR_Score'] = int(row['BCDR_Score'])

# Create dummy variables for the categorical variables
gender_dummy = []
education_dummy = []
crypto_exp_dummy = []
bcdr_exp_dummy = []
for row in data:
    gender = row['Gender']
    education = row['Education']
    crypto_exp = row['Cryptography_Exp']
    bcdr_exp = row['BCDR_Exp']
    gender_dummy.append(1 if gender == 'Male' else 0)
    education_dummy.append(1 if education == 'Bachelor' else 0)
    crypto_exp_dummy.append(1 if crypto_exp == 'Yes' else 0)
    bcdr_exp_dummy.append(1 if bcdr_exp == 'Yes' else 0)

# Set up the design matrix
design_matrix = []
for i, row in enumerate(data):
    design_matrix.append([
        gender_dummy[i],
        education_dummy[i],
        crypto_exp_dummy[i],
        bcdr_exp_dummy[i],
        row['Cryptography_Score'],
        row['BCDR_Score']
    ])

# Convert the design matrix to a numpy array
design_matrix = np.array(design_matrix)

# Set up the regression model
X = design_matrix[:, :-2]
Y = design_matrix[:, -2:]
X = sm.add_constant(X)
model = sm.OLS(Y, X)

# Fit the model and print the summary
results = model.fit()

print(results.summary())