class Node():
    def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None


class BinarySearchTree():
    def __init__(self, data):
            self.root = Node(data)
            self.size = 1

    def insert(self, root, value):
        if root is None:
            root = Node(value)
            return None

        if root.data > value:
            if root.left is None:
                root.left = Node(value)
                return None
            self.insert(root.left, value)

        if root.data < value:
            if root.right is None:
                root.right = Node(value)
                return None
            self.insert(root.right, value)

    def search(self, root, value):
        if root is None or root.data == value:
            return root

        if root.data > value:
            self.search(root.left, value)

        if root.data < value:
            self.search(root.right, value)

    def delete(self, root, value):
        if root is None:
            return root

        if root.data > value:
            root.left = self.delete(root.left, value)

        elif root.data < value:
            root.right = self.delete(root.right, value)

        else:
            if root.right is None:
                temp = root.left
                root = None
                return temp

            if root.left is None:
                temp = root.right
                root = None
                return temp

            curr = root.right
            while(curr.left is not None):
                curr = curr.left

            root.data = curr.data
            root.right = self.delete(root.right, curr.data)

        return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print (root.data)
        inorder(root.right)

def main():
    myBST = BinarySearchTree(10)
    myBST.insert(myBST.root, 9)
    myBST.insert(myBST.root, 12)
    myBST.insert(myBST.root, 5)
    myBST.insert(myBST.root, 17)
    inorder(myBST.root)
    myBST.delete(myBST.root, 12)
    print()
    inorder(myBST.root)
if __name__ == '__main__':
    main()
