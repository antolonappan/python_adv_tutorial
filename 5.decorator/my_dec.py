def subb(func):
    def wrapper(*args):
        return  args[0] - args[1]
    return wrapper
