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
    t = int(data[0])
    
    for idx in range(1, t + 1):
        n = int(data[idx])
        
        # Try to find the smallest factor a (starting from 2)
        a = 0
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                a = i
                break
        
        if a == 0:  # n is prime
            print("NO")
            continue
        
        # Now n = a * remaining
        remaining = n // a
        
        # Try to find factor b of remaining (b must be > a for distinctness)
        b = 0
        for i in range(a + 1, int(remaining**0.5) + 1):
            if remaining % i == 0:
                b = i
                break
        
        if b == 0:  # Can't find a valid b
            print("NO")
            continue
        
        # c = remaining / b
        c = remaining // b
        
        # Check if a, b, c are all distinct and >= 2
        if c > b and c >= 2:
            print("YES")
            print(f"{a} {b} {c}")
        else:
            print("NO")


if __name__ == "__main__":
    main()
