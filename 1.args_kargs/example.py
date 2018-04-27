'''
Whats are args and kargs?
-------------------------

1. args and kargs are just names, you can choose any name.
2. No. of astrids defines the purposes

*args
-----
For arguments without any assignments
ex: function(1,3)
args[i] gives the value of i^th element

**kargs
-------
For arguments with assignments
ex: function(a=1, b=3)
kargs['a'] gives the value binded to the key 'a'

------------------------------------------------------------
If no args or kargs given, then len(args) and len(kargs) = 0
------------------------------------------------------------

Where to use it ?
-----------------
Consider function1(a,b) and function2(c,d),
This two functions depends on two different set of variables.
If you want to call function2 directly from function1 with an option
to take arguments of function2. Then you can do it like

def function1(a,b,*args,**kargs):
     function2(*args,**kargs)

then call function1(1,2,3,4)
  =>  a and b takes the values 1 and 2 res.
  =>  usage of *args passes the value 3 and 4 to c and d res.

or for the call function1(1, 2, d=4, c=3)
  =>  a and b takes the values 1 and 2 res.
  =>  usage of *kargs passes the value 4 and 3 to d and c res.
  =>  IMP: since here you are passing arguments by assigning
           order doesn't matters, but in *args order matters.
'''
def test(a, *args, **kargs):
    print(a)
    print(args) #tweek to see  args[0] and kargs['variable']
    print(kargs)
    return None

if __name__ == '__main__':
    test(1,w=4)
    
