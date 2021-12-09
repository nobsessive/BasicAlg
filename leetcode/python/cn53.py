class Solution:
    def maxSubArray(self, nums): # O(n^2)
        max_value=-100001
        n=len(nums)
        s=[0]*n
        for l in range(1,n+1):
            b=[]
            for i in range(n-(l-1)):
                t=s[i]+nums[i+l-1]
                max_value=max(max_value, t)
                b.append(t)
            s=b
        return max_value

    def maxSubArray_brute_force(self, nums): # O(n^2)
        def sum_li(nums, j, i, n):
            if(j+i>n):
                return -100001
            s=0
            for k in range(j, j+i):
                s+=nums[k]
            return s
        max_value=-100001
        # operation
        n=len(nums)
        for i in range(1,n+1): # length of subarray
            for j in range(0,n): # start index of each subarray
                tmp=sum_li(nums, j, i, n)    # sum_li( array, start_index, length)
                if (tmp>max_value):
                    max_value=tmp

        return max_value


if __name__=="__main__": 
    s=Solution() 
    sample=[
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [-100000]
        ]
    expected=[
        6,
        1,
        -100000
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=s.maxSubArray(item)
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,"\nWrong List:---\n",wrong_list)
