#  -*- coding: utf-8 -*-
# by Ruslan Huseynov

# kod halinda isletdikde asagidakilari install edin
# pip install tkinter
# pip install sqlite3
# pip install mysql.connector
# pip install pymysql
# pip install numpy
# pip install pandas
# pip install matplotlib
# pip install sqlalchemy
import os
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import *
import sqlite3
import mysql.connector
from mysql.connector import Error
import pymysql as my
import numpy as np
import pandas as pd
import tkinter.messagebox as Mesaj

root=tk.Tk()
root.geometry("1217x944+2242+15")
root.minsize(148, 1)
root.maxsize(3844, 1055)
root.title("DATABASE")
root.configure(background="#272727")
root.configure(highlightbackground="#eb0214")
root.configure(highlightbackground="#eb0214")
root.configure(highlightcolor="#646464646464")
root.iconbitmap("icon2.ico")
root.resizable(False,False)



hostname=StringVar()
data=StringVar()
parol=StringVar()
username=StringVar()
cedvel=StringVar()


def Qosulma():

    connection=my.connect(host=Entry1.get(),
                          user=Entry1_2.get(),
                          password=Entry1_3.get(),
                          database=Entry1_4.get())
    cursor=connection.cursor()
    Mesaj.showinfo("Qosulma","Ugurla elaqe yaradildi")
    connection.close()



    
def Siyahi():
    Listbox1.delete(0,END)
    connection=my.connect(host=Entry1.get(),
                          user=Entry1_2.get(),
                          password=Entry1_3.get(),
                          database=Entry1_4.get())
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM"+" "+ Entry1_5.get())

    
    melumat=cursor.fetchall()
    
    for i in melumat:
        Listbox1.insert(END,i)

    connection.close()




def Sil():
    if (Entry2.get() == ""):
        Mesaj.showinfo("Silinəcəklər","Məlumat tapılmadı")
    else:
        connection=my.connect(host=Entry1.get(),
                              user=Entry1_2.get(),
                              password=Entry1_3.get(),
                              database=Entry1_4.get())
        cursor=connection.cursor()
        cursor.execute("DELETE FROM"+" "+Entry1_5.get()+" "+ "WHERE ID ='"+ Entry2.get() +"'")
        cursor.execute("commit")
        Mesaj.showinfo("Silinmə","Məlumat uğurla silindi")
        melumat=cursor.fetchall()
        for i in melumat:
            Listbox1.insert(END,i)
        connection.close()



def Cixis():
    a=Mesaj.askquestion("Çıxış", "Proqramdan çıxmaq istəyirsinizmi?")
    if a == "yes" or a == "Evet":
        root.destroy()





    

    
   
Labelframe1 = tk.LabelFrame(root)
Labelframe1.place(relx=0.008, rely=0.011, relheight=0.374
                , relwidth=0.472)
Labelframe1.configure(relief='groove')
Labelframe1.configure(borderwidth="6")
Labelframe1.configure(font="-family {Segoe UI} -size 10 -weight bold -slant roman -underline 1 -overstrike 0")
Labelframe1.configure(foreground="#5eaeae")
Labelframe1.configure(labelanchor="n")
Labelframe1.configure(text='''MySQL DATABASE QOŞULMA''')
Labelframe1.configure(background="#272727")
Labelframe1.configure(highlightbackground="#d9d9d9")
Labelframe1.configure(highlightcolor="black")



Label1 = tk.Label(Labelframe1)
Label1.place(relx=0.052, rely=0.113, height=26, width=235
                , bordermode='ignore')
Label1.configure(activebackground="#f9f9f9")
Label1.configure(activeforeground="#408080")
Label1.configure(background="#408080")
Label1.configure(disabledforeground="#a3a3a3")
Label1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label1.configure(foreground="#ffffff")
Label1.configure(highlightbackground="#d9d9d9")
Label1.configure(highlightcolor="black")
Label1.configure(text='''HOST NAME''')


Button1 = tk.Button(Labelframe1)
Button1.place(relx=0.052, rely=0.822, height=37, width=517
                , bordermode='ignore')
