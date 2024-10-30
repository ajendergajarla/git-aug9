'''
printing subsequences of a given array
ex:                     
input1: a = [3,1,2]
output1: 
[3, 1, 2]
[3, 1]
[3, 2]
[3]
[1, 2]
[1]
[2]
[]

input2: a = [1,2,3,4]
output2:
[1, 2, 3, 4]
[1, 2, 3]
[1, 2, 4]
[1, 2]
[1, 3, 4]
[1, 3]
[1, 4]
[1]
[2, 3, 4]
[2, 3]
[2, 4]
[2]
[3, 4]
[3]
[4]
[]
'''

def sub(ind, l, arr, n):
    if(ind == n):
        print(l)
        return
    
    l.append(arr[ind])
    sub(ind+1, l, arr, n)
    

    l.pop()
    sub(ind+1, l, arr, n)

arr=list(map(int,input("enter...").split()))
sub(0,[],arr,len(arr))
