from tkinter import Entry
from tkinter import END
from tkinter import Tk
from tkinter import Button
from tkinter import messagebox

from mainFunction import mainFunction

screen = Tk()
screen.title("CALCULATOR")

e = Entry(screen, width=45, borderwidth=10)
e.grid(row =0, column = 0,columnspan=3, padx = 20, pady =20)
def b_click(number):
    temp = e.get()
    e.delete(0,END)
    e.insert(0,str(temp)+ str(number))
    e.insert

def b_clear():
    e.delete(0,END)
def hola():

    a = e.get()
    e.delete(0,END)
    b = mainFunction(a)
    e.insert(0,str(b))


b1 = Button(screen, text = '1', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda :  b_click(1))
b2 = Button(screen, text = '2', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda :  b_click(2))
b3 = Button(screen, text = '3', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda :  b_click(3))

b4 = Button(screen, text = '4', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(4))
b5 = Button(screen, text = '5', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(5))
b6 = Button(screen, text = '6', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(6))

b7 = Button(screen, text = '7', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(7))
b8 = Button(screen, text = '8', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(8))
b9 = Button(screen, text = '9', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(9))

b0 = Button(screen, text = '0', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(0))
bb1 = Button(screen,text = '(', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click('('))
bb2 = Button(screen,text = ')', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :  b_click(')'))

badd = Button(screen,text = '+  ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda : b_click('+'))
bsub = Button(screen,text = '-   ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command =  lambda :b_click('-'))
bmulti = Button(screen,text = 'X ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda : b_click('*'))
bdivision = Button(screen,text = ' /   ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda : b_click('/'))
bpower = Button(screen,text = '^  ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda : b_click('^'))
bclear = Button(screen,text = 'AC ', font = ('TIMES NEW ROMAN', 22), padx=40,pady=20, bg = 'silver', command = lambda : b_clear())

bans = Button(screen,text = '  ANS  ', font = ('TIMES NEW ROMAN', 22), padx=85,pady=20, bg = 'silver', command = lambda: hola())

b1.grid(row = 3, column = 0)
b2.grid(row = 3, column = 1)
b3.grid(row = 3, column = 2)

b4.grid(row = 2, column = 0)
b5.grid(row = 2, column = 1)
b6.grid(row = 2, column = 2)

b7.grid(row = 1, column = 0)
b8.grid(row = 1, column = 1)
b9.grid(row = 1, column = 2)

b0.grid(row = 4, column = 1)
bb1.grid(row = 4, column = 0)
bb2.grid(row = 4, column = 2)

badd.grid(row = 1, column = 3)
bsub.grid(row = 1, column = 4)
bmulti.grid(row = 2, column = 3)
bdivision.grid(row = 2, column = 4)
bpower.grid(row = 3, column = 3)
bclear.grid(row = 3, column = 4)

bans.grid(row = 4, column = 3, columnspan = 2)





screen.mainloop()