import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    res = 0
    k = list(map(int,input().split()))[1]
    arr = list(map(int,input().split()))
    temp = arr[k]
    for i in arr:
        if i >= temp and i != 0:
            res+=1
    print(res)
if __name__ == "__main__":
    main()
