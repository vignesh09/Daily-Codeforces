# import sys
# from itertools import combinations

# def subsets_of_length_k(arr, k):
#     return list(combinations(arr, k))

    
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     arr = list(map(int, input().split()))
#     # logic here

# def main():
#     for _ in range(int(input())):
#         t = int(input())
#         count = 0
#         arr = list(map(int, input().split()))
#         for i in range (t):
#             for j in range(i+1, t):
#                 if arr[j]-arr[i] == j-i:
#                     count += 1
#         print(count)

# if __name__ == "__main__":
#     main()

import sys
from collections import defaultdict

def main():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        
        # Transform: we want pairs where a[j] - j = a[i] - i
        diff_count = defaultdict(int)
        count = 0
        
        for i in range(n):
            transformed = arr[i] - i
            # Add number of previous elements with same transformed value
            count += diff_count[transformed]
            diff_count[transformed] += 1
        
        print(count)

if __name__ == "__main__":
    main()

    