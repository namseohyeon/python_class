inStr = input("문자열을 입력하세요 :")
account1, account2, account3, account4, account5 = [0]*5
for i in inStr:
    if ord('0') <= ord(i) <= ord('9'):
        account1 = account1 + 1
    elif ord('가') <= ord(i) <= ord('힣'):
        account2 = account2 + 1
    elif ord('a') <= ord(i) <= ord('z'):
        account3 = account3 + 1
    elif ord('A') <= ord(i) <= ord('Z'):
        account4 = account4 + 1
    else:
        account5 = account5 + 1

print("대문자: %d 소문자: %d 숫자: %d 한글: %d 기타: %d" %(account4, account3, account1, account2, account5))


