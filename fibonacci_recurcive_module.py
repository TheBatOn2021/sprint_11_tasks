import math

def input_str():
    num, modus = input().split()
    return int(num), int(modus)


def fibonacci_recurcive(limit_number, modus):
    fibPrev = 0
    fib = 1
    for i in range(limit_number):
        fibOld = fib
        fib = (fib + fibPrev) % (10 ** modus)
        fibPrev = fibOld
        print (fib)
    return

if __name__ == '__main__':
    limit_number, modus = input_str()
    fibonacci_recurcive(limit_number, modus)
