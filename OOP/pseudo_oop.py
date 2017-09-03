#pseudo_constructor
#initialize object members
def person_init(name, money):
    obj = {'name' : name, 'money' : money}
    obj['give_money'] = Person[1]
    obj['get_money'] = Person[2]
    obj['show'] = Person[3]
    return obj

#instance method
def give_money(self, other, money):
    self['money'] -= money
    other['get_money'](other, money)
    
#instance method
def get_money(self, money):
    self['money'] += money

#instance method
def show(self):
    print('{} : {}'.format(self['name'], self['money']))

#class
#container of instance methods
Person = person_init, give_money, get_money, show

if __name__ == "__main__":
    #object creation
    g = Person[0]('greg', 5000)
    j = Person[0]('john', 2000)

    g['show'](g)
    j['show'](j)
    print('')
    
    #message passing
    g['give_money'](g, j, 2000)
    
    #does it work?
    g['show'](g)
    j['show'](j)


    
