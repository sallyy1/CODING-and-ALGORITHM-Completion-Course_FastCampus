# Chapter06-2
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# yield
# 코루틴(Coroutine)

# yield : 메인 루틴 <-> 서브 루틴
# 코루틴 제어, 코루틴 상태, 양방향 값 전송
# yield from

# 서브 루틴 : 메인 루틴에서 -> 리턴에 의해 호출 부분으로 돌아와 다시 프로세스 실행
# 코루틴 : 루틴 실행 중 멈춤 가능 -> 특정 위치로 돌아갔다가 -> 다시 원래 위치로 돌아와 수행을 가능하게 함. -> 동시성 프로그래밍 가능하게 함
# 코루틴 : 코루틴 스케쥴링 오버헤드가 매우 적다. (하나의 쓰레드에서 실행하기 때문에)
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 샅애 발생 가능성이 있음 (주의깊게 사용해야 함) => 컨텍스트 스위치 비용 발생, 자원 소비 가능성 증가



# 코루틴 예제 1

def coroutine1():
    print('>>> coroutine started.')
    i = yield # 메인 루틴한테 값을 받을 수 있음(=양방향 소통) -> yield : Generator
    print('>>> coroutine received : {}'.format(i))

# 제네레이터 선언

c1 = coroutine1()

print('EX1-1 -', c1, type(c1)) # <generator object coroutine1 at 0x7ff72c2a3c80> <class 'generator'>

# yield 실행 전까지 실행
#next(c1)
#next(c1) # 오류
'''
>>> coroutine received : None
Traceback (most recent call last):
  File "/Users/hyun/Desktop/FastCampus/python_test/chapter06-02.py", line 32, in <module>
    next(c1)
StopIteration
'''

# 기본으로 None 전달 가능
# next(c1)

# 값 전송
#c1.send(100)
'''
>>> coroutine started.
>>> coroutine received : 100
Traceback (most recent call last):
  File "/Users/hyun/Desktop/FastCampus/python_test/chapter06-02.py", line 45, in <module>
    c1.send(100)
StopIteration
'''


# 잘못된 사용

c2 = coroutine1()

#next(c2) # next로 c2를 호출해 -> i = yield에 두어야 -> 호출 가능
#c2.send(100) # 예외 발생 -> TypeError: can't send non-None value to a just-started generator


# 코루틴 예제 2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    y = yield x # y : 메인루틴 -> 코루틴 send할 값 / x : 메인루틴에 전달할 값
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


c3 = coroutine2(10)

from inspect import getgeneratorstate

print('EX1-2 -', getgeneratorstate(c3)) # TypeError: can't send non-None value to a just-started generator

print(next(c3))

print('EX1-3 -', getgeneratorstate(c3))

print(c3.send(15))

#print(c3.send(20)) # 예외 발생

'''
EX1-2 - GEN_CREATED
>>> coroutine started : 10
10
EX1-3 - GEN_SUSPENDED
>>> coroutine received : 15
25
'''
print()
print()


# 데코레이터 패턴

from functools import wraps

def coroutine(func):
    '''Decorator run until yield'''
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer # 클로저

@coroutine    
def sumer():
    total = 0
    term = 0
    while True:
        term = yield total # next(gen) 이 호출되면 어기서 멈춰있음
        total += term


su = sumer()

print('EX2-1 -', su.send(100)) # 100
print('EX2-2 -', su.send(40)) # 140
print('EX2-3 -', su.send(60)) # 200


# 코루틴 예제3 (예외처리)

class SampleException(Exception):
    '''설명에 사용할 예외 유형'''

def coroutine_except():
    print('>> coroutine started.')
    try:
        while True: # 무한반복
            try:
                x = yield
            except SampleException:
                print('-> SampleException handled. Continuing..')
            else:
                print('-> coroutine received : {}'.format(x))
    
    finally:
        print('-> coroutine ending')


exe_co = coroutine_except()

print('EX3-1 -', next(exe_co))
print('EX3-2 -', exe_co.send(10))
print('EX3-3 -', exe_co.send(100))
'''
EX3-1 - None
-> coroutine received : 10
EX3-2 - None
-> coroutine received : 100
EX3-3 - None
-> coroutine ending
'''
print('EX3-4 -', exe_co.throw(SampleException)) # -> SampleException handled. Continuing..
print('EX3-5 -', exe_co.send(1000))       

print('EX3-6 -', exe_co.close()) # GEN_CLOSED    
#print('EX3-7 -', exe_co.send(10)) # StopIteration

print()
print()

# 코루틴 예제4(return)

def averager_re():
    total = 0.0
    cnt = 0
    avg = None
    while True:
        term = yield
        if term is None: # 종료
            break
        total += term
        cnt += 1
        avg = total / cnt
    return 'Average : {}'.format(avg)


avger2 = averager_re()

next(avger2)

avger2.send(10)
avger2.send(30)
avger2.send(50)

try:
    avger2.send(None)
except StopIteration as e:
    print('EX4-1 -', e.value) # EX4-1 - Average : 30.0


# 코루틴 예제5 (yield from)
# StopIteration 자동 처리 (3.7 -> await)
# 중첩 코루틴 처리

def gen1():
    for x in 'AB': # 중첩 문
        yield x
    for y in range(1,4):
        yield y

t1 = gen1()

print('EX5-1 -', next(t1)) # A
print('EX5-2 -', next(t1)) # B
print('EX5-3 -', next(t1)) # 1
print('EX5-4 -', next(t1)) # 2
print('EX5-5 -', next(t1)) # 3

#print('EX5-6 -', next(t1)) # StopIteration

t2 = gen1()

print('EX5-7 -', list(t2)) # ['A', 'B', 1, 2, 3]

print()
print()

def gen2():
    yield from 'AB' # yield from 문
    yield from range(1,4)

t3 = gen2()

print('EX6-1 -', next(t3)) # A
print('EX6-2 -', next(t3)) # B
print('EX6-3 -', next(t3)) # 1
print('EX6-4 -', next(t3)) # 2
print('EX6-5 -', next(t3)) # 3

#print('EX6-6 -', next(t3)) # StopIteration


t4 = gen2()

print('EX6-7', list(t4)) # ['A', 'B', 1, 2, 3]


print()
print()


def gen3_sub():
    print('Sub coroutine.')
    x = yield 10
    print('Recv : ', str(x))
    x = yield 100
    print('Recv : ', str(x))

def gen4_main():
    yield from gen3_sub() # 알아서 위임 -> <yield from + 코루틴(=서브루틴)> 통해 흐름 제어 가능 (메인 & 서브 루틴 간 양방향 소통 가능)
    # (추가 가능) 예외처리

    
t5 = gen4_main()

print('EX7-1', next(t5)) # Sub coroutine.   # EX7-1 10
print('EX7-2', t5.send(7)) # Recv :  7  # EX7-2 100
print('EX7-2', t5.send(77)) # Recv :  77    # StopIteration
    



