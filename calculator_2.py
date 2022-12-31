#@by mohammadsam ansaripoor
from tkinter import *
from tkinter import font
from tkinter.font import Font
from typing import Sized
from PIL import Image , ImageTk
import tkinter.font as font
from math import *
window = Tk()
window.geometry('1000x800')
window.title('calculator')
window.resizable(width=False,height=False)
window.configure(bg='black')
input_dir = "data\\"
my_image = ImageTk.PhotoImage(Image.open(input_dir + "calculator-3-2.png"))
my_label = Label(image=my_image)
my_label.grid(row=1, column=1)
#import images
photo_mosavi = ImageTk.PhotoImage(Image.open(input_dir + '=.png'))
photo_0 = ImageTk.PhotoImage(Image.open(input_dir + '0.png'))
photo_1 = ImageTk.PhotoImage(Image.open(input_dir + '1.png'))
photo_2 = ImageTk.PhotoImage(Image.open(input_dir + "2.png"))
photo_3 = ImageTk.PhotoImage(Image.open(input_dir + '3.png'))
photo_4 = ImageTk.PhotoImage(Image.open(input_dir + '4.png'))
photo_5 = ImageTk.PhotoImage(Image.open(input_dir + '5.png'))
photo_6 = ImageTk.PhotoImage(Image.open(input_dir + '6.png'))
photo_7 = ImageTk.PhotoImage(Image.open(input_dir + '7.png'))
photo_8 = ImageTk.PhotoImage(Image.open(input_dir + '8.png'))
photo_9 = ImageTk.PhotoImage(Image.open(input_dir + '9.png'))
photo_mines = ImageTk.PhotoImage(Image.open(input_dir + '-.png'))
photo_plus = ImageTk.PhotoImage(Image.open(input_dir + '+.png'))
photo_taghsim = ImageTk.PhotoImage(Image.open(input_dir + '÷.png'))
photo_zarb = ImageTk.PhotoImage(Image.open(input_dir + 'x.png'))
photo_minesplus = ImageTk.PhotoImage(Image.open(input_dir + '+-.png'))
photo_dot = ImageTk.PhotoImage(Image.open(input_dir + 'dot.png'))
photo_delete = ImageTk.PhotoImage(Image.open(input_dir + 'delete.png'))
photo_threepoint = ImageTk.PhotoImage(Image.open(input_dir + '000 (Custom).png'))
photo_clear = ImageTk.PhotoImage(Image.open(input_dir + 'clear.png'))
photo_darsad = ImageTk.PhotoImage(Image.open(input_dir + 'darsad.png'))
photo_xf = ImageTk.PhotoImage(Image.open(input_dir + 'x!.png'))
photo_jazr = ImageTk.PhotoImage(Image.open(input_dir + 'radikal.png'))
photo_p = ImageTk.PhotoImage(Image.open(input_dir + 'pi.png'))
photo_1xom = ImageTk.PhotoImage(Image.open(input_dir + '1x.png'))
photo_xy = ImageTk.PhotoImage(Image.open(input_dir + 'x^y.png'))
photo_x2 = ImageTk.PhotoImage(Image.open(input_dir + 'x^2.png'))
photo_pnr = ImageTk.PhotoImage(Image.open(input_dir + 'p(n,r).png'))
photo_cnr = ImageTk.PhotoImage(Image.open(input_dir + 'c(n,r).png'))
#sizing 
my_size = 55 
text_font = font.Font(size=my_size)
    
#input field
mm = 1
mn = 1
shomarande = 1
looker = 2
momayez = 'f'
tak = 2
operation = ''
num_1 = StringVar()
num_2 = StringVar()
result_value = StringVar()
show = ''
k = 1
expersion = ''
expersion2 = ''
input_num_1 = Entry(window,textvariable=num_1,background='lightgray',font=text_font)
input_num_1.place(x=25,y=34,width=531,height=110)
result_field = Entry(window,textvariable=result_value,background='lightgray',font=text_font)
result_field.place(x=562,y=33,width=425,height=110)

