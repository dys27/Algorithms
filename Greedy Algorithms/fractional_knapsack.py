def fractional_knapsack(W=7,w=[2,3,4],v=[14,18,20]):
    V=0
    for i in range(len(w)):
        if W==0:
            return V
        elif w[i]<=W:
            W=W-w[i]
            V+=v[i]
        else:
            b=w[i]-W
            W=W-b
            V+=((v[i]/w[i])*b) 
    return V
        
        
    

        
    
               
            
    
