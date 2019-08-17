import collections
class RemoveDuplicated:
    def removeDuplicateLetters(self, s):
        stack=[]
        counter=collections.Counter(s)
        visited=collections.defaultdict(bool)
        for c in s:
            counter[c]-=1
            if visited[c]:
                continue
            while stack and stack[-1]>c and counter[stack[-1]]:
                visited[stack[-1]]=False
                stack.pop()
            visited[c]=True
            stack.append(c)
        return "".join(stack)