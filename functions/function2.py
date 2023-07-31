#args function

# def demo(a):
#     print(a)
    
# demo(10,20)    


def getData(k,*args,p):
    print("p =",p)
    print(k)
    print(args)
    print(type(args))

getData(10,20,30,40,50,p=1000)    