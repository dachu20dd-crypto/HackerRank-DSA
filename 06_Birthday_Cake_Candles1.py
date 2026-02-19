def birthdayCakeCandles(candles):
    tallest = max(candles)  # find tallest candle
    count = 0

    for i in candles:
        if i == tallest:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    candles = list(map(int, input().split()))

    result = birthdayCakeCandles(candles)
    print(result)
