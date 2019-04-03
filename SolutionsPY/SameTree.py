class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Same:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val==q.val:
                if self.isSameTree(p.left,q.left):
                    return self.isSameTree(p.right,q.right)
            return False
        