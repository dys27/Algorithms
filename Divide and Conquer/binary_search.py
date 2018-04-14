# Uses python3
import sys
def binary_search(a,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if x==a[mid]:
            return mid
        elif x<a[mid]:
            high=mid-1
        elif x>a[mid]:
            low=mid+1
    return -1

    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x,low=0,high=len(a)-1), end=' ')

                            
