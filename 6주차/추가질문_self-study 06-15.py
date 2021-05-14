i,j=0,0

while i<=9:
    i+=1
    if i<5 :
        j=0
        while j<5-i:
            j+=1
            print (' ',end='')
            
        j=0
        while j<i*2-1:
            j+=1
            print ('*',end='')
        print ('')
    else:
        j=0
        while j<i-5:
            j+=1
            print (' ',end='')
        j=0
        while j<(9-i)*2+1:
            j+=1
            print ('*',end='')
        print ('')

        
'''책의 예제(code 06-15)와 본 코드의 차이점은?
i가 0이 아닌 1부터 시작하여, while의 조건이 달라진다.
