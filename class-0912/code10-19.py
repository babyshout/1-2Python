from tkinter import *
# 패키지 만들때 (tkinter) simpledialog 는 포함이 안되어있어서 따로 임포트 해줘야됨
from tkinter.simpledialog import *

window = Tk()
window.geometry("400x400")

label1 = Label(window, text="입력된 값", anchor=CENTER)
label1.pack()

value = askinteger("확대배수", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

label1.configure(text=str(value))

if __name__ == '__main__':
    window.mainloop()
