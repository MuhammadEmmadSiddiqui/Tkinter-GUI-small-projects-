from tkinter import *

gui=Tk()
gui.title('Emmad\'s Calculator')

operator=''
def key(n):
    global operator
    operator=operator+str(n)
    textinput.set(operator)
def calculate():
    global operator
    result=str(eval(operator))
    textinput.set(result)
    
def clear():
    global operator
    operator=''
    textinput.set(operator)


textinput=StringVar()

screen=Entry(gui,bd=10,justify='right',bg='white',fg='black',insertwidth=10,width=40,textvariable=textinput)
screen.grid(row=0,columnspan=4)

btn7=Button(gui,text='7',padx=20,bd=5,command=lambda :key(7))
btn7.grid(row=1,column=0)
btn8=Button(gui,text='8',padx=20,bd=5,command=lambda :key(8))
btn8.grid(row=1,column=1)
btn9=Button(gui,text='9',padx=20,bd=5,command=lambda :key(9))
btn9.grid(row=1,column=2)
multiply=Button(gui,text='*',padx=20,bd=5,command=lambda :key('*'))
multiply.grid(row=1,column=3)
btn6=Button(gui,text='6',padx=20,bd=5,command=lambda :key(6))
btn6.grid(row=2,column=0)
btn5=Button(gui,text='5',padx=20,bd=5,command=lambda :key(5))
btn5.grid(row=2,column=1)
btn4=Button(gui,text='4',padx=20,bd=5,command=lambda :key(4))
btn4.grid(row=2,column=2)
minus=Button(gui,text='-',padx=20,bd=5,command=lambda :key('-'))
minus.grid(row=2,column=3)
btn3=Button(gui,text='3',padx=20,bd=5,command=lambda :key(3))
btn3.grid(row=3,column=0)
btn2=Button(gui,text='2',padx=20,bd=5,command=lambda :key(2))
btn2.grid(row=3,column=1)
btn1=Button(gui,text='1',padx=20,bd=5,command=lambda :key(1))
btn1.grid(row=3,column=2)
divide=Button(gui,text='/',padx=20,bd=5,command=lambda :key('/'))
divide.grid(row=3,column=3)
btn0=Button(gui,text='0',padx=20,bd=5,command=lambda :key(0))
btn0.grid(row=4,column=0)
clear=Button(gui,text='C',padx=20,bd=5,command=clear)
clear.grid(row=4,column=1)
plus=Button(gui,text='+',padx=20,bd=5,command=lambda :key('+'))
plus.grid(row=4,column=2)
equals=Button(gui,text='=',padx=20,bd=5,command=calculate)
equals.grid(row=4,column=3)
gui.mainloop()

