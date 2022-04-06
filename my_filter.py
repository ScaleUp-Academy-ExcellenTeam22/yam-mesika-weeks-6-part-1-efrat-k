
"""
My implementation of a filter function
"""
def my_filter(function, iter):
    return [i for i in iter if function(i)]

if __name__=="__main__":
    odd_number = lambda i: i%2==1
    list = [2,5,8,9,6,3,2,5]
    print(my_filter(odd_number,list))