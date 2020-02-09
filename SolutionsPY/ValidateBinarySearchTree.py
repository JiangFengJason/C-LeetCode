class ValidateBinarySearch:
    def isValidBST(self, root):
        def helper(node,lower=float('-inf'),higher=float('inf')):
            if not node:
                return True
            if node.val<=lower or node.val>=higher:
                return False
            if not helper(node.left,lower,node.val):
                return False
            if not helper(node.right,node.val,higher):
                return False
            return True
        return helper(root)