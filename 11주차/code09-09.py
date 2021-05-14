def multi(v1,v2):
    relist=[]
    res1=v1+v2
    res2=v1-v2
    relist.append(res1)
    relist.append(res2)
    return relist

mylist = []
hap,sub =0,0

mylist=multi(100, 200)
hap = mylist[0]
sub=mylist[1]
print("multi()에서 돌려준 값 ==>%d, %d" %(hap,sub))