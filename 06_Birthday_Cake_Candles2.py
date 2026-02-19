def birthdayCakeCandles(candles):
    tallest = max(candles)          # find tallest candle height
    return candles.count(tallest)   # count how many times it appears


if __name__ == "__main__":
    n = int(input())
    candles = list(map(int, input().split()))

    result = birthdayCakeCandles(candles)
    print(result)
