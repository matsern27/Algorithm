import pandas as pd
from random import randint

df = pd.read_csv("Numbers")
listNumbers = [df["0"][i] for i in range(len(df))]


def Merge(list1 : list, list2: list) -> list:
    leftPoint, rightPoint = 0,0
    FinelList = []
    while True:
        if list1[leftPoint] > list2[rightPoint]:
            FinelList.append(list2[rightPoint])
            rightPoint += 1
            if rightPoint == len(list2):
                return FinelList + list2[leftPoint:]
        else:
            FinelList.append(list1[leftPoint])
            leftPoint += 1
            if leftPoint == len(list1):
                return FinelList + list2[rightPoint:]

def MergeSort(NumberList : list) -> list:
    if len(NumberList) < 3:
        if len(NumberList) == 2:
            if NumberList[1] < NumberList[0]:
                return NumberList[::-1]
        return NumberList
    else:
        mid = len(NumberList) // 2
        right = NumberList[mid:]
        left = NumberList[:mid]
        return Merge(MergeSort(left), MergeSort(right))

