##전역
i, k = 0,0

##메인 코드부분##

i = 0
while i <9:
    if i < 5:
        k = 0
        while k < 4-i:
            print(' ',end='')
            k = k + 1
        k = 0
        while k < i*2 + 1:
            print('*', end='')
            k = k + 1
    else:
        k =0
        while k < i -4:
            print(' ', end='')
            k = k + 1
        k =0
        while k <(9-i)*2-1:
            print('*', end='')
            k = k + 1
        
    print()
    i = i + 1

