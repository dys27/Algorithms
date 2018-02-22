#The goal in this problem is to find the minimum number of coins
#needed to change the input value (an integer) into coins
#with denominations 1, 5, and 10. 
import sys

def get_change(m):
    count=0
    while m!=0:
        if m<10:
            if m<5:
                count+=m
                return count
            else:
                a=m/5
                m=m%5
                count+=a
        else:
            b=m/10
            m=m%10
            count+=b
            
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
