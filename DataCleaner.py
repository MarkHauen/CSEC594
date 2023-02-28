from ioTools import getDataLines, getCorrectAnswers,writeDataLines

def getPercent(lst, n):
    return ",".join(['%' + str(int(round(100 * round((x/n), 2), 0))) for x in lst])

newData = []
cryptoQuestionsCorrectAnswers = [0 for x in range(10)]
bcdrQuestionsCorrectAnswers = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersA = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersA = [0 for x in range(10)]
cryptoQuestionsCorrectAnswersB = [0 for x in range(10)]
bcdrQuestionsCorrectAnswersB = [0 for x in range(10)]
badCryptoAnswers = []
badBCDRAnswers = []
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
    if x.split("|")[2] == '1':
        print(x.replace("|", " & ").replace("_", "").replace("Training/Experience ", "").replace("School ", "").replace("Degree ", "").strip() + " \\\\")
for x in newData:
    if x.split("|")[2] == '2':
        print(x.replace("|", " & ").replace("_", "").replace("Training/Experience ", "").replace("School ", "").replace("Degree ", "").strip() + " \\\\")

print(f'Overall Cryptography: {getPercent(cryptoQuestionsCorrectAnswers, 26)}')
print(f'Overall BCDR: {getPercent(bcdrQuestionsCorrectAnswers, 26)}')

print(f'Group 1 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersA, 11)}')
print(f'Group 1 BCDR: {getPercent(bcdrQuestionsCorrectAnswersA, 11)}')

print(f'Group 2 Cryptography: {getPercent(cryptoQuestionsCorrectAnswersB, 15)}')
print(f'Group 2 BCDR: {getPercent(bcdrQuestionsCorrectAnswersB, 15)}')

writeDataLines("SurveyDataScored", "\n".join(newData))