Button1.configure(activebackground="#ff8000")
Button1.configure(activeforeground="#ff8000")
Button1.configure(background="#008000")
Button1.configure(borderwidth="5")
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font="-family {Segoe UI} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''CONNECT''')
Button1.configure(command=Qosulma)






Label1_1 = tk.Label(Labelframe1)
Label1_1.place(relx=0.052, rely=0.538, height=26, width=235
                , bordermode='ignore')
Label1_1.configure(activebackground="#f9f9f9")
Label1_1.configure(activeforeground="#408080")
Label1_1.configure(background="#408080")
Label1_1.configure(disabledforeground="#a3a3a3")
Label1_1.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label1_1.configure(foreground="#ffffff")
Label1_1.configure(highlightbackground="#d9d9d9")
Label1_1.configure(highlightcolor="black")
Label1_1.configure(text='''DATABASE''')


Label1_2 = tk.Label(Labelframe1)
Label1_2.place(relx=0.052, rely=0.255, height=26, width=233
                , bordermode='ignore')
Label1_2.configure(activebackground="#f9f9f9")
Label1_2.configure(activeforeground="#408080")
Label1_2.configure(background="#408080")
Label1_2.configure(disabledforeground="#a3a3a3")
Label1_2.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label1_2.configure(foreground="#ffffff")
Label1_2.configure(highlightbackground="#d9d9d9")
Label1_2.configure(highlightcolor="black")
Label1_2.configure(text='''USER''')



Label10 = tk.Label(Labelframe1)
Label10.place(relx=0.052, rely=0.397, height=26, width=233
                , bordermode='ignore')
Label10.configure(activebackground="#f9f9f9")
Label10.configure(activeforeground="#408080")
Label10.configure(background="#408080")
Label10.configure(disabledforeground="#a3a3a3")
Label10.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label10.configure(foreground="#ffffff")
Label10.configure(highlightbackground="#d9d9d9")
Label10.configure(highlightcolor="black")
Label10.configure(text='''PASSWORD''')



Entry1 = tk.Entry(Labelframe1)
Entry1.place(relx=0.503, rely=0.119, height=24, relwidth=0.442
                , bordermode='ignore')
Entry1.configure(background="#c9c9c9")
Entry1.configure(borderwidth="4")
Entry1.configure(disabledforeground="#a3a3a3")
Entry1.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry1.configure(foreground="#9a35ff")
Entry1.configure(highlightbackground="#d9d9d9")
Entry1.configure(highlightcolor="black")
Entry1.configure(insertbackground="black")
Entry1.configure(selectbackground="blue")
Entry1.configure(selectforeground="white")
Entry1.configure(textvariable=hostname)





Entry1_2 = tk.Entry(Labelframe1)
Entry1_2.place(relx=0.504, rely=0.255, height=24, relwidth=0.442
                , bordermode='ignore')
Entry1_2.configure(background="#c9c9c9")
Entry1_2.configure(borderwidth="4")
Entry1_2.configure(disabledforeground="#a3a3a3")
Entry1_2.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry1_2.configure(foreground="#9a35ff")
Entry1_2.configure(highlightbackground="#d9d9d9")
Entry1_2.configure(highlightcolor="black")
Entry1_2.configure(insertbackground="black")
Entry1_2.configure(selectbackground="blue")
Entry1_2.configure(selectforeground="white")
Entry1_2.configure(textvariable=username)





Entry1_3 = tk.Entry(Labelframe1)
Entry1_3.place(relx=0.504, rely=0.397, height=24, relwidth=0.442
                , bordermode='ignore')
Entry1_3.configure(background="#c9c9c9")
Entry1_3.configure(borderwidth="4")
Entry1_3.configure(disabledforeground="#a3a3a3")
Entry1_3.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry1_3.configure(foreground="#9a35ff")
Entry1_3.configure(highlightbackground="#d9d9d9")
Entry1_3.configure(highlightcolor="black")
Entry1_3.configure(insertbackground="black")
Entry1_3.configure(selectbackground="blue")
Entry1_3.configure(selectforeground="white")
Entry1_3.configure(textvariable=parol)





