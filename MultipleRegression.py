import numpy as np
from DataCleaner import Data
from T_Test import T_TestOutput

def formatCoefficients(coefficients):
    columns = ['\n   learning_group',
               'age',
               'gender',
               'education',
               'cryptography_exp',
               'BCDR_exp']
    return '\n'.join([f'   {columns[x]}: {round(coefficients[x], 10)}' for x in range(6)])

# stack the input variables into a single 2D array
X = np.column_stack((Data['learning_group'],
                     Data['age'],
                     Data['gender'],
                     Data['education'],
                     Data['cryptography_exp'],
                     Data['BCDR_exp']))

# define the output variable as a list
y = Data['exam1']
yy = Data['exam2']

# calculate the multiple regression coefficients
coefficients = np.linalg.lstsq(X, y, rcond=None)[0]
coefficients2 = np.linalg.lstsq(X, yy, rcond=None)[0]

All_OutPut = Data['output'] + T_TestOutput + \
             f'Coefficients For Exam 1: {formatCoefficients(coefficients)}\n\n' \
             f'Coefficients For Exam 2: {formatCoefficients(coefficients2)}'
