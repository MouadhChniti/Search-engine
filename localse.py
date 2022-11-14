from tkinter import * 
from posixpath import split
import glob
from unicodedata import name
if __name__ == "__main__":
    genre = input("what are u lookin for?:")
    


    if genre.upper() == 'MOVIES':
        nom = input("tap the name of "+genre+' please:')
        for file_name in glob.iglob('D:/biblio/movies/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)


    if genre.upper() == 'BOOKS':
        nom = input("tap the name of "+genre+' please:')
        for file_name in glob.iglob('D:/biblio/books/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)


    if genre.upper() == 'NEWSPAPER':
        nom = input("tap the name of "+genre+' please:')
        for file_name in glob.iglob('D:/biblio/newspaper/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)


    if genre.upper() == 'ANIME':
        nom = input("tap the name of "+genre+' please:')
        for file_name in glob.iglob('D:/biblio/newspaper/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)

    if genre.upper() == 'MANGA':
        nom = input("tap the name of "+genre+' please:')
        for file_name in glob.iglob('D:/biblio/newspaper/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)                 

    
    if genre.upper() == 'ALL':
        nom = input("tap the name of item please:")
        for file_name in glob.iglob('D:/biblio/**/*'+nom.lower()+'*.*', recursive=True):
            print(file_name)                
fenetre = Tk()

label = Label(fenetre, text="Bienvenu dans le chercheur de biblio")
label.pack()
bouton1=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton1.pack()
bouton2=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton2.pack()

fenetre.mainloop()






    
    