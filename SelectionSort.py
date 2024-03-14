import pandas as pd

df = pd.read_csv("Numbers")
listNumbers = [df["0"][i] for i in range(len(df))]


for fisrtNoSort in range(len(listNumbers) - 1):
    compnumber = listNumbers[fisrtNoSort]
    smallNumberInd = fisrtNoSort
    for nrComp in range(fisrtNoSort + 1, len(listNumbers)):
        if compnumber > listNumbers[nrComp]:
            compnumber = listNumbers[nrComp]
            smallNumberInd = nrComp
    listNumbers[fisrtNoSort], listNumbers[smallNumberInd] = listNumbers[smallNumberInd], listNumbers[fisrtNoSort]

print(listNumbers)
