#importation des modules
from tkinter import*
from colorama import Fore
import time


#création de la fenêtre
fen = Tk() 

# titre de la fenêtre
fen.title("Pong Game created by Nam Nguyen")






#fonction pour le déplacement de la balle
def deplacement():
  
  global dx, dy, flag, compteur1, compteur2, balle, mode
  
  
  #rebond de la balle contre les murs
  if interface.coords(balle)[3] > 440 or interface.coords(balle)[1] < 10:
    dy=-1*dy
  
  #augmentation du score du joueur 1
  if interface.coords(balle)[2] > 600:
    compteur1 += 1
    var_score1.set(compteur1)
    score1=Label(fen, textvariable=var_score1, font=("Modern",32), bg=couleur)
    score1.place(x=260, y=30)
    if compteur1<10:
      interface.coords(balle, 285, 215, 305, 235)
    elif compteur1>=10:
      flag=0
      fin1 = Label(fen, text= "JOUEUR 1 a gagné", font=("Minecraft", 25, "bold","italic"))
      fin1.pack()
      fin1.place(x=230, y=200)  
      fin1.after(5000, fin1.destroy)
      
      
  #augmentation du score du joueur 2
  if interface.coords(balle)[0] < 0:
    compteur2 += 1
    var_score2.set(compteur2)
    score2=Label(fen, textvariable=var_score2, font=("Modern",32), bg=couleur)
    score2.place(x=500, y=30)
    if compteur2<10:
      interface.coords(balle, 285, 215, 305, 235)
    elif compteur2>=10:
      flag=0
      fin2 = Label(fen, text= "JOUEUR 2 a gagné", font=("Minecraft", 25, "bold","italic"))
      fin2.place(x=230, y=200)  
      fin2.after(5000, fin2.destroy)
  
  #Test de la collision de la balle avec la joueur1 
  if interface.coords(balle)[0]<interface.coords(joueur1)[2] and interface.coords(balle)[3]>interface.coords(joueur1)[1] and  interface.coords(balle)[1]<interface.coords(joueur1)[3]:
    dx=-1*dx
  
    
  #collision avec le côté haut de la joueur1
  if interface.coords(balle)[0]<interface.coords(joueur1)[2] and   interface.coords(balle)[1]<interface.coords(joueur1)[1] and interface.coords(balle)[3]<interface.coords(joueur1)[3] and interface.coords(balle)[3]>interface.coords(joueur1)[1] and  interface.coords(balle)[1]<interface.coords(joueur1)[3]:
    dy=-1*dy
  
  #collision avec le côté bas de la joueur1  
  if interface.coords(balle)[0]<interface.coords(joueur1)[2] and interface.coords(balle)[1]>interface.coords(joueur1)[1] and interface.coords(balle)[3]>interface.coords(joueur1)[3] and interface.coords(balle)[3]>interface.coords(joueur1)[1] and  interface.coords(balle)[1]<interface.coords(joueur1)[3]:
    dy=-1*dy
  
  
  #collision de la balle avec la joueur2 
  if interface.coords(balle)[2]>interface.coords(joueur2)[0] and interface.coords(balle)[3]>interface.coords(joueur2)[1] and  interface.coords(balle)[1]<interface.coords(joueur2)[3]:
    dx=-1*dx

  #collision avec le côté haut de la joueur2
  if interface.coords(balle)[2]>interface.coords(joueur2)[0] and   interface.coords(balle)[1]<interface.coords(joueur2)[1] and interface.coords(balle)[3]<interface.coords(joueur2)[3] and interface.coords(balle)[3]>interface.coords(joueur2)[1] and  interface.coords(balle)[1]<interface.coords(joueur2)[3]:
    dy=-1*dy
  
  #collision avec le côté bas de la joueur2 
  if interface.coords(balle)[2]>interface.coords(joueur2)[0] and interface.coords(balle)[1]>interface.coords(joueur2)[1] and interface.coords(balle)[3]>interface.coords(joueur2)[3] and interface.coords(balle)[3]>interface.coords(joueur2)[1] and  interface.coords(balle)[1]<interface.coords(joueur2)[3]:
    dy=-1*dy
  
  
  if flag>0:
    
    #On déplace la balle 
    interface.move(balle,dx,dy)
   
    #On repete cette fonction
    fen.after(20,deplacement)

  #Déplacements de l'rdinateur si l'utilisateur choisit le mode "1 joueur"
  if mode == 1:
    if interface.coords(balle)[1] < interface.coords(joueur2)[3] and abs(interface.coords(joueur2)[1] - interface.coords(balle)[1] > 55):
      haut_bot()

    elif interface.coords(joueur2)[1] < interface.coords(balle)[3] and abs( interface.coords(balle)[3] - interface.coords(joueur2)[3] > 55):
      bas_bot()

      
    
#fonction pour démarrer le jeu
def démarrer():
  global flag, mode
  if flag == 0:
    flag=1
    time.sleep(1)
    deplacement()
   

# fonction pour mettre pause   
def pause():
  global flag 
  flag=0
  

