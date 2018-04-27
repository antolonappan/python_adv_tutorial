'''
In the previous example, arguments of the parameter function was asgined 
inside the host function. In this example you can see how we can pass 
the arguments of the parameter function while calling the host function.
'''
def addd(a,b): # parameter function
    return a + b

def enh_addd(func, c, *args): # host function
    return  c + func(*args)

print(enh_addd(addd, 3, 1, 2))
