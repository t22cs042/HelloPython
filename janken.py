import random

Acount = 0
Bcount = 0
while(Acount != 3 and Bcount !=3):
    A = random.randint(0,2)
    B = random.randint(0,2)
    if  A == B:
        if A == 0:
            print("Aの手 : グー v.s. Bの手 : グー → 引き分け")
            
        elif A == 1:
            print("Aの手 : チョキ v.s. Bの手 : チョキ → 引き分け")
            
        else:
            print("Aの手 : パー v.s. Bの手 : パー → 引き分け")
            
    elif A == 0 and B == 1:
        print("Aの手 : グー v.s. Bの手 : チョキ → Aの勝ち")
        Acount+=1

    elif A == 1 and B == 2:
        print("Aの手 : チョキ v.s. Bの手 : パー → Aの勝ち")
        Acount+=1

    elif A == 2 and B == 0:
        print("Aの手 : パー v.s. Bの手 : グー → Aの勝ち")
        Acount+=1
        
    elif A == 0 and B == 2:
        print("Aの手 : パー v.s. Bの手 : チョキ → Bの勝ち")
        Bcount+=1
        
    elif A == 1 and B == 0:
        print("Aの手 : チョキ v.s. Bの手 : グー → Bの勝ち")
        Bcount+=1
        
    elif A == 2 and B == 1:
        print("Aの手 : パー v.s. Bの手 : チョキ → Bの勝ち")
        Bcount+=1
        
if Acount ==3:
    print("A : 3回勝ち" )
elif Bcount ==3:
    print("B : 3回勝ち")



