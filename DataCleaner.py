from ioTools import getDataLines, getCorrectAnswers,writeDataLines

def getPercent(lst, n):
    return ",".join(['%' + str(int(round(100 * round((x/n), 2), 0))) for x in lst])

Data = {'exam1': [],
        'exam2': [],
        'learning_group': [],
        'age': [],
        'gender': [],
        'education': [],
        'cryptography_exp': [],
        'BCDR_exp': [],
        'output': ""}

newData = []
cryptoQuestionsCorrectAnswers = [0 for x in range(10)]
bcdrQuestionsCorrectAnswers = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersA = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersA = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersB = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersB = [0 for x in range(10)]
for entry in getDataLines():
    data = entry.split(",")
    CryptoAnswers = data[:10]
    BCDRAnswers = data[10:20]
    Demographics = [x.replace("None", "None_") for x in data[20:26]]
    if Demographics[0] == 'A':
        Demographics[0] = '1'
    else:
        Demographics[0] = '2'
    CryptoScore = 1
    BCDRScore = 1
    for i in range(len(CryptoAnswers)):
        if CryptoAnswers[i] == getCorrectAnswers().split(",")[i]:
            CryptoScore = CryptoScore + 1
            cryptoQuestionsCorrectAnswers[i] = cryptoQuestionsCorrectAnswers[i] + 1
            if Demographics[0] == '1':
                cryptoQuestionsCorrectAnswersA[i] = cryptoQuestionsCorrectAnswersA[i] + 1
            else:
                cryptoQuestionsCorrectAnswersB[i] = cryptoQuestionsCorrectAnswersB[i] + 1
    for i in range(len(BCDRAnswers)):
        if BCDRAnswers[i] == getCorrectAnswers().split(",")[i + 10]:
            BCDRScore = BCDRScore + 1
            bcdrQuestionsCorrectAnswers[i] = bcdrQuestionsCorrectAnswers[i] + 1
            if Demographics[0] == '1':
                bcdrQuestionsCorrectAnswersA[i] = bcdrQuestionsCorrectAnswersA[i] + 1
            else:
                bcdrQuestionsCorrectAnswersB[i] = bcdrQuestionsCorrectAnswersB[i] + 1
    newData.append("|".join([str(CryptoScore), str(BCDRScore)] + Demographics))

for x in newData:
    line =  x.split("|")
    if line[2] == '1':
        Data['learning_group'].append(1)
    if line[2] == '2':
        Data['learning_group'].append(2)
    Data['exam1'].append(int(line[0]))
    Data['exam2'].append(int(line[1]))
    Data['age'].append(int(line[3]))
    if line[4][0] == 'M':
        Data['gender'].append(1)
    else:
        Data['gender'].append(2)
    if line[5][0] == 'H':
        Data['education'].append(1)
    if line[5][0] == 'S':
        Data['education'].append(2)
    if line[5][0] == 'A':
        Data['education'].append(3)
    if line[5][0] == 'B':
        Data['education'].append(4)
    if line[5][0] == 'G':
        Data['education'].append(5)
    if line[5][0] == 'P':
        Data['education'].append(6)
    if line[6][0] == 'N':
        Data['cryptography_exp'].append(1)
    if line[6][0] == 'I':
        Data['cryptography_exp'].append(2)
    if line[6][0] == 'F':
        Data['cryptography_exp'].append(3)
    if line[7][0] == 'N':
        Data['BCDR_exp'].append(1)
    if line[7][0] == 'I':
        Data['BCDR_exp'].append(2)
    if line[7][0] == 'F':
        Data['BCDR_exp'].append(3)


Data['output'] = f'Percentage of correct answers for each Question:\n' + \
f'   Overall Cryptography: {getPercent(cryptoQuestionsCorrectAnswers, 26)}\n' + \
f'   Overall BCDR: {getPercent(bcdrQuestionsCorrectAnswers, 26)}\n' + \
f'   Group 1 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersA, 11)}\n' + \
f'   Group 1 BCDR: {getPercent(bcdrQuestionsCorrectAnswersA, 11)}\n' + \
f'   Group 2 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersB, 15)}\n' + \
f'   Group 2 BCDR: {getPercent(bcdrQuestionsCorrectAnswersB, 15)}'

writeDataLines("SurveyDataScored", "\n".join(newData))


