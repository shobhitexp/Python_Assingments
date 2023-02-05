X=int(input())
li = list(map(int,input().strip().split()))[:X]
N=int(input())
count=0
di=list()
for i in range(N): 
  di.append(list(map(int, input().split())))

for i in range(len(di)):
    if di[i][0] in li:
      li.remove(di[i][0])
      count+=di[i][1]
    else:
        pass
print(count)
