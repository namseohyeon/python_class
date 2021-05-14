animal={"닭":"병아리",
        "개":"강아지",
        "곰":"능소니",
        "명태":"노가리",
        "말":"망아지",
        "호랑이":"개호주",
        "고등어":"고도리"}



while(True):
    myanimal=input(str(list(animal.keys()))+'중 좋아하는 음식은?')
    if myanimal in animal:
        print("<%s>의 새끼는 <%s>입니다" %(myanimal,animal.get(myanimal)))
    elif myanilmal ==  '끝':
        break
    else:
        print("그런 동물이 없습니다.확인해보세요")
