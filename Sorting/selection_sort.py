def selection_sort(arr):
    n=len(arr)
    for i in range(n):
        min_no=i
        for j in range(i+1,n):
            if arr[j]<arr[min_no]:
                min_no=j
        arr[i],arr[min_no]=arr[min_no],arr[i]
    return arr
            
