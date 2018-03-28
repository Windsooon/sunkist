import inspect
import timeit
from math import sqrt


def cal_time(func, setup):
    func_strings = inspect.getsource(func)
    setup = globals()[setup]
    print(timeit.timeit(stmt=func_strings, setup=setup, number=10000000))


def myFunc():
    lst = []
    for x in range(100):
        lst.append(sqrt(x))


mysetup = "from math import sqrt"
mycode = '''
def example():
    mylist = []
    for x in range(100):
        mylist.append(sqrt(x))
'''
cal_time(myFunc, 'sqrt')

# code snippet whose execution time is to be measured

# timeit statement
print(timeit.timeit(setup=mysetup, stmt=mycode, number=10000000))
