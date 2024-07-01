'''
30) Boring Arrays
You are given an array A of size N. In one operation you can select any two elements
from it, add their absolute difference in your score.
Your task is to find and return an integer value, representing the maximum score.
Note:
Assume 1 based indexing
The elements on which operation has been performed cannot be selected again.
Input Specification:
Input1: An integer value N, representing the size of array A
input2: An integer array A
Output Specification:
Return an integer value, representing the maximum score
Sample Input:
4
1 2 3 4
Sample Output:
4
'''

input1=input()
input2=input().split()
arr=[] 
x=input2.index(input1)
for i in range(len (input2)): 
    if input2[i]=="-":
        arr.append(i)
s=1000
for i in arr:
    if abs(i-x)<s:
        s=i
print(s-1)