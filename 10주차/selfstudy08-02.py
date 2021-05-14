instr="<<<파<<이>>썬>>>"
outstr=''

for i in range(0, len(instr)):
    if (instr[i] != '<' and instr[i] != '>'):
        outstr= outstr+instr[i]

print("원래 문자열 ==>" + '['+instr+']')
print("공백 삭제 문자열 ==>" + '['+outstr+']')