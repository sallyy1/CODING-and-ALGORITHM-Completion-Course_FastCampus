# Chapter05-2
# 파이썬 심화
# 파이썬 클래스 특별 메소드 심화 활용 및 상속
# Class Abstruct

# class 선언
class VectorP(object):
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    def __iter__(self):
        return (i for i in (self.__x, self.__y)) # Generator (데이터가 많을 땐 Generator 사용하는 것이 좋음)

    @property # Getter 매소드
    def x(self):
        print('Called Property X')
        return self.__x

    @x.setter # Setter 매소드
    def x(self, v): # v : 내가 변경할 값
        print('Called Property X Setter')
        sef.__x = float(v)


    @property # Getter 매소드
    def y(self):
        print('Called Property Y')
        return self.__y

    @y.setter # Setter 매소드
    def y(self, v): # v : 내가 변경할 값
        if v < 30:
            raise ValueError('30 Below is not possible')
        print('Called Property Y Setter')
        self.__y = float(v)



# 객체 선언
v = VectorP(20, 40)

#print('EX1-1 -', v.__x, v.__y) # 언더바 2개는 파이썬에서 가려져 있음 (직접 접근 불가능)
# AttributeError: 'VectorP' object has no attribute '__x'
#print('EX1-1 -', v._x, v._y) # 언더바 1개하면 -> 값 볼 수 있음

# Getter, Setter : 값 가져올 때(Read), 할당할 때(Write) 사용

#v.y = 20 # 은닉화 유지하면서 값 변경 시도 가능
print('EX1-2 -', dir(v), v.__dict__)
# ['_VectorP__x', '_VectorP__y', '__class__', '__delattr__', '__dict__', '__dir__', 
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__',
#  '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', 'x', 'y'] {'_VectorP__x': 20.0, '_VectorP__y': 40.0}
print('EX1-3 -', v.x, v.y)

# Iter 확인
for val in v:
    print('EX1-2 -', val)


# __slot__
# 파이썬 인터프리터에게 통보
# 해당 클래스가 가지는 속성을 제한
# __dict__ 속성 최적화 -> 다수 객체 생성 시 -> 메모리 사용 공간 대폭 감소
# 해당 클래스에 만들어진 인스턴스 속성 관리에 딕셔너리 대신 Set 형태를 사용

class TestA(object):
    __slots__ = ('a',)

class TestB(object):
    pass

use_slot = TestA()

print(dir(use_slot))


no_slot = TestB()

print('EX2-1 -', use_slot)
#print('EX2-2 -', use_slot.__dict__) # AttributeError: 'TestA' object has no attribute '__dict__'

print('EX2-3 -', no_slot) # <__main__.TestA object at 0x7f8ae6a581f0>
print('EX2-4 -', no_slot.__dict__) # <__main__.TestB object at 0x7f8ae6a4fa30>

# 메모리 사용량 비교
import timeit

# 측정을 위한 함수 선언
def repeat_outer(obj):
    def repeat_inner(): # 클로저
        obj.a = 'TEST'
        del obj.a
    return repeat_inner

#print(min(timeit.repeat(repeat_outer(use_slot), number = 500000)))
#print(min(timeit.repeat(repeat_outer(no_slot), number = 500000)))

print()
print()


# 객체 슬라이싱
class Objects:
    def __init__(self):
        self._numbers = [n for n in range(1, 10000, 3)]
        
    def __len__(self): # 매직메소드 오버라이딩
        return len(self._numbers)

    def __getitem__(self, idx):
        return self._numbers[idx]

s = Objects()

print('EX3-1 -', s.__dict__)
print('EX3-2 -', len(s))
print('EX3-3 -', len(s._numbers)) # len 메소드 안 만들었다면, len(s._numbers) 출력해야 함
print('EX3-4 -', s[-1]) # 메소드 -> 바로 슬라이싱 가능
print('EX3-5 -', s[::10]) # 처음~끝 까지, 10개씩 점프하면서

print()
print()


# 파이썬 추상클래스
# 참고: https://docs.python.org/3/library/collections.abc.html

# 자체적으로 객체 생성 불가
# 상속을 통해서 자식 클래스에서 인스턴스를 생성해야 함
# 개발과 관련된 공통된 내용(필드, 메소드) 추출 및 통합해서 공통된 내용으로 작성하게 하는 것

