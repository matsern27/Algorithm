import pandas as pd
df = pd.read_csv("Numbers")
nums = [df["0"][n] for n in range(len(df))]
for pointInd in range(len(nums)):
    for compareNumber in range(len(nums) - (1 + pointInd)):
        if nums[compareNumber] > nums[compareNumber + 1]:
            nums[compareNumber], nums[compareNumber + 1] = nums[compareNumber + 1], nums[compareNumber]
print(nums)
