# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    a=[]
    W=[]
    V=[]
    j=0
    for i in range (len(weights)):
        a.append(values[i]/float(weights[i]))
    b=sorted(a,reverse=True)
    for i in b:
        k=a.index(i)
        W.append(weights[k])
        V.append(values[k])
    while j <(len(W)):
        if capacity==0:
            return value
        elif W[j]<=capacity:
            capacity-=W[j]
            value+=V[j]
            j+=1
        elif W[j]>capacity:
            value+=(b[j]*capacity)
            capacity=0
            j+=1
    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
