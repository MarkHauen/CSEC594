import pandas as pd
import statsmodels.api as sm
from DataCleaner import getDataPath

# Load the data from the CSV file
data = pd.read_csv(getDataPath('SurveyDataScored'), sep='|')

# Convert the categorical variables to dummy variables
#data = pd.get_dummies(data, columns=['Group', 'Gender', 'Education', 'Cryptography_Exp', 'BCDR_Exp'])
for x in ['Group', 'Gender', 'Education', 'Cryptography_Exp', 'BCDR_Exp']:
    data[x] = data[x].astype('category')

data["Cryptography_Score"] = data["Cryptography_Score"].astype('int64')
#data["BCDR_Score"] = data["BCDR_Score"].astype('int64')

# Separate the outcome variables from the predictor variables
predictors = data.drop(['Cryptography_Score', 'BCDR_Score'], axis=1)
cryptography_outcome = data['Cryptography_Score']
bcdr_outcome = data['BCDR_Score']

# Fit a multiple regression model for the Cryptography_Score outcome
cryptography_model = sm.OLS(cryptography_outcome, predictors).fit()


# Fit a multiple regression model for the BCDR_Score outcome
bcdr_model = sm.OLS(bcdr_outcome, predictors).fit()

print(cryptography_model.summary())
print(bcdr_model.summary())
