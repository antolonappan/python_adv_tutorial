'''
Here one can see how a function takes another function
as an argument.

To see modified codes see example_2.py and example_3.py
'''

def addd(a,b):
    return a + b

def enh_addd(func, c):
    x = 1
    y = 1
    return  c + func(x,y)

print(enh_addd(addd, 1))
