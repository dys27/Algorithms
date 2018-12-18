# Uses python3
import sys
def binary_search(arr,x,low,high):
    while low<=high:
        mid=low+(high-low)//2
        if x==arr[mid]:
            return mid
        elif x<arr[mid]:
            high=mid-1
        elif x>arr[mid]:
            low=mid+1
    return -1

    # write your code here

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    arr = data[1: n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(arr, x,low=0,high=len(a)-1), end=' ')

                            
