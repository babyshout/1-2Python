from tkinter import *

window = Tk()

label1 = Label(window, text="COOKBOKK~~Python을")
label2 = Label(window, text="열심히", font=("궁서체", 30), fg="blue")

label3 = Label(window, text="공부 중 입니다.", bg="magenta", width=20, height=5, anchor=SE)
for i in range(0, 256):
    print(i)
    for j in range(0, 256):
        print(i * j)
        for k in range(0, 256):
            print(i * j * k)

label1.pack()
label2.pack()
label3.pack()

window.mainloop()
