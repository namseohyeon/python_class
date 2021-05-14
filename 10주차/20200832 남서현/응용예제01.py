indtr,outstr="",""
ch=""
count,i=0,0

if __name__=="__main__":
    instr=input("문자열을 입력하세요: ")
    count=len(instr)

    for i in range(0, count):
        ch = instr[i]
        if (ord(ch)>=ord("A") and ord(ch)<= ord("Z")):
            newch = ord(ch) + 32
        elif (ord(ch)>=ord("a") and ord(ch)<= ord("z")):
            newch = ord(ch) - 32


        outstr = outstr + chr(newch)
    print("대소문자 변환 결과 -->%s" %outstr)
