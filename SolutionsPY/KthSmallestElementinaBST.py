from SameTree import TreeNode
class KthSmallestElement:
    def kthSmallest(self, root, k):
        if root is None:
            return root

        stack=[]
        container=[]
        curr=root

        while curr or stack:
            if curr is not None:
                stack.append(curr)
                curr=curr.left
            else :
                num=stack.pop()
                container.append(num.val)
                if len(container)==k:
                    break
                curr=num.right
        
        return container.pop()