# Chapter02-2.py
# 파이썬 심화
# Special Method(Magic Method)
# 참조 1: https://docs.python.org/3/reference/datamodel.html
# 참조 2: https://www.tutorialsteacher.com/python/magic-methods-in-python

# 매직메소드 실습 = 스페셜메소드 : __ 2개로 시작하는 메소드
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Fuction), 클래스(Class)

# 매직메소드 기초 설명

# 기본형

print(int)

# 모든 속성 및 메소드 출력
print(dir(int))

print()
print()

n = 100

# 사용
print('EX1-1 -', n + 200)
print('EX1-1 -', n.__add__(200))
print('EX1-3 -', n.__doc__) # doc type
print('EX1-4 -', n.__bool__(), bool(n)) # 0 -> True, 0이외의 모든 값 -> False
print('EX1-5 -', n * 100, n.__mul__(100))

print()
print()

# 클래스 예제 1
class Student:
    def __init__(self, name, height):
        self._name = name
        self._height = height

    def __str__(self):
        return 'Student Class Info : {}, {}'.format(self._name, self._height)

    def __ge__(self, x): # x: 비교할 대상
        print('Called >> __ge__ Method.')
        if self._height >= x._height:
            return True
        else:
            return False

    def __le__(self, x): # self <- s1, x <- s2
        print('Called >> __le__ Method.')
        if self._height <= x._height:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__Method.')
        return abs(self._height - x._height)

# 인스턴스 생성
s1 = Student('James', 181)
s2 = Student('Mie', 165)

#print(s1 + s2) # Error
print(s1._height > s2._height)


# 매직메소드 출력
print('EX2-1 -', s1 >= s2) 
# 출력 : Called >> __ge__ Method. EX2-1 - True
print('EX2-2 -', s1 <= s2)
# 출력 : Called >> __le__ Method. EX2-2 - False

print('EX2-3 -', s1 - s2)
print('EX2-4 -', s2 - s1)

print('EX2-5 -', s1)
print('EX2-6 -', s2)


print()
print()


# 클래스 예제2

# 벡터(Vector) # Numpy

class Vector(object):
    def __init__(self, *args):
        '''Create a vector, example : v = Vector(1,2)'''
        if len(args) == 0: # 값이 하나도 안 들어왔을 때 -> (0, 0) 생성
            self._x, self._y = 0, 0
        else:
            self._x, self._y = args
        
    def __repr__(self): # __str__ 대신 __repr__ 가능
        '''Returns the vector information'''
        return 'Vector(%r, %r)' % (self._x, self._y)

    # 더하기
    def __add__(self, other):
        '''Returns the vector addition of self and other'''
        return Vector(self._x + other._x, self._y + other._y)

    # 곱하기
    def __mul__(self, y):
        return Vector(self._x * y, self._y * y)

    def __bool__(self):
        return bool(max(self._x, self._y))


# Vector 인스턴스 생성
v1 = Vector(3, 5)
v2 = Vector(15, 20)
v3 = Vector()

# 매직메소드 출력
print('EX3-1 -', Vector.__init__.__doc__)
print('EX3-2 -', Vector.__repr__.__doc__)
print('EX3-3 -', Vector.__add__.__doc__)
print('EX3-4 -', v1, v2, v3)

print('EX3-5 -', v1 + v2)
print('EX3-6 -', v1 * 4)

print('EX3-7 -', v2 * 10)

print('EX3-8 -', bool(v1), bool(v2))
print('EX3-9 -', bool(v3))

print()
print()