#fonction pour redémarrer le jeu
def relancer():
  global balle, joueur1, joueur2, compteur1, compteur2, flag
  flag=0
  interface.coords(balle, 285, 215, 305, 235)
  interface.coords(joueur1, 22, 180, 48, 270 )
  interface.coords(joueur2, 552, 180, 578, 270)
  var_score1.set(0), var_score2.set(0)
  compteur1 = "0"
  compteur2 = "0"
  
# fonction pour le déplacement du joueur1 vers le haut
def haut_joueur1(event):
  global flag
  if flag==1:
    if (interface.coords(joueur1)[1]>30):
      interface.move(joueur1, 0,-30)
    else:
      interface.move(joueur1, 0, 0)
  
# fonction pour le déplacement du joueur1 vers le bas 
def bas_joueur1(event):
  global flag
  if flag==1:
    if (interface.coords(joueur1)[3]<410):
      interface.move(joueur1, 0, 30)
    else:
      interface.move(joueur1, 0, 0)
  
# fonction pour le déplacement du joueur2 vers le haut
def haut_joueur2(event):
  global flag
  if flag==1:
    if (interface.coords(joueur2)[1]>30):
      interface.move(joueur2, 0,-30)
    else:
      interface.move(joueur2, 0, 0)

# fonction pour le déplacement du joueur2 vers le bas 
def bas_joueur2(event):
  global flag
  if flag==1:
    if (interface.coords(joueur2)[3]<410):
      interface.move(joueur2, 0, 30)
    else:
      interface.move(joueur2, 0, 0)
  
#fonction pour le déplacement de l'ordinateur vers le haut
def haut_bot():
  global flag
  if flag==1:
    if (interface.coords(joueur2)[1]>30):
      interface.move(joueur2, 0,-30)
    else:
      interface.move(joueur2, 0, 0)

#fonction pour le déplacement de l'ordinateur vers le bas
def bas_bot():
  global flag
  if flag==1:
    if (interface.coords(joueur2)[3]<410):
      interface.move(joueur2, 0, 30)
    else:
      interface.move(joueur2, 0, 0)

#fonction pour le mode Pong 1 joueur
def solo():
  global mode
  mode = 1
  print(Fore.RED + "Vous avez changé de mode de jeu !!!\n" + Fore.BLUE + "Tentez de battre l'ordinateur !!!\n" + Fore.RESET + "Utilisez les touches " + Fore.BLUE + "w" + Fore.RESET + " et " + Fore.BLUE + "s" + Fore.RESET + " pour se déplacer")


#fonction pour le mode Pong 2 joueurs
def multi():
  global mode
  mode = 2
  print(Fore.RED+ "Vous avez changé de mode de jeu !!!\n" + Fore.RESET + "Pour le " + Fore.BLUE + "joueur 1 " + Fore.RESET + ", utilisez les touches " + Fore.BLUE + "w" + Fore.RESET + " et " + Fore.BLUE + "s" + Fore.RESET + " pour se déplacer\nPour le " + Fore.BLUE + "joueur 2" + Fore.RESET + ", utilisez les touches " + Fore.BLUE + "↑ " + Fore.RESET + " et " + Fore.BLUE + "↓" + Fore.RESET + " pour se déplacer")


