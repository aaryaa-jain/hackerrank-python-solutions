# Problem: Average of Sets
# Platform: HackerRank

def average(array):
    unique_values = set(array)
    result = sum(unique_values) / len(unique_values)
    return round(result, 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(average(arr))
