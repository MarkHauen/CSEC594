import csv
from scipy.stats import ttest_ind

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
print(f'Cryptography Score t-value: {round(crypto_t, 2)}')
print(f'Cryptography Score p-value: {round(crypto_p, 2)}')
print(f'BCDR Score t-value: {round(bcdr_t, 2)}')
print(f'BCDR Score p-value: {round(bcdr_p, 2)}\n')

