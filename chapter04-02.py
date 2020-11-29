# Chapter04-2
# 파이썬 심화
# 일급 함수(일급 객체)

# Decorator & Closure

# 파이썬 변수 범위(global)

# 예제 1
def func_v1(a):
    print(a)
    print(b)

# 예외
#func_v1(5)

# 예제 2
b = 10 # 전역 변수

def func_v2(a):
    print(a)
    print(b)

func_v2(5)


# 예제 3
b = 10 # 전역 변수

def func_v3(a):
    print(a)
    print(b)
    b = 5 # 지역 변수 > 전역 변수 우선

#func_v3(10) # UnboundLocalError: local variable 'b' referenced before assignment


from dis import dis

print('EX1-1 -')
print(dis(func_v3)) # dis() 함수

'''
 31           0 LOAD_GLOBAL              0 (print)
              2 LOAD_FAST                0 (a)
              4 CALL_FUNCTION            1
              6 POP_TOP

 32           8 LOAD_GLOBAL              0 (print)
             10 LOAD_FAST                1 (b)
             12 CALL_FUNCTION            1
             14 POP_TOP

 33          16 LOAD_CONST               1 (5)
             18 STORE_FAST               1 (b)
             20 LOAD_CONST               0 (None)
             22 RETURN_VALUE
None
'''

print()
print()

# Closure(클로저)
# 반환되는 내부 함수에 대해서 선언된 연결을 가지고 참조하는 방식
# 반환 당시 함수의 유효범위를 벗어난 변수 또는 메소드에 직접 접근이 가능하다

a = 10

print('EX2-1 -', a + 10)
print('EX2-2 -', a + 100)

# 결과를 누적할 수 없을까?
print('EX2-3 -', sum(range(1, 51)))
print('EX2-4 -', sum(range(51, 100)))

print()
print()


# 클래스 이용
class Averager():
    def __init__(self):
        self._series = []

    def __call__(self, v):
        self._series.append(v)
        print('class >>> {} / {}'.format(self._series, len(self._series)))
        return sum(self._series) / len(self._series)

# 인스턴스 생성
avg_cls = Averager()

# 누적 확인
print('EX3-1 -', avg_cls(15))
print('EX3-2 -', avg_cls(35))
print('EX3-3 -', avg_cls(40))

print()
print()


# 클로저(Closure) 사용
# 전역변수 사용 갑소
# 디자인 패턴에도 적용 가능

def closure_avg1():
    # Free Variable 영역
    series = [] # 스냅 샷
    # 클로저 영역 -> 함수의 실행이 끝나도 사용이 가능
    def averager(v):
        #series = [] # 여기서 선언하면 유지가 되지 않음. 한 값만 저장됨
        series.append(v)
        print('def1 >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)

    return averager # 내부 함수를 리턴, Not averager()

avg_closuer1 = closure_avg1()

print('EX4-1 -', avg_closuer1) # 함수가 리턴된 상태 : <function closure_avg1.<locals>.averager at 0x7f8a13ae3c10>
print('EX4-2 -', avg_closuer1(15))
# def >>> [15] / 1
# EX4-2 - 15.0

print('EX4-3 -', avg_closuer1(35))
# def >>> [15, 35] / 2
# EX4-3 - 25.0

print('EX4-1 -', avg_closuer1(45))
# def >>> [15, 35, 45] / 3
# EX4-1 - 31.666666666666668

print()
print()

print('EX5-1 -', dir(avg_closuer1))
# ['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
print()
print('EX5-2 -', dir(avg_closuer1.__code__))
# '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'co_argcount', 'co_cellvars', 'co_code', 'co_consts', 'co_filename', 'co_firstlineno', 'co_flags', 'co_freevars', 'co_kwonlyargcount', 'co_lnotab', 'co_name', 'co_names', 'co_nlocals', 'co_posonlyargcount', 'co_stacksize', 'co_varnames', 'replace']
print()
print('EX5-3 -', avg_closuer1.__code__.co_freevars)
# ('series',)
print()
print('EX5-4 -', dir(avg_closuer1.__closure__[0]))
print('EX5-4 -', dir(avg_closuer1.__closure__[0].cell_contents))

print()
print()

# 잘못된 클로저 사용 예

def closure_avg2():
    # Free variable
    cnt = 0
    total = 0
    # 클로저 영역
    def averager(v):
        nonlocal cnt, total # 예약어 nonlocal -> 주석 해제 후 실행
        cnt += 1
        total += v
        print('def2 >>> {} / {}'.format(total, cnt))
        return total / cnt
    return averager

avg_closure2 = closure_avg2()

print('EX6-5 -', avg_closure2(15))
print('EX6-5 -', avg_closure2(35))
print('EX6-5 -', avg_closure2(45))


# 데코레아터 실습
# 1. 중복 제거, 코드 간결
# 2. 클로저 보다 문법 간결
# 3. 조합해서 사용 용이

# 단점
# 1. 디버깅 어려움
# 2. 에러의 모호함

import time

def perf_clock(func):
    # 스냅샷 영역
    def perf_clocked(*args):
        # 시작 시간
        st = time.perf_counter()
        result = func(*args)
        # 종료 시간
        et = time.perf_counter() - st
        # 함수명
        name = func.__name__
        # 매개변수
        arg_str = ','.join(repr(arg) for arg in args)
        # 출력
        print('Result : [%0.5fs] %s(%s) -> %r' %(et, name, arg_str, result))
        return result
    return perf_clocked

@perf_clock
def time_func(seconds):
    time.sleep(seconds)

@perf_clock
def sum_func(*numbers):
    return sum(numbers)

@perf_clock
def fact_func(n):
    return 1 if n < 2 else n * fact_func(n-1)


# 데코레이터 미사용
non_deco1 = perf_clock(time_func)
non_deco2 = perf_clock(sum_func)
non_deco3 = perf_clock(fact_func)

print('EX7-1', non_deco1, non_deco1.__code__.co_freevars) # <function perf_clock.<locals>.perf_clocked at 0x7ff0772e3040> ('func',)
print('EX7-2', non_deco1, non_deco2.__code__.co_freevars) # ('func',) 로 튜플에 들어가 있음
print('EX7-3', non_deco1, non_deco3.__code__.co_freevars)



print('*' *40, 'Called Non Deco -> time_func')
print('EX7-4')
non_deco1(2)

print('*' *40, 'Called Non Deco -> sum_func')
print('EX7-5')
non_deco2(100)
non_deco2(100, 200, 300, 500)

print('*' *40, 'Called Non Deco -> fact_func')
print('EX7-6')
non_deco2(10)
non_deco2(100, 200, 300, 500)

print()
print()

# 데코레이터 사용

print('*' *40, 'Called Deco -> time_func') 
print('EX7-7')
time_func(2)

print('*' *40, 'Called Deco -> sum_func')
print('EX7-8')
sum_func(10,20,30,40,50)

print('*' *40, 'Called Deco -> fact_func')
print('EX7-9')
fact_func(100)