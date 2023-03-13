from ioTools import getDataLines, getCorrectAnswers, writeDataLines

def getPercent(lst, n):  # Return a a list of numbers as string of percentages
    return ",".join(['%' + str(int(round(100 * round((x / n), 2), 0))) for x in lst])

# Dictionary to hold data for each participant
RegressionData = {
    'exam1': [],
    'exam2': [],
    'learning_group': [],
    'age': [],
    'gender': [],
    'education': [],
    'cryptography_exp': [],
    'BCDR_exp': [],
    'output': ""}

# Dictionaries to translate answers into scalar values for regression
edu_dict = {'H': 1, 'S': 2, 'A': 3, 'B': 4, 'G': 5, 'P': 6}
crypto_dict = {'N': 1, 'I': 2, 'F': 3}
bcdr_dict = {'N': 1, 'I': 2, 'F': 3}

# List to hold the data for the output file
newData = []

# Lists to hold the number of correct answers for each question for each group
cryptoQuestionsCorrectAnswers = [0 for x in range(10)]
bcdrQuestionsCorrectAnswers = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersA = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersA = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersB = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersB = [0 for x in range(10)]

# Loop through the data and calculate the scores for each participant
for entry in getDataLines():
    data = entry.split(",")  # Split the data into a list
    CryptoAnswers = data[:10]  # Get the answers for the cryptography exam
    BCDRAnswers = data[10:20]  # Get the answers for the BCDR exam
    # Get the demographics, replace values to avoid errors
    Demographics = [x.replace("None", "None_") for x in data[20:26]]
    Demographics[0] = '1' if Demographics[0] == 'A' else '2'  # Convert the learning group to a number
    CryptoScore = 1  # Set the score to 1 to avoid division by zero
    BCDRScore = 1  # Set the score to 1 to avoid division by zero
    for i in range(len(CryptoAnswers)):  # Loop through the Cryptography answers and calculate the score
        if CryptoAnswers[i] == getCorrectAnswers()[i]:  # If the answer is correct
            CryptoScore += 1  # Add 1 to the score
            cryptoQuestionsCorrectAnswers[i] += 1  # Add 1 to the number of correct answers for this question
            if Demographics[0] == '1':  # If the participant is in group 1
                # Add 1 to the number of correct answers for this question in group 1
                cryptoQuestionsCorrectAnswersA[i] += 1
            else:  # If the participant is in group 2
                # Add 1 to the number of correct answers for this question in group 2
                cryptoQuestionsCorrectAnswersB[i] += 1
    for i in range(len(BCDRAnswers)):  # Loop through the BCDR answers and calculate the score
        if BCDRAnswers[i] == getCorrectAnswers()[i + 10]:  # If the answer is correct
            BCDRScore += 1  # Add 1 to the score
            bcdrQuestionsCorrectAnswers[i] += 1  # Add 1 to the number of correct answers for this question
            if Demographics[0] == '1':  # If the participant is in group 1
                # Add 1 to the number of correct answers for this question in group 1
                bcdrQuestionsCorrectAnswersA[i] += 1
            else:  # If the participant is in group 2
                # Add 1 to the number of correct answers for this question in group 2
                bcdrQuestionsCorrectAnswersB[i] += 1
    newData.append("|".join([str(CryptoScore), str(BCDRScore)] + Demographics))  # Add the data to the list

# Write the data to RegressionData Dictionary
for x in newData:
    line = x.split("|")
    RegressionData['learning_group'].append(1 if line[2] == '1' else 2)
    RegressionData['exam1'].append(int(line[0]))
    RegressionData['exam2'].append(int(line[1]))
    RegressionData['age'].append(int(line[3]))
    RegressionData['gender'].append(1 if line[4][0] == 'M' else 2)
    RegressionData['education'].append(edu_dict[line[5][0]])
    RegressionData['cryptography_exp'].append(crypto_dict[line[6][0]])
    RegressionData['BCDR_exp'].append(bcdr_dict[line[7][0]])
RegressionData['output'] = f'Percentage of correct answers for each Question:\n' + \
                           f'   Overall Cryptography: {getPercent(cryptoQuestionsCorrectAnswers, 26)}\n' + \
                           f'   Overall BCDR: {getPercent(bcdrQuestionsCorrectAnswers, 26)}\n' + \
                           f'   Group 1 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersA, 11)}\n' + \
                           f'   Group 1 BCDR: {getPercent(bcdrQuestionsCorrectAnswersA, 11)}\n' + \
                           f'   Group 2 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersB, 15)}\n' + \
                           f'   Group 2 BCDR: {getPercent(bcdrQuestionsCorrectAnswersB, 15)}'

# Write the data to the output file
writeDataLines("SurveyDataScored", "\n".join(newData))
