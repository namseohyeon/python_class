x = input('문자열 입력')

if (x.isalpha()==True):
    print("글씨입니다")
elif(x.isdigit()==True):
    print("숫자입니다")
elif(x.isalnum()==True):
    print("글자+숫자입니다")
