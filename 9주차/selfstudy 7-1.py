aa=[]


for i in range(0,10):
    aa.append(0)
hap = 0
i=0
while i<10:
    aa[i]=int(input(str(i+1)+"번째 숫자:"))
    i = i+1

hap = aa[0]+aa[1]+aa[2]+aa[3]+aa[4]+aa[5]+aa[6]+aa[7]+aa[8]+aa[9]
print("합계==>%d" %hap)
