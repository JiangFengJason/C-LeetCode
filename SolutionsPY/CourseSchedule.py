class CourseSchedu:
    def canFinish(self, numCourses, prerequisites):
        if numCourses==0:
            return True
        in_degree=[0 for _ in range(numCourses)]
        adj=[set() for _ in range(numCourses)]
        
        for second, first in prerequisites:
            in_degree[second]+=1
            adj[first].add(second)

        queue=[]
        count=0
        for second in range(len(in_degree)):
            if in_degree[second]==0:
                queue.append(second)
        
        while queue:
            top=queue.pop(0)
            count+=1
            for t in adj[top]:
                in_degree[t]-=1
                if in_degree[t]==0:
                    queue.append(t)
        return count==numCourses