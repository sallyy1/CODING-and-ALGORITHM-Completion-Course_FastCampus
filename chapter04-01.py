# Chapter04-1
# 파이썬 심화

# 일급 함수(일급 객체)

# 파이썬 함수 특징
# 1. 런타임 초기화 가능
# 2. 변수 등에 할당 가능
# 3. 함수에 인수로 전달 가능 - sorted(keys=len(a))
# 4. 함수 결과로 반환 가능 - return funcs

# 함수 객체 예제

def factorial(n):
    '''Factorial Function -> n: int'''
    #print('run!!')
    if n == 1: # n < 2
        return 1
    return n * factorial(n-1)

class A:
    pass

print('EX1-1 -', factorial(5))
print('EX1-2 -', factorial.__doc__)
print('EX1-3 -', type(factorial), type(A)) # <class 'function'> <class 'type'>
print('EX1-4 -', sorted(set(dir(factorial)) - set(dir(A))) ) # 함수만 남음 ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
print('EX1-5 -', factorial.__name__) # factorial
print('EX1-5 -', factorial.__code__) # <code object factorial at 0x7fc6de190500, file "/Users/hyun/Desktop/FastCampus/python_test/chapter04-01.py", line 14>

print()
print()


# 변수 할당
var_func = factorial # factorial() 만 쓰면 n이 없어 오류 뜸

print('EX2-1 -', var_func) # <function factorial at 0x7f99b0dba160>
print('EX2-2 -', var_func(5)) # 120
print('EX2-3 -', map(var_func, range(1,6))) # <map object at 0x7ff0d3a57f40>
print('EX2-4 -', list(map(var_func, range(1,6)))) # [1, 2, 6, 24, 120]

# map 함수 : 함수 인자를 받아서, 연속적인 iterator 갯수만큼 함수를 실행해주는 역할


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-Order-Function)

print('EX3-1 -', list(map(var_func, filter(lambda x: x%2, range(1,6))))) # 홀수(1!, 3!, 5!)만 실행됨 -> [1, 6, 120]
print('EX3-2 -', [var_func(i) for i in range(1, 6) if i % 2])

print()
print()


# reduce() 함수
from functools import reduce
from operator import add

print('EX3-3 -', reduce(add, range(1, 11))) # add는 함수
print('EX3-4 -', sum(range(1, 11)))


# 익명함수(lambda)
# 가급적 주석 사용
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장

print('EX3-5 -', reduce(lambda x, t: x + t, range(1, 11)))

print()
print()

# Callable : 호출 연산자 (매직 메소드)-> 메소드 형태로 호출 가능한지 확인
#funcs()


import random

# 로또 추첨 클래스 선언
class LottoGame:
    def __init__(self):
        self._balls = [n for n in range(1, 46)]

    def pick(self):
        random.shuffle(self._balls)
        return sorted([random.choice(self._balls) for n in range(6)])

    def __call__(self):
        return self.pick() # 자신의 메소드를 호출할 수 있도록 함수 만들 수 있음

# 객체 생성
game = LottoGame()

# 게임 실행
# 호출 가능 확인
print('EX4-1 -', callable(str), callable(list), callable(factorial), callable(3.14)) # True True True False
print('EX4-2 -', game.pick())

#game() # TypeError: 'LottoGame' object is not callable
print('EX4-3 -', game()) # 이제 호출 가능 -> 함수에 인자로서도 넣을 수 있음
print('EX4-4 -', callable(game)) # True

print()
print()


# 다양한 매개변수 입력(*args, **kwargs) -> 튜플 형태 vs 딕셔너리 형태로 받음
def args_test(name, *contents, point=None, **attrs):
    return '<agrs_test> -> ({})({})({})({})'.format(name, contents, point, attrs)

print('EX5-1 -', args_test('test1'))
# <agrs_test> -> (test1)(())(None)({})

print('EX5-2 -', args_test('test1', 'test2'))
# <agrs_test> -> (test1)(('test2',))(None)({})

print('EX5-3 -', args_test('test1', 'test2', 'test3', id='admin'))
# <agrs_test> -> (test1)(('test2', 'test3'))(None)({'id': 'admin'})

print('EX5-4 -', args_test('test1', 'test2', 'test3', id='admin', point=7))
# <agrs_test> -> (test1)(('test2', 'test3'))(7)({'id': 'admin'})

print('EX5-5 -', args_test('test1', 'test2', 'test3', id='admin', point=7, password='1234'))
# <agrs_test> -> (test1)(('test2', 'test3'))(7)({'id': 'admin', 'password': '1234'})

print()
print()

# 함수 Gignatures
from inspect import signature

sg = signature(args_test)

print('EX6-1 -', sg) # (name, *contents, point=None, **attrs)
print('EX6-2 -', sg.parameters) # OrderedDict([('name', <Parameter "name">), ('contents', <Parameter "*contents">), ('point', <Parameter "point=None">), ('attrs', <Parameter "**attrs">)])

print()
print()


# 모든 정보 출력
for name, param in sg.parameters.items():
    print('EX6-3 -', name, param.kind, param.default)

'''
EX6-3 - name POSITIONAL_OR_KEYWORD <class 'inspect._empty'>
EX6-3 - contents VAR_POSITIONAL <class 'inspect._empty'>
EX6-3 - point KEYWORD_ONLY None
EX6-3 - attrs VAR_KEYWORD <class 'inspect._empty'>
EX6-3 - (name, *contents, point=None, **attrs)
'''

print()
print()

# partial 사용법 : 인수 고정 -> 인수를 고정 후 콜백 함수에 사용
# 하나 이상의 인수가 이미 할당된(채워진) 함수의 새 버전 반환
# 함수의 새 객체 타입은 이전 함수의 자체를 기술하고 있다

from operator import mul
from functools import partial

print('EX7-1 -', mul(10, 100))

# 인수 고정
five = partial(mul, 5) # mul 함수에 인수 하나는 고정

# 고정 추가
six = partial(five, 6)

print('EX7-2 -', five(100))
print('EX7-3 -', six())
print('EX7-4 -', [five(i) for i in range(1, 11)]) # list Generator 만들기에 활용 -> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
print('EX7-5 -', list(map(five, range(1,11)))) # map 활용 -> [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

