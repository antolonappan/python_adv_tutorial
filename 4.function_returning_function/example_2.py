'''
This modified version can use as 'normal' also as 'enh'
'''
def addd(a, b,**kargs):
    def enh_addd(c):
        return a + b + c

    if len(kargs) is not 0:
        if kargs['enh']:
            return enh_addd
        elif not kargs['enh']:
            return a + b
    else:
        return a + b


print(addd(1,2)) # prints 3
print(addd(1,2,enh=True)) # prints function id and memory
d = addd(1,2,enh=True)
print(d(1)) # prints 4
print(addd(1,2, enh=False)) # prints 3
