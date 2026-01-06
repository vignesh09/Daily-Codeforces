import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    t = int(input())
    x=0
    for _ in range(t):
        if "+" in input():
            x+=1
        else:
            x-=1
    print(x)

if __name__ == "__main__":
    main()
