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
        n, x = map(int, input().split())
        arr = list(map(int, input().split()))

        odd = sum(a % 2 for a in arr)
        even = n - odd

        # Try using an odd number of odd elements
        found = False
        for k_odd in range(1, min(odd, x) + 1, 2):
            if x - k_odd <= even:
                found = True
                break

        print("Yes" if found else "No")

if __name__ == "__main__":
    main()
