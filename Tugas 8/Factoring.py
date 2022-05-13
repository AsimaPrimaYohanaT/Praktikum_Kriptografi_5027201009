# alternative:  http://factordb.com
# Result:
# status (?)	digits	    number
# P	            23 (show)	19704762736204164635843<23> = 19704762736204164635843<23>

# answer = 19704762736204164635843 

from math import sqrt

def PrimeFactor(n):
    m = n
    while n%2==0:
        n = n//2
    if n == 1:         # check if only 2 is largest Prime Factor 
        return 2
    i = 3
    sqrt = int(m**(0.5))  # loop till square root of number
    last = 0              # to store last prime Factor i.e. Largest Prime Factor
    while i <= sqrt :
        while n%i == 0:   
            n = n//i       # reduce the number by dividing it by it's Prime Factor
            last = i
        i+=2
    if n> last:            # the remaining number(n) is also Factor of number 
        return n
    else:
        return last

num = 510143758735509025530880200653196460532653147

print(PrimeFactor(num)) 