Entry1_4 = tk.Entry(Labelframe1)
Entry1_4.place(relx=0.504, rely=0.538, height=24, relwidth=0.442
                , bordermode='ignore')
Entry1_4.configure(background="#c9c9c9")
Entry1_4.configure(borderwidth="4")
Entry1_4.configure(disabledforeground="#a3a3a3")
Entry1_4.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry1_4.configure(foreground="#9a35ff")
Entry1_4.configure(highlightbackground="#d9d9d9")
Entry1_4.configure(highlightcolor="black")
Entry1_4.configure(insertbackground="black")
Entry1_4.configure(selectbackground="blue")
Entry1_4.configure(selectforeground="white")
Entry1_4.configure(textvariable=data)



Label10_3 = tk.Label(Labelframe1)
Label10_3.place(relx=0.052, rely=0.68, height=26, width=233
                , bordermode='ignore')
Label10_3.configure(activebackground="#f9f9f9")
Label10_3.configure(activeforeground="#408080")
Label10_3.configure(background="#408080")
Label10_3.configure(disabledforeground="#a3a3a3")
Label10_3.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label10_3.configure(foreground="#ffffff")
Label10_3.configure(highlightbackground="#d9d9d9")
Label10_3.configure(highlightcolor="black")
Label10_3.configure(text='''CƏDVƏL''')


Entry1_5 = tk.Entry(Labelframe1)
Entry1_5.place(relx=0.504, rely=0.68, height=24, relwidth=0.442
                , bordermode='ignore')
Entry1_5.configure(background="#c9c9c9")
Entry1_5.configure(borderwidth="4")
Entry1_5.configure(disabledforeground="#a3a3a3")
Entry1_5.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry1_5.configure(foreground="#9a35ff")
Entry1_5.configure(highlightbackground="#d9d9d9")
Entry1_5.configure(highlightcolor="black")
Entry1_5.configure(insertbackground="black")
Entry1_5.configure(selectbackground="blue")
Entry1_5.configure(selectforeground="white")
Entry1_5.configure(textvariable=cedvel)




Labelframe2 = tk.LabelFrame(root)
Labelframe2.place(relx=0.501, rely=0.011, relheight=0.374
                , relwidth=0.48)
Labelframe2.configure(relief='groove')
Labelframe2.configure(borderwidth="6")
Labelframe2.configure(font="-family {Segoe UI} -size 11 -weight bold -slant roman -underline 1 -overstrike 0")
Labelframe2.configure(foreground="#5eaeae")
Labelframe2.configure(labelanchor="n")
Labelframe2.configure(text='''Məlumat Silmə''')
Labelframe2.configure(background="#272727")
Labelframe2.configure(highlightbackground="#d9d9d9")
Labelframe2.configure(highlightcolor="black")



Label2 = tk.Label(Labelframe2)
Label2.place(relx=0.067, rely=0.119, height=42, width=514
                , bordermode='ignore')
Label2.configure(activebackground="#f9f9f9")
Label2.configure(activeforeground="black")
Label2.configure(background="#408080")
Label2.configure(disabledforeground="#a3a3a3")
Label2.configure(font="-family {Segoe UI} -size 9 -weight bold -slant roman -underline 0 -overstrike 0")
Label2.configure(foreground="white")
Label2.configure(highlightbackground="#d9d9d9")
Label2.configure(highlightcolor="black")
Label2.configure(text='''ID NÖMRƏ :''')



Entry2 = tk.Entry(Labelframe2)
Entry2.place(relx=0.067, rely=0.295, height=34, relwidth=0.872
                , bordermode='ignore')
Entry2.configure(background="#c9c9c9")
Entry2.configure(borderwidth="7")
Entry2.configure(disabledbackground="#f0f0f0f0f0f0")
Entry2.configure(disabledforeground="#a3a3a3")
Entry2.configure(font="-family {Courier New} -size 10 -weight bold -slant roman -underline 0 -overstrike 0")
Entry2.configure(foreground="#ff0000")
Entry2.configure(highlightbackground="#d9d9d9")
Entry2.configure(highlightcolor="black")
Entry2.configure(insertbackground="black")
Entry2.configure(selectbackground="blue")
Entry2.configure(selectforeground="white")



