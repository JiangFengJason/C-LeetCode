from PlusOne import PlusOne
from AddBinary import AddBinary
from mySqrt import mysqrt
from ClimbingStairs import climb
from RemoveDuplicatesfromSortedList import Remove
# from RemoveDuplicatesfromSortedList import ListNode
from SameTree import TreeNode
from SameTree import Same
from SwapNodesinPairs import ListNode
from SwapNodesinPairs import Swap
from DivideTwoIntegers import divideTwo
from RegularExpressionMatching import Regular
from NextPermutation import NextPer
from JumpGame import Jump
from MergeIntervals import MergeInter

# digit=[1,0,0,0,0]
# PlusOne=PlusOne()
# res=PlusOne.plusOne(digit)
# print(res)

# add=AddBinary()
# print(add.addBinary("1010","1011"))

# sqrt=mysqrt()
# print(sqrt.mySqrt(4))

# stairs=climb()
# print(stairs.climbStairs(3))

# a=ListNode(1)
# a.next=ListNode(1)
# a.next.next=ListNode(2)
# re=Remove()
# result=re.deleteDuplicates(a)
# while result:
#     print(result.val)
#     result=result.next

# a=TreeNode(1)
# a.left=TreeNode(2)
# a.right=TreeNode(3)

# b=TreeNode(1)
# b.left=TreeNode(2)
# b.right=TreeNode(3)

# isSame=Same()
# trigger=isSame.isSameTree(a,b)
# print(trigger)

# todivide=divideTwo()
# dividend=10
# divisor=3
# res=todivide.divide(dividend,divisor)
# print(res)

# nums=[1,2,3,4]
# nexP=NextPer()
# res=nexP.nextPermutation(nums)
# print(res)

# nums=[3,2,1,0,4]
# nextJump=Jump()
# res=nextJump.canJump(nums)
# print (res)

nums=[[1,4],[0,1]]
mer=MergeInter()
res=mer.merge(nums)
print (res)