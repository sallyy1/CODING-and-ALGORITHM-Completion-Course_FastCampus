# Chapter03-1
# 파이썬 심화
# 시퀀스 형
# 컨테이너(Container) : 서로 다른 자료형을 저장할 수 있는 것 [list, tuple, collections.deque]
# Flat : 한 개의 자료형만 저장할 수 있음[str, bytes, bytearray, array.array, memoryview] -> 이게 컨테이너보다 속도, 퍼포먼스가 좋음

# 가변 : list, bytearray, array.array, memoryview, deque
# 불변 : tuple, str, bytes

# 지능형 리스트(Comprehending Lists)

# Non Comprehending List
chars = '!@#$%^&*()_+'
codes1 = []

for s in chars:
    codes1.append(ord(s))

print('EX1-1 -', codes1)


# Comprehending List
codes2 = [ord(s) for s in chars]

print('EX1-2 -', codes2)


# Comprehending List + Map, Filter 함수
# 속도 약간 우세
codes3 = [ord(s) for s in chars if ord(s) > 40] # if 조건
# 출력 : [64, 94, 42, 41, 95, 43]
codes4_1 = list(map(ord, chars))
# 출력 : [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43]
codes4 = list(filter(lambda x : x > 40, map(ord, chars)))
# 출력 : [64, 94, 42, 41, 95, 43]

print('EX1-3 -', codes3)
print('EX1-4 -', codes4_1)
print('EX1-4 -', codes4)

print('EX1-5 -', [chr(s) for s in codes1])
print('EX1-6 -', [chr(s) for s in codes2])
print('EX1-7 -', [chr(s) for s in codes3])
print('EX1-8 -', [chr(s) for s in codes4])


print()
print()


# Generator
import array

# Generator : 한 번에 한 개의 항목을 생성(메모리 유지x -> 성능 좋음)
tuple_g = (ord(s) for s in chars)

print('EX2-1 -', tuple_g) # 출력 : <generator object <genexpr> at 0x7fd2c62a3f90>
                            # 값이 나오지 않고 대기상태
print('EX2-2 -', next(tuple_g))
print('EX2-3 -', next(tuple_g))


# Array
array_g = array.array('I', (ord(s) for s in chars))
print('EX2-4 -', array_g) # 출력 : array('I', [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43])
print('EX2-5 -', array_g.tolist()) # 출력 : [33, 64, 35, 36, 37, 94, 38, 42, 40, 41, 95, 43]


print()
print()


# 제네레이터 예제 : 값을 발생하는 구조만 정의하는 개념
print('EX3-1', ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)))

for s in ('%s' % c + str(n) for c in ['A', 'B', 'C', 'D'] for n in range(1,11)):
    print('EX3-2 -', s)

print()
print()


# 리스트 주의 할 점
marks1 = [['~'] * 3 for n in range(3)]
marks2 = [['~']* 3] * 3

print('EX4-1 -', marks1)
print('EX4-2 -', marks2)

print()

marks1[0][1] = 'X'
marks2[0][1] = 'X'

print('EX4-3 -', marks1) # [['~', 'X', '~'], ['~', '~', '~'], ['~', '~', '~']]
print('EX4-4 -', marks2) # [['~', 'X', '~'], ['~', 'X', '~'], ['~', 'X', '~']]


# 증명
print('EX4-5 -', [id(i) for i in marks1]) # 서로 다른 주소
print('EX4-5 -', [id(i) for i in marks2]) # 서로 같은 주소



# Tuple Advanced

# Packing & Unpacking

print('EX5-1 -', divmod(100, 9))
print('EX5-2 -', divmod(*(100, 9))) # Packing
                                    # 출력은 (11, 1) 로 같음

print('EX5-3 -', *(divmod(100, 9))) # 출력: 11, 1 로 풀려서 결괏값 나몽

print()

x, y, *rest = range(10)
print('EX5-4 -', x, y, rest) # 0 1 [2, 3, 4, 5, 6, 7, 8, 9]

x, y, *rest = range(2)
print('EX5-5 -', x, y, rest) # 0 1 []

x, y, *rest = 1,2,3,4,5
print('EX5-6 -', x, y, rest) # 1 2 [3, 4, 5]

def test(*args, **args2): # * -> Packing 되어서 넘어온 것을 Unpack 해서 함수내에서 사용하겠다
    pass                 # ** -> Dictionary 형태로 받겠다

print()
print()



# Mutable(가변) vs Immutable(불변)

l = (10, 15, 20)
m = [10, 15, 20]


print('EX6-1 -', l, m, id(l), id(m)) # (10, 15, 20) [10, 15, 20] 140669181397568 140669181878720

l = l * 2
m = m * 2

print('EX6-2 -', l, m, id(l), id(m)) # (10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20] 140669181176320 140669181878528


l *= 2
m *= 2

print('EX6-3 -', l, m, id(l), id(m)) # (10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20) [10, 15, 20, 10, 15, 20, 10, 15, 20, 10, 15, 20] 140198220733456 140198221263360
                                    # 튜플는 새로운 객체 생성 (주소 바뀜)
                                    # 리스트는 주소 바뀌지 않고, 자기 자체에서 재할당 됨

print()
print()


# sort vs sorted
# reverse, key=len, key=str.lower, key=func

f_list = ['orange', 'apple', 'mango', 'papaya', 'strawberry', 'coconut']

# 1) sorted : 정렬 후 '새로운' 객체 반환 ! (원본은 그대로 있음)

print('EX7-1 -', sorted(f_list))
print('EX7-2 -', sorted(f_list, reverse=True)) # 역순으로 정렬
print('EX7-3 -', sorted(f_list, key=len)) # 글자의 길이 순서대로 정렬
print('EX7-4 -', sorted(f_list, key=lambda x: x[-1])) # 단어의 끝 글자를 기준으로 정렬
print('EX7-5 -', sorted(f_list, key=lambda x: x[-1], reverse=True))

print('EX7-6 -', f_list) # 원본은 변경되지 않았음


# 2) sort : 정렬 후 객체 직접 변경
# 반환 값 확인 -> None 값을 반환하는 함수 = 객체를 직접 변경하는 함수라고 해석하면 됨
a = f_list.sort()

print(a, f_list)

print('EX7-7 -', f_list.sort(), f_list)
print('EX7-8 -', f_list.sort(reverse=True), f_list)
print('EX7-9 -', f_list.sort(key=len), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1]), f_list)
print('EX7-10 -', f_list.sort(key=lambda x: x[-1], reverse=True), f_list)



