
class Solution:
    '''
    Author: P.H.
    Time: O(n)
    Space: O(n)
    1.Build T, root=0
    2.Turn T into Parent=[[]],Child=[[]] as well as getting a leaf node
    3. Get the number of nodes in its subtree Nin[] for each node i
    4. Calculate sum[0]
    5. Calculate sum[1 through n-1] by sum[i]=sum[parent]+(n-1-Nin[i])-Nin[i]-1
    Speed: 0%
    Mem: 77%
    '''
    def sumOfDistancesInTree(self, n: int, edges):
        # build parent-child relationship from node root 
        # while calculate sum of distance from root
        # while derive Nin[]
        import copy
        def buildParentChild2(T,root): 
            #parent=[[] for _ in range(n)]
            #child=[[] for _ in range(n)]
            distance=0
            Nin=[0]*n # initialize Nin to 0, because all leaf nodes' Nin are 0
            leaf=[]
            level=0
            s=[root] # stack 
            while s:
                cur=s[-1]
                if T[cur]==[]:
                    s.pop()
                    level-=1 # each edge weights 1
                    if (cur in leaf) and s:
                        Nin[s[-1]]+=1 # parent's Nin increase by 1
                    elif s:
                        Nin[s[-1]]+=Nin[cur]+1 # parent's Nin increase by (child's Nin +1)
                    continue
                cur_child=T[cur][0]
                #child[cur].append(cur_child)
                level+=1 # add weight when delete an edge
                distance+=level
                T[cur].remove(cur_child) 
                T[cur_child].remove(cur)               
                #parent[cur_child].append(cur)
                s.append(cur_child)
                if T[cur_child]==[]:
                    leaf.append(cur_child)
            # print('Child', child)
            # print('Parent', parent)
            # print('Distance', distance)
            return distance,Nin
        T=[[] for _ in range(n)]
        for edge in edges:
            T[edge[0]].append(edge[1])
            T[edge[1]].append(edge[0])
        distance_root,Nin=buildParentChild2(copy.deepcopy(T),0)
        ret=[0]*n
        ret[0]=distance_root
        s=[0]
        while s:
            cur=s[-1]
            if T[cur]==[]:
                s.pop()
                continue
            cur_child=T[cur][0]
            T[cur].remove(cur_child)
            T[cur_child].remove(cur)
            s.append(cur_child)
            ret[cur_child]=ret[cur]+n-2-2*Nin[cur_child]
        return ret



# build parent-child relationship from node root
# T is a list of adjacent nodes T=[[i,j,k,...],[], ...]
def buildParentChild(T,root): 
    n=len(T)
    parent=[[] for _ in range(n)]
    child=[[] for _ in range(n)]
    s=[root] # stack 
    while s:
        cur=s[-1]
        if T[cur]==[]:
            s.pop()
            continue
        cur_child=T[cur][0]
        child[cur].append(cur_child)
        T[cur].remove(cur_child) 
        T[cur_child].remove(cur)
        parent[cur_child].append(cur)
        s.append(cur_child)
    return child, parent


# reference answer
class Solution2(object):
    def sumOfDistancesInTree(self, N, edges):
        import collections
        graph = collections.defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        count = [1] * N
        ans = [0] * N
        def dfs(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    ans[node] += ans[child] + count[child]

        def dfs2(node = 0, parent = None):
            for child in graph[node]:
                if child != parent:
                    ans[child] = ans[node] - count[child] + N - count[child]
                    dfs2(child, node)

        dfs()
        dfs2()
        return ans
if __name__=="__main__":
    s=Solution2() 
    sample=[
        [6,[[0,1],[0,2],[2,3],[2,4],[2,5]]],
        [1,[]],
        [2,[[1,0]]]
        ]
    expected=[
        [8,12,6,10,10,10],
        [0],
        [1,1]
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.sumOfDistancesInTree(item[0],item[1])
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)