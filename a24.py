'''
This weeks code chef contest problem: https://www.codechef.com/problems/CAKEHALF?tab=statement
'''
import math
def ab(A,B,C):
    if A==B: return C
    else: 
        if A>B:
            t=math.ceil(A/2)
            C+=t
            return ab(A-t,B,C)
            
        else: 
            t=math.ceil(B/2)
            C+=t
            return ab(A,B-t,C)
            
for i in range(int(input())):
    A,B = map(int,input().split())
    print(ab(A,B,C=0))