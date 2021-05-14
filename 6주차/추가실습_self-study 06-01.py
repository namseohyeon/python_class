i, hap  = 0, 0

for i in range (1,1000,1):
    if i < 100:
        if i % 7 ==0:
            hap = hap + i
    else:
        break
        
print("0과 100사이에 있는 7의 배수 합계: %d" %hap)
