'''
The purpose of this example is same as previous one
but here we are using **kargs
'''

def addd(a,b):
    return a + b

def enh_addd(c, func, **kargs):
    if len(kargs) != 0: 
        a = float(kargs['a'])
        b = float(kargs['b'])
        return  c + func(a,b)
    else:
        raise Exception('no arguments')

print(enh_addd(1, addd, a=1, b=1))
print(enh_addd(1, addd)) # This  will give an error
