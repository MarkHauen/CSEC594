import csv
from scipy.stats import ttest_ind
from T_TestEqualVariants import t_test_equal_variances

def Ave(lst):
    return sum(lst) / len(lst)

# Load the data from the CSV file
with open('SurveyDataScored.csv') as f:
    data = [row for row in csv.DictReader(f, delimiter='|')]

# Separate the data into two groups based on the 'Group' column
group_a = [row for row in data if row['Group'] == '1']
group_b = [row for row in data if row['Group'] == '2']

# Convert the Cryptography_Score and BCDR_Score columns to numeric types
for row in data:
    row['Cryptography_Score'] = float(row['Cryptography_Score'])
    row['BCDR_Score'] = float(row['BCDR_Score'])

# Extract the Cryptography_Score and BCDR_Score columns for each group
group_a_crypto = [row['Cryptography_Score'] for row in group_a]
group_b_crypto = [row['Cryptography_Score'] for row in group_b]
group_a_bcdr = [row['BCDR_Score'] for row in group_a]
group_b_bcdr = [row['BCDR_Score'] for row in group_b]

# Perform a two-sample t-test on the Cryptography_Score column
crypto_t, crypto_p = ttest_ind(group_a_crypto, group_b_crypto)

# Perform a two-sample t-test on the BCDR_Score column
bcdr_t, bcdr_p = ttest_ind(group_a_bcdr, group_b_bcdr)

# Print the results
print(f'Group A (Chat GTP for BCDR) Average Score:\n  Cryptography: {Ave(group_a_crypto)}\n  BCDR: {Ave(group_a_bcdr)}\n'
      f'Group B (Chat GTP for Cryptography) Average Score:\n  Cryptography: {Ave(group_b_crypto)}\n  BCDR: {Ave(group_b_bcdr)}\n')
print('Cryptography Score t-value:', crypto_t)
print('Cryptography Score p-value:', crypto_p)
print('BCDR Score t-value:', bcdr_t)
print('BCDR Score p-value:', bcdr_p)
print(f'\nGroup A Equal Variances Test:{t_test_equal_variances(group_a_crypto, group_a_bcdr)}')
print(f'Group B Equal Variances Test:{t_test_equal_variances(group_b_crypto, group_b_bcdr)}\n')

# Perform Welch's t-test on the Cryptography_Score column
crypto_t, crypto_p = ttest_ind(group_a_crypto, group_b_crypto, equal_var=False)

# Perform Welch's t-test on the BCDR_Score column
bcdr_t, bcdr_p = ttest_ind(group_a_bcdr, group_b_bcdr, equal_var=False)

# Print the results
print('Cryptography Score Welch\'s t-value:', crypto_t)
print('Cryptography Score Welch\'s p-value:', crypto_p)
print('BCDR Score Welch\'s t-value:', bcdr_t)
print('BCDR Score Welch\'s p-value:', bcdr_p)
