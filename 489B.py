import sys
from itertools import combinations
import time
import tracemalloc
from functools import wraps

"""
The first line contains an integer n (1 ≤ n ≤ 100) — the number of boys. The second line contains sequence a1, a2, ..., an (1 ≤ ai ≤ 100), where ai is the i-th boy's dancing skill.

Similarly, the third line contains an integer m (1 ≤ m ≤ 100) — the number of girls. The fourth line contains sequence b1, b2, ..., bm (1 ≤ bj ≤ 100), where bj is the j-th girl's dancing skill.

Output
Print a single number — the required maximum possible number of pairs.
"""

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

# @measure_time_memory
def main():
    b = int(input())
    boys = list(map(int, input().split()))
    g = int(input())
    girls = list(map(int, input().split()))
    boys.sort()
    girls.sort()
    b_i = 0
    g_i = 0
    pairs = 0
    while b_i < b and g_i < g:
        if abs(boys[b_i] - girls[g_i]) <= 1:
            pairs += 1
            b_i += 1
            g_i += 1    
        elif  boys[b_i] <  girls[g_i]:
            b_i += 1    
        else:
            g_i += 1   
    print(pairs)

if __name__ == "__main__":
    main()
