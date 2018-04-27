'''
A defintion can also return another function

'''
def addd(a, b):
    def enh_addd(c):
        return a + b + c
    return enh_addd

if __name__ == "__main__":
    print(addd(1,2)) # prints the function object and its memory location
    
    d = addd(1,2) # d is an another function which can take a single argument
    print(d(3))
