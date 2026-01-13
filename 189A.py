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
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    a,b,c = list(map(int, data[1:]))
    NEG = -10**9
    dp = [NEG] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        if i - a >= 0:
            dp[i] = max(dp[i], dp[i - a] + 1)
        if i - b >= 0:
            dp[i] = max(dp[i], dp[i - b] + 1)
        if i - c >= 0:
            dp[i] = max(dp[i], dp[i - c] + 1)

    print(dp[n])


if __name__ == "__main__":
    main()
