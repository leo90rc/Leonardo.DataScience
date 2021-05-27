import sys
import os

#os.getcwd()  # --> utilizarlo con jupyter notebook

def function1():
    return "function1"

def f2():
    return 2.0

def utiliza_a():
    # function_a
    pass

if __name__ == '__main__':
    import os
    dir = os.path.dirname
    src_path = dir(dir(__file__))
    print("")
    print(src_path)
    sys.path.append(src_path)
    
    from dashboard.a import function_a
    function_a()