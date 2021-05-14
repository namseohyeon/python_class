##변수 선언 부분##
num1,num2,num3 = 0,0,0

num1 = int(input("input number1:"))
num2 = int(input("input number2:"))
num3 = int(input("input number3:"))

if num1 < num2 :
    if num2 < num3:
            print("%d" %num3)
    else:
            print("%d" %num2)

elif num1 > num2 :
    if num3 < num1:
         print("%d" %num1)
    else:
         print("%d" %num3)
