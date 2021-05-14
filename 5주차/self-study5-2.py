a, b, c, answer = 1, 0, 0, 0

a = int(input("***첫 번째 수를 입력하세요"))
b = int(input("***두 번째 수를 입력하세요"))
c = int(input("***더할 숫자를 입력하세요"))

if a<b :
    for i in range(a, b+1, c):
        answer = answer + i
    print("%d + %d +.. +%d는 %d입니다"%(a, a+3 , b , answer))
else:
    for i in range(b, a+1, c):
        answer = answer + i
    print("%d + %d +.. +%d는 %d입니다"%(b, b+3 , a , answer))
