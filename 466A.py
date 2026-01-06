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
    # n is the number rides
    # m is the number of rides you can take with a special ticket
    # a is the cost of a single ride ticket
    # b is the cost of a special ticket
    n,m,a,b = map(int, input().split())
    if m * a <= b:
        print(n * a)
    else:
        total = (n // m) * b + min((n % m) * a, b)
        print(total)
    

if __name__ == "__main__":
    main()
