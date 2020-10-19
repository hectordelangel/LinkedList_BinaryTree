class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, n):
        self.next = n

    def set_next(self, n):
        self.next = n


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def print(self):
        if self.is_empty():
            print("La lista está vacía")
        current = self.head
        while current is not None:
            print(current.get_data())
            current = current.get_next()

    def insert(self, number):
        current = self.head
        previous = None
        while current is not None:
            if current.get_data() > number:
                break
            else:
                previous = current
                current = current.get_next()
        new = Node(number)
        if previous is None:
            new.set_next(self.head)
            self.head = new
        else:
            new.set_next(current)
            previous.set_next(new)

    def calculate_prom(self):
        if self.is_empty():
            return 0
        else:
            count = 0
            sum = 0
            current = self.head
            while current is not None:
                sum += current.get_data()
                current = current.get_next()
                count += 1
        return sum / count


linked_list = LinkedList()
option = -1


def one():
    num = int(input("\nEscriba un número: "))
    linked_list.insert(num)


def two():
    print("\n")
    linked_list.print()


def three():
    prom = linked_list.calculate_prom()
    print("\nEl promedio es:", prom)


def switch(option):
    switcher = {
        1: one,
        2: two,
        3: three,
    }
    switcher.get(option)()


while option != 0:
    print("\n1, insertar número en la lista")
    print("2, imprime la lista")
    print("3, calcule el promedio")
    option = int(input("Seleccione una opción: "))
    switch(option)
