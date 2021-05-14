score = int(input("점수를 입력하세요"))

if score <= 90:
        if score <= 80:
                if score <= 70: 
                        if score <= 60:
                                print("F")

                        else:
                            print("D")
                    
                else:
                    print("C")
            
        else:
            print("B")
else:
    print ("A")

   
