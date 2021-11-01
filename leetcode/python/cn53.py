class Solution:
    def maxSubArray(self, nums):
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
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        ]
    expected=[
        6
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
