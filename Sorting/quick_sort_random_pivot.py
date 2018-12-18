#QuickSort
from random import randint
def quick_sort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quick_sort(arr,low,pi-1)
        quick_sort(arr,pi+1,high)
    return arr
def partition(arr,low,high):
    pivot=randint(low,high)
    i=low-1
    arr[high],arr[pivot]=arr[pivot],arr[high]
    for j in range(low,high):
        if arr[j]<=arr[high]:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
