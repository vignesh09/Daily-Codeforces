import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    t = int(input())
    vector = [0,0,0]
    for _ in range(t):
        x, y, z = list(map(int, input().split()))

        vector[0] += x
        vector[1] += y
        vector[2] += z

    if vector == [0,0,0]:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
