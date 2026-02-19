def miniMaxSum(arr):
    sums = []

    for i in range(len(arr)):
        total = 0
        for j in range(len(arr)):
            if j == i:
                continue
            total += arr[j]
        sums.append(total)

    print(min(sums), max(sums))


if __name__ == "__main__":
    arr = list(map(int, input().split()))
    miniMaxSum(arr)
