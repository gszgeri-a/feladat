from tkinter import * 
from tkinter import ttk
from ctypes import windll
from PIL import ImageTk,Image,ImageFont,ImageDraw
import requests,json,os,sqlite3



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
loginroot.iconbitmap("logo.ico")
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

sign_button = PhotoImage(file="signbtn.png")

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
    global indulhat,mainroot,felhasznalonev,jelszo
    indulhat = False
    uname = str(username.get())
    pwd = str(password.get())
    if uname == '' or pwd == '':
        emptyFunction(loginroot)
    else:
        conn = sqlite3.connect('database.db') 
        cursor = conn.cursor()
        cursor.execute('SELECT * from users where felhasznalonev="%s" and jelszo="%s"' % (uname, pwd))
        if cursor.fetchone():
            felhasznalonev = uname
            jelszo = pwd
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
            conn = sqlite3.connect('database.db') 
            with conn:
                curs = conn.cursor()
                adat = ("INSERT INTO users (felhasznalonev, jelszo) VALUES (?, ?)")
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
mainroot.iconbitmap("logo.ico")
g = 0
mainroot.overrideredirect(1)

mainroot.after(10, lambda: set_appwindow(mainroot))
def minimizeGUI1():
    global g
    mainroot.state('withdrawn')
    mainroot.overrideredirect(False)
    mainroot.state('iconic')
    g = 1

def frameMapped1(event=None):
    global g
    mainroot.overrideredirect(True)
    if g == 1:
        set_appwindow(mainroot)
        g = 0

mainroot.bind("<Map>", frameMapped1)





custframe_photo = PhotoImage(file="customframe.png")

custom_btn_img = PhotoImage(file="custom_btn.png")

custom_btn_back = PhotoImage(file="custom_btn_back.png")

crypto_frame_img = PhotoImage(file="cryptbg.png")

mainframe_photo = PhotoImage(file='mainfrom.png')

custom_photo = PhotoImage(file="customeimg.png")

inter_photo = PhotoImage(file="interimg.png")

fold_photo = PhotoImage(file="folderimg.png")

logout_photo = PhotoImage(file="logoutimg.png")

shut_photo = PhotoImage(file="shutimg.png")

crypt_photo = PhotoImage(file="cryptoimg.png")

taskbarbg_img = PhotoImage(file="taskbarbg_main.png")

close_photo = PhotoImage(file="close.png")
exit_photo = PhotoImage(file='close_main.png')

min_btn = PhotoImage(file="min_main.png")

query_btn_img = PhotoImage(file="query_btn.png")

name_place = Image.open("name.png")

name_placer = ImageDraw.Draw(name_place)
font_size = 26

text_font = ImageFont.truetype("Inter-Bold.ttf",size=font_size)

name_placer.text((135,0),f"{felhasznalonev.capitalize()}!",("#579033"),font=text_font)

name_place.save("named.png")

named_placed = PhotoImage(file="named.png")

def customize():
    def update():
        update_username = str(custom_username_entry.get())
        update_password = str(custom_pwd_entry.get())
        if update_username == '' or update_password == '':
            pass
        else:
            conn = sqlite3.connect('database.db') 
            cursor = conn.cursor()
            if update_username != felhasznalonev:
                cursor.execute("UPDATE users SET felhasznalonev=? WHERE felhasznalonev=?",(update_username,felhasznalonev))
            if update_password != jelszo:
                cursor.execute("UPDATE users SET jelszo=? WHERE jelszo=?",(update_password,jelszo))
            conn.commit()

            
    def show():
        if custom_pwd_entry.cget("show") == "":
            custom_pwd_entry.configure(show="*")
        else:
            custom_pwd_entry.configure(show="")
    custroot = Toplevel(mainroot)
    custroot.title("Custome")
    app_width = 372
    app_height = 382
    screen_width = custroot.winfo_screenwidth()
    screen_height = custroot.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2 ) - (app_height / 2)
    custroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
    custroot.overrideredirect(1)
    custroot.wm_attributes("-transparentcolor","grey")
    custframe_label = Label(custroot, border=0,bg="grey",image=custframe_photo)
    custframe_label.pack(fill=BOTH,expand=True)
    custom_username_entry = Entry(custroot,justify='center',width=40,border=0,borderwidth=0)
    custom_username_entry.place(x=66,y=120)
    custom_pwd_entry = Entry(custroot,justify='center',show="*",width=40,border=0,borderwidth=0)
    custom_pwd_entry.place(x=66,y=201)
    
    custom_username_entry.insert(0, felhasznalonev)
    custom_pwd_entry.insert(0, jelszo)
    showpwd = Checkbutton(custroot,bg="white",command=show)
    showpwd.place(x=310,y=245)
    edit_btn = Label(custroot,image=custom_btn_img,borderwidth=0)
    edit_btn.place(x=76,y=279)
    back_btn = Label(custroot,image=custom_btn_back,borderwidth=0)
    back_btn.place(x=136,y=334)
    back_btn.bind("<Button>", lambda e: custroot.destroy())
    edit_btn.bind("<Button>",lambda e:update())
    
