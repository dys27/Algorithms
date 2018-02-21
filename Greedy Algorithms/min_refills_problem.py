def minRefills(x=[0,200,375,550,750,950],n=4 ,L=400) :
            numRefills=0
            currentRefill=0
            while currentRefill<=n:
               lastRefill=currentRefill
               while (currentRefill<=n and (x[currentRefill+1]-x[lastRefill]<=L)):
                  currentRefill=currentRefill+1
               if currentRefill == lastRefill:
                  return "Not Possible"
               if currentRefill<=n:
                  numRefills=numRefills+1
            return numRefills
               
            
    
