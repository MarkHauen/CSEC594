from os import path

dataFileName = "SurveyDataTrimed"
finalHeaders = "Cryptography_Score|BCDR_Score|Group|Gender|Education|Cryptography_Exp|BCDR_Exp"

def getRoot():
    return path.dirname(path.realpath(__file__))

def getDataPath(fileName):
    return "{r}\\{fn}.csv".format(r=getRoot(), fn=fileName)

def getFileLines(fileName):
    with open(getDataPath(fileName), mode='rt') as reader:
        return reader.readlines()

def getCorrectAnswers():
    return getFileLines(dataFileName)[1]

def getDataLines():
    return getFileLines(dataFileName)[2:]

def writeDataLines(fileName, dataLines):
    with open("{r}\\{fn}.csv".format(r=getRoot(), fn=fileName), mode='wt') as writer:
        writer.write("{h}\n{dl}".format(h=finalHeaders, dl=dataLines))

newData = []

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
    for i in range(len(BCDRAnswers)):
        if BCDRAnswers[i] == getCorrectAnswers().split(",")[i + 10]:
            BCDRScore = BCDRScore + 1
    x = "|".join([str(CryptoScore), str(BCDRScore)] + Demographics)

    newData.append(x)


writeDataLines("SurveyDataScored", "\n".join(newData))