def ntw_reset():
    try:
        os.system('cmd /c'"ipconfig /release")
        os.system('cmd /c'"ipconfig /renew")
    except:
        pass
    
def makedir():
    try:
        os.mkdir(f"{felhasznalonev} mappája")
    except:
        pass

def shutDown():
    os.system('cmd /c'"shutdown -s")

def logOut():
    os.system('cmd /c'"shutdown -l")

def cryptO():
    def reqCryptApi():
        lib = {
            "HUF" :"Ft",
            "USD" : "$",
            "EUR" : "€",
            "JPY" : "¥",
            "GBP" : "£"
        }
        currecy = str(currecy_drop_down.get())
        crypt_currecy = str(crypt_currecy_drop_down.get())
        if currecy != "" and crypt_currecy != "":
            URL = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={crypt_currecy}&tsyms={currecy}")
            data = URL.text

            findata = json.loads(data)
            current_price.config(text=f"{findata[currecy]} {lib[currecy]}")
        

    
    style= ttk.Style()
    style.theme_use('clam')
    style.configure("TCombobox", fieldbackground= "#333453", background= "#333453",lightcolor="black")

    curr_option_var = StringVar()
    crpy_option_var = StringVar()
    cryptoroot = Toplevel(mainroot)
    cryptoroot.option_add("*TCombobox*Listbox*Background", "#3F4058")
    cryptoroot.option_add("*TCombobox*Listbox*Foreground", "white")
    cryptoroot.title("Custome")
    app_width = 450
    app_height = 450
    screen_width = cryptoroot.winfo_screenwidth()
    screen_height = cryptoroot.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2 ) - (app_height / 2)
    cryptoroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    cryptoroot.overrideredirect(1)
    cryptoroot.wm_attributes("-transparentcolor","grey")
    crypto_frame = Label(cryptoroot, border=0,bg="grey",image=crypto_frame_img)
    crypto_frame.pack(fill=BOTH,expand=True)
    cls_btn = Label(cryptoroot,image=close_photo,bg="#222338")
    cls_btn.place(x=399,y=13)
    currecy_drop_down = ttk.Combobox(cryptoroot, width=6,textvariable=curr_option_var)
    currecy_drop_down.place(x=46,y=285)
    currecy_drop_down['values'] = ('HUF','USD','EUR','JPY','GBP')
    currecy_drop_down.current()

    crypt_currecy_drop_down = ttk.Combobox(cryptoroot, width=6,textvariable=crpy_option_var)
    crypt_currecy_drop_down.place(x=350,y=285)
    crypt_currecy_drop_down['values'] = ('BTC','ETH','USDT','BUSD','DOGE')
    crypt_currecy_drop_down.current(0)
    current_price = Label(cryptoroot,bg="#222338",font=("inter, 18"),foreground="#585DBA")
    current_price.place(x=150,y=280)
        
    query_btn = Label(cryptoroot,image=query_btn_img,border=0,borderwidth=0)
    query_btn.place(x=135,y=350)
    
    query_btn.bind("<Button>",lambda e:reqCryptApi())
    cls_btn.bind("<Button>",lambda e:cryptoroot.destroy())

def close():
    mainroot.destroy()



app_width = 900
app_height = 500
screen_width = mainroot.winfo_screenwidth()
screen_height = mainroot.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2 ) - (app_height / 2)
mainroot.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')



mainframe = Label(mainroot, border=0,bg="grey",image=mainframe_photo)

mainframe.pack(fill=BOTH,expand=True)


taskbarlabel = Label(mainroot, image=taskbarbg_img, bd=0)

taskbarlabel.place(x=777,y=23)



name_place_label = Label(mainroot,image=named_placed,borderwidth=0,border=0)
name_place_label.place(x=115,y=38)


exit_button = Label(mainroot, image=exit_photo,border=0)
exit_button.place(x=828,y=29)

min_label = Label(mainroot, image=min_btn,border=0)
min_label.pack(fill=BOTH,expand=True)
min_label.place(x=782,y=29)

min_label.bind("<Button>",lambda e: minimizeGUI1())


custom_btn = Label(mainroot,image=custom_photo,border=0)
custom_btn.place(x=152,y=119)

network_btn = Label(mainroot,image=inter_photo,border=0)
network_btn.place(x=351,y=119)


fold_btn = Label(mainroot,image=fold_photo,border=0)
fold_btn.place(x=550,y=119)

#második sor

logout_btn = Label(mainroot,image=logout_photo,border=0)
logout_btn.place(x=152,y=270)


shut_btn = Label(mainroot,image=shut_photo,border=0)
shut_btn.place(x=351,y=270)

crypt_btn = Label(mainroot,image=crypt_photo,border=0)
crypt_btn.place(x=550,y=270)

exit_button.bind("<Button>",lambda e:close())


custom_btn.bind("<Button>",lambda fd: customize())

network_btn.bind("<Button>",lambda fd:ntw_reset())

fold_btn.bind("<Button>",lambda fd:makedir())

logout_btn.bind("<Button>",lambda fd:logOut())

shut_btn.bind("<Button>",lambda fd:shutDown())

crypt_btn.bind("<Button>",lambda fd:cryptO())

try:
    if indulhat:

        mainroot.mainloop()
except:
    pass
