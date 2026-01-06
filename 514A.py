import sys
from itertools import combinations

def subsets_of_length_k(arr, k):
    return list(combinations(arr, k))

    
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    t = int(input())
    n= []
    while t > 0:
        n.append(t % 10)
        t = t // 10
    n.reverse()
    # print(n)
    res = []
    for i in range(len(n)):
        if n[i] == 9 and i == 0:
            res.append(str(n[i]))
        elif n[i] >= 5:
            res.append(str(9-n[i]))
        else:
            res.append(str(n[i]))
    # print(res)
    print("".join(str(i) for i in res))

if __name__ == "__main__":
    main()
