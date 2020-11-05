# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

#print('Test)

#if True
    #pass

#x => y


# NameError : 참조변수 없음
a = 10
b = 15

#print(c)


# ZeroDivisionError : 0 나누기 에러
#print(10 / 0)


# IndexError : 인덱스 범위 오버

x = [10, 20, 30]
print(x[0])
#print(x[3])


# KeyErro

dic = {'name': 'Kim', 'Age': 33, 'City': 'Seoul'}

#print(dic['hobby])
print(dic.get('hobby')) # get() 메소드 -> None 뜸 (안전)


# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 예외

import time
print(time.time())
#print(time.month())


# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

#x.remove(10)
#x.index(10)


# FileNotFoundError -> 외부 파일을 처리할 때 예외 발생

#f = open('test.txt', 'r')


# TypeError
x = [1, 2]
y = (1, 2)
z = 'test'

#print(x + y) # 예외
#print(x + z)

print(x + list(y)) # 형 변환(casting) 하여 해결할 수 있음.


# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생 시 예외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행


# 예제 1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # 'Cho'라고 하면 예외 발생
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except ValueError: # try문이 작동되지 않으면 실행됨
    print('Not found it! - Occurred ValueError!')
else: # try문이 정상 작동되면 실행됨
    print('OK! else!')


# 예제 2
try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 모든 에러 발생 시 작동됨
    print('Not found it! - Occurred Error!')
else: # try문이 정상 작동되면 실행됨
    print('OK! else!')


# 예제 3
try:
    z = 'Cho'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))
except: # 모든 에러 발생 시 작동됨
    print('Not found it! - Occurred Error!')
else: # try문이 정상 작동되면 실행됨
    print('OK! else!')
finally: # 에러가 발생하던, 발생하지 않던 무조건 실행됨
    print('finally ok!')


# 예제 4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('Try')
finally:
    print('Ok Finally!!!!')


# 예제 5
try:
    z = 'C'
    x = name.index(z)
    print('{} Found it! in name'.format(z, x+1))

# 에러를 계층적으로 여러개 잡을 수도 있음
#except ValueError as l: # alias를 주고 에러의 내용을 출력할 수도 있음
#    print(l) # "" 'C' is not in list " 출력됨
except ValueError:
    print('Not found it! - Occurred ValueError!')
except IndexError:
    print('Not found it! - Occurred IndexError!')
except Exception: # 나머지 에러는 Exception으로 마지막으로 잡음
    print('Not found it! - Occurred Error!')

else: # try문이 정상 작동되면 실행됨
    print('OK! else!')
finally: # 에러가 발생하던, 발생하지 않던 무조건 실행됨
    print('finally ok!')



# 예제 6
# 예외 발생 : raise (고급)
# raise 키워드로 예외 직접 발생시킬 수 있음
try:
    a = '333'
    if a == 'Kim':
        print('Ok 허가!')
    else:
        raise ValueError # 직접 예외 클래스를 규정 가능
except ValueError:
    print('문제 발생!')
except Exception as f:
    print(f)
else:
    print('Ok!')

