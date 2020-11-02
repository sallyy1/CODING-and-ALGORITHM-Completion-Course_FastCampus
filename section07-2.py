# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제 1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능

# "상속" : 코드의 재사용 가능 & 중복을 최소화 (장점)

# 라면 -> 속성(종류, 회사, 맛, 면 종류, 이름) : 공통요소 -> 부모 & 나머지 -> 자식 클래스에서 생성

#
class Car:
    """Parent Class""" # 클래스 이름 정의
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "show Method!"'


class BmwCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모 클래스의 init()메소드 호풀
        self.car_name = car_name

    def show_model(self) -> None: # 리턴 값이 없음을 Hinting
        return "Your Car Name : %s" % self.car_name
    

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모 클래스의 init()메소드 호풀
        self.car_name = car_name

    def show_model(self) -> None: # 리턴 값이 없음을 Hinting
        return "Your Car Name : %s" % self.car_name

    def show(self): # 부모한테도 있는 메소드를 자식한테 선언해봄 (오버라이딩)
        print(super().show()) # super() -> 부모에 있는 메소드를 자식에서 호출하고 싶을 때
        return 'Car Info : %s %s %s' % (self.car_name, self.type, self.color)



# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super 에서 가져옴
print(model1.type) # Super 에서 상속받음

print(model1.car_name) # Sub의 속성
print(model1.show()) # Super의 show() 메소드
print(model1.show_model()) # Sub

print(model1.__dict__) # 자식에서 생성할 때 초기화 한 값 & 부모에서 생성할 때 초기화 한 값 모두 가지고 있음


# Method Overriding(오버라이딩)
model2 = BenzCar("220d", 'suv', "black")
print(model2.show()) # 부모 메소드를 반드시 그대로 상속받지 않고, 개선/수정 등 재활용 가능 !


# Parent Method Call
model3 = BenzCar("350s", 'sedan', 'silver')
print(model3.show()) # 오버라이딩 된 show() 가 호출됨



# Inheritance Info(상속 정보)
print(BmwCar.mro()) # mro() 메소드 ! -> 상속 정보를 list 타입으로 반환해줌
print(BenzCar.mro())


# 예제 2
# 다중 상속
class X():
    pass
    
class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z): # 여러 클래스를 상속받을 수 있음 (유연)
    pass

print(M.mro())
print(A.mro())