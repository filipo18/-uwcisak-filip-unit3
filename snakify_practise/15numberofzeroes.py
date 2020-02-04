#This program counts number of zeroes 
N=int(input())
answer=0
for i in range(N):
    N=int(input())
    if N==0:
        answer+=1
print(answer)
