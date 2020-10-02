arr=list(map(int,input().split()))
search=int(input())
for i in range(len(arr)):
    if arr[i]==search:
        print(i+1)
        break
    
