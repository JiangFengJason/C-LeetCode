from PlusOne import PlusOne
from AddBinary import AddBinary
from mySqrt import mysqrt
from ClimbingStairs import climb
from RemoveDuplicatesfromSortedList import Remove
from RemoveDuplicatesfromSortedList import ListNode
from SameTree import TreeNode
from SameTree import Same
# from SwapNodesinPairs import ListNode
from SwapNodesinPairs import Swap
from DivideTwoIntegers import divideTwo
from RegularExpressionMatching import Regular
from NextPermutation import NextPer
from JumpGame import Jump
from MergeIntervals import MergeInter
from WildcardMatching import Wildcard
from JumpGameII import JumpG
from BestTimetoBuyandSellStockII import Best
from GasStation import GasStat
from Candy import Can
from RemoveDuplicateLetters import RemoveDuplicated
from CreateMaximumNumber import CreateMaximum
from LongestPalindromicSubstring import LongestPalindromicSub
from ThreeSumClosest import SumClosest
from SearchinRotatedSortedArray import SearchinRotatedSorted
from BestTimetoBuyandSellStock import BestTimetoBuy
from MergekSortedLists import MergeKsorted
from MultiplyStrings import multiplyStrings
from Permutations import Permu
from SpiralMatrixII import Sprial
from RotateList import RotateL
from UniquePaths import Unique
from Subsets import SubSet
from MergeSortedArray import MergeSortedArra
from GrayCode import Gray
from BinaryTreeMaximumPathSum import BinaryTree
from MinStack import MinS
from MajorityElement import MajorityEl
from KthLargestElementinanArray import KthLargestElement
from ContainsDuplicate import ContainsDu
from KthSmallestElementinaBST import KthSmallestElement
from PowerofTwo import Power
from FindFirstandLastPositionofElementinSortedArray import FindFirstandLastPosition
from ProductofArrayExceptSelf import ProductofArray
from ReverseWordsinaStringIII import ReverseWordsinaString
from CombinationSum import CombinationS
from GroupAnagrams import GroupAnag
from MinimumPathSum import MinimusPath
from SortColors import SortColor
from WordSearch import WordSear
from UniqueBinarySearchTrees import UniqueBinarySearch
from WordBreak import WordBrea
from MaximumProductSubarray import MaximumProdect
from HouseRobber import HouseRobb
from CourseSchedule import CourseSchedu
from PerfectSquares import PerfectSquare
from FindtheDuplicateNumber import FindtheDuplicateN
from LongestIncreasingSubsequence import LongestIncreasingSub
from BestTimetoBuyandSellStockwithCooldown import BestTimetoButandSellStock
from CoinChange import CoinC
from LongestPalindrome import LongestPalindr

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

# nums=[[1,4],[0,1]]
# mer=MergeInter()
# res=mer.merge(nums)
# print (res)

# s="aa"
# p="*"
# wild=Wildcard()
# res=wild.isMatch(s,p)
# print(res)

# nums=[2,3,1,1,4]
# j=JumpG()
# res=j.toJump(nums)
# print(res)

# prices=[7,1,5,3,6,4]
# b=Best()
# res=b.maxProfit(prices)
# print(res)

# gas=[1,2,3,4,5]
# cost = [3,4,5,1,2]
# gasStat=GasStat()
# res=gasStat.canCompleteCircuit(gas,cost)
# print(res)

# ratings=[1,3,2,2,1]
# c=Can()
# res=c.candy(ratings)
# print (res)

# s="cbacdcbc"
# r=RemoveDuplicated()
# res=r.removeDuplicateLetters(s)
# print(res)

# nums1 = [3, 4, 6, 5]
# nums2 = [9, 1, 2, 5, 8, 3]
# k = 5
# c=CreateMaximum()
# res=c.maxNumber(nums1,nums2,k)
# print(res)

# s="cbbdbabad"
# l=LongestPalindromicSub()
# res=l.longestPalindrome(s)
# print(res)

# nums = [-1, 2, 1, -4]
# target = 1
# s=SumClosest()
# res=s.threeSumClosest(nums,target)
# print(res)

# nums=[4,5,6,7,0,1,2]
# target=0
# s=SearchinRotatedSorted()
# res=s.search(nums,target)
# print(res)

# prices=[7,1,5,3,6,4]
# b=BestTimetoBuy()
# res=b.maxProfit(prices)
# print(res)

# nums1="123"
# nums2="456"
# m=multiplyStrings()
# ans=m.multiply(nums1,nums2)
# print(ans)

