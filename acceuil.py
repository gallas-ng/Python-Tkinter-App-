from cProfile import label
from dataclasses import dataclass
from itertools import tee
from logging import root
from pickle import FRAME
from tkinter import font, ttk
from tkinter import *
from tkinter import messagebox
from sqlite3 import Cursor, Row
from numpy import insert

import tkinter as tk
import sqlite3 
import os




class Etudiant:
    
    def __init__(self,root) :
        
        self.root = root
        self.root.title("GESTIONNAIRE D'Etudiants ")
        self.root.geometry("2100x1200")
        self.root.config(bg="black")
        
        #formulaire
        gestion_Etudiant = Frame(self.root,bd=5,relief=GROOVE,bg="#1E3F66")
        gestion_Etudiant.place(x=20,y=20,width=1300,height=300)

        # declaration des variable

        self.matricule =StringVar()
        self.nom = StringVar()
        self.prenom =StringVar()
        self.dateN = StringVar()
        self.Fil = StringVar()
        self.dep = StringVar()
        self.moy = StringVar()
        self.anne = StringVar()

        self.rec_par = StringVar()
        self.rec = StringVar()


        gestion_title = tk.Label(gestion_Etudiant,text="=======================Gestion des Etudiants======================",font=("Javanese Text",25,"bold"),bg="#87CEEB")
        gestion_title.place(x=60,y=5)

        # chamsp id avec lecture
        #id_matricule = tk.Label(gestion_Etudiant,text="ID_ETUDIANT",font=("Comic Sans MS",20,"bold"),bg="#87CEEB",borderwidth = 6,relief="ridge")
        #id_matricule.place(x=30,y=100)

        #champ_id_matricule = tk.Entry(gestion_Etudiant,textvariable=self.matricule,font=("Comic Sans MS",20),bg="lightgrey")
        #champ_id_matricule.place(x=220,y=100)

        # marticule etudiant
        matricule = tk.Label(gestion_Etudiant,text="Numero ",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        matricule.place(x=30,y=100)

        champ_matricule = tk.Entry(gestion_Etudiant,textvariable=self.matricule,font=("Comic Sans MS",17),bg="lightgrey")
        champ_matricule.place(x=170,y=100,width=160)

        ## nom etudiant
        nom = tk.Label(gestion_Etudiant,text="Nom",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        nom.place(x=350,y=100)

        champ_nom = tk.Entry(gestion_Etudiant,textvariable=self.nom,font=("Comic Sans MS",17),bg="lightgrey")
        champ_nom.place(x=440,y=100,width=160)

        ## prenom etudiant
        prenom = tk.Label(gestion_Etudiant,text="Prenom",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        prenom.place(x=620,y=100)

        champ_prenom = tk.Entry(gestion_Etudiant,textvariable=self.prenom,font=("Comic Sans MS",17),bg="lightgrey")
        champ_prenom.place(x=760,y=100,width=160)

        ## dateNaissance etudiant
        dateN = tk.Label(gestion_Etudiant,text="Birth/Date",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        dateN.place(x=950,y=100)

        champ_dateN= tk.Entry(gestion_Etudiant,textvariable=self.dateN,font=("Comic Sans MS",17),bg="lightgrey")
        champ_dateN.place(x=1110,y=100,width=160)

        ## filiere etudiant
        filiere = tk.Label(gestion_Etudiant,text="Filiere",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        filiere.place(x=30,y=160)

        champ_filiere = ttk.Combobox(gestion_Etudiant,textvariable=self.Fil,font=("Comic Sans MS",17),state="readonly")
        champ_filiere["values"]= ("GL","IAGE","GDA","RIS","CS","II","DS")
        champ_filiere.place(x=170,y=160,width=160)
        champ_filiere.current(0)

        ## departement etudiant
        dep = tk.Label(gestion_Etudiant,text="Dprt",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        dep.place(x=350,y=150)

        champ_dep = ttk.Combobox(gestion_Etudiant,textvariable=self.dep,font=("Comic Sans MS",17,"bold"),state="readonly")
        champ_dep["values"]= ("Genie","Reseaux","Gestion","Mecanique","Eltronique")
        champ_dep.place(x=440,y=160,width=160)
        champ_dep.current(0)

        ## anne inscription etudiant
        filiere = tk.Label(gestion_Etudiant,text="An Iscpt",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        filiere.place(x=620,y=160)

        champ_filiere = tk.Entry(gestion_Etudiant,textvariable=self.anne,font=("Comic Sans MS",17,"bold"),bg="lightgrey")
        champ_filiere.place(x=760,y=160,width=160)

        ## moyenne etudiant
        moy = tk.Label(gestion_Etudiant,text="Moyenne",font=("Comic Sans MS",17,"bold"),bg="white",borderwidth = 6,relief="ridge")
        moy.place(x=950,y=150)

        champ_moy = tk.Entry(gestion_Etudiant,textvariable=self.moy,font=("Comic Sans MS",17,"bold"),bg="lightgrey")
        champ_moy.place(x=1110,y=160,width=160)
        
        # bouton ajouter
        buttonAjout = tk.Button(gestion_Etudiant,command=self.ajou_etudiant,text="Ajouter",font=("Comic Sans MS",15),bd=8,relief=GROOVE,bg="#52BE80")
        buttonAjout.place(x=510,y=220,width=200)

        # bouton modifie
        buttonModifier = tk.Button(gestion_Etudiant,command=self.modifier,text="Modifier",font=("Comic Sans MS",15),bd=8,relief=GROOVE,bg="#E67E22")
        buttonModifier.place(x=320,y=220)

        # bouton supprimer
        buttonSup = tk.Button(gestion_Etudiant,command=self.supprimer,text="Supprimer",font=("Comic Sans MS",15),bd=8,relief=GROOVE,bg="#C0392B")
        buttonSup.place(x=820,y=220)

        #Affichage

        detail_frame = Frame(self.root,bd=5,relief=GROOVE,bg="#87CEEB")
        detail_frame.place(x=70,y=335,width=1200,height=350)

        detail_frame1 = Frame(self.root,bd=5,relief=GROOVE,bg="#1E3F66")
        detail_frame1.place(x=20,y=335,width=40,height=350)

        detail_frame2 = Frame(self.root,bd=5,relief=GROOVE,bg="#1E3F66")
        detail_frame2.place(x=1280,y=335,width=40,height=350)

        resultat = tk.Label(detail_frame,text="-------------------------------:)>)Liste Des Etudiants(<(:------------------------------",font=("Javanese Text",25),bg="#87CEEB")
        resultat.place(x=20,y=15)

        buttonAffTou  =tk.Button(detail_frame,command=self.affiche,text="Raffraichir",font=("Javanese Text",15,"bold"),bd=8,relief=GROOVE,bg="#1E3F66")
        buttonAffTou.place(x=910,y=100,height=45)

        buttonVider  =tk.Button(detail_frame,command=self.reni,text="Vider Champs",font=("Javanese Text",15,"bold"),bd=8,relief=GROOVE,bg="#979A9A")
        buttonVider.place(x=900,y=160,height=45)

        buttonQ  =tk.Button(detail_frame,command=self.quit,text="Fermer APP",font=("Javanese Text",15,"bold"),bd=8,relief=GROOVE,bg="#1E3F66")
        buttonQ.place(x=910,y=220,height=45)

        ## affichet tout les elements
        
        tout_fram = Frame(detail_frame,bd=5,relief=GROOVE,bg="#87CEEB")
        tout_fram.place(x=10,y=100,width=880,height=200)

        scoll_x = Scrollbar(tout_fram,orient=HORIZONTAL)
        scoll_y = Scrollbar(tout_fram,orient=VERTICAL)

        self.tabl_resul=ttk.Treeview(tout_fram,columns=("numeroCarte","nom","prenom","anneNais","filiere","departement","anneeIns","moyenne"),xscrollcommand=scoll_x.set,yscrollcommand=scoll_y.set)
        scoll_x.pack(side=BOTTOM,fill=X)
        scoll_y.pack(side=RIGHT,fill=Y)
        #self.tabl_resul.heading("id",text="ID")
        self.tabl_resul.heading("numeroCarte",text="Matricule")
        self.tabl_resul.heading("nom",text="NOM")
        self.tabl_resul.heading("prenom",text="PRENOM")
        self.tabl_resul.heading("anneNais",text="DATE NAIS")
        self.tabl_resul.heading("filiere",text="FILIERE")
        self.tabl_resul.heading("departement",text="DEPARTEMENT")
        self.tabl_resul.heading("anneeIns",text="ANNE INS")
        self.tabl_resul.heading("moyenne",text="MOYENNE")

        self.tabl_resul["show"]="headings"

        #self.tabl_resul.column("id",width=100)
        self.tabl_resul.column("numeroCarte",width=100)
        self.tabl_resul.column("nom",width=120)
        self.tabl_resul.column("prenom",width=120)
        self.tabl_resul.column("anneNais",width=100)
        self.tabl_resul.column("filiere",width=120)
        self.tabl_resul.column("departement",width=120)
        self.tabl_resul.column("anneeIns",width=100)
        self.tabl_resul.column("moyenne",width=100)

        self.tabl_resul.pack()

        self.tabl_resul.bind("<ButtonRelease-1>",self.information)
        self.affiche()
    def quit(self):
        self.root.destroy()
    
    def ajou_etudiant(self):
        
        if self.nom.get() == "" or self.matricule.get()=="" or self.anne.get()=="" or self.dateN.get()=="" or self.dep.get()=="" or self.Fil.get()=="" or self.moy.get()=="" or self.prenom.get()=="":
            messagebox.showerror("erreur","champs manquantes",parent = self.root)
        else:
            con = sqlite3.connect("etudiant1.db")
            cur = con.cursor()
            cur.execute("insert into Etudiant(numeroCarte,nom,prenom,anneNais,filiere,departement,anneeIns,moyenne) values(?,?,?,?,?,?,?,?)",(self.matricule.get(),self.nom.get(),self.prenom.get(),self.dateN.get(),self.Fil.get(),self.dep.get(),self.anne.get(),self.moy.get()))
            con.commit()
            self.affiche()
            self.reni()
            con.close()
            
    def affiche(self):
        con = sqlite3.connect("etudiant1.db")
        cur = con.cursor()
        cur.execute("select * from Etudiant")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert("",END,values=row)
        con.commit()
        self.reni()
        con.close()
    def reni(self):
        self.matricule.set("")
        self.nom.set("")
        self.prenom.set("")
        self.anne.set("")
        self.dateN.set("")
        self.Fil.set("")
        self.dep.set("")
        self.moy.set("")

    def information(self,ev):
        cursors_row = self.tabl_resul.focus()
        contents = self.tabl_resul.item(cursors_row)
        row = contents["values"]
        self.matricule.set(row[0])
        self.nom.set(row[1])
        self.prenom.set(row[2])
        self.dateN.set(row[3])
        self.Fil.set(row[4])  
        self.dep.set(row[5])
        self.anne.set(row[6]) 
        self.moy.set(row[7])

    def modifier(self):
        con = sqlite3.connect("etudiant1.db")
        cur = con.cursor()
        sql ="update Etudiant set nom = ?,prenom = ?,anneNais = ?,filiere = ?,departement =?,anneeIns =?,moyenne =? where numeroCarte=? "
        data = (self.nom.get(),self.prenom.get(),self.dateN.get(),self.Fil.get(),self.dep.get(),self.anne.get(),int(self.moy.get()),int(self.matricule.get()))
        cur.execute(sql,data)
        con.commit()
        self.affiche()
        self.reni()
        con.close()

    def supprimer(self):
        con = sqlite3.connect("etudiant1.db")
        cur = con.cursor()
        x = (self.matricule.get())
        print(x)
        sql = """delete from Etudiant where numeroCarte= ?"""
        id = int(x)
        cur.execute(sql, (id,))
        con.commit()  
        self.reni()
        self.affiche()
        con.close()
    def recherche_info(self):
        con = sqlite3.connect("etudiant1.db")
        cur = con.cursor()
        cur.execute("select * Etudiant where "+str(self.rec_par.get())+"LIKE'%"+str(self.rec.get())+"%'")
        rows = cur.fetchall()
        if len(rows)!= 0:
            self.tabl_resul.delete(*self.tabl_resul.get_children())
            for row in rows:
                self.tabl_resul.insert('',END,values=row)
        con.commit()
        con.close()
root =tk.Tk()
obj = Etudiant(root)
root.mainloop()