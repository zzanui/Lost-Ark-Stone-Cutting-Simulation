import os
from Stone_Function import Function_Clear,  Rd_T_F
from os import truncate
from tkinter import *
from typing import Tuple

root = Tk()



w = 400
h = 200
x = (root.winfo_screenwidth()/2) - (w/2)
y = (root.winfo_screenheight()/2) - (h/2)



root.title('Stone_Simulator')
root.geometry('%dx%d+%d+%d' % (w,h,x,y))
root.resizable(0,0)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
    
root.iconbitmap(False,resource_path('IMG\mococo.ico'))


canvas = Canvas(root,width=400,height=200)
canvas.pack()

li = [[[0 for col in range(2)]for row in range(10)]for i in range(3)]#마름모 좌표 저장
y = [54,94,154]

num = '75'
cnt1 , cnt2 , cnt3 = 0 , 0 , 0


def CRT_POLY(x,y,line,color):#마름모 생성 함수(x위치,y위치,크기)
    canvas.create_polygon(x,y,x-(line/2),y+(line/2),x,y+line,x+(line/2),y+(line/2),fill=color)

def Change_Color0():#버튼 입력시 색 변경

    global li,cnt1,num

    booli , num = Rd_T_F(0)
    Probability_label(str(num))
    
    if booli:
        CRT_POLY(li[0][cnt1][0],li[0][cnt1][1],18,'blue')
    else:
        CRT_POLY(li[0][cnt1][0],li[0][cnt1][1],18,'black')

    cnt1 += 1

def Change_Color1():#버튼 입력시 색 변경

    global li,cnt2,num
    booli , num = Rd_T_F(1)
    Probability_label(str(num))

    if booli:
        CRT_POLY(li[1][cnt2][0],li[1][cnt2][1],18,'blue')
    else:
        CRT_POLY(li[1][cnt2][0],li[1][cnt2][1],18,'black')
    cnt2 += 1

def Change_Color2():#버튼 입력시 색 변경

    global li,cnt3,num
    booli , num = Rd_T_F(2)
    Probability_label(str(num))

    if booli:
        CRT_POLY(li[2][cnt3][0],li[2][cnt3][1],18,'red')
    else:
        CRT_POLY(li[2][cnt3][0],li[2][cnt3][1],18,'black')
        
    cnt3 += 1
    
def Probability_label(num): #레이블 표시
    lb3 = Label(text='성공 확률 ' + num + '%',width=13,anchor=CENTER).place(x=300,y=28)
    lb4 = Label(text='균열 확률 ' + num + '%',width=13,anchor=CENTER).place(x=300,y=125)

    #lb5 = Label(text=0,width=2,anchor=CENTER).place(x=260,y=28)    성공횟수 적으려다가 귀찮아서 포기
    #lb6 = Label(text=0,width=2,anchor=CENTER).place(x=260,y=125)
    

def claer(): #초기화
    global num , cnt1 , cnt2 , cnt3   
    num = '75'
    cnt1 , cnt2 , cnt3 = 0 , 0 , 0
    
    Function_Clear()
    First_Button()
    Probability_label(num)
    
def First_Button():
    for i in range(10):
        CRT_POLY(li[0][i][0],li[0][i][1],18,'gray')
        CRT_POLY(li[1][i][0],li[1][i][1],18,'gray')
        CRT_POLY(li[2][i][0],li[2][i][1],18,'gray')


for i in range(3):
    x = 15
    for j in range(10):
        x += 25
        li[i][j][0] = x
        li[i][j][1] = y[i]

lb1 = Label(text='증가 능력',width=13,anchor=CENTER).place(x=2,y=28)
lb2 = Label(text='감소 능력',width=13,anchor=CENTER).place(x=2,y=125)


Probability_label(num)

btn_clear = Button(root,text='초기화',width=12,command=claer).place(x = 300 , y = 2)

btn1 = Button(root,text='세공',width=12,command=Change_Color0).place(x=300,y=50)
btn2 = Button(root,text='세공',width=12,command=Change_Color1).place(x=300,y=90)
btn3 = Button(root,text='세공',width=12,command=Change_Color2).place(x=300,y=150)

First_Button()
root.mainloop()
