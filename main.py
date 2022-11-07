import pymysql, os, random, time, pygame, threading, socket, logging
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import filedialog
from tkinter.simpledialog import askstring
icon = "ico.ico"
path = "music"
otl_music= os.listdir(path)
def log(x):
    logging.basicConfig(filename='system.log', level=logging.INFO, format='%(asctime)s: %(levelname)s:%(message)s')
    logging.info((str(x)))
siker = 0
y = "Program elindult"
log(y)
def show():
    if entry2.cget('show') == "":
        entry2.configure(show="*")
    else:
        entry2.configure(show='')

login = Tk()
login.geometry("200x240")
login.title("Login system")
login.eval('tk::PlaceWindow . center')
login.resizable(False, False)
login.iconbitmap(icon)

def loginsys():
    global power,siker,username,uname,meret,pwd,vendeg
    uname = str(entry1.get())
    pwd = str(entry2.get())
    if uname == '' or pwd == '':
        messagebox.showinfo("HIBA", "NINCS KITOLTVE")
        y = "Hibas bejelentkezes!"
        log(y)
    else:
        conn = pymysql.connect(host="sql11.freemysqlhosting.net",
                               user="sql11471564",
                               passwd="HG8HvntxAZ",
                               database="sql11471564"
                               )
        cursor = conn.cursor()

        cursor.execute('SELECT * from users where username="%s" and password="%s"' % (uname, pwd))
        if cursor.fetchone():
            messagebox.showinfo("Login", "Sikeres bejelentkezes")
            login.destroy()
            meret = '235x700'
            siker += 1
            power = 1
            vendeg = uname
            y = f"Bejelentkezett {uname} felhasznalo"
            log(y)
            hostname = socket.gethostname()
            ipszar = socket.gethostbyname(hostname)
            adat = ("INSERT INTO iplogin (username, ip) VALUES (%s, %s)")
            felhasznalo_ip = (uname, ipszar)
            cursor.execute(adat, felhasznalo_ip)
            conn.commit()
            conn.close()
        else:
            messagebox.showinfo("HIBA", "Hibas bejelentkezes")
            y = "Hibas bejelentkezes by:" + str(uname)
            log(y)
def loginsave():
    with open("mentes.txt", "w") as myfile:
        data = myfile.write(uname, pwd)


def register():
    def show2():
        if password_entry.cget('show') == "":
            password_entry.configure(show="*")
        else:
            password_entry.configure(show='')
    def regszar():
        felhasz = str(username_entry.get())
        jelszo = str(password_entry.get())
        conn = pymysql.connect(host="sql11.freemysqlhosting.net",
                               user="sql11471564",
                               passwd="HG8HvntxAZ",
                               database="sql11471564"
                               )
        with conn:
            curs = conn.cursor()
            adat = ("INSERT INTO users (username, password) VALUES (%s, %s)")
            valtozok = (felhasz, jelszo)
            curs.execute(adat, valtozok)
            conn.commit()
        messagebox.showinfo("Regisztráció", "Sikeres regisztráció.")
        y = f"Regisztralt felhasznalonev : {felhasz}"
        log(y)
        register_window.destroy()
    register_window = Toplevel(login)
    register_window.title("Register system by:gszgeri")
    register_window.geometry("300x300")
    register_window.resizable(False, False)

    register_label_username = Label(register_window, text="Felhasznalonev")
    username_entry = Entry(register_window)
    register_label_password = Label(register_window, text="Jelszo")
    password_entry = Entry(register_window,show="*")
    reg_chack = Checkbutton(register_window, text="Jelszo mutatas", command=show2)
    regbutton = Button(register_window, text="Regisztráció", command=regszar)

    register_label_username.pack(anchor=CENTER)
    username_entry.pack(anchor=CENTER)
    register_label_password.pack(anchor=CENTER)
    password_entry.pack(anchor=CENTER)
    reg_chack.pack(anchor=CENTER)
    regbutton.pack(anchor=CENTER)
    register_window.mainloop()

def guest_command():
    y = "Vendeg bejelentkezes"
    log(y)
    global power,siker,meret,vendeg
    power = 0
    siker += 1
    meret = '150x440'
    vendeg = "Vendeg"
    login.destroy()

