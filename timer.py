import time

def timer(f, *param):
    """
    A function that checks the duration of functions
    :param fanction
    :param parameter to the fanction
    :return The time it took to activate the function
    """
    Initial_time_check = time.time()
    f(param)
    Final_time_check = time.time()
    return(Final_time_check - Initial_time_check)


if __name__ == "__main__":
    print(timer(print, "Hello"))
    print(timer(zip, [1, 2, 3], [4, 5, 6]))
    print()