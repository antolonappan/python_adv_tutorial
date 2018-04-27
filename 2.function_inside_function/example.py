'''
See how to define fuction inside function,
you can define multiple functions.

'''


def arith(a,b,c):
    def ins(c):
        return c**2
    return a + b + ins(c)

print(arith(1,1,1))
