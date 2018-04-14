# Uses python3
import sys
from collections import defaultdict
def get_majority_element(a):
    b=defaultdict(list)
    for i in (a):
        if i not in b:
            b[i]=1
        else:
            b[i]+=1
    for j in b.values():
        if j>(len(a)/2):
            return 1
    #write your code here
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n=data[0]
    a=data[1:n+1]
    if get_majority_element(a) == 1:
        print(1)
    else:
        print(0)
