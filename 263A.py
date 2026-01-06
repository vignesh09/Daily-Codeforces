import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    arr = []
    for i in range(5):
        arr.append(list(map(int, input().split())))
    # print(arr)
    for i in range(5):
        for j in range(5):
            # print("i=", i, "j=", j)
            if arr[i][j] == 1:
                print(abs(i - 2) + abs(j - 2))
                return

if __name__ == "__main__":
    main()
