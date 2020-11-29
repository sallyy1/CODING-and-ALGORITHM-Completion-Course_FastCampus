# Chapter06-1
# 파이썬 심화
# 흐름제어, 병행처리(Concurrency)
# 제네레이터, 반복형
# Generator

# 파이썬 반복형 종류
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args
# 공부할 것 : 반복형 객체 내부적으로 iter 함수 내용, 제네레이터 동작 원리, yield from

# 반복 가능한 이유? -> iter(x) 함수 호출

t = 'ABCDEF'

# for 사용
for c in t:
    print('EX1-1 -', c)

print()

# while 사용
w = iter(t)

while True:
    try:
        print('EX1-2 -', next(w))
    except StopIteration: # 마지막 인자 -> 없으면 next에서 에러 뜨므로
        break

print()



from collections import abc

# 반복형 확인
print('EX1-3 -', hasattr(t, '__iter__')) # True
print('EX1-4 -', isinstance(t, abc.Iterable)) # True
# +) dir 찍어봤을 때 __iter__ 있으면 반복형

print()
print()


# next 사용

class WordSplitIter: # Iterator
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ') # 공백 띄어쓰기 기준으로 list 만듦

    def __next__(self):
        print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration()
        self._idx += 1
        return word

    def __iter__(self):
        print('Called __iter__')
        return self
    
    def __repr__(self): # print문 사용 시
        return 'WordSplit(%s)' % (self._text)
        

wi = WordSplitIter('Who says the night are for sleeping')

print('EX2-1 -', wi)
print('EX2-2 -', next(wi))
print('EX2-3 -', next(wi))
print('EX2-4 -', next(wi))
print('EX2-5 -', next(wi))
print('EX2-6 -', next(wi))
print('EX2-7 -', next(wi))
print('EX2-8 -', next(wi))
#print('EX2-9 -', next(wi))

print()
print()


# Generator 패턴
# 1. 지능형 리스트, 딕셔너리, 집합 -> 데이터 셋이 증가 될 경우, 메모리 사용량 증가 -> 제네레이터가 이를 완화하는 효과
# 2. 단위 실행 가능한 코루틴(Coroutine) 구현에 아주 중요
# 3. 딕셔너리, 리스트 한 번 호출 할 때마다 하나의 값만 리턴 -> 아주 작은 메모리 양을 필요로 함

class WordSplitGenerator: # Generator
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ') # 공백 띄어쓰기 기준으로 list 만듦

    def __iter__(self):
        for word in self._text:
            yield word # 제네레이터
        return
    
    def __repr__(self): # print문 사용 시
        return 'WordSplit(%s)' & (self._text)


wg = WordSplitGenerator('Who says the night are for sleeping')

wt = iter(wg)

print('EX3-1 -', wt)
print('EX3-2 -', next(wt))
print('EX3-3 -', next(wt))
print('EX3-4 -', next(wt))
print('EX3-5 -', next(wt))
print('EX3-6 -', next(wt))
print('EX3-7 -', next(wt))
print('EX3-8 -', next(wt))
#print('EX3-9 -', next(wt)) # StopIteration


print()
print()


# Generator 예제 1

def generator_ex1():
    print('start')
    yield 'AAA'
    print('continue')
    yield 'BBB'
    print('end')

temp = iter(generator_ex1())


#print('EX4-1 -', next(temp)) # start EX4-1 - AAA
#print('EX4-2 -', next(temp)) # continue EX4-2 - BBB
#print('EX4-3 -', next(temp)) # end StopIteration ->알아서 예외 던지고 끝남 (클로저와 같이)
# end StopIteration


for v in generator_ex1():
    print('EX4-4 -', v)

print()

# Generator 예제 2


temp2 = [x * 3 for x in generator_ex1()] # ['AAAAAAAAA', 'BBBBBBBBB'] -> 메모리에 이미 올림
temp3 = (x * 3 for x in generator_ex1()) # <generator object <genexpr> at 0x7ffe76aa3dd0> -> 메모리에 아직 올리지 않음

print('EX5-1 -', temp2) # 지능형 리스트 (List Comprehension)
print('EX5-2 -', temp3) # 지능형 제네레이터

for i in temp2:
    print('EX5-3 -', i)
'''
EX5-3 - AAAAAAAAA
EX5-3 - BBBBBBBBB
'''

for i in temp3:
    print('EX5-4 -', i)
'''
start
EX5-4 - AAAAAAAAA
continue
EX5-4 - BBBBBBBBB
end
'''


print()
print()


# Generator 예제 3 (자주 사용하는 함수)

import itertools

gen1 = itertools.count(1, 2.5) # 무한

print('EX6-1 -', next(gen1)) # 1
print('EX6-2 -', next(gen1)) # 3.5
print('EX6-3 -', next(gen1)) # 6.0
print('EX6-4 -', next(gen1)) # 8.5
# ... 무한


# 조건
print()

gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print('EX6-5 -', v)

print()


# 필터 반대
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print('EX6-6 -', v)

print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print('EX6-7 -', v)

# 연결1
gen5 = itertools.chain('ABCDE', range(1, 11, 2))

print('EX6-8 -', list(gen5)) # ['A', 'B', 'C', 'D', 'E', 1, 3, 5, 7, 9]

# 연결2
gen6 = itertools.chain(enumerate('ABCDE'))

print('EX6-9 -', list(gen6)) # [(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]

# 개별
gen7 = itertools.product('ABCDE')

print('EX6-10 -', list(gen7)) # [('A',), ('B',), ('C',), ('D',), ('E',)]

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print('EX6-11 -', list(gen8)) # [('A', 'A'), ('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'A'), ('B', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'A'), ('C', 'B'), ('C', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'A'), ('D', 'B'), ('D', 'C'), ('D', 'D'), ('D', 'E'), ('E', 'A'), ('E', 'B'), ('E', 'C'), ('E', 'D'), ('E', 'E')]


# 그룹화
gen9 = itertools.groupby('AABBCCCCDDEEE')

#print('EX6-12 -', list(gen9))

for chr, group in gen9:
    print('EX6-12 -', chr, ' : ', list(group))
'''
EX6-12 - A  :  ['A', 'A']
EX6-12 - B  :  ['B', 'B']
EX6-12 - C  :  ['C', 'C', 'C', 'C']
EX6-12 - D  :  ['D', 'D']
EX6-12 - E  :  ['E', 'E', 'E']
'''

print()
