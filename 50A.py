def main():
    m, n = map(int, input().split())
    # Maximum dominoes = total squares // 2
    print((m * n) // 2)

if __name__ == "__main__":
    main()
