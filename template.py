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
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
