from cProfile import run


# class Solution:
#     def trans(self , s: str, n: int) -> str:
#         n=len(s)
#         # write code here
#         def ret_n(c):   # return next word's start
#             while c>-1 and s[c]==" " :
#                 c-=1
#             return c
#         def ret_w(c):   # return this word's end
#             if c == n:
#                 return
#             while c>-1 and s[c]!=" " :
#                 c-=1
#             return c
#         tail = ret_n(n-1)
#         head = 0
#         while s[head]==" ":
#             head+=1
#         ret = ""
#         cur, nxt, tmp = n-1, ret_n(n-1), 0
#         run_time = 1
#         while True:           
#             cur = ret_n(cur)
#             if cur < 0:
#                 break
#             tmp = nxt - cur
#             ret+= ''.join([" "]*tmp)
#             nxt = ret_w(cur)
#             ret += s[nxt+1:cur+1] 
#             cur = nxt

            
#         ret = ret.swapcase()
#         ret = ''.join([' ']*(n-tail-1)) + ret + ''.join([' ']*head)
#         return ret

class Solution:
    def trans(self , s: str, n: int) -> str:
        n=len(s)
        # write code here
        def ret_n(c, space=1):   # Func:move over;  space: move over space?
            condition = True if space == 1 else False
            while c>-1 and (s[c]==" ") == condition :
                c-=1
            return c
        ret = ''
        cur, nxt = n-1, n-1
        while True:
            if s[cur] == " ":
                nxt = ret_n(cur)
                ret += ''.join([" "]*(cur-nxt))
                cur = nxt
            else:
                cur = ret_n(cur)
                nxt = ret_n(cur, 0)
                ret+=s[nxt+1:cur+1]
                cur = nxt
            if cur == -1:
                break
        ret = ret.swapcase()
        return ret




def dprint(s):
    ret = ""
    for i in s:
        ret += "_" if i == " " else i
    print(ret)


s="h i "    # _I_H
n=4
solver = Solution()
dprint(solver.trans(s,n))


s="This is"
n=16
solver = Solution()
dprint(solver.trans(s,n))


s="This is a sample"
n=16
solver = Solution()
dprint(solver.trans(s,n))

s=" h i"    # I_H_
n=4
solver = Solution()
dprint(solver.trans(s,n))


