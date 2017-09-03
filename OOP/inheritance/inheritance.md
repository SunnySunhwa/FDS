# Computer Science School
## Inheritance
---

## relations between classes
  - choose either inheritance or composition
---

## IS-A 
  - A laptop IS-A computer
  - ~은 ~의 한 종류이다.
  - Inheritance
    - reusability
      - has members and methods of base classes
      - adds members and methods

```python
#base, parent class
class Computer:
    pass
    
#derived, child class
class Laptop(Computer):
    pass 
```
---
## HAS-A
  - A policeman has a gun
  - ~이 ~을 가지고 있다. or 포함하고 있다.
  - Composition(합성) or Aggregation(통합)

```python
class Gun:
	pass
        
class Police:
    def __init__(self):
        self.gun = Gun()
```
---
## Polymorphism
  - 다형성
  - Inheritance에서 가장 중요한 개념
```python
from abc import *
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
```
---
## Polymorphism
  - In inheritance, 
    the same instance method of
    objects from different classes
    results in different behaviors.
    
---
## Method overriding
  - overrides(replaces) a method provided by base class
  - same name, args
  - execution : by the object 
---
## abstract class
  - 추상 클래스
    - 인스턴스를 만들 수 없다.
    - abstract method
      - pure virtual method
       : 몸체(body)가 없는 함수
      - 파생 클래스에서 반드시 overriding 해야 함
