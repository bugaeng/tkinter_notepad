from tkinter import *
from tkinter.filedialog import *

#창 크기, 사이징불가, 이름 지정
window = Tk()
window.title("NotePad")
window.geometry("400x400")
window.resizable(False,False)

#메뉴 바 추가
menu=Menu(window)
menu_1=Menu(menu,tearoff=0)
menu_1.add_command(label="New_file")
menu_1.add_command(label="Save")
menu_1.add_separator()
menu_1.add_command(label="Exit",command=window.destroy)
menu.add_cascade(label="File",menu=menu_1)
menu_2=Menu(menu,tearoff=0)
menu_2.add_command(label="Made By Bugaeng")
menu.add_cascade(label="Maker",menu=menu_2)
window.config(menu=menu)

window.mainloop()