# Uses python3
import sys

def get_change(m):
    arr=[1,3,4]
    minCoins=[0]*(m+1)
    coinsUsed=[0]*(m+1)
    for i in range (m+1):
        coinCount=i
        newCoin=1
        for j in [ c for c in arr if c<=i]:
            if minCoins[i-j]+1<coinCount:
                coinCount=minCoins[i-j]+1
                newCoin=j
        minCoins[i]=coinCount
        coinsUsed[i]=newCoin
    print minCoins
    print coinsUsed
    return (minCoins[m])

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
