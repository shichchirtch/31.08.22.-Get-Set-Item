class Person:
    def __init__(self, fio, job, age, salary, year_job):
        self.fio, self.job, self.age, self.salary, self.year_job = fio, job, age, salary, year_job
        self.kit = [self.fio, self.job, self.age, self.salary, self.year_job]
    def __getitem__(self, num):
        if num >= len(self.kit):
            raise IndexError('неверный индекс')
        else:
            return self.kit[num]


    def __setitem__(self, num, value):
        if num >= len(self.kit):
            raise IndexError('неверный индекс')
        else:
            self.kit[num] = value




pers = Person('Гейтс Б.', 'бизнесмен', 61, 1000000, 46)
pers[0] = 'Балакирев С.М.'
for x in pers.kit:
    print(x)

# for v in pers:
#     print(v)
pers[5] = 123  # IndexError
