instr=" 한글 python 프로그래밍"
outstr=''

for i in range(0, len(instr)):
    if instr[i] != ' ':
        outstr= outstr+instr[i]

print("원래 문자열 ==>" + '['+instr+']')
print("공백 삭제 문자열 ==>" + '['+outstr+']')