Label(login, text="Felhasznalonev").pack(anchor=CENTER)
entry1 = Entry(login, bd=3)
entry1.pack(anchor=CENTER)
Label(login, text="Jelszo").pack(anchor=CENTER)
entry2 = Entry(login, show="*", bd=3)
entry2.pack(anchor=CENTER)
Button(login, text="Login", command=loginsys).pack(anchor=CENTER)
check = Checkbutton(login, text="Jelszo mutatas", command=show).pack(anchor=CENTER)
check_button = Checkbutton(login, text="Bejelentkezve marad", command=loginsave).pack(anchor=CENTER)
Button(login, text="Register", command=register).pack(anchor=CENTER)
guest = Button(login, text="Vendeg",command=guest_command).pack(anchor=CENTER, pady=5)

bezaras = 0
def on_closing():
    global root
    global bezaras
    if messagebox.askokcancel("Quit", "Most komolyan bezarod?"):
        panicstop()
        bezaras += 1

login.mainloop()

global meret
root = Tk()
root.title('60 secundum')
root.iconbitmap(icon)
frm = ttk.Frame(root, padding=3)
frm.grid()
root.geometry(meret)
root.resizable(False, False)
menubar = Menu(frm)
root.config(menu=menubar)
def bezar():
    root.destroy()
file_menu = Menu(menubar)
file_menu.add_command(label='TITOK',command=bezar)
menubar.add_cascade(label="Menu",menu=file_menu)

def remotesys():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    local_pc = socket.gethostbyname(socket.gethostname())
    port = 12345
    azonos = uname
    s.bind((local_pc, port))
    threading.Thread(target=s.listen()).start()
    parancsok = ['spoti = Spotify megnyitas', 'spotioff = Spotify leallitas', 'progoff = Program leallitasa']

    while True:
        print("Varakozas a szerverre.")
        status.set("WAITING")
        conn, addr = s.accept()
        print("Sikeres csatlakozas: ", addr)
        print(parancsok)
        status.set("ONLINE")
        y = "Sikeres lekeres: " + str(addr)
        log(y)
        try:
            while True:
                command = askstring("Szerver by:gszg", 'Adja meg a parancsot: ')
                conn.sendall(azonos.encode())
                conn.sendall(command.encode())
                parancs = "Elkuldott parancs: " + str(command)
                log(parancs)
        except:
            print("Lecsatlakozva: ", addr)
            disconnect = "Lecsatlakozva: " + str(addr) + "-rol"
            status.set("OFFLINE")
            log(disconnect)
            break

def panicstop():
    os.system('cmd /c'"taskkill /IM python.exe /f")
    y = "Azonnali Leallítas"
    log(y)

def ablak():
    global vendeg
    global newWindow
    koszones = ['Szia ', 'Szevasz ', 'Szotyi ', 'Csá ']
    koszones_forma = random.randint(0, 3)
    newWindow = Toplevel(frm)
    newWindow.title("Koszones")
    newWindow.geometry("200x200")
    def szivatas():
        newWindow1 = Toplevel(newWindow)
        newWindow1.title("Szivatas")
        newWindow1.geometry("765x956")
        newWindow1.resizable(False, False)
        y = "Új ablak letrehozasa [abukas.jpg]"
        log(y)
    koszones = Label(newWindow, text=koszones[koszones_forma] + vendeg, font="Arial").pack(anchor=CENTER)
    uj_ablak_gomb = Button(newWindow, text="Kilepes", command=szivatas).pack(anchor=CENTER)
    y = "Új ablak letrehozasa [Koszones]"
    log(y)


def leallitas():
    os.system('cmd /c'"shutdown -s")
    y = "Leallítas"
    log(y)


def kijelentkeztets():
    os.system('cmd /c'"shutdown -l")
    y = "Kijelentkezes"
    log(y)


def ujip():
    os.system('cmd /c'"ipconfig /renew")
    y = "Új ip [renew]"
    log(y)


def halozat():
    os.system('cmd /c'"ipconfig /release")
    y = "Halozat lekapcsolasa [release]"
    log(y)


def spoti():
    os.system('cmd /c'"Spotify.exe")
    y = "Alkalmazas megnyitas [Spotify.exe]"
    log(y)



def logclear():
    with open("system.log", 'r+') as f:
        f.truncate(0)
    f.close()


def open_file():
    file = askopenfilename()
    os.system('"%s"' % file)
    y = f"File open {file}"
    log(y)

time1 = ''
clock = Label(frm, font=('times', 15, 'bold'))
clock.grid(column=1, row=0)


def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)


def music():
    global zene
    index = len(otl_music)
    on_the_low = random.randint(0, index)
    zene = otl_music[on_the_low]
    file = 'music/' + zene
    pygame.init()
    pygame.mixer.music.load(file)
    threading.Thread(target=pygame.mixer.music.play()).start()
    messagebox.showinfo("", zene)
    y = f"Play music: {zene}"
    log(y)


