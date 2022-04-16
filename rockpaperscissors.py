#importing libraries
import random
from tkinter import *

#intialize the window
ws =Tk()
ws.title('Rockpaper')
ws.config(bg='Black')
ws.resizable(0,0)
ws.geometry('400x400')

Label(ws, text="Rock, Paper,Scissors", font='arial 20 bold', bg='seashell2').pack()

#for your choice
user_take=StringVar()
Label(ws, text= 'Choose any one: rock , paper, scissors', ).place(x=20,y=70)
Entry(ws,font='arial 15', textvariable= user_take, bg='antiquewhite2').place(x=90,y=130)

#for computer choice
comp_pick=random.randint(1,3)
if comp_pick == 1:
    comp_pick='rock'
elif comp_pick== 2:
    comp_pick='paper'
else:
    comp_pick='scissors'
result =StringVar()
#function to start game
def play():
    user_pick= user_take.get()
    if user_pick == comp_pick:
        result.set('TIE ,you both select same')
    elif user_pick == 'rock' and comp_pick=='paper':
        result.set('You loose , computer select paper')
    elif user_pick == 'rock' and comp_pick == 'scissors':
        result.set('You win , computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'scissors':
        result.set('You loose , computer select scissors')
    elif user_pick == 'paper' and comp_pick == 'rock':
        result.set('You win , computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'rock':
        result.set('You loose , computer select rock')
    elif user_pick == 'scissors' and comp_pick == 'paper':
        result.set('You loose , computer select paper')
    else:
        result.set('invalid :choose any one -- rock, paper, scissors')
#function to reset
def Reset():
    result.set("")
    user_take.set("")

#define exit
def Exit():
    ws.destroy()

#defining buttons
Entry(ws,font='arial 10 bold', textvariable= result, bg ='antiquewhite2', width=50,).place(x=25,y=250)
Button(ws,font='arial 13 bold', text='PLAY',padx=5,bg='seashell4', command=play).place(x=150,y=190)
Button(ws,font='arial 13 bold', text='RESET',padx=5,bg='seashell4', command=Reset).place(x=70,y=310)
Button(ws,font='arial 13 bold', text='EXIT',padx=5,bg='seashell4', command=Exit).place(x=230,y=310)
ws.mainloop()





