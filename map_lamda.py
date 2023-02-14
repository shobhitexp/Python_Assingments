cube = lambda x:x**3# complete the lambda function 

def fibonacci(n):
    list = []
    
    for i in range(n):
        
        if(i==0):
            x=0
            list.append(x)
        elif(i==1):
            x = 1
            list.append(x)
        else:
            x=list[i-1]+list[i-2]
            list.append(x)
    return list  

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
