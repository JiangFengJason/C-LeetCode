class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class ConstructBinaryTree:
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None
        root=TreeNode(preorder[0])
        i=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:i+1],inorder[:i])
        root.right=self.buildTree(preorder[i+1:],inorder[i+1:])
        return root