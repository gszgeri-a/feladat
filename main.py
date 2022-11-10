from tkinter import * 
from tkinter import ttk
from ctypes import windll
import pymysql

GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080


def set_appwindow(fasz):
    hwnd = windll.user32.GetParent(fasz.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
    fasz.wm_withdraw()
    fasz.after(10, lambda: fasz.wm_deiconify())




loginroot = Tk()
aktiv = None
loginroot.title("Login")
z = 0
loginroot.overrideredirect(1)
loginroot.wm_attributes("-transparentcolor","grey")
loginroot.after(10, lambda: set_appwindow(loginroot))


nev = StringVar()
app_width = 800
app_height = 400
screen_width = loginroot.winfo_screenwidth()
screen_height = loginroot.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
loginroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')








def move_app(e):
    loginroot.geometry(f'+{e.x_root}+{e.y_root}')

def close():
    loginroot.destroy()


def minimizeGUI():
    global z
    loginroot.state('withdrawn')
    loginroot.overrideredirect(False)
    loginroot.state('iconic')
    z = 1

def frameMapped(event=None):
    global z
    loginroot.overrideredirect(True)
    if z == 1:
        set_appwindow(loginroot)
        z = 0


frame_photo = PhotoImage(file='loginform.png')


signframe_photo = PhotoImage(file="signform.png",master=loginroot)

login_btn = PhotoImage(file="loginbutton.png")

sign_btn = PhotoImage(file="regbtn.png")

sep_line = PhotoImage(file="sep.png")

exit_photo = PhotoImage(file='close.png')

min_btn = PhotoImage(file="min.png")

sign_button = PhotoImage(file="signbtnteszt.png")

sign_backbtn = PhotoImage(file="signback.png")


taskbarbg_img = PhotoImage(file="taskbarbg.png")




def emptyFunction(cucc):
    emptyroot = Toplevel(cucc)
    emptyroot.geometry("300x67")
    x = cucc.winfo_x()
    y = cucc.winfo_y()
    emptyroot.geometry("+%d+%d" % (x + 250, y + 10))
    emptyroot.overrideredirect(1)
    emptyroot.wm_attributes("-transparentcolor","grey")
    
    
    empty_popup = PhotoImage(file="ureshiba.png")


    invalid_frame_label = Label(emptyroot, border=0,bg="grey",image=empty_popup)

    invalid_frame_label.pack(fill=BOTH,expand=True)

    emptyroot.after(4000,lambda: emptyroot.destroy())

    emptyroot.mainloop()
    



def invalid():
    invaldroot = Toplevel(loginroot)
    invaldroot.geometry("300x67")
    x = loginroot.winfo_x()
    y = loginroot.winfo_y()
    invaldroot.geometry("+%d+%d" % (x + 250, y + 10))
    invaldroot.overrideredirect(1)
    invaldroot.wm_attributes("-transparentcolor","grey")
    
    
    inframe_photo = PhotoImage(file="teszthiba.png")

    invalid_frame_label = Label(invaldroot, border=0,bg="grey",image=inframe_photo)

    invalid_frame_label.pack(fill=BOTH,expand=True)

    invaldroot.after(4000,lambda: invaldroot.destroy())
    try:
        username.delete(0,END)
        password.delete(0,END)
    except:
        pass

    invaldroot.mainloop()
    
    
def login():
    global indulhat,nev_label
    indulhat = False
    uname = str(username.get())
    pwd = str(password.get())
    if uname == '' or pwd == '':
        emptyFunction(loginroot)
    else:
        conn = pymysql.connect(host="sql7.freesqldatabase.com",
                               user="sql7545459",
                               passwd="1lEUskSrmn",
                               database="sql7545459"
                               )
        cursor = conn.cursor()
        cursor.execute('SELECT * from users where felhasznalonev="%s" and jelszo="%s"' % (uname, pwd))
        if cursor.fetchone():
            aktiv = uname
            loginroot.destroy()
            indulhat = True
            print(f"Bejelentkeztél mint: {aktiv}")
        else:
            invalid()

def register():
    
    
    def succ():
        def geciszar():
            sucroot.destroy()
            signroot.destroy()
            loginroot.deiconify()
        sucroot = Toplevel(signroot)
        sucroot.geometry("300x67")
        x = loginroot.winfo_x()
        y = loginroot.winfo_y()
        sucroot.geometry("+%d+%d" % (x + 250, y + 10))
        sucroot.overrideredirect(1)
        sucroot.wm_attributes("-transparentcolor","grey")
        
        
        sign_suc = PhotoImage(file="sgn_suc.png")


        suc_frame_label = Label(sucroot, border=0,bg="grey",image=sign_suc)
        suc_frame_label.pack(fill=BOTH,expand=True)
        sucroot.after(1000,lambda: geciszar())

        try:
            regusername.delete(0,END)
            regpassword.delete(0,END)
            regemail.delete(0,END)
        except:
            pass
        sucroot.mainloop()



    def sign_up():
        felhasz = str(regusername.get())
        jelszo = str(regpassword.get())
        mail = str(regemail.get())
        if felhasz == "" or jelszo == "" or mail == "":
            emptyFunction(signroot)
            
        else:
            conn = pymysql.connect(host="sql7.freesqldatabase.com",
                                user="sql7545459",
                                passwd="1lEUskSrmn",
                                database="sql7545459"
                                )
            with conn:
                curs = conn.cursor()
                adat = ("INSERT INTO users (felhasznalonev, jelszo) VALUES (%s, %s)")
                valtozok = (felhasz, jelszo)
                curs.execute(adat, valtozok)
                conn.commit()
            succ()

                    
                    
                
    def move_sgn(e):
        signroot.geometry(f'+{e.x_root}+{e.y_root}')

    def sgnclose():
        signroot.destroy()
        loginroot.deiconify()
    def sgnback():
        signroot.destroy()
        loginroot.deiconify()
    loginroot.withdraw()
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
    
    signbutton = Button(signroot,image=sign_button,borderwidth=0,command=sign_up)
    signbutton.place(x=513,y=247)
    
    sign_back_button = Button(signroot,image=sign_backbtn,border=0,command=sgnback)
    sign_back_button.place(x=553,y=317)
    
    exit_label.bind("<Button>",lambda e: sgnclose())
    signframe_label.bind("<B1-Motion>",move_sgn)



frame_label = Label(loginroot, border=0,bg="grey",image=frame_photo)

frame_label.pack(fill=BOTH,expand=True)




taskbarlabel = Label(loginroot, image=taskbarbg_img, border=0)

taskbarlabel.place(x=696,y=8)
exit_button = Button(loginroot, image=exit_photo,border=0)

exit_button.place(x=745,y=14)

min_label = Button(loginroot, image=min_btn,border=0,command=minimizeGUI)

min_label.place(x=701,y=14)





username = Entry(loginroot,justify='center',width=40,border=0,borderwidth=0)
username.place(x=502,y=112)


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

exit_button.bind("<Button>",lambda e:close())


loginroot.bind("<Map>", frameMapped)


loginroot.mainloop()









mainroot = Tk()
mainroot.wm_attributes("-transparentcolor","gray")
mainroot.overrideredirect(1)



def close():
    mainroot.destroy()

def move_app(e):
    mainroot.geometry(f'+{e.x_root}+{e.y_root}')


app_width = 900
app_height = 500
screen_width = mainroot.winfo_screenwidth()
screen_height = mainroot.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
mainroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

mainframe_photo = PhotoImage(file='mainfrom.png')



#Label(mainroot,text="Welcome,",font=("inter 26")).place(x=113,y=38)


taskbarbg_img = PhotoImage(file="taskbarbg.png")


exit_photo = PhotoImage(file='close.png')

min_btn = PhotoImage(file="min.png")

mainframe = Label(mainroot, border=0,bg="grey",image=mainframe_photo)

mainframe.pack(fill=BOTH,expand=True)


taskbarlabel = Label(mainroot, image=taskbarbg_img, bd=0)

taskbarlabel.pack(fill=BOTH,expand=True)
taskbarlabel.place(x=777,y=23)



exit_button = Label(mainroot, image=exit_photo,border=0)
exit_button.place(x=828,y=29)

min_label = Label(mainroot, image=min_btn,border=0)
min_label.pack(fill=BOTH,expand=True)
min_label.place(x=782,y=29)





nev_label = Entry(mainroot,font=("inter 26"),fg="#28611F",border=0,borderwidth=0)
nev_label.place(x=244,y=38)
nev_label.insert(0,f"{aktiv}")


exit_button.bind("<Button>",lambda e:close())

mainframe.bind("<B1-Motion>",move_app)

nev_label.pack()


if indulhat:
    mainroot.mainloop()
