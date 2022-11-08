from tkinter import * 
from tkinter import ttk
from ctypes import windll

loginroot = Tk()

loginroot.title("Login")

loginroot.overrideredirect(1)
loginroot.wm_attributes("-transparentcolor","grey")

app_width = 800
app_height = 400
screen_width = loginroot.winfo_screenwidth()
screen_height = loginroot.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
loginroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')


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
    loginroot.destroy()


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

sign_button = PhotoImage(file="signbtn.png")

sign_backbtn = PhotoImage(file="signback.png")

def invalid():
    invaldroot = Toplevel(loginroot)
    invaldroot.overrideredirect(1)
    invaldroot.wm_attributes("-transparentcolor","grey")
    invaldroot.geometry("300x67")
    
    inframe_photo = PhotoImage(file="teszthiba.png")

    invalid_frame_label = Label(invaldroot, border=0,bg="grey",image=inframe_photo)

    invalid_frame_label.pack(fill=BOTH,expand=True)

    invaldroot.after(4000,lambda: invaldroot.destroy())
    invaldroot.mainloop()
    
    
def login():
    uname = str(username.get())
    pwd = str(password.get())
    if uname == '' or pwd == '':
        invalid()

def register():
    
    def move_sgn(e):
        signroot.geometry(f'+{e.x_root}+{e.y_root}')

    def sgnclose():
        signroot.destroy()
    def sgnback():
        signroot.destroy()
    signroot = Toplevel(loginroot)
    signroot.title("Sign Up")
    
    
    app_width = 800
    app_height = 400
    screen_width = signroot.winfo_screenwidth()
    screen_height = signroot.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2 ) - (app_height / 2)
    signroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    signroot.geometry("800x400")
    signroot.overrideredirect(1)
    signroot.wm_attributes("-transparentcolor","grey")
    signframe_label = Label(signroot, border=0,bg="grey",image=signframe_photo)
    signframe_label.pack(fill=BOTH,expand=True)
    exit_label = Label(signroot, image=exit_photo,border=0)
    exit_label.place(x=750,y=10)
    
    regusername = Entry(signroot,width=40,justify='center',border=0,borderwidth=0)
    regusername.place(x=502,y=100)
    Label(signroot, image=sep_line,border=0).place(x=502,y=115)
    Label(signroot,text="Username:",bg="white",font=("inter 15")).place(x=400,y=92)
    
    regemail = Entry(signroot,width=40,justify='center',border=0,borderwidth=0)
    regemail.place(x=502,y=156)
    Label(signroot, image=sep_line,border=0).place(x=502,y=171)
    Label(signroot,text="Email:",bg="white",font=("inter 15")).place(x=446,y=147)
    
    regpassword = Entry(signroot,width=40,justify='center',show="*",border=0,borderwidth=0)
    regpassword.place(x=502,y=207)
    Label(signroot, image=sep_line,border=0).place(x=502,y=227)
    Label(signroot,text="Password:",bg="white",font=("inter 15")).place(x=400,y=203)
    
    signbutton = Button(signroot,image=sign_button,borderwidth=0)
    signbutton.place(x=513,y=247)
    
    sign_back_button = Button(signroot,image=sign_backbtn,border=0,command=sgnback)
    sign_back_button.place(x=553,y=317)
    
    exit_label.bind("<Button>",lambda e: sgnclose())
    signframe_label.bind("<B1-Motion>",move_sgn)



frame_label = Label(loginroot, border=0,bg="grey",image=frame_photo)

frame_label.pack(fill=BOTH,expand=True)





exit_label = Label(loginroot, image=exit_photo,border=0)

exit_label.place(x=750,y=10)

min_label = Label(loginroot, image=min_btn,border=0)

min_label.place(x=698,y=10)





username = Entry(loginroot,justify='center',width=40,border=0,borderwidth=0)
username.place(x=502,y=115)


Label(loginroot, image=sep_line,border=0).place(x=502,y=130)
Label(loginroot,text="Username:",bg="white",font=("inter 15")).place(x=395,y=110)



password = Entry(loginroot,show="*",justify='center',width=40,border=0,borderwidth=0)
password.place(x=502,y=179)


Label(loginroot, image=sep_line,border=0).place(x=502,y=195)
Label(loginroot,text="Password:",bg="white",font=("inter 15")).place(x=395,y=173)


login_button = Button(loginroot,image=login_btn,borderwidth=0, command=login)

login_button.place(x=513,y=231)

signup_button = Button(loginroot,image=sign_btn,borderwidth=0,command=register)

signup_button.place(x=548,y=317)



frame_label.bind("<B1-Motion>",move_app)

exit_label.bind("<Button>",lambda e:close())

min_label.bind("<Button>",minimize)


hasstyle = False


loginroot.update_idletasks()
loginroot.withdraw()
set_appwindow()


loginroot.mainloop()
