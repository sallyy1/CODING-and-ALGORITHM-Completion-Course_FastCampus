## 퀴즈
# 1번 -> c !
class Foo:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print('I am' + self.name)
    
class Bar(Foo):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("You are " + self.name)

bar = Bar('John')
bar.speak()


# 2번 -> a

# 3번 -> d?

# 4번 -> c?

# 5번 -> a ?
"""
클래스변수(static변수)
  - 클래스변수는 클래스가 정의만 되어도 접근 가능한 변수로 독립적인 저장공간을 갖는 인스턴스변수와는 달리 클래스변수는 모든 인스턴스가 저
    장 공간을 공유한다. 따라서 한클래스에서 생성된 인스턴스들이 공통적인 값을 유지해야하는 경우 클래스변수로 선언하여 값을 공유할수 있도록
    한다.

출처: https://lueseypid.tistory.com/3 [DevNori]
"""

# 6번 -> d
"""
#sum = 0
def int_sum(*args):
    #global sum
    sum = []
    try:
        for n in args:
            sum += n
    except:
        print('error')
    return sum

#int_sum("abcd")
#print(int_sum(10))
print(int_sum([1, 10]))
#int_sum(1)
"""

# 7번
#from pkg.foo import Foo

# 8번 -> datetime.datetime.now()
import datetime
now = datetime.datetime.now()
print(now)

# 9번 -> 인스턴스?

# 10번 -> Static Method ?


#################
## 과제

# 1번



# 2번

class Median:
    def __init__(self):
        pass
 
    def get_item(self, item):
        item.sort()
        #lt = []
        #lt.append(x)
        #lt.sort()
 
    def clear(self):
        pass
 
    def show_result(self):
        if len(lt) % 2 == 0:
            print((lt[len(lt)-1] + lt[len(lt)]) / 2)
        else:
            print(lt[round(len(lt)-1)])

 
median= Median()
for x in range(10):
    median.get_item(x) # x = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
median.show_result()
 
median.clear()
for x in [0.5, 6.2, -0.4, 9.6, 0.4]:
    median.get_item(x)
median.show_result()



# 3번
"""
class Animal:
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' cannot move.')
 
 
class Dog(Animal):
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' cannot speak.')
 
    def move(self):
        print(self.name + ' moves like a jagger.')
 
 
class Retriever(Dog):
    def __init__(self, name):
        self.name = name
 
    def speak(self):
        print(self.name + ' is smart enough to speak.')
 
    def move(self):
        print(self.name + ' moves like a jagger.')
 
 
dog = Dog('Nancy')
dog.speak()
dog.move()
 
super_dog = Retriever('Michael')
super_dog.speak()
super_dog.move()
"""

# 4번

class Foo:
    def bar():
        print('A')

    def func():
        print('B')
 
Foo.bar()
Foo().func()
Foo.Bar.func()
print(Foo())