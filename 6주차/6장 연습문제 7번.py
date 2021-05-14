i,hap = 0,0
for i in range(1,1001,2):
    hap = hap + i
    if hap > 1000:
        break
print("0과 1000사이에 있는 홀수의 합계를 최초로 1000이 넘게 하는 숫자:%d" %i)
