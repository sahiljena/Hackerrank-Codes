'''
Author @ Shubhanshu jain
'''

#Firstly take a input for test 
#For every test case take input n
#Find the value of 2 power n
#Subtract one from that value and print using % 100000

def powers(val,p):
  x = val**p
  return x

t=int(input())
for i in range(t):
    n=int(input())
    n=powers(2,n)
    n=n-1;
    print(n%100000)


