# generate_max_474B_input.py
n = 100_000
a = [10] * n
total = sum(a)  # 1_000_000
m = 100_000
queries = [i * 10 for i in range(1, n + 1)]  # 10,20,...,1_000_000

with open("max_input.txt", "w") as f:
    f.write(f"{n}\n")
    f.write(" ".join(map(str, a)) + "\n")
    f.write(f"{m}\n")
    f.write(" ".join(map(str, queries)) + "\n")