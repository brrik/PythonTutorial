def printItem(var):
    print(var)

def sub_func1():
    x = "subfunc1-1"
    printItem(x)

def sub_func2():
    x = "subfunc1-2"
    printItem(x)

__all__ = ["sub_func1","sub_func2"]