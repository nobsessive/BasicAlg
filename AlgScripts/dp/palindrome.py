class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dynamic programming approach
        ls = len(s)
        if ls < 2:
            return s
        dpe, dpo = [0]* ls, [0]*ls  #index of the center of odd/even palindrome
        # assumption even center: begining of second half, init to 1
        # assumption odd center: center index, init to 0
        dpe[0], dpo[1] = 1, 0
        last, max_const_str_len, const_str_char, cnt = s[0], 1, s[0], 1 # constant string check
        m = 1   # maximum length of palindrome
        m_idx = 0 # index of the center of max palindrome
        o_flag = 1 # max palindrome is of odd length, initialize to true
        for i in range(1, ls):# submit error!: can't be range(ls), otherwise 'ac' results index out of range
            # Find the optimality equation
            # 13531 dpo[4] dpo[i] 5512321 2*4-6
            if (2*dpo[i-1]-i)>=0 and s[i] == s[2*dpo[i-1]-i]:
                diff = i - dpo[i-1]
                dpo[i] = dpo[i-1]
                candidate_len = 2*diff+1
                if candidate_len > m:
                    m = max(m, candidate_len)
                    m_idx = dpo[i]
                    o_flag = 1
            else:
                dpo[i] = i
            # 5512344321 dpe[9] 2*6-9
            # 0123456789
            if (2*dpe[i-1]-i-1) >=0 and s[i] == s[2*dpe[i-1]-i-1]:   # submit error!: when 2*dpe[i-1]-i-1 == -1, 
                # it's possible because the begining of first half is the one before 0-th element
                # coincidently python takes it as the last element. Case 'ccd'. Must do range check first. On
                # the other hand, odd palindrome does not need this check
                dpe[i]=dpe[i-1]
                candidate_len = 2*(i-(dpe[i]-1))
                if candidate_len > m:
                    m = max(m, candidate_len)
                    m_idx = dpe[i]
                    o_flag = 0
                # print(f"i{i},m{m}")
            else:
                dpe[i]=i+1
            # constant string check
            if s[i] == last:
                cnt += 1
                if cnt > m:
                    max_const_str_len = cnt
                    const_str_char=s[i]
                    m = max_const_str_len
            else:
                last = s[i]
                cnt = 1

            # print(f"dpe{dpe}")
            print(f"dpo{dpo}")
        if max_const_str_len >= m:
            res = [const_str_char] * max_const_str_len
            return ''.join(res)
        if o_flag == 1:
            res = s[m_idx-m//2:m_idx+m//2+1]
        else:
            res = s[m_idx-m//2:m_idx+m//2]

        return res

testcase =[
    # 'cbbd',
    # 'babad',
    # 'csdbbdsd',
    # 'ac',
    # 'ccd', # submit error!: index of even dp should be checked
    # 'bb',    # submit error: index of odd dp should also be checked
    # 'aaaa',  # submit error!: dynamic state transition has design flaw: odd length palindrome including index i-1 can extend to even length palindrome at index i. I should have included check of constant string.
    'bananas'   # submit error!: @i=4, 'nan' can't expand to 'anana' since 3 is not store at dpo[3]
] 

ans = [
    3
]

# solver = Solution()
# for i in testcase:
#     print(solver.longestPalindrome(i))


testcase1 =[
    'cbbd',
    'babad',
    'csdbbdsd',
    'ac',
    'ccd', 
    'bb',    
    'aaaa',  
    'bananas',
    'dabbcd'
] 

# def longestPalindrome(s: str) -> str:
#     if len(s)==0:
#         return ""
#     d={}
#     for i,value in enumerate(s):
#         if value in d:
#             d[value].append(i)
#         else:
#             d.update({value:[i]})
#     #  
#     maxlen=1
#     mp=mq=0
#     for value in d :
#         l=d[value]
#         while len(l)>1:
#             t=len(l)-1
#             while t>0:
#                 p=l[0]
#                 q=l[t]
#                 if q-p+1<maxlen:
#                     break
#                 flag=True
#                 while p<q:
#                     if s[p]!=s[q]:
#                         flag=False
#                         break
#                     p+=1
#                     q-=1
#                 if flag==True and (l[t]-l[0]+1>maxlen):
#                     maxlen=l[t]-l[0]+1
#                     mp=l[0]
#                     mq=l[t]
#                     flag2=True
#                     break
#                 t-=1
#             l=l[1:]
#     return s[mp:mq+1]

# for i in testcase1:
#     print(longestPalindrome(i))

