from time import strftime
from tkinter import Label,Tk

#GUI Code For Window
window = Tk()
window.title("Digital")
window.geometry("200x100")
window.configure(bg = "white")
window.resizable(False,False)

#Label Config In The Window
clock_label = Label(window , bg = "black",fg = "white", font = ("Times",30,'bold'),relief = 'flat')
clock_label.place(x= 20,y=20)


def updating_label():
    current_time = strftime('%H: %M: %S')
    clock_label.configure(text = current_time)
    clock_label.after(80,updating_label)


updating_label()
window.mainloop()