class Symmetric:
    def isSymmetric(self, root):
        if not root :
            return True
        def doSymmetric(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            if left.val != right.val:
                return False
            return doSymmetric(left.left,right.right) and doSymmetric(left.right,right.left)
        return doSymmetric(root.left,root.right) 