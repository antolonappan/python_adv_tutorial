'''
Decorators
----------

Here you can see I have used same defintion with two different name
Both functions performs addition of two given nos.

But you can see after running, the second definition perform substraction
even though it is defined as addition

@ is for decorators.

Since you gone through the previous 4 lessons, it is easy to figure out
what subb is doing. See my_dec.py

you will explore few builtin decorators in coming examples.
'''



from my_dec import subb


def addd1(a,b):
    return a + b

@subb
def addd2(a,b):
    return a + b

print(addd1(3,2))
print(addd2(3,2))
