##변수 선언##
c500,c100,c50,c10, money= 0,0,0,0, 0

money = int(input("돈을 입력하세요"))

c500=money//500
money = money%500

c100=money//100
money = money%100

c50=money//50
money = money%50

c10 = money//10
money = money%10

print("\n 500원 짜리 -----> %d개" %c500)
print("\n 100원 짜리 -----> %d개" %c100)
print("\n 50원 짜리 -----> %d개" %c50)
print("\n 10원 짜리 -----> %d개" %c10)
print("\n 바꾸지 못한 잔돈-----> %d원" %money)



