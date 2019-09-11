from SameTree import TreeNode
class BinaryTree:
    def maxPathSum(self, root):
        # 负无穷
        max_sum=float("-inf")
        def max_gain(root):
            nonlocal max_sum
            if root==None:
                return 0
            left_gain=max(max_gain(root.left),0)
            right_gain=max(max_gain(root.right),0)

            price=root.val+left_gain+right_gain

            max_sum=max(max_sum,price)

            return root.val+max(left_gain,right_gain)

        max_gain(root)
        return max_sum