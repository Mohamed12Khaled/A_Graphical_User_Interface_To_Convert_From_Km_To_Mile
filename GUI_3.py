from tkinter import *


def main():
    window = Tk()
    window.title("Miles to kilometers Converter")
    window.geometry("375x200")

    label1 = Label(window, text="Enter Miles:")
    label1.place(x=50, y=30)

    label2 = Label(window, text="Kilometers:")
    label2.place(x=50, y=100)

    textbox1 = Entry(window, width=12)
    textbox1.place(x=200, y=35)

    label3 = Label(window, text=" ")
    label3.place(x=180, y=100)

    def btn_click():
        kilom = (int(textbox1.get())) * 1.60934
        label3.configure(text=str(kilom) + ' Kilometers')

    btn1 = Button(window, text="Convert", command=btn_click)
    btn1.place(x=90, y=150)
    window.mainloop()


main()
