from tkinter import *
from tkinter import font

root = Tk()
root.geometry('200x250')

inputFont = font.Font(size=36)
userInput = Entry(root, width=3, font=inputFont)
userInput.place(x=55, y=20)

class Convert:
    def __init__(self, cTemp, fTemp):
        self.cTemp = cTemp
        self.fTemp = fTemp
        
    def celcius(self):
        cTemp = (userInput.get() * 9/5) + 32
        return cTemp
    
    def fahrenheit(self):
        fTemp = (userInput.get() - 32) * 5/9
        return fTemp

cBtn = Button(root, text='CELCIUS', fg='#4A4A4A', command=celcius())
cBtn.place(x=20, y=100)

fBtn = Button(root, text='FAHRENHEIT', fg='#4A4A4A', command=fahrenheit())
fBtn.place(x=100, y=100)


root.mainloop()