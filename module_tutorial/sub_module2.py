def sub_function2():
    print("__name__ : ",__name__)
    return "Hello From Sub_Function 2"

if __name__ == "__main__" :
    print("Sub 2 is Main")
    x = sub_function2()
    print(x)