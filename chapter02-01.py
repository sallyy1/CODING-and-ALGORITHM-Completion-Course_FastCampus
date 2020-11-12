# Chapter02-1
# 파이썬 심화
# 데이터 모델(Data Model)
# 참조 : https://docs.python.org/3/reference/datamodel.html
# Namedtuple 실습
# 파이썬의 중요한 핵심 프레임워크 -> 시퀀스(Sequence), 반복(Iterator), 함수(Fuction), 클래스(Class)

# 객케 -> 파이썬의 데이터를 추상화
# 모든 객체 -> id, type -> value 가 있음 !

a = 7
print(id(a), type(a), dir(a))

# 출력 : 4317993504 <class 'int'> ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', 
# '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', 
# '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', 
# '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', 
# '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', 
# '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', 
# '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', 
# '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', 
# '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 
# 'imag', 'numerator', 'real', 'to_bytes']

# 그리고 dir() 는 리스트이기 때문에 iterator 를 사용할 수 있음
for a in dir(a):
    print(a)


# 파이썬 -> 일관성이 있음

# 일반적인 튜플 사용
# 0 : x, 1 : y
pt1 = (1.0, 5.0) # 튜플 : 불변형, 데이터 추가는 가능하나, 한번 선언한 값은 수정이 불가능 !
pt2 = (2.5, 1.5)

from math import sqrt
line_leng1 = sqrt((pt2[0] - pt1[0]) ** 2 + (pt2[1] - pt1[1]) ** 2) 

print('EX1-1 -', line_leng1)


# '네임드 튜플' 사용
from collections import namedtuple

# '네임드 튜플' 선언
Point = namedtuple('Point', 'x y') # 튜플 -> 클래스 같음
                                    # 띄어쓰기로

# 두 점 선언
pt1 = Point(1.0, 5.0) 
pt2 = Point(2.5, 1.5)

# 계산
line_leng2 = sqrt((pt2.x - pt1.x) ** 2 + (pt2.y - pt1.y) ** 2) # 클래스.함수 형식

print('EX1-2 -', line_leng2)


# 출력
print('EX1-2 -', line_leng2)
print('EX1-3 -', line_leng1 == line_leng2) # True


# 네임드 튜플 선언 방법
Point1 = namedtuple('Point', ['x', 'y']) # list 로
Point2 = namedtuple('Point', 'x, y') # , 로
Point3 = namedtuple('Point', 'x y') # 띄어쓰기로
Point4 = namedtuple('Point', 'x y x class', rename = True) # Default = False
# rename -> x 가 중복되기 때문에, 자기가 알아서 새로운 이름으로 랜덤 배정해줌 (두 번째 x => _2)
# rename -> class는 파이썬 예약어이기 때문에,  자기가 알아서 새로운 이름으로 랜덤 배정해줌 (class => _3)

# 출력
print('EX2-1 -', Point1, Point2, Point3, Point4)


# Dict to Unpacking
temp_dict = {'x' : 75, 'y' : 55}


# 객체 생성
p1 = Point1(x=10, y=35)
p2 = Point2(20, 40)
p3 = Point3(45, y=35)
p4 = Point4(10, 20, 30, 40)

p5 = Point3(**temp_dict) # ** -> 딕셔너링 언패킹 시


print('EX2-2 -', p1, p2, p3, p4, p5)
# 출력 : EX2-2 - Point(x=10, y=35) Point(x=20, y=40) Point(x=45, y=35) Point(x=10, y=20, _2=30, _3=40)

print()
print()


# 사용
print('EX3-1 -', p1[0] + p2[1]) # Index Error 주의
print('EX3-2 -', p1.x + p2.y) # 클래스 변수 접근 방식 (추천)

# Unpacking
x, y = p3 # 1개로 묶여져 있는 것을 x, y로 짐을 풀어 2개의 변수에 연결해줌
print('EX3-3 -', x + y)


# Rename 테스트
print('EX3-4 -', p4)

print()
print()


# 네임드 튜플 메소드
temp = [52, 38]

# _make() : 새로운 객체 생성
p4 = Point1._make(temp)

print('EX4-1 -', p4)

# _fields() : 필드 네임 확인
print('EX4-2 -', p4._fields, p2._fields, p3._fields)

# _asdict() : OrderedDict 반환 -> 정렬된 dictionary로 반환
print('EX4-3 -', p1._asdict(), p4._asdict())


# _replace() : 수정된 "새로운" 객체 반환 ! (튜플은 불변형이기에 -> id 값이 달라짐)
print('EX4-4 -', p2._replace(y=100))

print(
print()

# 실 사용 실습
# 학생 전체 그룹 생성
# 반20명, 4개의 반 -> (A,B,C,D) 번호

# 네임드 튜플 선언
Classes = namedtuple('Classes', ['rank', 'number'])

# 그룹 리스트 선언
numbers = [str(n) for n in range(1, 21)]
ranks = 'A B C D'.split()
print(rank, numbers)


# 지능형 리스트 (List Comprehension)
# (참고) 원래는
numbers2 = []

for n in range(1, 21):
    numbers2.append(str(n))

print(numbers2)


# List Comprehension
students = [Classes(rank, number) for rank in ranks for number in numbers] # 4개 < 20개
print(students)
print('EX5-1 -', len(students))
print('EX5-2 -', students) # Classes(rank='A', numbers='5)
print('EX5-3 -', students[4].rank) # Classes(rank='A', numbers='5) ->의 rank -> A 출력


print()
print()

# 가독성 x (추천 NO)
students2 = [Classes(rank, number) 
                    for rank in 'A B C D'.split() 
                        for number in str(n) 
                            for n in range(1, 21)]
print(students2)
print('EX6-1 -', len(students2))
print('EX6-2 -', students2) # Classes(rank='A', numbers='5)
print('EX6-3 -', students2[4].rank) # Classes(rank='A', numbers='5) ->의 rank -> A 출력

print()
print()

# 출력
for s in students:
    print('EX7-1', s)