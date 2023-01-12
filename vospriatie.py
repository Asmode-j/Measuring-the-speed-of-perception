from tkinter import *
import threading
import time
import random

global t
t=0.300


def main():
    m1=threading.Thread(target=rand)
    m1.start()

def pol():
    global t
    t=float(txt1.get())
   
def rand():
    global x
    x=random.randint(1000,9999)
    print(x)
    time.sleep(3)
    lbl3.configure(text=f'{x}', font=("Arial Bold", 26))
    time.sleep(t)
    lbl3.configure(text='')

def proverka():
    y=int(txt.get())
    if y==x:
        global t
        lbl1.configure(text=f'Верно {t}')
        t=round((t-0.0005), 4)
        print(t)
    else:
        lbl1.configure(text=f'Неверно, ваше время {t}')

window = Tk()
window.title("Программа тренировки")
window.geometry('400x250')


lbl= Label(window, text='Нажмите', font=("Arial Bold", 16) )  
lbl.grid(column=0, row=0)
btn = Button(window, text="Старт", font=("Arial Bold", 14), command=main)  
btn.grid(column=1, row=0)

txt1 = Entry(window,width=10)  
txt1.grid(column=3, row=0)
btn = Button(window, text="Изменить t", font=("Arial Bold", 14), command=pol)  
btn.grid(column=4, row=0)


lbl3= Label(window, text='', font=("Arial Bold", 16) )  
lbl3.grid(column=0, row=2)


txt = Entry(window,width=10)  
txt.grid(column=0, row=3) 
btn = Button(window, text="Проверить", font=("Arial Bold", 14), command=proverka)  
btn.grid(column=1, row=3)

lbl1= Label(window, text='', font=("Arial Bold", 16) )  
lbl1.grid(column=0, row=4)


window.mainloop()
