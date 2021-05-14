import operator

trainDic, traninList={},[]
trainDic ={'Thomas':'토마스', 'Edward':'에드워드', 'HENRY':'헨리', 'Gothen':'고든', 'james':'제임스'}

trainList=sorted(trainDic.items(),key=operator.itemgetter(0))

print(trainList)
