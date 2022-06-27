import random


chance_num = 0
row = 10 #행
column = 3  #열
li = list()

def Function_Clear():
    global chance_num,li
    chance_num = 75
    li = [['0' for _ in range(row)] for _ in range(column)] #각인 리스트 선언

def Rd_T_F(Engraving): # 성공,실패 출력
    global chance_num , li

    Rd = random.randrange(1,100)
    
    if Rd <= chance_num:      
        li[Engraving][li[Engraving].index('0')] = True
        Success_T_F(True)
        return True,chance_num
        
    else:
        li[Engraving][li[Engraving].index('0')] = False
        Success_T_F(False) 
        return False,chance_num
    print(chance_num)


def Success_T_F(chance): #성공,실패 후 확률 조정
    global chance_num
    

    if chance:
        if chance_num > 25:         
            chance_num -= 10
    else:
        if chance_num < 75:
            chance_num += 10
    print()

Function_Clear()











