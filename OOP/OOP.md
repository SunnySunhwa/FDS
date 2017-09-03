# Computer Science School
## OOP
---
## Object-oriented
  - 실제 세계의 객체를 어떻게 모델링하는가?
    - member 
      -  무엇이 이 객체를 다르게 하는가?
    - method  
      - 이 객체는 무엇을 하는가?
      - 이 객체를 이용하면 무엇을 할 수 있는가?
---

## Encapsulation
  - 멤버(변수)와 메서드(함수)를 클래스로 묶는 것
  - the bundling of data with methods
  - 정보 은닉을 포함 
---

## information hiding
  - restrict direct access to member or method
  - hide a member from user
  - allow access by access functions
```python
>>> class Base:
	def __init__(self, data):
		self.data = data
	def get_data(self):
		return self.data
	def set_data(self, data):
		self.data = data
```
---
## information hiding
  - access modifiers
    - public, protected, private in C++
```C++
class Base{
private:
	int x;
public:
	int get_x() { return x; }
	void set_x(int n) { x = n; }
};
```  
---
---
## information hiding
  - python DO NOT support Information hiding
```python
>>> class Base:
	def __init__(self, n):
        #looks like information hiding......
		self.__x = n	
>>> b = Base(5)
>>> b.__x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.__x
AttributeError: 'Base' object has no attribute '__x'
```
---
## information hiding
```python
# it is not information hiding
>>> b.__dict__
{'_Base__x': 5}
>>> b._Base__x
5
```
---
## information hiding
```python
>>> class Base:
	def __f(self):
		print('__f executed')		
>>> b = Base()
>>> b.__f()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.__f()
AttributeError: 'Base' object has no attribute '__f'
```
---
## information hiding
```python
>>> dir(b)
['_Base__f', '__class__', ...]
>>> b._Base__f()
__f executed
```