# nums=[1,2,3]
# p=Permu()
# res=p.permute(nums)
# print(res)

# n=3
# s=Sprial()
# matrix=s.generateMatrix(n)
# print(matrix)

# l=ListNode(0)
# p=l
# for i in range(1,6):
#     p.next=ListNode(i)
#     p=p.next
# r=RotateL()
# res=r.rotateRight(l.next,2)
# while res:
#     print(res.val)
#     res=res.next

# m=4
# n=4
# u=Unique()
# res=u.uniquePaths(m,n)
# print(res)

# nums=[1,2,3]
# s=SubSet()
# res=s.subsets(nums)
# print(res)

# nums1=[1,2,3,0,0,0]
# m=3
# nums2=[2,5,6]
# n=3
# mer=MergeSortedArra()
# res=mer.merge(nums1,m,nums2,n)
# print(res)

# n=2
# g=Gray()
# res=g.grayCode(n)
# print(res)

# a=TreeNode(1)
# a.left=TreeNode(2)
# a.right=TreeNode(3)
# b=TreeNode(-10)
# b.left=TreeNode(9)
# b.right=TreeNode(20)
# b.right.left=TreeNode(15)
# b.right.right=TreeNode(7)
# binary=BinaryTree()
# res=binary.maxPathSum(b)
# print(res)

# minStack=MinS()
# minStack.push(512)
# minStack.push(-1024)
# minStack.push(-1024)
# minStack.push(512)
# minStack.pop()
# minStack.getMin()
# minStack.pop()
# minStack.getMin()
# minStack.pop()
# minStack.getMin()

# m=MajorityEl()
# nums=[2,2,1,1,1,2,2]
# res=m.majorityElement(nums)
# print (res)

# kth=KthLargestElement()
# nums=[3,2,3,1,2,4,5,5,6]
# k=4
# res=kth.findKthLargest(nums,k)
# print(res)

# c=ContainsDu()
# nums=[1,3,4,2]
# res=c.containsDuplicate(nums)
# print(res)

# p=Power()
# n=16
# res=p.isPowerOfTwo(n)
# print(res)

# f=FindFirstandLastPosition()
# nums=[5,7,7,8,8,10]
# target =8
# res=f.searchRange(nums,target)

# p=ProductofArray()
# nums=[1,2,3,4]
# res=p.productExceptSelf(nums)
# print(res)

# r=ReverseWordsinaString()
# s="Let's take LeetCode contest"
# res=r.reverseWords(s)
# print(res)

# c=CombinationS()
# candidates = [2,3,5]
# target = 8
# res=c.combinationSum(candidates,target)
# print(res)

# g=GroupAnag()
# strs=["eat", "tea", "tan", "ate", "nat", "bat"]
# res=g.groupAnagrams(strs)
# print(res)

# m=MinimusPath()
# grid=[[1,3,1],[1,5,1],[4,2,1]]
# res=m.minPathSum(grid)
# print(res)

# s=SortColor()
# nums=[2,0,2,1,1,0]
# res=s.sortColors(nums)
# print(res)

# w=WordSear()
# board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
# word="ABCCED"
# res=w.exist(board,word)
# print(res)

# u=UniqueBinarySearch()
# n=3
# res=u.numTrees(n)
# print(res)

# w=WordBrea()
# s = "leetcode"
# wordDict = ["leet", "code"]
# res=w.wordBreak(s,wordDict)
# print(res)

# m=MaximumProdect()
# nums=[-2,0,-1]
# res=m.maxProduct(nums)
# print(res)

# h=HouseRobb()
# nums=[1,2,3,1]
# res=h.rob(nums)
# print(res)

# c=CourseSchedu()
# numCourses=2
# prerequisites=[[1,0],[0,1]]
# res=c.canFinish(numCourses,prerequisites)
# print(res)

# p=PerfectSquare()
# n=12
# res=p.numSquares(n)
# print(res)

# f=FindtheDuplicateN()
# nums=[3,1,3,4,2]
# res=f.findDuplicate(nums)
# print(res)

# l=LongestIncreasingSub()
# nums=[10,9,2,5,3,7,101,18]
# res=l.lengthOfLIS(nums)
# print(res)

# 注意查看力扣上的6题股票问题套路
# b=BestTimetoButandSellStock()
# prices=[1,2,3,0,2]
# res=b.maxProfit(prices)
# print(res)

# c=CoinC()
# coins = [1, 2, 5]
# amount = 11
# res=c.coinChange(coins,amount)
# print(res)

l=LongestPalindr()
s="abccccdd"
res=l.longestPalindrome(s)
print(res)