num=int(input())
l=[]
for i in range(num):
    l.append(input())
Dict = {}
for i in range(0,len(l)):
    if(l[i] in Dict ):
        Dict[l[i]]+=1
    else:
        Dict[arr[i]]=1   
print(len(Dict.keys()))
print(*(Dict.values()), sep=" ")