#fonction pour changer la couleur du terrain et la vitesse de la balle
def paramètres():
  
  def mode():
    menu.destroy()
    choix_mode = Toplevel(width=195, height=451) 
    choix_mode.title(" Modes ")
    texte_mode=Label(choix_mode, text="Choisissez le mode de jeu", font=("Modern",10), bg = couleur)
    texte_mode.place(x=10, y=10)
    btn_solo = Button(choix_mode, text='Pong (1 Joueur)', command = solo)
    btn_solo.place(x=25, y=50)
    btn_multi = Button(choix_mode, text='Pong (2 Joueurs)', command = multi)
    btn_multi.place(x=25, y=90)
    
  def rouge():
    global couleur
    couleur= "red"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def bleu():
    global couleur
    couleur= "blue"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def cyan():
    global couleur
    couleur= "cyan"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def vert():
    global couleur
    couleur= "green"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def jaune():
    global couleur
    couleur= "yellow"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def orange():
    global couleur
    couleur= "orange"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def rose():
    global couleur
    couleur= "magenta"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)

  def gris():
    global couleur
    couleur= "light grey"
    interface ['bg'] = couleur
    interface.itemconfig(cercle, fill=couleur)
    
  def facile():
    global dx, dy
    dx=3
    dy=3

  def moyen():
    global dx,dy
    dx=4
    dy=4
    
  def difficile():
    global dx, dy
    dx=6
    dy=6

  def hacker():
    global dx, dy
    dx=10
    dy=10

  def couleurs():
    menu.destroy()
    choix_couleurs = Toplevel(width=195, height=451) 
    choix_couleurs.title(" Couleurs ")
    texte_couleur=Label(choix_couleurs, text=" Couleur du Terrain ", font=("Modern",11), bg = couleur)
    texte_couleur.place(x=20, y=10)
    btn_r = Button(choix_couleurs, text= 'Rouge', command = rouge)
    btn_r.place(x=55, y=50)
    btn_b = Button(choix_couleurs, text= 'Bleu', command = bleu)
    btn_b.place(x=55, y=90)
    btn_c = Button(choix_couleurs, text= 'Cyan', command = cyan)
    btn_c.place(x=55, y=130)
    btn_v = Button(choix_couleurs, text= 'Vert', command = vert)
    btn_v.place(x=55, y=170)
    btn_j = Button(choix_couleurs, text= 'Jaune', command = jaune)
    btn_j.place(x=55, y=250)
    btn_o = Button(choix_couleurs, text= 'Orange', command = orange)
    btn_o.place(x=55, y=290)
    btn_m = Button(choix_couleurs, text= 'Rose', command = rose)
    btn_m.place(x=55, y=330)
    btn_g = Button(choix_couleurs, text= 'Gris', command= gris)
    btn_g.place(x=55, y=210)
    
  
  def difficulté():
    menu.destroy()
    choix_difficulté = Toplevel(width=195, height=451) 
    choix_difficulté.title(" Niveaux ")
    texte_difficulté=Label(choix_difficulté, text=" Niveau de Difficulté ", font=("Modern",10), bg = couleur)
    texte_difficulté.place(x=20, y=10)
    btn_facile = Button(choix_difficulté, text='Facile', command = facile)
    btn_facile.place(x=55, y=50)
    btn_moyen = Button(choix_difficulté, text='Moyen', command = moyen)
    btn_moyen.place(x=55, y=90)
    btn_difficile = Button(choix_difficulté, text='Difficile', command= difficile)
    btn_difficile.place(x=55, y=130)
    btn_hacker = Button(choix_difficulté, text="Hacker", command= hacker)
    btn_hacker.place(x=55, y=170)
  
  
  global flag
  flag=0
  menu = Toplevel(width=195, height=451)
  texte = Label(menu , text="Modifiez les Paramètres", font=("Modern",11), bg=couleur)
  texte.place(x=10, y=10)
  btn_couleurs = Button(menu , text = '   Couleur   ', command = couleurs)
  btn_couleurs.place(x=45, y=60)
  btn_difficulté = Button(menu, text='   Difficulté  ', command = difficulté)
  btn_difficulté.place(x=45, y=100)
  btn_mode = Button(menu, text= 'Mode de Jeu', command = mode)
  btn_mode.place(x=45, y=140)

#couleur du terrain par défaut
couleur = "cyan"

#interface du terrain
interface = Canvas(width = 600, height = 450, bg = couleur)
interface.pack()

#création de la balle
balle = interface.create_oval(285, 215, 305, 235, fill="white")

#création de la joueur1
joueur1 = interface.create_rectangle(22, 180, 48, 270, fill="white")
joueur2 = interface.create_rectangle(552, 180, 578, 270, fill="white")

#mode de jeu par défaut
mode= 1
print(Fore.BLUE + "Tentez de battre l'ordinateur !!!\n" + Fore.RESET + "Utilisez les touches " + Fore.BLUE + "w" + Fore.RESET + " et " + Fore.BLUE + "s" + Fore.RESET + " pour se déplacer")

#variable flag
flag = 0

#création du compteur
compteur1 = int()
compteur2 = int()
#StringVar est un print qui va varier
var_score1 = StringVar()
var_score2 = StringVar()

#création des lignes du terrain
cercle= interface.create_oval(240,175,350,275, fill= couleur, width=2) 
interface.create_line(10,10,590,10, width= 2)
interface.create_line(10,10,10,440, width= 2)
interface.create_line(590,10,590,440, width= 2)
interface.create_line(10,440,590,440, width= 2)
milieu = interface.create_line(295,10,295,440, width=2)
interface.create_line(10,130,95,130, width= 2)
interface.create_line(95,130,95,320, width=2)
interface.create_line(10,320,95,320, width= 2)
interface.create_line(505,130,590,130, width=2)
interface.create_line(505,130,505,320, width=2)
interface.create_line(505,320,590,320, width=2)

#création du fond d'écran
fond = Canvas(width=800, height = 0)
fond.pack()

#les cordonnées pour le déplacement sur l'axe des x et y par défaut
dx=3
dy=3

#flèches du haut et du bas: permet de lier les commandes aux touches du clavier
fen.bind("<w>", haut_joueur1)
fen.bind("<s>", bas_joueur1)

fen.bind("<Up>", haut_joueur2)
fen.bind("<Down>", bas_joueur2)

#bouton pour fermer le jeu
btn = Button(fen, text = 'Quitter', command = fen.destroy)
btn.place(x=10, y=400)
#bouton pour démarrer le jeu
btn1 = Button(fen, text = "Démarrer", command = démarrer)
btn1.place(x=10, y=240)
#bouton pour mettre sur pause le jeu
btn2 = Button(fen, text = "Pause", command = pause)
btn2.place(x=10, y=280)
#bouton pour redémarrer le jeu
btn3 = Button(fen, text = "Relancer", command = relancer)
btn3.place(x=10, y=320)

btn4 = Button(fen, text = "Réglages", command = paramètres)
btn4.place(x=10, y=360)


fen.mainloop()


