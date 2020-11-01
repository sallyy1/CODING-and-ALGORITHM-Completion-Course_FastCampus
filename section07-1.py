# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요 !
# 네임스페이스 : 각 객체를 인스턴스화 할 때 저장된 공간
# 클래스 변수 : 직접 사용 가능, 객체 보다 먼저 생성
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용


# 선언
#class 클래스명:
#    함수
#    함수
#    함수


# 예제 1
class UserInfo:
    # 클래스의 구성: (1)속성, (2)메소드
    def __init__(self, name, height): #weight, address 등등 추가 가능 # 클래스를 최초 초기화할 때 사용하는 init() 함수
        self.name = name
        print("초기화 : ", name)
        self.height = height
        print("초기화 : ", height)

    def user_info_p(self):
        print("Name : ", self.name)
        print("height : ", self.height)
    # pass

# 네임 스페이스
user1 = UserInfo("Kim", 180)
user1.user_info_p()

user2 = UserInfo("Park", 160)
user2.user_info_p()


print(id(user1)) # id() 함수 -> 주소값을 알려주는 함수 (클래스 내 각 인스턴스들은 독립적 공간에 자기이름 및 주소 등을 저장함)
print(id(user2))
print(user1.__dict__) # __dict__ -> 네임스페이스를 확인하는 명령어
print(user2.__dict__)



# 예제 2
# self의 이해
class SelfTest:
    def function1(): # 클래스 메소드
        print('function1 called')
    def function2(self): # 인스턴스 메소드
        print(id(SelfTest))
        print('function2 called')

self_test = SelfTest()
# self_test.function1() -> 불가능
SelfTest.function1() # 가능 (self 인자가 없음 -> 클래스에서 바로 function1()을 불러와야)
self_test. function2() # 가능 (1. 인스턴스 생성해서 인스턴스에서 function2() 호출)

print(id(self_test))
SelfTest.function2(self_test) # 가능 (2. 클래스에서 바로 function2() 호출. <- 이때는 인자를 함수에 넣어줘야 함 !)


# 예제 3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 (모두가 공유) -> 예: 연봉인상율
    stock_num = 0
    def __init__(self, name): # 인스턴스 호출 시에 init() 메소드가 호출되므로, self를 받을 필요가 있음
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1


user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)
print(WareHouse.__dict__) # 'stock_num': 3 이 출력됨 (중요 !)
                          # 클래스 네임스페이스, 클래스 변수 (공유)

print(user1.name)
print(user2.name)
print(user3.name)

print(user1.stock_num) # 자기(인스턴스) 네임스페이스에 없으면, 클래스 네임스페이스에 가서 찾는다 -> 클래스에도 없으면 에러를 호출
print(user2.stock_num)
print(user3.stock_num)



del user1 # del -> 인스턴스를 메모리에서 지울 수 있음

print(user2.stock_num)
print(user3.stock_num)



