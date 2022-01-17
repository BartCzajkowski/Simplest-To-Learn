from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#Początek aplikacji
root = Tk()
root.title('Kółko i Krzyżyk')
#Stałe
iks = True
licznik = 0
#Funkcje
def koniec_gry():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)

def wygrana():
    global wygrany
    wygrany = False
    if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz X wygrywa!')
        koniec_gry()
    elif b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
        b1.config(bg='green')
        b2.config(bg='green')
        b3.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
        b4.config(bg='green')
        b5.config(bg='green')
        b6.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
        b7.config(bg='green')
        b8.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
        b1.config(bg='green')
        b4.config(bg='green')
        b7.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
        b2.config(bg='green')
        b5.config(bg='green')
        b8.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
        b3.config(bg='green')
        b6.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
        b1.config(bg='green')
        b5.config(bg='green')
        b9.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
        b3.config(bg='green')
        b5.config(bg='green')
        b7.config(bg='green')
        wygrany = True
        messagebox.showinfo('Kółko i krzyżyk', 'Gracz O wygrywa!')
        koniec_gry()
    if licznik == 9 and wygrany is False:
        messagebox.showinfo('Kółko i krzyżyk', 'Remis!')
        koniec_gry()

def b_click(b):
    global iks, licznik
    if b['text'] == '' and iks is True:
        b['text'] = 'X'
        iks = False
        licznik += 1
        wygrana()
    elif b['text'] == '' and iks is False:
        b['text'] = 'O'
        iks = True
        licznik += 1
        wygrana()
    else:
        messagebox.showerror('Kółko i Krzyżyk', 'Pole zajęte!\nWybierz inne')

def restart():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global iks, licznik
    iks = True
    licznik = 0

    #Wnętrze
    b1 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b1) )
    b2 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b2) )
    b3 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b3) )

    b4 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b4) )
    b5 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b5) )
    b6 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b6) )

    b7 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b7) )
    b8 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b8) )
    b9 = Button(root, text='', font=(20), height = 5, width=10, bg='SystemButtonFace', command=lambda: b_click(b9) )

    b10 = Button(root, text='Koniec', font=(30), command=root.quit)

    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

    b10.grid(row=3, column=1)

opcje = Menu(root)
root.config(menu=opcje)
opcje_wybor = Menu(opcje)
opcje.add_cascade(label='Opcje', menu=opcje_wybor)
opcje_wybor.add_command(label='Restart', command=restart)
restart()
#Koniec aplikacji
root.mainloop()
