from tkinter import *
from tkinter.filedialog import *

#메뉴 클릭시 동작을 위한 함수추가
def new_file(): #New_file
    text_area.delete(1.0,END)

def save_file(): #Save
    f=asksaveasfile(mode= "w",defaultextension=".txt",filetypes=[('Text files','.txt')])
    text_save = str(text_area.get(1.0,END))
    f.write(text_save)
    f.close()

def maker():
    help_view=Toplevel(window)
    help_view.geometry("300x50")
    help_view.title("Maker")
    lb = Label(help_view,text="NotePad made by Bugaeng.")
    lb.pack()

#창 크기, 사이징불가, 이름 지정
window = Tk()
window.title("NotePad")
window.geometry("400x400")
window.resizable(False,False)

#메뉴 바 추가
menu=Menu(window)
menu_1=Menu(menu,tearoff=0)
menu_1.add_command(label="New_file",command=new_file)
menu_1.add_command(label="Save",command=save_file)
menu_1.add_separator()
menu_1.add_command(label="Exit",command=window.destroy)
menu.add_cascade(label="File",menu=menu_1)
menu_2=Menu(menu,tearoff=0)
menu_2.add_command(label="Maker",command=maker)
menu.add_cascade(label="Credit",menu=menu_2)

#텍스트 입력창(메모장의 주요기능) 추가
text_area=Text(window)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N+E+S+W)

window.config(menu=menu)
window.mainloop()