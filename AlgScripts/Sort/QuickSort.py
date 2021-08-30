from random import randint
def sorted(arr):
    n=len(arr)
    if n==1:
        return arr
    mid=n//2
    s1=sorted(arr[:mid]) # 0 to mid-1
    s2=sorted(arr[mid:]) # mid to n-1
    t=mid
    q=n-mid
    s=[]
    while(t>0 and q>0):
        if s1[0]<s2[0]:
            s.append(s1.pop(0))
            t-=1
        else:
            s.append(s2.pop(0))
            q-=1
    return s+s1+s2
if __name__=="__main__":
    seq=[]
    for i in range(10):
        seq.append(randint(0,9))
    print(seq,sorted(seq))