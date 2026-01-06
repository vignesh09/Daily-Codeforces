import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    t = int(input())

    # upper half
    for i in range(t + 1):
        # leading spaces
        print("  " * (t - i), end="")

        nums = []

        for j in range(i):
            nums.append(str(j))
        for j in range(i, -1, -1):
            nums.append(str(j))

        print(" ".join(nums))

    # lower half
    for i in range(t - 1, -1, -1):
        print("  " * (t - i), end="")

        nums = []

        for j in range(i):
            nums.append(str(j))
        for j in range(i, -1, -1):
            nums.append(str(j))

        print(" ".join(nums))



if __name__ == "__main__":
    main()
