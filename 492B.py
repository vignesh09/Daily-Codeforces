import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # logic here

def main():
    _, l = list(map(int, input().split()))
    distance_list = []
    point = list(map(int, input().split()))
    sorted_points = sorted(point)
    if sorted_points[0] != 0:
        distance_list.append(sorted_points[0] - 0)
    if sorted_points[-1] != l:
        distance_list.append(l - sorted_points[-1])
    for index in range(_-1):
        distance_list.append((sorted_points[index+1] - sorted_points[index])/2)
    print(max(distance_list))

if __name__ == "__main__":
    main()  
