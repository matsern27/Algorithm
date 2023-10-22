import pandas as pd

df = pd.read_csv("Numbers")
numberList = [df["0"][i] for i in range(len(df))]

for comparePosStart in range(1,len(numberList)):
    for valueInd in range(comparePosStart,0, -1):
        if numberList[valueInd] < numberList[valueInd-1]:
            numberList[valueInd], numberList[valueInd-1] = numberList[valueInd-1], numberList[valueInd]
        else:
            break

print(numberList)
