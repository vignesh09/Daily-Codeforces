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
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    q = list(map(int, input().split()))
    dict_count = {}
    sum = 1
    index = 1
    for num in a:
        tmp_sum = sum+ num-1
        while sum <= tmp_sum:
            dict_count[sum] = index
            sum += 1
        index += 1
    # print(dict_count)
    for query in q:
        print(dict_count[query])


if __name__ == "__main__":
    main()
