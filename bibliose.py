from tkinter import * 
from posixpath import split
import glob
from unicodedata import name
from xml.dom.expatbuilder import FragmentBuilder

from numpy import place





fenetre = Tk()
fenetre.geometry('250x350')

label = Label(fenetre, text="Bienvenu dans le chercheur de biblio")
label.pack()


label = Label(fenetre, text="Enter le nom de ficher:")
label.pack()

def getEntry():
    res = name.get()
    return res

name = Entry(fenetre)
name.focus_set()
name.pack()


def ctous(name):
    for file_name in glob.iglob('D:/biblio/**/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()


def clivres(name):
    for file_name in glob.iglob('D:/biblio/livres/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()


def cfilms(name):
    for file_name in glob.iglob('D:/biblio/films/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()


def cjournal(name):
    for file_name in glob.iglob('D:/biblio/journal/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()

def canime(name):
    for file_name in glob.iglob('D:/biblio/anime/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()
def cmanga(name):
    for file_name in glob.iglob('D:/biblio/manga/*'+name.lower()+'*.*', recursive=True):
        p1=file_name.find('\\')
        p2=file_name.find('.')
        label = Label(fenetre, text=file_name[p1:p2])
        label.pack()               








bouton1=Button(fenetre,width=10 ,text="Tous", command=lambda:ctous(name.get()))
bouton1.pack()


bouton2=Button(fenetre, width=10,text="livres", command=lambda:clivres(name.get()))
bouton2.pack()


bouton3=Button(fenetre,width=10, text="films", command=lambda:cfilms(name.get()))
bouton3.pack()


bouton4=Button(fenetre,width=10, text="journeaux", command=lambda:cjournal(name.get()))
bouton4.pack()


bouton1=Button(fenetre,width=10, text="manga", command=lambda:cmanga(name.get()))
bouton1.pack()

bouton1=Button(fenetre,width=10, text="anime", command=lambda:canime(name.get()))
bouton1.pack()
bouton2=Button(fenetre,width=15, text="Fermer", command=fenetre.quit).place(x=708 ,y=600)



fenetre.mainloop()

