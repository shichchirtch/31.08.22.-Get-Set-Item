class Bag:
    def __init__(self, max_weight):
        self.max_w = max_weight
        self.kit = []

    def check_weight(self, obj):
        if not isinstance(obj, Thing):
            raise TypeError ("Класс создан только для работы с ЭК Thing")
        if len(self.kit) == 0:
            if obj.weight <= self.max_w:
                return obj
        if len(self.kit)>0:
            wes = sum(thing.weight for thing in self.kit)
            if wes +obj.weight <= self.max_w:
                return obj
            else:
                raise ValueError('превышен суммарный вес предметов')

    def add_thing(self, thing: 'Thing'):
        if self.check_weight(thing):
            self.kit.append(thing)
    def __getitem__(self, num:int):
        if num<len(self.kit):
            return self.kit[num]
        raise  IndexError

    def __setitem__(self, num:int, predmet:'Thing'):
        if num>=len(self.kit):
            raise  IndexError
        wes = sum(thing.weight for thing in self.kit)
        if wes + (predmet.weight - self.kit[num].weight) <= self.max_w:
            self.kit[num]= predmet
        else :
            raise ValueError('превышен суммарный вес предметов, замена невозможна, сумка не выдержит !!!')
    def __delitem__(self, num):
        if num>=len(self.kit):
            raise  IndexError
        del self.kit[num]
        return self

class Thing:
    def __init__(self, name:str, weight):
        self.name= name
        self.weight = weight

    def __repr__(self):
        return f'{self.name}'

bag = Bag(1000)
bag.add_thing(Thing('книга', 100))
bag.add_thing(Thing('носки', 200))
bag.add_thing(Thing('рубашка', 400))
bag.add_thing(Thing('рубашка2', 100))
# bag.add_thing(Thing('рубашка3', 444))
print(bag.kit)
# bag.add_thing(Thing('ножницы', 300)) # генерируется исключение ValueError
print(bag[2].name) # рубашка
bag[1] = Thing('платок', 100)
print(bag[1].name) # платок
del bag[0]
print(bag[0].name) # платок
# t = bag[4] # генерируется исключение IndexError





