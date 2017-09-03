# Computer Science School
## class
---

## Account
```python
# 객체 생성
>>> acnt = Account('greg', 5000)
```
---

## method vs. function
```python
>>> type(acnt.deposit)
<class 'method'>

>>> type(Account.deposit)
<class 'function'>
```
---

## method 
```python
>>> acnt.deposit.__func__ is Account.deposit
True
>>> acnt.deposit.__self__ is acnt
True
```
---

## internal
  - 'classobject.h'
```C
typedef struct {
    PyObject_HEAD
    PyObject *im_func; /* The callable object */
    PyObject *im_self; /* The instance it is bound to */
    PyObject *im_weakreflist;
} PyMethodObject;
```
