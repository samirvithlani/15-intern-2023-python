def demo():
    print("This is function 1")
    #no return statement no arg


def add(a,b):
    #x = a+b
    #return x    
    return a+b

def greet(name):
    print("Hello",name)
    # return

demo()    

ans = add(10,20)
print(ans)
print(add(100,200))

greet("sachin")
print(greet("samyak")) #None


def test():
    return 10.20


p = test()
print("p -",p)