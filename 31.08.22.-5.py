class IterColumn:
    def __init__(self, lst, column):
        self.lst = lst
        self.column = column

    def __iter__(self):
        for x in self.lst:
            for y in range(len(x)):
                if self.column ==  y:
                    # raise IndexError ('index out of range (выход индекса за допустимый диапазон')
                    yield x[y]



lst = [['x00', 'x01', 'x02'],
       ['x10', 'x11', 'x12'],
       ['x20', 'x21', 'x22'],
       ['x30', 'x31', 'x32']]

# it = IterColumn(lst, 0)

it = IterColumn(lst, 2)
for x in it:  # последовательный перебор всех элементов столбца списка: x12, x22, ..., xM2
    print(x)

it_iter = iter(it)
x = next(it_iter)