# 폰 -> 걸다, 끊다, 배터리 충전 : 폰을 상속받은 갤럭시s9, v30 인스턴스들은 자기만의 독특한 메소드를 가지면서 & 부모가 내려준 반드시 오버라이딩해야하는 메소드 구현해야 함.


# 1) Sequence 상속 받지 않았지만, 자동으로 기능 __iter__, __contain__, __len__ 등 (Sequence형에 필요한)기능 작동
# 객체 전체를 자동으로 조사 -> 시퀀스 프로토콜

class IterTestA():
    def __getitem__(self, idx): # 매직 메소드
        return range(1, 50, 2)[idx] # range(1, 50, 2)

i1 = IterTestA()

print('EX4-1 -', i1[4]) # 1, 3, 5, 7, 9, ...
print('EX4-2 -', i1[4:10])
print('EX4-3 -', 3 in i1[1:10]) # 구현하지 않은 __contain__ 기능도 알아서 작동하고 있음.
print('EX4-4 -', [i for i in i1]) # __iter__ 메소드, next 메소드 알아서 구현

print()
print()

# 2) Sequence 상속
# 요구사항인 추상메소드를 모두 구현해야 동작

from collections.abc import Sequence

class IterTestB(Sequence):
    def __getitem__(self, idx):
        return range(1, 50, 2)[idx]

    def __len__(self, idx):
        return len(range(1, 50, 2)[idx])

i2 = IterTestB() # __len__ 메소드 FM으로 안 만들어주면 -=> TypeError: Can't instantiate abstract class IterTestB with abstract methods __len__

print('EX4-5 -', i2[4]) # 1, 3, 5, 7, 9, ...
print('EX4-6 -', i2[4:10])
print('EX4-7 -', 3 in i2[4:10])

print()
print()

# abc 활용 예제
import abc

class RandomMachine(abc.ABC): #metaclass = abc.ABCMeta(3.4 이하 구버전)
    # __metaclass__ = abc.ABCMeta
    
    # 추상 메소드
    @abc.abstractmethod
    def load(self, iterobj):
        '''Iterable 항목 추가'''

    # 추상 메소드
    @abc.abstractmethod
    def pick(self, iterobj):
        '''무작위 항목 뽑기'''

    def inspect(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
            return tuple(sorted(items))


import random

class CraneMachine(RandomMachine): # 부모로 RandomMachine 상속받음
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()

        except IndexError:
            raise LookupError('Empty Crane Box')

    def __call__(self): # callable 함수
        return self.pick()

# 서브 클래스 확인
print('EX5-1 -', issubclass(RandomMachine, CraneMachine)) # (서브, 부모) # False
print('EX5-2 -', issubclass(CraneMachine, RandomMachine)) # True

# 상속 구조 확인
print('EX5-3 -', CraneMachine.__mro__) # 순서 가계도 보여줌 # (<class '__main__.CraneMachine'>, <class '__main__.RandomMachine'>, <class 'abc.ABC'>, <class 'object'>)

cm = CraneMachine(range(1, 100)) # 추상 메소드 구현(오버라이딩) 안하면 에러 <- @데코레이터 한 load & pick 서브 클래스에서 구현해줘야 함

print('EX5-4 -', cm._items) # [31, 58, 22, 11, 79, 7, 62, 95, 46, 59, 88, 68, 73, 65, 80, 86, 8, 84, 15, 30, 3, 14, 71, 51, 13, 4, 38, 72, 41, 42, 48, 27, 20, 74, 61, 94, 10, 19, 75, 57, 66, 37, 83, 54, 76, 16, 63, 99, 47, 18, 43, 29, 2, 28, 97, 44, 87, 81, 89, 12, 35, 50, 40, 92, 78, 55, 90, 24, 26, 5, 96, 93, 1, 98, 34, 9, 85, 52, 82, 17, 70, 67, 33, 64, 32, 77, 39, 6, 45, 60, 69, 49, 23, 25, 36, 91, 53, 56, 21]
print('EX5-5 -', cm.pick()) # 21
print('EX5-6 -', cm()) # 56
print('EX5-7 -', cm.inspect()) # (11, )

