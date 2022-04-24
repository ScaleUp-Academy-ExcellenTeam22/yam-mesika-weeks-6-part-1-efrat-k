import time
"""
A function that checks the duration of functions
"""
def timer(f, *param):
    start = time.time()
    f(param)
    time.sleep(1)
    end = time.time()
    return(end - start-1)


if __name__=="__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print()
