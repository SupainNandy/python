#amking binery tree
class Node:
    def __init__(self,data):
        self.data= data
        self.left=None
        self.right=None
    

class BineryTree:
    def __init__(self):
        self.root = None

    # 1->Create binery tree
    def create_tree(self):
        self.root = Node(10)

        self.root.left=Node(20)
        self.root.right=Node(30)


        self.root.left.left= Node(40)
        self.root.left.right=Node(50)

        self.root.right.right=Node(60)

    # Inorder Traversal

    def inorder(self,root):
        if root is None:
            return
        
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)

    # preorder Traversal -> Root,left,right
    def preorder(self,root):
        if root is None:
            return
        
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)



    


if __name__ == "__main__":
    tree = BineryTree()
    tree.create_tree()
    tree.inorder(tree.root)
    print("\nPreorder")
    tree.preorder(tree.root)



