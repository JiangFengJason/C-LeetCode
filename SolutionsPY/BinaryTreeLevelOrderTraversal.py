class BinaryTreeLevelOrder:
    def levelOrder(self, root):
        levels=[]
        if not root:
            return levels

        def helper(root,level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(root.val)

            if root.left:
                helper(root.left,level+1)
            if root.right:
                helper(root.right,level+1)

        helper(root,0)
        return levels

        # 层序遍历，将每层节点逐个放入list中
        # if not root:
        #     return []
        # res=[]
        # helper=[root]
        # while helper:
        #     temp=[]
        #     for node in helper:
        #         res.append(node.val)
        #         if node.left:
        #             temp.append(node.left)
        #         if node.right:
        #             temp.append(node.right)
        #     helper=temp
        # return res
    
        