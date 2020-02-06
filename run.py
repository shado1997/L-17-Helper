from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
import math
from PIL import Image, ImageTk

root = Tk()
root.resizable(False, False)
root.title('L-17 Helper')
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
w = w//2 # середина экрана
h = h//2
w = w - 200 # смещение от середины
h = h - 200
root.geometry('250x250+{}+{}'.format(w, h))


def stat():
    try:
        bs = BaseStat.get()
        iv = Iv.get()
        ev = Ev.get()
        lvl = Lvl.get()
        char = variable_char.get()
        trn = variable_train.get()
        print(bs, iv, ev, lvl, char, trn)
        if char == 1 and trn == 1:
            ask = messagebox.askyesno('Stat HP', 'Do you want to calculate HP stat?')
            print(ask)
            if ask:
                Res = (float(bs) * 2 + float(iv) + float(ev) / 2) * float(lvl) / 100 + 10 + float(lvl)
                Stat['text'] = "Stat = " + str(round(Res))
                return 1
            else:
                Res = ((float(bs)*2 + float(iv) + float(ev)/2)*float(lvl)/100 + 5)*char*trn
                Stat['text'] = "Stat = " + str(round(Res))
                return 1
        Res = ((float(bs) * 2 + float(iv) + float(ev) / 2) * float(lvl) / 100 + 5) * char * trn
        Stat['text'] = "Stat = " + str(round(Res))
    except ValueError:
        messagebox.showwarning('Warning', 'Please paste data into all fields and don"t try to input text!')


def damage():
    att = float(Attack.get())
    defe = float(Defense.get())
    pow = float(BasePower.get())
    lvl = float(Level.get())
    type = variable_type.get()
    stab = variable_stab.get()
    other = variable_other.get()
    Res = ((2*lvl + 10)/250*att/defe*pow + 2)*type*stab*other
    Min_res = round(Res*0.85)
    Damage['text'] = "Damage: " + str(Min_res) + "-" + str(round(Res))


def get_ss():
    try:
        type_of_ss = {0: "Bug", 1: "Dark", 2: "Dragon", 3: "Electric", 4: "Fight", 5: "Fire", 6: "Air", 7: "Ghost",
                      8: "Grass",
                      9: "Ground", 10: "Ice", 11: "Water", 12: "Poison", 13: "Psyhic", 14: "Rock", 15: "Steel"}
        genokod = Genokod.get()
        get_gens = re.split('[h,a,d,s,sa,sd,.]', genokod)
        div = []
        filtered_genokod = [x for x in get_gens if x]
        for x in filtered_genokod:
            if int(x) % 2 == 0:
                x = 0
                div.append(x)
            else:
                x = 1
                div.append(x)
        hp = int(div[0])
        a = int(div[1])
        d = int(div[2])
        s = int(div[3])
        sa = int(div[4])
        sd = int(div[5])
        total = hp + a * 2 + d * 4 + s * 8 + sa * 16 + sd * 32
        ss = math.floor(total * 15 / 63)
        type = type_of_ss[ss]
        Ss['text'] = "Type of secret power: " + str(type)
    except (IndexError, ValueError):
        messagebox.showwarning('Warning', 'Please input genokod!')


nb = ttk.Notebook(root)
nb.pack(fill='both', expand='yes')

