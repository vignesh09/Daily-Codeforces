import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    t = input()
    # print("t=",t)
    res = []
    for letter in t:
        print("letter=",letter)
        if letter.lower() not in "aeiouy" and letter.isalpha():
            res.append(".")
            res.append(letter.lower())
    print(res)
    print("".join(res))

if __name__ == "__main__":
    main()
