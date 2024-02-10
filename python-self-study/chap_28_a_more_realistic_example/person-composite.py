# embedding-based Manager alternative
class Person:
    def __init__ (self, name, job=None, pay=0): # job and pay are optional
        self.name = name # fill out fields when created
        self.job = job # self is the instance object
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self): # overwrites printing of an instance
        return '[Person: %s %s]' % (self.name, self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay) # embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus) # intercept and delegate
    def __getattr__(self, attr):
        return getattr(self.person, attr) # delegate all other attrs
    def __repr__(self):
        return str(self.person) # must overload again

if __name__ == '__main__':
    bob = Person('Bob Smith') # test the class
    sue = Person('Sue Jones', job='dev', pay=100000) # runs __init__ automatically

    print(bob)
    print(sue)

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)

    tom = Manager('Tom Jones', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)