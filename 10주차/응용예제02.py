import operator

instr='''내가 그의 이름을 불러주기 저에는 그는 다만 하나의 몸짓에 지나지 않았다. 내가 그의 이름을 불러주었을때, 그는 내게로 와 꽃이 되었다.
내가 그의 이름을 불러주었을때, 그는 내게로 와 꽃이 되었다. 내가 그의 이름을 불러준 거처럼 나의 이 빛깔과 향기에 알맞은 누가 나의 이름을 불러다오.
그에게로 가서 나도 그의 꽃이 되고 싶다. 우리들은 모두 무엇이 되고 싶다.
나는 너에게 너는 나에게 잊혀지지 않는 하나의 눈짓이 되고 싶다 '''
dic={}
list=[]

if __name__=="__main__":
    for ch in instr:

        if'ㄱ'<=ch and ch <='힣':
            if ch in dic:
                dic[ch]=dic[ch]+1
            else:
                dic[ch]=1

    list=sorted(dic.items(),key=operator.itemgetter(1), reverse=True)
    print('원문\n',instr)
    print("-----------------")
    print("문제\t빈도수")
    print("-----------------")
    for i in range(0, len(list)):
        print(list[i][0], '\t', list[i][1])
