#QuickSort
from random import randint
def QuickSort(a,low,high):
    if low<high:
        pi=partition(a,low,high)
        QuickSort(a,low,pi-1)
        QuickSort(a,pi+1,high)
    return a
def partition(a,low,high):
    pivot=randint(low,high)
    i=low-1
    a[high],a[pivot]=a[pivot],a[high]
    for j in range(low,high):
        if a[j]<=a[high]:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return (i+1)
