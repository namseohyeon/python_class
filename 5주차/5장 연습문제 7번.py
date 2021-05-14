import random

A = random.randrange(1,7)
B = random.randrange(1,7)

print("A의 숫자는 %d 입니다" %A)
print("B의 숫자는 %d 입니다" %B)

if A > B:
    print("A가 이겼습니다.")
elif A < B:
    print("B가 이겼습니다")
else:
    print("비겼습니다.")
