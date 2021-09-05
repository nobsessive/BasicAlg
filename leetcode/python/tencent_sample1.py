'''
number of 'STAR' in the string
Given a string consists of only 'S', 'T', 'A' and 'R', find the number of 'STAR' in the string.
Requirement:
    1.'S', 'T', 'A' and 'R' must not be adjacent in the original string.
    2.Index of 'S', 'T', 'A' and 'R' must be increasing in original string.
'''
def solver(n,str):
    if(n<4):
        return 0
    vs,vt,va,vr=[0,0],[0,0],[0,0],[0,0]
    for i in range(n):
        if(str[i]=='S'):
            vs[0]+=1
            vs[1]=1
        elif(str[i]=='T'):
            if(i>0 and str[i-1]=='S'):
                vt[0]=vs[0]-vs[1]
            else:
                vt[1]=vs[0]
                vt[0]=vt[1]+vt[0]              
        elif(str[i]=='A'):
            if(i>0 and str[i-1]=='T'):
                va[0]=vt[0]-vt[1]
                
            else:
                va[1]=vt[0]
                va[0]=va[1]+va[0]
        else:# 'R'
            if(i>0 and str[i-1]=='A'):
                vr[0]=va[0]-va[1]
            else:
                vr[1]=va[0]
                vr[0]=vr[1]+vr[0]           
    return vr[0]
if __name__=="__main__": 
    sample=[
        [7,'SSSTAAR'],
        [8,'SSTTAARR'],
        [7,'SSTAARR']
        
        ]
    expected=[
        0,
        4,
        1
        
    ]
    correct_flag=True
    wrong_list=[]
    for i,item in enumerate(sample):
        c=solver(item[0],item[1])
        print(c)
        if c!=expected[i]:
           correct_flag=False
           wrong_list.append(i)
    print(correct_flag,wrong_list)