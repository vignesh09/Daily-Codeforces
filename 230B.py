import sys
from itertools import combinations
import time
import tracemalloc
from functools import wraps
import math



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


def sieve(limit: int):
    is_prime = bytearray(b"\x01") * (limit + 1)
    if limit >= 0: is_prime[0] = 0
    if limit >= 1: is_prime[1] = 0
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            step = i
            start = i * i
            is_prime[start:limit+1:step] = b"\x00" * ((limit - start) // step + 1)
    return is_prime

@measure_time_memory
def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = list(map(int, data[1:]))

    MAX_R = 10**6
    is_prime = sieve(MAX_R)

    out = []
    for x in xs:
        r = math.isqrt(x)          # exact integer sqrt
        if r * r == x and is_prime[r]:
            out.append("YES")
        else:
            out.append("NO")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
