##전역 변수 선언 부분##
i, k, gugudanLine = 0, 0, ""

##메인코드 부분##
for i in range(9, 1, -1):
    gugudanLine = gugudanLine + (" #  %d단  #" %i)

print(gugudanLine)

for i in range(9,1, -1):
    gugudanLine=""
    for k in range(9,1, -1):
        gugudanLine= gugudanLine +str("%2dX %2d= %2d"%(k,i,k*i))
    print(gugudanLine)
