# Chapter05-1
# 파이썬 심화
# 객체 참조 중요한 특징들
# Python Object Referrence


print('EX1-1 -1')
print(dir()) # '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
print(__name__) # __main__

# id vs __eq__(==) 증명
x = {'name': 'kim', 'age': 33, 'city': 'Seoul'}
y= x # 얕은 복사

print('EX2-1 -', id(x), id(y)) # 얕은 복사 (주소값 같음)
print('EX2-2 -', x == y) # True
print('EX2-3 -', x, y)

x['class'] = 10
print('EX2-5 -', x, y)


print()
print()

z = {'name': 'kim', 'age': 33, 'city': 'Seoul', 'class': 10}

print('EX2-6 -', x, z) # 값은 똑같이 나오나
print('EX2-7 -', x is z) # False (id값은 다름) <같은 객체 판별>
print('EX2-8 -', x is not z) # True
print('EX2-9 -', x == z) # True <값이 같은지 판별>

# 객체 생성 후 완전 불변 -> 즉, id는 객체 주소(정체성) 비교, ==(__eq__) 는 값 비교

print()
print()

# 튜플 불변형의 비교
tuple1 = (10, 15, [100, 1000])
tuple2 = (10, 15, [100, 1000])

print('EX3-1 -', id(tuple1), id(tuple2)) # 튜플은 한 번 선언하면 불변형 -> 값은 같아도 Id값은 다름
print('EX3-2 -', tuple1 is tuple2) # False
print('EX3-3 -', tuple1 == tuple2) # True
print('EX3-4 -', tuple1.__eq__(tuple2)) # True

print()
print()


# Copy, Deepcopy (얕은 복사, 깊은 복사)

# Copy
tl1 = [10, [100, 105], (5, 10, 15)]
tl2 = tl1
tl3 = list(tl1) # 값 같음 => 여기서 list()가 얕은 복사 (??)

print('EX4-1 -', tl1 == tl2) # True
print('EX4-2 -', tl1 is tl2) # True

print('EX4-3 -', tl1 == tl3) # True
print('EX4-4 -', tl1 is tl3) # False

# 증명
tl1.append(1000)
tl1[1].remove(105)

print('EX4-5 -', tl1) # (그대로) [10, [100], (5, 10, 15), 1000]
print('EX4-6 -', tl2) # (그대로) [10, [100], (5, 10, 15), 1000]
print('EX4-7 -', tl3) # (바뀜) [10, [100], (5, 10, 15)]

print()

print(id(tl1[2]))
tl1[1] += [110, 120]
tl1[2] += (110, 120) # 튜플은 수정이 불가

print('EX4-8 -', tl1)
print('EX4-9 -', tl2) # 튜플이 재할당됨 (객체가 새로 생성됨)
print('EX4-10 -', tl3) 
print(id(tl1[2])) # id 값 바뀜


print()
print()

# Deep Copy

# 장바구니
class Basket:
    def __init__(self, products=None):
        if products is None:
            self._products = [] # 값이 없을 경우 -> 빈 리스트 생성
        else:
            self._products = list(products) # 값이 있을 경우 -> products를 리스트화
    
    def put_prod(self, prod_name):
        self._products.append(prod_name)

    def del_prod(self, prod_name):
        self._products.remove(prod_name)


import copy

basket1 = Basket(['Apple', 'Bag', 'TV', 'Snack', 'Water'])
basket2 = copy.copy(basket1) # copy.copy => 얕은 복사 (?)
basket3 = copy.deepcopy(basket1) # copy.deepcopy => 깊은 복사 (?)

print('EX5-1 -', id(basket1), id(basket2), id(basket3))
# 140518967608368 140518967572032 140518967918544
print('EX5-2 -', id(basket1._products), id(basket2._products), id(basket3._products))
# 140518968072000 140518968072000(얕은 복사) 140518967940160(깊은 복사)

print()

basket1.put_prod('Orange')
basket2.del_prod('Snack')

print('EX5-3 -', basket1._products)
print('EX5-4 -', basket2._products) # 얕은 복사 -> 문제 생김
print('EX5-5 -', basket3._products) # 깊은 복사 -> 안전
'''
EX5-3 - ['Apple', 'Bag', 'TV', 'Water', 'Orange']
EX5-4 - ['Apple', 'Bag', 'TV', 'Water', 'Orange']
EX5-5 - ['Apple', 'Bag', 'TV', 'Snack', 'Water']
'''

print()
print()

# 함수 매개변수 전달 사용법

def mul(x, y):
    x += y
    return x

x = 10
y = 5

print('EX6-1 -', mul(x, y), x, y) # 15 10 5
print() # 정수형일 땐 문제 없음

# 가변형 & 불변형 일 때 주의
# 리스트 (<- 가변형)
a = [10, 100]
b = [5, 10]

print('EX6-2 -', mul(a, b), a, b) # [10, 100, 5, 10] [10, 100, 5, 10] [5, 10]
# 문제 발생 : a 변경됨
# 가변형 일 땐 (a) => 원본 데이터가 변경됨 !

# 튜플 (<- 불변형)
c = (10, 100)
d = (5, 10)

print('EX6-3 -', mul(c, d), c, d) # (10, 100, 5, 10) (10, 100) (5, 10)
# 튜플은 immutable이라 c 변경 안 돼서 문제 안 생김
# 불변형 c -> 원본 데이터 변경 안 됨 !


# 파이썬 불변형 예외 (<- 성능 및 효율성을 위해)
# str, bytes, frozenset, tuple : 사본 생성 x -> 참조 반환

tt1 = (1, 2, 3, 4, 5)
tt2 = tuple(tt1) # id 값 안 바뀜 (=참조값 가져와서 반환)
tt3 = tt1[:]


print('EX7-1 - ', tt1 is tt2, id(tt1), id(tt2)) # True 140264527950128 140264527950128
print('EX7-2 - ', tt1 is tt3, id(tt1), id(tt3)) # True 140336326046000 140336326046000

tt4 = (10, 20, 30, 40, 50)
tt5 = (10, 20, 30, 40, 50)
ss1 = 'Apple'
ss2 = 'Apple'

print('EX7-3 - ', tt4 is tt5, tt4 == tt5, id(tt4), id(tt5)) # True True 140563829815712 140563829815712
print('EX7-4 - ', ss1 is ss2, ss1 == ss2, id(ss1), id(ss2)) # True True 140366505503216 140366505503216
