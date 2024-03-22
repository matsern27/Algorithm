import pandas as pd


df = tuple(pd.read_csv("Numbers")["0"])


def pancake_sort(numbers=df):

    for ind in range(len(numbers)-1):
        large_ind = numbers[:len(numbers)-ind].index(max(numbers[:len(numbers)-ind]))
        numbers = numbers[:large_ind+1][::-1] + numbers[large_ind+1:]
        numbers = numbers[:len(numbers)-ind][::-1] + numbers[len(numbers)-ind:]

    return numbers


def main():
    print(pancake_sort(df))


if __name__ == "__main__":
    main()
