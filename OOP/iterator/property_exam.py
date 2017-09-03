class Person:
    def __init__(self, money):
        self._m = money

    @property
    def money(self):
        print('getter')
        return self._m

    @money.setter
    def money(self, money):
        print('setter')
        self._m = money

if __name__ == "__main__":
    p1 = Person(1000)
    #setter 호출
    p1.money = 3000
    #getter 호출 
    m = p1.money
    print(m)
