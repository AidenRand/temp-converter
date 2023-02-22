from tkinter import *
from tkinter import font

# Create application window
root = Tk()
root.geometry("380x155")
root.title("Temp converter")
root.config(bg="#EAEAEA")

# Get user input
inputFont = font.Font(size=16)
userInput = Entry(root, width=5, font=inputFont)
userInput.place(x=60, y=10)

# Convert temperature to selected unit
class Convert:
    def __init__(self, temp):
        self.temp = int(temp)

    def celcius(self):
        cTemp = (self.temp * 9 / 5) + 32
        return cTemp

    def fahrenheit(self):
        fTemp = (self.temp - 32) * 5 / 9
        return fTemp

# Create celcius object
def create_celc():
    conv = Convert(userInput.get())
    conv.celcius()
    tempFont = font.Font(size=26)
    outTemp = Label(
        root,
        text=(round(conv.fahrenheit(), 1), "°"),
        width=8,
        height=2,
        font=tempFont,
        bg="#EAEAEA",
    )
    outTemp.place(x=190, y=40)
    userInput.delete(0, END)

# Create fahrenheit object
def create_fahrenheit():
    conv = Convert(userInput.get())
    conv.fahrenheit()
    tempFont = font.Font(size=26)
    outTemp = Label(
        root,
        text=(round(conv.celcius(), 1), "°"),
        width=8,
        height=2,
        font=tempFont,
        bg="#EAEAEA",
    )
    outTemp.place(x=190, y=40)
    userInput.delete(0, END)


# Create fahrenheit and celcius buttons
btnFont = font.Font(size=16)

cBtn = Button(
    root, 
    text="CELCIUS",
    fg="#2D2D2D",
    bg="#FAFAFA",
    font=btnFont,
    command=create_celc
)
cBtn.place(x=39, y=50)

fBtn = Button(
    root,
    text="FAHRENHEIT",
    fg="#2D2D2D",
    bg="#FAFAFA",
    font=btnFont,
    command=create_fahrenheit,
)
fBtn.place(x=20, y=100)

root.mainloop()
