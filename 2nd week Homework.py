# 1번

import csv

with open('./a.csv', 'r') as f:
    content = csv.reader(f, delimiter=',')
    
    sum = 0

    print(type(content)) # content의 type : <class '_csv.reader'>

    for elem in content: # elem의 type : list
        for a in elem: # a의 type : string
            sum += int(a) # int 형 변환

    print(sum)


# 2번

# 과제 3번 코드란

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
