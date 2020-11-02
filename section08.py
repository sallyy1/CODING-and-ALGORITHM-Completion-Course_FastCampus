# Section08
# 파이썬 모듈과 패키지

# 패키지(=폴더) 예제
# 상대 경로
# .. : 부모 디렉토리로 이동
# . : 현재 디렉토리로 이동


# 사용1(클래스)

from pkg.fibonacci import Fibonacci # from 폴더.파일 import 클래스

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)


# 사용2(클래스) -> 권장x
from pkg.fibonacci import *

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)


# 사용3(클래스)
from pkg.fibonacci import Fibonacci as fb # alias

Fibonacci.fib(500)

print("ex3 : ", fb.fib2(400))
print("ex3 : ", fb().title)



# 사용4(함수)
import pkg.calculations as c # 해당 파일에는 클래스는 없고 함수들만 있음 -> 바로 import 폴더.파일 

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))


# 사용5(함수)
from pkg.calculations import div as d # 필요한 특정 함수만 가져오기
print("ex5 : ", int(d(100,10)))


# 사용6
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
print(dir(builtins))