Button3 = tk.Button(Labelframe2)
Button3.place(relx=0.07, rely=0.442, height=43, width=509
                , bordermode='ignore')
Button3.configure(activebackground="#ff0000")
Button3.configure(activeforeground="white")
Button3.configure(activeforeground="#000000")
Button3.configure(background="#ff0000")
Button3.configure(borderwidth="5")
Button3.configure(disabledforeground="#a3a3a3")
Button3.configure(font="-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
Button3.configure(foreground="#000000")
Button3.configure(highlightbackground="#d9d9d9")
Button3.configure(highlightcolor="black")
Button3.configure(pady="0")
Button3.configure(text='''MƏLUMAT SİL''')
Button3.configure(command=Sil)



Button3_5 = tk.Button(Labelframe2)
Button3_5.place(relx=0.07, rely=0.646, height=43, width=509
                , bordermode='ignore')
Button3_5.configure(activebackground="#00ff00")
Button3_5.configure(activeforeground="#000000")
Button3_5.configure(background="#008000")
Button3_5.configure(borderwidth="5")
Button3_5.configure(disabledforeground="#a3a3a3")
Button3_5.configure(font="-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
Button3_5.configure(foreground="#000000")
Button3_5.configure(highlightbackground="#d9d9d9")
Button3_5.configure(highlightcolor="black")
Button3_5.configure(pady="0")
Button3_5.configure(text='''SİYAHIDAKI MƏLUMATI GÖRÜNTÜLƏ''')
Button3_5.configure(command=Siyahi)




Button3_6 = tk.Button(Labelframe2)
Button3_6.place(relx=0.07, rely=0.824, height=43, width=509
                , bordermode='ignore')
Button3_6.configure(activebackground="#ececec")
Button3_6.configure(activeforeground="#000000")
Button3_6.configure(background="#808080")
Button3_6.configure(borderwidth="6")
Button3_6.configure(disabledforeground="#a3a3a3")
Button3_6.configure(font="-family {Segoe UI Black} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
Button3_6.configure(foreground="#000000")
Button3_6.configure(highlightbackground="#d9d9d9")
Button3_6.configure(highlightcolor="black")
Button3_6.configure(pady="0")
Button3_6.configure(text='''PROQRAMDAN ÇIXIŞ''')
Button3_6.configure(command=Cixis)




Labelframe3 = tk.LabelFrame(root)
Labelframe3.place(relx=0.008, rely=0.403, relheight=0.576
                , relwidth=0.974)
Labelframe3.configure(relief='groove')
Labelframe3.configure(borderwidth="5")
Labelframe3.configure(font="-family {Segoe UI} -size 11 -weight bold -slant roman -underline 1 -overstrike 0")
Labelframe3.configure(foreground="#489191")
Labelframe3.configure(labelanchor="n")
Labelframe3.configure(text='''MƏLUMAT LÖVHƏSİ''')
Labelframe3.configure(background="#272727")
Labelframe3.configure(highlightbackground="#d9d9d9")
Labelframe3.configure(highlightcolor="black")



Listbox1 = tk.Listbox(Labelframe3)
Listbox1.place(relx=0.017, rely=0.055, relheight=0.919
                , relwidth=0.966, bordermode='ignore')
Listbox1.configure(background="#408080")
Listbox1.configure(disabledforeground="#a3a3a3")
Listbox1.configure(font="-family {Courier New} -size 10 -weight bold")
Listbox1.configure(foreground="#000000")

s=Scrollbar(Labelframe3)
Listbox1.config(yscrollcommand=s.set)
s.config(command=Listbox1.yview)

hostname=Entry1.get()
username=Entry1_2.get()
parol=Entry1_3.get()
data=Entry1_4.get()
cedvel=Entry1_5.get()

root.mainloop()























