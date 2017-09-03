
name = 'Good life'
interest_rate = 7.0
kind = 'demand deposit'

@classmethod
def get_account_info(cls):
    '''
    cls.get_account_info() -> (name, interest_rate, kind)
    '''
    return Account.name,\
            Account.interest_rate,\
            Account.kind
    

def __init__(self, name, money):
    self.user = name
    self.balance = money

def __del__(self):
    pass

    
def deposit(self, money):
    if money < 0:
        return
    self.balance += money

def withdraw(self, money):
    if money > 0 and money <= self.balance:
        self.balance -= money
        return money
    else:
        return None

def transfer(self, other, money):
    '''
    obj.transfer(other, money) -> bool
    other : The object to interact with
    money : money the user wants to send

    returns True if the balance is enough to transfer
    returns False if not
    '''
    mon = self.withdraw(money)
    if mon:
        other.deposit(mon)
        return True
    else:
        return False

def __str__(self):
    return 'user : {}, balance : {}'.format(self.user, self.balance)

Account = type('Account', (), 
              {
                  'name' : name,
                  'interest_rate' : interest_rate,
                  'kind' : kind,
                  'get_account_info' : get_account_info,
                  '__init__' : __init__,
                  '__del__' : __del__,
                  'deposit' : deposit,
                  'withdraw' : withdraw,
                  'transfer' : transfer,
                  '__str__' : __str__
              })

if __name__== "__main__":
    #object를 생성하는 방법
    my_acnt = Account('greg', 5000)
    your_acnt = Account('john', 1000)

    #생성 확인
    print('object created')
    print(my_acnt)
    print(your_acnt)
    print('')

    #object method를 호출하는 방법
    #1. by object
    my_acnt.deposit(500)
    #2. by class
    #Account.deposit(my_acnt, 500)

    #deposit 확인
    print('deposit')
    print(my_acnt)
    print('')
    
    #withdraw 함수 사용법
    print('withdraw')
    money = my_acnt.withdraw(1500)
    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print('')
    
    #class member에 접근하는 방법
    print('class member')
    #1.by class 
    print(Account.name, Account.interest_rate, Account.kind)    
    #2.by object
    #print(my_acnt.name, my_acnt.interest_rate, my_acnt.kind)
    print('')

    #class method를 호출하는 방법
    print('class method')
    #1.by class
    info = Account.get_account_info()
    #2.by object
    #info = my_acnt.get_account_info()
    
    print('''Acount info
name : {}
interest rate : {}
kind : {}'''.format(info[0], info[1], info[2]))
    print('')
    
    #message passing
    print("message passing")
    print(my_acnt)
    print(your_acnt)
    res = my_acnt.transfer(your_acnt, 2000)
    if res:
        print('transfer succeeded')
    else:
        print('transfer failed')
    print(my_acnt)
    print(your_acnt)
    print('')

    print('type of my_acnt.deposit : ', type(my_acnt.deposit))
    print('type of Account.deposit : ', type(Account.deposit))

    print('my_acnt.deposit.__func__ is Account.deposit : ',
          my_acnt.deposit.__func__ is Account.deposit)
    
