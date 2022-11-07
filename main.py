from tkinter import * 
from tkinter import ttk
from ctypes import windll

loginroot = Tk()
loginroot.geometry("800x400")
loginroot.title("Login")
loginroot.overrideredirect(1)
loginroot.wm_attributes("-transparentcolor","grey")


def set_appwindow():
    global hasstyle
    GWL_EXSTYLE=-20
    WS_EX_APPWINDOW=0x00040000
    WS_EX_TOOLWINDOW=0x00000080
    if not hasstyle:
        hwnd = windll.user32.GetParent(loginroot.winfo_id())
        style = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
        style = style & ~WS_EX_TOOLWINDOW
        style = style | WS_EX_APPWINDOW
        res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)
        loginroot.withdraw()
        loginroot.after(10, lambda:loginroot.wm_deiconify())
        hasstyle=True

def move_app(e):
    loginroot.geometry(f'+{e.x_root}+{e.y_root}')

def close():
    loginroot.quit()


def minimize(hide=True):
    hwnd = windll.user32.GetParent(loginroot.winfo_id())
    windll.user32.ShowWindow(hwnd, 0 if hide else 6)









frame_photo = PhotoImage(file='loginform.png')

signframe_photo = PhotoImage(file="signform.png",master=loginroot)


login_btn = PhotoImage(file="loginbutton.png")

sign_btn = PhotoImage(file="regbtn.png")

sep_line = PhotoImage(file="sep.png")

exit_photo = PhotoImage(file='close.png')

min_btn = PhotoImage(file="min.png")





def register():
    def move_sgn(e):
        signroot.geometry(f'+{e.x_root}+{e.y_root}')


    signroot = Toplevel()
    signroot.title("Sign Up")
    signroot.geometry("800x400")
    signroot.overrideredirect(1)
    signroot.wm_attributes("-transparentcolor","grey")
    signframe_label = Label(signroot, border=0,bg="grey",image=signframe_photo)
    signframe_label.pack(fill=BOTH,expand=True)
    signframe_label.bind("<B1-Motion>",move_sgn)
    
    




frame_label = Label(loginroot, border=0,bg="grey",image=frame_photo)

frame_label.pack(fill=BOTH,expand=True)





exit_label = Label(loginroot, image=exit_photo,border=0)

exit_label.place(x=750,y=10)

min_label = Label(loginroot, image=min_btn,border=0)

min_label.place(x=698,y=10)





username = Entry(loginroot,width=40,border=0,borderwidth=0)
username.place(x=502,y=115)


Label(loginroot, image=sep_line,border=0).place(x=502,y=130)
Label(loginroot,text="Username:",bg="white",font=("inter 15")).place(x=395,y=110)



password = Entry(loginroot,width=40,border=0,borderwidth=0)
password.place(x=502,y=179)
Label(loginroot, image=sep_line,border=0).place(x=502,y=195)
Label(loginroot,text="Password:",bg="white",font=("inter 15")).place(x=395,y=173)


#text="Login",font=("Times", "15", "bold"),bg="#5286FF",fg="white",height=1,width=15

login_button = Button(loginroot,image=login_btn,borderwidth=0)

login_button.place(x=513,y=231)



# text="Sign Up",font=("Times", "15", "bold"),bg="#97C1FF",fg="white",height=1,width=10

signup_button = Button(loginroot,image=sign_btn,borderwidth=0,command=register)

signup_button.place(x=548,y=317)



frame_label.bind("<B1-Motion>",move_app)

exit_label.bind("<Button>",lambda e:close() )

min_label.bind("<Button>",minimize)


hasstyle = False


loginroot.update_idletasks()
loginroot.withdraw()
set_appwindow()


loginroot.mainloop()
