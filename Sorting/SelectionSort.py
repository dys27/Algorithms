def SelectionSort(a):
    n=len(a)
    for i in range(n):
        min_no=i
        for j in range(i+1,n):
            if a[j]<a[min_no]:
                min_no=j
        a[i],a[min_no]=a[min_no],a[i]
    return a
            
