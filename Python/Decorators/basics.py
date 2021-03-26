

def my_deco(func):
    # print("Test0000")
    def mwrapper(*args, **kwargs):
        # # print("Test111")
        # if len(args) != 2:
        #     print("Error in input args, no decorator executed")
        #     return func(*args)
        # # print("Test")
        # print(args)
        return func(args[1], args[0])
    return mwrapper

@my_deco
def mypow(a,b):
    return a**b


print(mypow(2,3))