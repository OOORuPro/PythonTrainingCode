A,B=map(int,input().split())
k=1
for item in range(A,B+1,1):
    for j in range(k):
        print(item)
    k+=1
