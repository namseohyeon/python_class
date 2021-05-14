i, hap =0, 0

for i in range(1, 1000, 1):
    if i > 500:
        if i % 2 == 0:
            continue
        else:
            hap = hap + i;
    else: 
        continue

print("500과 1000 사이에 있는 홀수의 합계: %d" %hap)
