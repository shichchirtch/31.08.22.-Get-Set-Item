class TriangleListIterator:
    def __init__(self, spisok):
        self.lst = spisok
    def __iter__(self):
        a = 0
        for x in self.lst:
            for y in range(len(x)):
                a += 1
                if len(x)> a:
                    raise IndexError ('index out of range (выход индекса за допустимый диапазон')
                yield x[y]



arr =  [['x00'],
       ['x10', 'x11'],
       ['x20', 'x21', 'x22', 'x44', 'x55'],
       ['x30', 'x31', 'x32', 'x33']]
it = TriangleListIterator(arr)
for x in it:  # последовательный перебор всех элементов списка: x00, x10, x11, x20, ...
    print(x, end= " ")
