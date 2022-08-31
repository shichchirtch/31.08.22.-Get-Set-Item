class StackObj:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def check_node(self, node):
        if not isinstance(node, StackObj):
            return False
        if not self.top:
            return True
        h = self.top
        while h:
            if h == node:
              #  print("This node is already exists !!!")
                return False
            #print("Next node checks")
            h = h.next
        return True
    def get_by_index(self, num):
        """Функция возвращает элемент по запрашиваемому индексу"""
        if not isinstance(num, int) or num>=len(self):
            raise IndexError
        for i, node in enumerate(self):
            if i == num:
                return node

    def __len__(self):
        if not self.top:
            return 0
        return sum(1 for _ in self)

    def __iter__(self):
        h = self.top
        while h:
            yield h
            h = h.next

    def __getitem__(self, item):
        return  self.get_by_index(item).data

    def __setitem__(self, num, value):
        self.get_by_index(num).data = value
        # self.replace(num, node)
        return self

    def push(self, node):
        if not self.check_node(node):
            return
        if not self.top:
            self.top = node
            return
        if self.top:
            *_, last = self
            last.next = node
            return
    def push_front(self, obj):
        if not self.check_node(obj):
            return
        if not self.top:
            self.top = obj
            return self
        if self.top:
            obj.next = self.top
            self.top = obj
            return self
    # def pop_back(self):
    #     if not self.top:
    #         print("Empty list")
    #         return
    #     if not self.top.next:
    #         self.top = None
    #         return
    #     if self.top.next:
    #         *_, p_last, last = self
    #         p_last.next = None
    #         return
    def replace(self, num, new_node):
        lenth =len(self)
        if not isinstance(num, int) or num>=len(self):
            raise IndexError
        if not isinstance(new_node, StackObj):
            raise TypeError ("В связный список можно добавлять только ЭК StackObj !!!")

        if num >= lenth or type(num) != int:
            print("Index Error")
            return
        if (lenth == 1 or lenth == 0) and num == 0:
            self.top = new_node
            return
        if lenth > 1 and num == 0:
            new_node.next = self.top.next
            self.top = new_node
            return
        if lenth > 1:
            h = self.get_by_index(num - 1)
            new_node.next = h.next.next
            h.next = new_node
            return
    def show_chain(self):
        if not self.top:
            print("Empty list!!")
            return
        for x in self:
            print(x.data, end = " ")


ob = StackObj("one")
ob2 = StackObj("two")
ob3 = StackObj("three")
ob5 = StackObj("five")
st_obj =Stack()
st_obj.push(ob)
st_obj.push(ob2)
st_obj.push_front(ob5)
print(st_obj.get_by_index(1))
print(st_obj[0])
st_obj[0] = "new!!!"
for obj in st_obj: # перебор объектов стека (с начала и до конца)
    print(obj.data)  # отображение данных в консоль
# ob4 = StackObj("four")
# print(len(st_obj))
# print(st_obj[2].data)
# # st_obj.show_chain()
# st_obj[1]=ob3
# print(st_obj[1].data)
# st_obj.push(ob4)
# print(st_obj[0].data)
# st_obj.show_chain()
#