flag = 0 
list_1 = []
list_2 = []
def set_number(number):
    pio = 'yes'
    pio2 = 'yes'
    global expersion 
    global expersion2 
    global mm 
    global mn 
    global shomarande
    global looker
    global momayez
    global list_1
    global list_2
    if flag == 0 : 
        if len(list_1) == 0 :
            pio = 'no'
        if len(list_1) != 0 :
            pio = 'yes'
        if number == 10:
            for i in range(3):
                expersion  = expersion + str(0)
                list_1.append(str(0))
                num_1.set(expersion)
            expersion = str(expersion)
            num_1.set(expersion)
        elif number == 13 :
            list_1 = []
            pnj = ['1','3','.','1','4','5','1']
            pno = ''
            for pk in range(7):
                pn  = pnj[pk]
                pno = pno + pn
                list_1.append(pn)
            expersion = pno
            num_1.set(expersion)
        elif number == 11:
            k = int(expersion)
            k = k * -1
            list_1.append(str(k))
            expersion = str(k)
            num_1.set(expersion)
        elif number == 15 :
            expersion = expersion + '.'
            list_1.append('.')
            num_1.set(expersion)
        
        elif number == 19 and pio == 'yes' : 
            y = ''
            tool = len(list_1)
            for i in range(len(list_1)-1):
                y += list_1[i]
            del list_1[tool-1]
            expersion = y
            num_1.set(expersion)
        elif number != 19  : 
            expersion = expersion + str(number)
            list_1.append(str(number))
            num_1.set(expersion)
    if flag == 1 : 
        if len(list_2) == 0 :
            pio2 = 'no'
        if len(list_2) != 0 :
            pio2 = 'yes'
        if number == 10:
            for i in range(3):
                expersion2  = expersion2 + str(0)
                list_2.append(str(0))
                num_2.set(expersion2)
            expersion2 = str(expersion2)
            num_2.set(expersion2)
        elif number == 13 :
            list_2 = []
            pnj = ['1','3','.','1','4','5','1']
            pno = ''
            for pk in range(7):
                pn  = pnj[pk]
                pno = pno + pn
                list_2.append(pn)
            expersion2 = pno
            num_2.set(expersion2)
        elif number == 11:
            k = int(expersion2)
            k = k * -1
            expersion2 = str(k)
            list_2.append(str(k))
            num_2.set(expersion2)
        elif number == 15 :
            expersion2 = expersion2 + '.'
            list_2.append('.')
            num_2.set(expersion2)
        
        elif number == 19 and pio2 == 'yes' : 
            y = ''
            tool = len(list_2)
            for i in range(len(list_2)-1):
                y += list_2[i]
            if tool != 0 :
                del list_2[tool-1]
                expersion2 = y
            num_2.set(expersion2)
        elif number != 19:
            expersion2 = expersion2 + str(number)
            list_2.append(str(number))
            num_2.set(expersion2)
        
def factoreil(n):
    k = 1  
    while n>0:
        k = k * n
        n = n - 1
    return k 
def set_operation(op):
    global operation
    global show
    global flag
    global changer
    flag = 1
    operation = op 
    global tak
    if op == 'x!' or op == '√' or op == '1÷x' or op == 'x^2' :
        tak = 0
        if operation == 'x!':
            result = factoreil(float(num_1.get()))
            if result % 1 == 0 :
                result = int(result)
            result_value.set(result)
        if operation == '√':
            result = sqrt(float(num_1.get()))
            if result % 1 == 0 :
                result = int(result)
            result_value.set(result)
        if operation == '1÷x':
            result = 1/(float(num_1.get()))
            if result % 1 == 0 :
                result = int(result)
            result_value.set(result)
        if operation == 'x^2':
            result = (float(num_1.get())) ** 2
            if result % 1 == 0 :
                result = int(result)
            result_value.set(result)
    else:
        show = op
        result_value.set(show)
        global num_2
        num_2 = StringVar()
        input_num_1 = Entry(window,textvariable=num_2,background='lightgray',font=text_font)
        input_num_1.place(x=25,y=34,width=531,height=110)
        result_field = Entry(window,textvariable=result_value,background='lightgray',font=text_font)
        result_field.place(x=562,y=33,width=425,height=110)
def show_result():
    if operation == '%':
        a = (float(num_1.get()))/100
        result = a * (float(num_2.get()))
        if result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == '-':
        result = float(num_1.get()) - float(num_2.get())
        if result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == '+':
        result = float(num_1.get()) + float(num_2.get())
        if result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == '×':
        result = float(num_1.get()) * float(num_2.get())
        if result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == '÷':
        result = float(num_1.get()) / float(num_2.get())
        if result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == '^':
        result = float(num_1.get()) ** float(num_2.get())
        if  result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == 'pnr':
        if float(num_1.get()) < float(num_2.get()):
            result = 'invalid input'
        else:
            a = factoreil(float(num_1.get()))
            b = factoreil(float(num_1.get()) - float(num_2.get()))  
            result = a/b
        if result != 'invalid input' and result % 1 == 0 :
            result = int(result)
        result_value.set(result)
    if operation == 'cnr':
        if float(num_1.get()) < float(num_2.get()):
            result = 'invalid input'
        else :
            a = factoreil(float(num_1.get()))
            b = factoreil((float(num_1.get())) - (float(num_2.get())))
            c = factoreil(float(num_2.get()))
            result = a/(b*c)
        if result != 'invalid input' and result % 1 == 0 :
            result = int(result)
        result_value.set(result)
        
