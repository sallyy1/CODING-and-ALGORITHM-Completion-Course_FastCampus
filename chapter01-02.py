# Chapter01-2
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등

# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수


# 클래스 재 선언
class Student(): # class Student(Object):
    """
    Student
    Author : Lee
    Date : 2020.11.07
    """

    # 클래스 변수 (=공용)
    student_count = 0

    def __init__(self, name, number, grade, details, email=None): # email값이 없으면 None을 넣어줘라
        # 인스턴스 변수들 (=내꺼, private)
        self._name = name
        self._number = number
        self._grade = grade
        self._details = details
        self._email = email

        Student.student_count += 1 # 클래스 변수에 접근할 땐 -> 클래스명.변수

    def __str__(self):
        return 'str {}'.format(self.__name)

    def __repr__(self):
        return 'repr {}'.format(self.__name)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Student Detail Info : {} {} {}'.format(self._name, self._email, self._details))

    def __del__(self):
        Student.student_count -= 1


# self 의미
studt1 = Student('Cho', 2, 3, {'gender': 'Male', 'score1': 65, 'score2':  44})
studt2 = Student('Chang', 4, 1, {'gender': 'Female', 'score1': 85, 'score2':  74}, 'stu2@naver.com')

# ID 확인
print(id(studt1))
print(id(studt2))

print(studt1._name == studt2._name) # False (값을 비교)
print(studt1 is studt2) # False (레퍼런스 레이블 비교)


a = 'ABC'
b = a
print(a is b) # True (레퍼런스 레이블 비교)
print(a == b) # True (값을 비교)


# dir & __dict__ 확인
print(dir(studt1))
print(dir(studt2))

print()
print()

print(studt1.__dict__) # 인스턴스의 속성 값도 같이 보여줌
print(studt2.__dict__)

# Doctring (닥스트링)
print(Student.__doc__) # 클래스 주석 확인 가능

# 실행
studt1.detail_info() # 클래스 내 detail_info() 메소드
studt2.detail_info()


# 에러 -> 이유 : self 라는 아규먼트가 없음
#Student.detail_info()


# 에러 없이 "클래스에 직접 접근" 하고 싶다면
Student.detail_info(studt1) # 메소드 안에 인스턴스화된 변수를 넣어주면 가능 !
Student.detail_info(studt2)


# 비교
print(studt1.__class__, studt2.__class__) # 부모 클래스를 알려줌
print(id(studt1.__class__) == id(studt2.__class__)) # True

print()


# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)

#studt1._name = 'HAHAHA' # 권장X
print(studt1._name, studt2._name)
print(studt1._email, studt2._email)

print()
print()

# 클래스 변수

# 접근
print(studt1.student_count) # 클래스 변수에 접근 가능
print(studt2.student_count) # 2
print(Student.student_count)
# "인스턴스 변수" 는 각 "인스턴스화된 변수이름" 으로 직접 접근해야 함

print()
print()


# 공유 확인
print(Student.__dict__) # student_count : 2 있음
print(studt1.__dict__) # student_count 없음

# 근데 어떻게 가능?

# 인스턴스 네임스페이스에 없으면 상위에서 검색 !
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수)) !

del studt2

print(studt1.student_count) # 1
print(Student.student_count) # 1

# 반대로 상위 -> 하위 검색은 불가
#print(Student._name) # AttributeError: type object 'Student' has no attribute '_name'