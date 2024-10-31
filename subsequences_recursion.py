'''
printing subsequences of a given array
problem link for leetcode: https://leetcode.com/problems/subsets/description/ (easy)
GFG: https://www.geeksforgeeks.org/problems/subsets-1613027340/1 (little bit tricky)
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


'''
This problem is based on taking/adding the item to list and not taking/not adding the item to the same list.
'''

'''
leetcode answer:
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        f,l=[],[]
        def subs(ind):
            if ind == len(nums):
                f.append(l[:])
                return
                
            l.append(nums[ind])
            subs(ind+1)

            l.pop()
            subs(ind+1)

        subs(0)
        return f
'''

#gfg problem soln: passed 140/1111 took help from chatgpt
'''
#User function Template for python3

class Solution:
    def subsets(self, arr):
        # code here
        arr = sorted(set(arr)) #removed duplicates and sorted
        final =[]
        l = []
        
        def sub(i):
            if i == len(arr):
                final.append(l[:])
                return
            
            l.append(arr[i]) #including current elemet
            sub(i+1)
            
            l.pop() #excluding current elemet
            sub(i+1)
    
        sub(0)
        return sorted(final) #lexicographical order
'''