f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
BaseStat_lb = Label(f1, text='Base Stat').place(relx=0.02, rely=0.05)
BaseStat = Entry(f1)
BaseStat.place(relx=0.25, rely=0.05, relwidth=0.2)
Iv_lb = Label(f1, text='IV').place(relx=0.02, rely=0.15)
Iv = Entry(f1)
Iv.place(relx=0.25, rely=0.15, relwidth=0.2)
Ev_lb = Label(f1, text='EV').place(relx=0.02, rely=0.25)
Ev = Entry(f1)
Ev.place(relx=0.25, rely=0.25, relwidth=0.2)
Lvl_lb = Label(f1, text='Level').place(relx=0.02, rely=0.35)
Lvl = Entry(f1)
Lvl.place(relx=0.25, rely=0.35, relwidth=0.2)
Char_lb = Label(f1, text='Character').place(relx=0.5, rely=0.05)
variable_char = DoubleVar()
variable_char.set(1.1)
Char = OptionMenu(f1, variable_char, 0.9, 1, 1.1).place(relx=0.73, rely=0.05, relwidth=0.25)
Train_lb = Label(f1, text='Train').place(relx=0.5, rely=0.25)
variable_train = DoubleVar()
variable_train.set(1)
Train = OptionMenu(f1, variable_train, 1, 1.1, 1.18, 1.25, 1.31, 1.36, 1.4).place(relx=0.73, rely=0.25, relwidth=0.25)
Calculate = Button(f1, text="Calculate", command=stat).place(relx=0.4, rely=0.45, relwidth=0.3, relheight=0.2)
Stat = Label(f1, relief=RIDGE)
Stat.place(relx=0.3, rely=0.7, relwidth=0.5, relheight=0.1)
Label(f1, text='Designed by Vasyl Venhrov', justify=CENTER, relief=RIDGE).place(relx=0.0, rely=0.9, relwidth=1)
nb.add(f1, text='Stat')

Attack_lb = Label(f2, text='Attack').place(relx=0.02, rely=0.05)
Attack = Entry(f2)
Attack.place(relx=0.25, rely=0.05, relwidth=0.2)
Defense_lb = Label(f2, text='Defense').place(relx=0.02, rely=0.15)
Defense = Entry(f2)
Defense.place(relx=0.25, rely=0.15, relwidth=0.2)
Bp_lb = Label(f2, text='Power').place(relx=0.02, rely=0.25)
BasePower = Entry(f2)
BasePower.place(relx=0.25, rely=0.25, relwidth=0.2)
Level_lb = Label(f2, text='Level').place(relx=0.02, rely=0.35)
Level = Entry(f2)
Level.place(relx=0.25, rely=0.35, relwidth=0.2)
Stab_lb = Label(f2, text='Stab').place(relx=0.5, rely=0.05)
variable_stab = DoubleVar()
variable_stab.set(1)
Stab = OptionMenu(f2, variable_stab, 1, 1.5).place(relx=0.73, rely=0.05, relwidth=0.25)
Type_lb = Label(f2, text='Type').place(relx=0.5, rely=0.18)
variable_type = DoubleVar()
variable_type.set(1)
Type = OptionMenu(f2, variable_type, 0.25, 0.5, 1, 1.5, 2, 4).place(relx=0.73, rely=0.18, relwidth=0.25)
Other_lb = Label(f2, text='Other').place(relx=0.5, rely=0.31)
variable_other = DoubleVar()
variable_other.set(1)
Other = OptionMenu(f2, variable_other, 1, 1.1, 1.25).place(relx=0.73, rely=0.31, relwidth=0.25)
Calc = Button(f2, text="Calculate", command=damage).place(relx=0.4, rely=0.45, relwidth=0.3, relheight=0.2)
Damage = Label(f2, relief=RIDGE)
Damage.place(relx=0.3, rely=0.7, relwidth=0.5, relheight=0.1)
Label(f2, text='Designed by Vasyl Venhrov', justify=CENTER, relief=RIDGE).place(relx=0.0, rely=0.9, relwidth=1)
nb.add(f2, text='Damage')
Genokod_lb = Label(f3, text='Genokod').place(relx=0.02, rely=0.05)
Genokod = Entry(f3)
Genokod.place(relx=0.25, rely=0.05, relwidth=0.6)
Calcul = Button(f3, text="Calculate", command=get_ss).place(relx=0.35, rely=0.25, relwidth=0.3, relheight=0.2)
Ss = Label(f3, relief=RIDGE)
Ss.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.3)
Label(f3, text='Designed by Vasyl Venhrov', justify=CENTER, relief=RIDGE).place(relx=0.0, rely=0.9, relwidth=1)
nb.add(f3, text='SS')

root.mainloop()