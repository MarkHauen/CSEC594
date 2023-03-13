import numpy as np
from DataCleaner import RegressionData
from T_Test import T_TestOutput

def formatCoefficients(coefficients): # format the coefficients for printing
    columns = ['\n   Learning_group',
               'Age',
               'Gender',
               'Education',
               'Cryptography_Exp',
               'BCDR_Exp']
    return '\n'.join([f'   {columns[x]}: {round(coefficients[x], 5)}' for x in range(6)])

# stack the input variables into a single 2D array
X = np.column_stack((RegressionData['learning_group'],
                     RegressionData['age'],
                     RegressionData['gender'],
                     RegressionData['education'],
                     RegressionData['cryptography_exp'],
                     RegressionData['BCDR_exp']))

# define the output variables as lists
y = RegressionData['exam1']
yy = RegressionData['exam2']

# calculate the multiple regression coefficients
coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
coefficients2 = np.linalg.lstsq(X, yy, rcond=None)[0]

# print the coefficients
All_OutPut = RegressionData['output'] + T_TestOutput + \
             f'Coefficients For Cryptography Exam: {formatCoefficients(coefficients)}\n\n' \
             f'Coefficients For BCDR Exam: {formatCoefficients(coefficients2)}'
