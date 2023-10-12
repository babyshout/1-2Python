import random

myList = ['하나', '둘', '셋', '넷', '다섯', '여섯']

while (True):
    response = input("주사위 던지기를 계속 하시겠습니까? (yes, no)")
    if response.lower() == 'yes':
        # coin = random.choice(myList)
        coin = myList[random.randint(0, 6)]
        print(coin)
    else:
        break

# exit()
# quit()

from tkinter import *

window = Tk()

button1 = Button(window, text='quit', command=quit)
button2 = Button(window, text='exit', command=exit)

button1.pack()
button2.pack()

window.mainloop()
