from tkinter import *
from tkinter import messagebox


def clickImage(event):
    messagebox.showinfo('마우스', '토끼에서 마우스가 클릭됐어요~~')


window = Tk()
window.geometry("400x400")

photo = PhotoImage(file="../gif/rabbit.gif")
label1 = Label(window, image=photo)

label1.bind("<Button>", clickImage)

# TODO expand 는 뭐지?
# expand 매개변수는 tkinter의 pack.py() 메서드에서 사용되며,
# 해당 매개변수의 값을 1로 설정하면 위젯이 부모 위젯에 대한 확장(expansion)을 활성화합니다.
# 이것은 주로 위젯이 부모 위젯 내에서 공간을 확장하도록 하는데 사용됩니다.
#
# expand를 1로 설정하는 것은 주로 윈도우 크기가 변경될 때 위젯의 크기를 조절하기 위해 사용됩니다.
# 예를 들어, 윈도우 크기가 확장되면 expand가 활성화된 위젯은 부모 위젯 내에서 더 많은 공간을 차지하게 됩니다.
# 이것은 사용자 인터페이스를 더 다이나믹하게 만들고 윈도우 크기가 조정될 때 위젯의 크기도 조절하려는 경우에 유용합니다.
#
# expand를 0 또는 생략한 경우 위젯은 확장되지 않고 고정 크기를 유지합니다.

label1.pack(expand=1, anchor=CENTER)
window.mainloop()
