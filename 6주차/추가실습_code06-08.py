i, k, guguLine = 0,0,""

for i in range(2,10):
    print(" #  %d단  #" %i, end='')

print(guguLine)

for i in range(1, 10):
    guguLine = ''
    for k in range(2,10):
        print("%2dX %2d= %2d" %(k,i, k*i), end="")
    print(guguLine)
    

   
