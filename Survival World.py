import pygame, time, sys, random
from pygame.locals import *

pygame.init()

#starts the game.
def start():
    print("Darkenders Productions...")
    time.sleep(4)
    print("Presents to you")
    time.sleep(4)
    print("Survival World")
    time.sleep(4)
    print("hello and welcome to Survival World!")
    time.sleep(3)
    username = input("please type in your preffered usrename: ")
    print("Loading...")
    time.sleep(3)
    print("your username is " + username + ".")
    print("Loading...")
    time.sleep(3)
    play = input("do you want to play?: ")
    if play == "yes":
        print("Loading...")
        time.sleep(3)
        print("" + username + " has joined the game...")

#creates the slash function.
def do_slash():
    print("swoosh!")

#lets the player walk
def walk():
    print("walking...")
    stop = input(">")
    if stop == "s":
        print("not walking")

def craft():
    sword = 0
    pickaxe = 0
    torch = 0
    block = 0
    craft = input("what do you want to craft?: ")
    if craft == "sword":
        print("you crafted a sword!")
        sword += 1
    elif craft == "pickaxe":
        print("you crafted a pickaxe!")
        pickaxe += 1
    elif craft == "torch":
        print("you crafted a torch!")
        torch += 1
    elif craft == "block":
        print("you crafted a block!")
        block +=  1
        
def music():
    pygame.mixer.music.load('supernova.mp3')
    pygame.mixer.music.play(-1, 0.0)
    musicPlaying = True
    
#creates the game.
def game():
    
    playerhealth = 100
    while True:
     game = input(">")
     if game == " ":
         do_slash()
     if game == "w":
         walk()
         fight_one = input("a zombie is attacking you what do you want to do?!: ")
         if fight_one == "fight":
             slash = input(">")
             if slash == " ":
                 do_slash()
                 print("zombie health = 50% your heath = 100%")
                 print("zombies turn")
                 print("your health = 50% zombie health = 50%")
                 playerhealth -= 50
                 print("your turn")
                 slash = input(">")
                 if slash == " ":
                     print("oh no! you missed")
                     print("zombies turn")
                     print("your health = 0% zombie health = 50%")
                     playerhealth -= 50
     while playerhealth == 0:
            print("you died!")
            respawn = input("do you want to respawn?: ")
            if respawn == "yes":
                
               playerhealth = 100
               sword = 0
               pickaxe = 0
               block = 0
               torch = 0        
                 
     if game == "c":
          craft()
    
    
if __name__ == "__main__":
    music()
    start()
    game()
