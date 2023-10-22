import numpy as np

def pybogosort(l):
    while True:
        l = np.random.permutation(l)
        if not sum(map(lambda tup: tup[0] > tup[1], zip(l[:-1], l[1:]))):
            return l


def bogosort(l):
    while True:
        l = np.random.permutation(l)
        print(l)
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                break
            elif i == len(l)-2:
                return l


def test():
    l = np.random.randint(0, 10, 4)
    print(l)
    # print(bogosort(l))
    print()
    print(pybogosort(l))


def main():
    test()

main()
