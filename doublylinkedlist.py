class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addFirst(self, value):
        newNode = Node(value)

        if self.head is None and self.tail is None:
            self.head = self.tail = newNode
            return

        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode
        self.size += 1

    def append(self, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1

        self.tail.next = newNode
        newNode.prev = self.tail
        self.tail = newNode
        self.size += 1


    def insert(self, key, value):
        newNode = Node(value)

        if self.head is None:
            self.head = self.tail = newNode
            self.size += 1

        temp = self.head
        while temp.next is not None:
            if temp.value == key:
                newNode.next = temp.next
                temp.next.prev = newNode
                temp.next = newNode
                newNode.prev = temp
                self.size += 1
                return
            temp = temp.next

        newNode.prev = temp
        temp.next = newNode
        self.tail = newNode
        self.size += 1

    def removeFirst(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.head.prev = None
        self.size -= 1

    def removeLast(self):
        if self.head is None:
            return

        self.tail = self.tail.prev
        self.tail.next = None
        self.size -= 1


    def remove(self, key):
        if self.head is None:
            return

        temp = self.head
        while temp.next is not None:
            if temp.value == key:
                previous = temp.prev
                previous.next = temp.next
                temp.next.prev = previous
                self.size -= 1
                return
            temp = temp.next

        self.tail = temp.prev
        temp.prev = None
        self.tail.next = None
        self.size -= 1


    def get_size(self):
        return self.size

    def get_tail(self):
        return self.tail.value

    def get_head(self):
        return self.head.value

    def myPrint(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


def main():
    """
    Testing LinkedList
    """
    myList = LinkedList()
    myList.addFirst(1)
    myList.addFirst(10)
    myList.append(2)
    myList.insert(1, 4)
    myList.insert(2, 9)
    myList.removeFirst()
    myList.append(6)
    myList.append(23)
    myList.removeLast()
    myList.remove(4)
    #myList.remove(6)
    myList.myPrint()
    print("Tail value: {}".format(myList.get_tail()))
    print("Head value: {}".format(myList.get_head()))

if __name__ == '__main__':
    main()
