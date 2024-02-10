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
        Person.__init__(self, name, "mgr", pay)
    def giveRaise(self, percent, bonus=.10):
        Person.giveRaise(self, percent + bonus)

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