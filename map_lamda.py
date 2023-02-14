cube = lambda x:x**3 
def fibonacci(n):
    ls=[]
    for i in range(n):
        if(i/2<1):
            x=i
            ls.append(x)
        else:
            x=ls[i-1]+ls[i-2]
            ls.append(x)
    return ls   
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
