class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.previous = None

    def get_data(self):
        return self.data

    def get_right(self):
        return self.right

    def get_left(self):
        return self.left

    def get_previous(self):
        return self.previous

    def set_data(self, n):
        self.data = n

    def set_right(self, n):
        self.right = n

    def set_left(self, n):
        self.left = n

    def set_previous(self, n):
        self.previous = n


class BinaryTree:
    def __init__(self):
        self.head = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def search(self, letter):
        if self.is_empty():
            print("La lista está vacía")
        else:
            node = self.search_node(self.head, letter)
            if node is not None:
                return print("La letra está en el árbol")
            else:
                return print("La letra no está en el árbol")

    def search_node(self, node, letter):
        if node is None:
            return None
        elif node.get_data() == letter:
            return node
        elif node.get_data() > letter:
            return self.search_node(node.get_left(), letter)
        elif node.get_data() < letter:
            return self.search_node(node.get_right(), letter)

    def delete(self, letter):
        current = self.search_node(self.head, letter)
        if current is not None:
            previous = current.get_previous()
            # Caso 1
            if current.get_right() is None and current.get_left() is None:
                if current.get_data() < previous.get_data():
                    previous.set_left(None)
                else:
                    previous.set_right(None)
            # Caso 2
            if current.get_left() is not None and current.get_right() is None:
                new = current.get_left()
                new.set_previous(previous)
                if current.get_data() < previous.get_data():
                    previous.set_left(new)
                else:
                    previous.set_right(new)
            elif current.get_left() is None and current.get_right() is not None:
                new = current.get_right()
                new.set_previous(previous)
                if current.get_data() < previous.get_data():
                    previous.set_left(new)
                else:
                    previous.set_right(new)
            # Caso 3
            if current.get_right() is not None and current.get_left() is not None:
                new = current.get_right()
                last=None
                while new is not None:
                    last = new
                    new = new.get_left()
                self.delete(last.get_data())
                current.set_data(last.get_data())

        else:
            return print("El número no está en el árbol")

    def print(self, type):
        if self.is_empty():
            print("La lista está vacía")
        else:
            if type == 1:
                self.in_order(self.head)
            elif type == 2:
                self.pre_order(self.head)
            else:
                self.post_order(self.head)

    def in_order(self, head):
        if head is not None:
            self.in_order(head.get_left())
            print(head.get_data())
            self.in_order(head.get_right())

    def pre_order(self, head):
        if head is not None:
            print(head.get_data())
            self.pre_order(head.get_left())
            self.pre_order(head.get_right())

    def post_order(self, head):
        if head is not None:
            self.post_order(head.get_left())
            self.post_order(head.get_right())
            print(head.get_data())

    def insert(self, letter):
        if self.head is None:
            new = Node(letter)
            self.head = new
            self.count = self.count + 1
        else:
            if self.head != letter:
                self.insert_tree(self.head, letter)
            else:
                print("La letra insertada ya existe, ingrese otro")

    def insert_tree(self, node, letter):
        current = node
        if current.get_data() != letter:
            if current.get_data() > letter:
                if current.get_left() is None:
                    new = Node(letter)
                    current.set_left(new)
                    new.set_previous(current)
                    self.count = self.count + 1
                else:
                    self.insert_tree(current.get_left(), letter)
            elif current.get_data() < letter:
                if current.get_right() is None:
                    new = Node(letter)
                    current.set_right(new)
                    new.set_previous(current)
                    self.count = self.count + 1
                else:
                    self.insert_tree(current.get_right(), letter)
        else:
            print("Ese número ya existe, ingrese otro")


binary_tree = BinaryTree()

option = -1


def one():
    letter = input("\nEscriba una letra: ")
    binary_tree.insert(letter)


def two():
    print("\n")
    binary_tree.print(1)


def three():
    print("\n")
    binary_tree.print(2)


def four():
    print("\n")
    binary_tree.print(3)

def six():
    letter = input("\nEscriba la letra a buscar: ")
    binary_tree.search(letter)

def seven():
    letter = input("\nEscriba la letra a eliminar: ")
    binary_tree.delete(letter)


def switch(option):
    switcher = {
        1: one,
        2: two,
        3: three,
        4: four,
        6: six,
        7: seven,
    }
    switcher.get(option)()


while option != 0:
    print("\n1, Insertar letra en el árbol")
    print("2, In-order")
    print("3, Pre-order")
    print("4, Post-order")
    print("6, Buscar una letra")
    print("7, Eliminar una letra")
    option = int(input("Seleccione una opción: "))
    switch(option)

# binary_tree.insert(10)
# binary_tree.insert(4)
# binary_tree.insert(2)
# binary_tree.insert(3)
# binary_tree.insert(13)
# binary_tree.insert(12)
# binary_tree.insert(105)
# binary_tree.insert(301)
# binary_tree.insert(99)
# binary_tree.insert(85)
#
#
#
# binary_tree.search(13)
#
# binary_tree.delete(13)
# binary_tree.search(13)
# binary_tree.print(3)



