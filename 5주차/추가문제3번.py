dollar = 1167
yen = 1.096
euro = 1268
yuan = 171

currency = int(input("환전할 통화는?"))
cost = int(input("환전할 금액은?"))

if currency == 1:
    d = cost*dollar
    print( "%g" %d)
if currency == 2:
    y = cost*yen
    print( "%g" %y)
if currency == 3:
    e = cost*euro
    print( "%g" %e)
if currency == 4:
    y = cost*yuan
    print( "%g" %y)



