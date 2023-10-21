import pandas as pd

df = pd.read_csv("Numbers")
listNumbers = [df["0"][n] for n in range(len(df))]

for pointInd in range(len(listNumbers)):
    for compareNumber in range(len(listNumbers)-(1+pointInd)):
        if listNumbers[compareNumber] > listNumbers[compareNumber+1]:
            listNumbers[compareNumber], listNumbers[compareNumber+1] = listNumbers[compareNumber+1], listNumbers[compareNumber]


print(listNumbers)
