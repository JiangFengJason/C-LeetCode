class BinaryTreeInorder:
    def inorderTraversal(self, root):
        nums=[]
        return self.helper(root,nums)

    def helper(self, root, nums):
        if root is not None:
            if root.left is not None:
                self.helper(root.left,nums)
            nums.append(root.val)
            if root.right is not None:
                self.helper(root.right,nums)
        return nums
         