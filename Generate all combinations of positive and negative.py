import itertools

a=[(1,2),(2,1)]
result=[]
for mid in a:
  ls=list(itertools.product((1,-1),repeat=2))
  ls=[(mid[0]*x,mid[1]*y) for (x,y) in ls]
  result.extend(ls)
print(result)
