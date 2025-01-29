import numpy as np


def sigmoid_1(x: int):
    return 1 / (1 + np.exp(-x))


def sigmoid_2(x: int):
    return 1 / (1 + _exp(-x))


# exp() 함수(자연로그 e의 x 승 값)는 테일러 급수, 무한급수로 구현이 가능하다.
def _exp(x, terms=100):
    result = 0.0
    factorial = 1.0
    for n in range(terms):
        result += x**n / factorial
        factorial *= (n + 1)
    return result

print(sigmoid_1(1))  # e^1 = e
print(sigmoid_2(1))  # e^1 = e

print(np.exp(-1))
print(_exp(-1))

x = 2
y = 2.2
z = '1'
z1 = "1"
zz = (1, 1)
zzz = [1, 1]
zzzz = 1.1,

print(f'{type(x)}, {type(y)}, {type(z)}')
print(f'{type(zzzz)}')

'''
0.7310585786300049
0.7310585786300049
0.36787944117144233
0.36787944117144245
<class 'int'>, <class 'float'>, <class 'str'>
<class 'tuple'>
'''