import sys
from itertools import combinations
import time
import tracemalloc
from functools import wraps



input = sys.stdin.readline

def measure_time_memory(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.perf_counter()
        
        result = func(*args, **kwargs)
        
        end_time = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        print(f"Time: {end_time - start_time:.6f}s")
        print(f"Memory: {peak / 1024 / 1024:.2f} MB")
        return result
    return wrapper



def subsets_of_length_k(arr, k):
    return list(combinations(arr, k))



def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

@measure_time_memory
def main():
    input = sys.stdin.readline
    n = int(input().strip())
    a = list(map(int, input().split()))

    # 1) find first inversion
    l = -1
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            l = i
            break

    # already sorted -> reverse any length-1 segment
    if l == -1:
        print("yes")
        print(1, 1)
        return

    # 2) extend while strictly decreasing
    r = l
    while r + 1 < n and a[r] > a[r + 1]:
        r += 1

    # 3) reverse that segment
    b = a[:]
    b[l:r+1] = reversed(b[l:r+1])

    # 4) check sorted
    if all(b[i] < b[i + 1] for i in range(n - 1)):
        print("yes")
        print(l + 1, r + 1)  # convert to 1-based
    else:
        print("no")


if __name__ == "__main__":
    main()
