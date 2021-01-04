#3. Longest Substring Without Repeating Characters
# python3 77%
import string
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # a=list(string.ascii_lowercase)
        # d={}
        # for i in a:
        #     d.update({i:None})
        
        d={}
        if len(s)==0:
            return 0
        m=1
        t=0
        d.update({s[0]:0})
        for i in range(1,len(s)):
            if s[i] in d:
                idx=d[s[i]]
            else:
                idx=None
                d.update({s[i]:i})
            
            if idx!=None: # element s[idx] == s[i]
                d.update({s[i]:i})
                if idx+1>=t:  # obstacle No.1
                    t=idx+1
                q=i-t+1
                if q>m:
                    m=q 
            else:
                d.update({s[i]:i})
                if i-t+1>m:
                    m=i-t+1
                    
        return m

s=Solution()
st=["aabaab!bb","abba","abcabcbb","bbbbb","pwwkew",
"",
'au',
'bwf',
"dvdf"
]
for i in st:
    print(s.lengthOfLongestSubstring(i))

# 3 2 3 1 3 0 2 3 3

# next
# reference
# python 99.7%
# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         dicts = {}
#         maxlength = start = 0
#         for i,value in enumerate(s):
#             if value in dicts:
#                 sums = dicts[value] + 1
#                 if sums > start:
#                     start = sums
#             num = i - start + 1
#             if num > maxlength:
#                 maxlength = num
#             dicts[value] = i
#         return maxlength