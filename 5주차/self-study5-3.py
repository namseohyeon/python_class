a = int(input("숫자를 입력하세요:"))

for i in range(2, a):
    if a % i == 0:
        b = 1
        break
    else:
        b = 0

if b == 1:
    print("%d는 소수가 아닙니다" %a)
else:
    print("%d는 소수입니다" %a)
        
