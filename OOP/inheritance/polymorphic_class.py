#simple example of polymorphism
from abc import *

#추상 클래스
#인스턴스를 만들 수 없다.
#인터페이스를 제공한다.
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        print('BOW-WOW')

class Cat(Animal):
    def say(self):
        print('MEW MEW')

class Duck(Animal):
    def say(self):
        print('QUACK QUACK')
    
if __name__ == "__main__":
    animals = []
    
    animals.append(Dog())
    animals.append(Cat())
    animals.append(Duck())

    #어떤 동물인지 알 필요 없다.
    #객체에 따라 그에 맞는 메서드가 호출됨
    for animal in animals:
        animal.say()

        
