i, k, star = 0,0,0
numStr, ch, starStr='','',''

##메인 코드 부분##
if __name__=="__main__":
    numStr = input("숫자를 여러개 입력하세요:")
    print("")
    i = 0
    ch = numStr[i]
    while True:
        star = int(ch)
        starStr=""
        for k in range(0, star):
            starStr= starStr + 2*'\u2605'
            k = k + 1

        print(starStr)

        i = i +1
        if(i > len(numStr)-1):
            break


        ch = numStr[i]

