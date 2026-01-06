import sys
input = sys.stdin.readline

def solve():
    pass

def main():
    t = int(input())
    n = 0
    for _ in range(t):
        arr = list(map(int, input().split()))
        if sum(arr)>=2:
            n+=1
    print(n)
if __name__ == "__main__":
    main()
