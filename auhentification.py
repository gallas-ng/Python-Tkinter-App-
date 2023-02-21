from cProfile import label
import tkinter as tk
from tkinter import *
import sqlite3
from tkinter import messagebox
import os


class login():
    
    def __init__(self,root): 
        self.root = root
        self.root.title("GESTIONNAIRE ETUDIANT")
        self.root.geometry("700x600")
        self.root.config(bg="black")
        self.root.focus_force()


        ## frame du login 
        frame1 = Frame(self.root,bg="white")
        frame1.place(x=50,y=50,width=600,height=500)

        title = tk.Label(frame1,text="======PAGE DE CONNEXION=====",font=("Javanese Text",20,"bold"),bg="white",fg="black",justify="center")
        title.place(x=50,y=30)

        label_User  = tk.Label(frame1,text="USER",font=("Comic Sans MS",20,"bold"),bg="#87CEEB",borderwidth = 6,relief="ridge")
        label_User.place(x=30,y=150,width=150)

        self.label_User = tk.Entry(frame1,font=("Comic Sans MS",20,"bold"),bg="lightgrey",justify="center")
        self.label_User.place(x=250,y=154,width=320)

        label_password = tk.Label(frame1,text="MOT DE PASSE",font=("Comic Sans MS",15,"bold"),bg="#87CEEB",borderwidth = 6,relief="ridge")
        label_password.place(x=30,y=270,width=200)

        self.label_password = tk.Entry(frame1,show="*",font=("Comic Sans MS",20,"bold"),bg="lightgrey",justify="center")
        self.label_password.place(x=250,y=265,width=320)
        
        buttonValider = tk.Button(frame1,text="Connexion",command=self.connexion,cursor="hand2",font=("Comic Sans MS",15,"bold"),bg="lightgrey",fg="black")
        buttonValider.place(x=250,y=350)

        foot = tk.Label(frame1,text="------------======+)+++++++O+O+++++++(+=====-----------",font=("Javanese Text",10,"bold"),bg="white",fg="black",justify="center")
        foot.place(x=90,y=410)
    def connexion(self):
        if self.label_User.get()=="" or self.label_password.get()=="":
            messagebox.showerror("erreur","veillez remplir tout les champs",parent = self.root)
        else:
            try:
                con = sqlite3.connect("etudiant1.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM user WHERE adrres = ? AND password = ?",(self.label_User.get(),self.label_password.get()))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("erreur","Veillez mettre les bon Identifiants", parent = self.root)
                else:
                    #messagebox.showinfo('success',"Bienvenue")
                    self.root.destroy()
                    import acceuil
                    #con.commit()
                    con.close()
                pass
            except Exception as ex:
                messagebox.showerror("erreur",f"Erreur de connexion {str(ex)}",parent = self.root)
                

root = tk.Tk()
obj = login(root)
root.mainloop()