class FlattenBinaryTree:
    def flatten(self, root):
        while root!=None:
            if root.left!=None:
                most_right=root.left
                while most_right.right!=None:
                    most_right=most_right.right
                most_right.right=root.right
                root.right=root.left
                root.left=None
            root=root.right