def music_stop():
    pygame.mixer.music.stop()
    y = f"Stop music: {zene}"
    log(y)


def hang(x):
    global hanglog
    global sad
    val = hang_csuszka.get()
    val = val * 100
    sad.set(round(val, 0))
    pygame.mixer.music.set_volume(hang_csuszka.get())
    hanglog = hang_csuszka.get() * 100
    y = f"Hang allitva: {round(hanglog, 0)} %"
    log(y)



global power
if power >= 1:
    panic = Button(frm, text="Azonnali leallítas", command=panicstop, fg="White", background="#F72E2E").grid(column=1, row=2, pady=10)

    leallitas_gomb = Button(frm, text="Leállítás", command=leallitas, fg="White", background="#F72E2E").grid(column=1, row=3, pady=10)

    kijelentkezes_gomb = Button(frm, text="Kijelentkezes", command=kijelentkeztets, fg="Red").grid(column=1, row=4,pady=10)

    internet_reset = Button(frm, text="Halozati reset", command=halozat, fg="White", background="#F72E2E").grid(column=1, row=5, pady=10)

    uj_ip_gomb = Button(frm, text="Új Ip letrehozas", command=ujip, fg="Red").grid(column=1, row=7, pady=10)

    log_button = Button(frm, text="Log clear", command=logclear).grid(column=1, row=9, pady=10)

    status = StringVar()
    status.set("OFFLINE")

    csatlakozas = Button(frm, text="CONNECT", command=remotesys).grid(column=0, row=12, pady=10)
    status_bar = Label(frm, textvariable=status, font="Arial", fg="Red").grid(column=0, row=13, pady=5)


spoti_gomb = Button(frm, text="Spotify", command=spoti).grid(column=1, row=12, pady=10)

ablak_gomb = Button(frm, text="Köszönés", command=ablak).grid(column=1, row=11, pady=10)

fileopen = Button(frm, text='File megnyitas', command=open_file).grid(column=1, row=13, pady=10)

hang_disz = LabelFrame(frm, text="Hangero")
hang_disz.grid(column=2, row=17)

sad = IntVar()
scale_var = DoubleVar()
scale_var.set(100)
sad.set(100)
asd = Label(hang_disz,textvariable=sad).pack()


hang_csuszka = ttk.Scale(hang_disz, from_=1, to=0, orient=VERTICAL, command=hang, length=100, variable=scale_var)
hang_csuszka.pack()

gomb = Button(frm, text="OTL", command=music).grid(column=1, row=17, pady=10)
gomb1 = Button(frm, text="OTL vége", command=music_stop).grid(column=1, row=18, pady=10)



def musicplayer():
    def zeneadd():
        global song
        song = filedialog.askopenfilename(initialdir='audio/', title="Válasz egy szamot",filetypes=(("mp3 Files", "*.mp3"),))
        zenek.insert(END, song)

        y = f"{song} zenet hozzadatak"
        log(y)
    def lejatszas():
        song = zenek.get(ACTIVE)
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        y = f"Zene lejatszas a lejatszoba {song}"
        log(y)

    def leallitas():
        pygame.mixer.music.stop()
        y = f"Zene megallitva a lejatszoba {song}"
        log(y)

    def hangallitas(x):
        pygame.mixer.music.set_volume(hang.get())
        hanglog = hang.get() * 100
        y = f"Hang allitva: {round(hanglog, 0)} %"
        log(y)

    zene = Toplevel(frm)
    zene.title("Zenelejatszo")
    zene.geometry("350x300")
    pygame.mixer.init()

    zenek = Listbox(zene, bg="black", fg="white", width=50, selectbackground="grey", selectforeground="black")
    zenek.pack(pady=10)
    hang = ttk.Scale(zene, from_=1, to=0, orient=HORIZONTAL, value=1, command=hangallitas, length=100)
    hang.pack()
    iranyitas = Frame(zene)
    iranyitas.pack()
    lejatszas_gomb = Button(iranyitas, text="Lejatszas", border=3, command=lejatszas)
    megallitas = Button(iranyitas, text="Megallitas", border=3, command=leallitas)
    zene_add = Button(iranyitas, text="Zene hozzadas", border=3, command=zeneadd)
    lejatszas_gomb.grid(column=1, row=2)
    megallitas.grid(column=2, row=2)
    zene_add.grid(column=0, row=2)

music_player = Button(frm, text='Zenelejatszo', command=musicplayer)
music_player.grid(column=1, row=19, pady=10)

tick()

if siker == 1:
    root.mainloop()
y = "Program leallt"
log(y)