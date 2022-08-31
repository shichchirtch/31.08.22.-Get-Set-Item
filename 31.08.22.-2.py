class SparseTable:
    def __init__(self):
        self.rows, self.cols = 0, 0
        self.table = [[0 for x in range(self.rows)] for _ in range(self.cols)]
        self.ins_dict = {}
    def update(self):
        self.rows = max(key[0] for key in self.ins_dict)+1
        self.cols = max(key[1] for key in self.ins_dict) +1

    def add_data(self, row:int, col:int, data:'Cell'):
        # if row > self.rows:
        #     self.rows = row
        # if col> self.cols:
        #     self.cols = col
        # if not isinstance(col, int) and not isinstance(row, int):
        #     raise TypeError ('Нужны инты !')
        # for r in range(self.rows):
        #     if r == row:
        #         for c in range(self.cols):
        #             if c == col:
        #                 self.table[r][c] = data
        self.ins_dict[(row, col)] = data
        self.update()
    def remove_data (self, row, col):
        try:
            del self.ins_dict[(row, col)]
            self.update()
        except KeyError:
            raise IndexError ("Ячейка не существует !")

    def __getitem__(self, item):
        if len(item) == 2:
            try:
                return self.ins_dict[tuple(item)].value
            except KeyError:
                raise ValueError ("No data")

    def __setitem__(self, key, value):
        if len(key) == 2:
            if not key in self.ins_dict:
                self.ins_dict[tuple(key)]=Cell(value)
                self.update()
            else:
                self.ins_dict[tuple(key)] = Cell(value)

class Cell:
    def __init__(self, data):
        self.value = data
        self.__pr = 100


st = SparseTable()
st.add_data(2, 5, Cell("cell_25"))
print(st.ins_dict)
st.add_data(0, 0, Cell("cell_00"))
print(st.ins_dict)
st[2, 5] = 25 # изменение значения существующей ячейки
# print(st.ins_dict[(2,5)].value)
st[11, 7] = 'cell_117' # создание новой ячейки
print(st[0, 0]) # cell_00
st.remove_data(2, 5)
print(st.rows, st.cols) # 12, 8 - общее число строк и столбцов в таблице
for x in range(st.rows):
    print()
    for y in range(st.cols):
        if (x, y) in st.ins_dict.keys():
            print(st[x, y], end = " ")
        else:
            print(y, end = " ")
# val = st[2, 5] # ValueError
# st.remove_data(12, 3) # IndexError
# # a = SparseTable(3, 3)
# # print(a.table)
# a.add_data(1,1,99999999999)
# print(a.table)
f = Cell("one")
print(f._Cell__pr)
