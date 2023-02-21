from tkinter import *
from tkinter import font

root = Tk()
root.geometry("200x250")

userInput = Entry(root, width=50)
userInput.place(x=50, y=10)

class Convert:
    def __init__(self, temp):
        self.temp = int(temp)
        
    def celcius(self):
        cTemp = (self.temp * 9/5) + 32
        return cTemp
    
    def fahrenheit(self):
        fTemp = (self.temp - 32) * 5/9
        return fTemp

def create_celc():
    conv = Convert()
    conv.celcius(userInput.get())


def create_fahrenheit():
    conv = Convert(userInput.get())
    conv.fahrenheit()

cBtn = Button(root, text="CELCIUS", fg="#4A4A4A", command=create_celc)
cBtn.place(x=20, y=100)

fBtn = Button(root, text="FAHRENHEIT", fg="#4A4A4A", command=create_fahrenheit)
fBtn.place(x=100, y=100)

root.mainloop()