def cleaning():
    global num_1
    global num_2
    global expersion
    global expersion2
    global flag
    global result_value
    global show
    global operation
    global list_1
    global list_2
    list_1 = []
    list_2 = []
    operation = ''
    show = ''
    result_value = StringVar() 
    expersion2 = ''
    expersion = ''
    flag = 0
    num_2 = StringVar()
    num_1 = StringVar()
    input_num_1 = Entry(window,textvariable=num_1,background='lightgray',font=text_font)
    input_num_1.place(x=25,y=34,width=531,height=110)
    result_field = Entry(window,textvariable=result_value,background='lightgray',font=text_font)
    result_field.place(x=562,y=33,width=425,height=110)
#buttons
button_0 = Button(window,image=photo_0,command=lambda:set_number(0))
button_0.place(x=440,y=650)
button_1 = Button(window,image=photo_1,command=lambda:set_number(1))
button_1.place(x=440.5,y=525)
buttun_2 = Button(window,image=photo_2,command=lambda:set_number(2))
buttun_2.place(x=580.5,y=525)
button_3 = Button(window,image=photo_3,command=lambda:set_number(3))
button_3.place(x=715.5,y=525)
button_4 = Button(window,image=photo_4,command=lambda:set_number(4))
button_4.place(x=440,y=400)
button_5 = Button(window,image=photo_5,command=lambda:set_number(5))
button_5.place(x=580,y=400)
button_6 = Button(window,image=photo_6,command=lambda:set_number(6))
button_6.place(x=715,y=400)
button_7 = Button(window,image=photo_7,command=lambda:set_number(7))
button_7.place(x=440,y=275)
button_8 = Button(window,image=photo_8,command=lambda:set_number(8))
button_8.place(x=580,y=275)
button_9 = Button(window,image=photo_9,command=lambda:set_number(9))
button_9.place(x=715,y=275)
button_mines = Button(window,image=photo_mines,command=lambda:set_operation('-'))
button_mines.place(x=860,y=275)
button_plus = Button(window,image=photo_plus,command=lambda:set_operation('+'))
button_plus.place(x=860,y=400)
button_taghsim = Button(window,image=photo_taghsim,command=lambda:set_operation('÷'))
button_taghsim.place(x=860,y=525)
button_zarb = Button(window,image=photo_zarb,command=lambda:set_operation('×'))
button_zarb.place(x=860,y=650)
button_minesplus = Button(window,image=photo_minesplus,command=lambda:set_number(11))
button_minesplus.place(x=715,y=650)
button_dot = Button(window,image=photo_dot,command=lambda:set_number(15))
button_dot.place(x=580,y=650)
button_delete = Button(window,image=photo_delete,command=lambda:set_number(19))
button_delete.place(x=855,y=175)
button_threepoint = Button(window,image=photo_threepoint,command=lambda:set_number(10))
button_threepoint.place(x=579,y=175)
button_clear = Button(window,image=photo_clear,command=lambda : cleaning())
button_clear.place(x=435,y=175)
button_darsad = Button(window,image=photo_darsad,command=lambda:set_operation('%'))
button_darsad.place(x=277,y=175)
button_xf = Button(window,image=photo_xf,command=lambda:set_operation('x!'))
button_xf.place(x=155,y=175)
button_jazr = Button(window,image=photo_jazr,command=lambda:set_operation('√'))
button_jazr.place(x=30,y=175)
button_p = Button(window,image=photo_p,command=lambda:set_number(13))
button_p.place(x=277,y=342)
button_1xom = Button(window,image=photo_1xom,command=lambda:set_operation('1÷x'))
button_1xom.place(x=155,y=342)
button_xy = Button(window,image=photo_xy,command=lambda:set_operation('^'))
button_xy.place(x=30,y=342)
button_x2 = Button(window,image=photo_x2,command=lambda:set_operation('x^2'))
button_x2.place(x=277,y=505)
button_pnr = Button(window,image=photo_pnr,command=lambda:set_operation('pnr'))
button_pnr.place(x=155,y=505)
button_cnr = Button(window,image=photo_cnr,command=lambda:set_operation('cnr'))
button_cnr.place(x=30,y=505)
button_mosavi = Button(window,image=photo_mosavi,command=lambda:show_result())
button_mosavi.place(x=30,y=650)

window.mainloop()
#@mohammadsam ansaripoor