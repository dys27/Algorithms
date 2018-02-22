def min_groups(x=[3.0,4.1,5.0,5.1,5.4,6.7],n=5,L=1.0):
    current_index=0
    no_group=1
    while current_index<n:
        last_index=current_index
        while ((current_index<=n) and (x[current_index+1]-x[last_index]<=L)):
            current_index+=1
        if (x[current_index+1]-x[current_index]>L):
            current_index+=1
        if current_index<n:
            no_group+=1
    if x[current_index]-x[last_index]>L:
        no_group+=1
    return no_group
               
            
    
