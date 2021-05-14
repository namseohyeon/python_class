scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _= scores
print(valid_score)

scores1 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a, b, *valid_score1 = scores1
print(valid_score1)

scores2 = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
a,*valid_score2,c=scores2
print(valid_score2)

temp ={"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(temp)
temp['조스바']=1200
temp['월드콘']=1500
print(temp)


ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
print("메로나 가격: ", ice["메로나"])

ice["메로나"] = 1300
del ice["메로나"]



