#This program finds lost car
answer=0
N=int(input())
N2=N
for i in range(N-1):
    N=int(input())
    answer+=N
for i in range(N2):
    N2+=i
    i+=1
N2-=answer
print(N2)