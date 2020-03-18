#this is a basic program
#!/usr/bin/env python
import time
import os
import pyglet
import pygame
from PIL import Image

print("The year is 2020...")
time.sleep(2)
print("A virus is spreading the world, and yet...")
time.sleep(2)
print("People have priorities. Such as, but not limited to...toilet paper.")
time.sleep(2)
print("But on the other side of the planet lived a strange blonde girl")
time.sleep(2)
print("who was unable to ask people questions normally")
time.sleep(2)
print("so she made programs that do that for her instead")
time.sleep(2)
print("welcome to Hana's legacy.")
time.sleep(3)
#
# song = pyglet.media.load('melissathecrazycyberbitch.mp3')
# song.play()
# pyglet.app.run()
pygame.mixer.init()
pygame.mixer.music.load("melissathecrazycyberbitch.mp3")
pygame.mixer.music.play(-1,0.0)

#random idea: the keys make a sound each time a user presses it
#this image thing doesn't work because it opens up an instance of the
#image in a separate software instead of the terminal, as I imagined it
#makes me sad
# my_logo=Image.open("3xblogo.png")
# my_logo.show();

time.sleep(2)
os.system('clear')

#character selection
gender_question = input("What's your gender?")
time.sleep(0.5)
height_question=input("How tall are you?")
time.sleep(0.4)
name = str(input("Type in your name and last name, please. "))
weight_question=input("How much do you weigh?")
while type(weight_question) != int:
  print('Please, type in a goddamn number. ')
  weight_question=input("How much do you weigh? ")
  break
time.sleep(0.5)

#automate this using a for loop
#write a loop that increments the three dots after the loading
#now, if the user says no to the first question,
#use ad hominem arguments against him
#such as:
#if weight_question > = 220:
    #print('you fucking fatass')
#this program doesn't take in accout that you're
#human being with emotions.

print("loading.")
print("loading..")
print("loading...")

time.sleep(3)
os.system('cls')
#write a loop that exits once the user inputs an integer
# while weight_question != type(int):
#   weight_question=int(input("How much do you weigh?"))
#   print('Please, type in a goddamn number.')

pygame.mixer.stop()

#this part plays that intense part of that song from hotline miami
# pygame.mixer.init()
# pygame.mixer.music.load("melissathecrazycyberbitch.mp3")
# pygame.mixer.music.play(-1,0.0)


name.reverse()
print("Good morning, sir, ", name[::-1])
time.sleep(0.5)
os.system('cls')




os.system('cls')
time.sleep(2)

print("Hey uuh...")

time.sleep(2)

print("You're kinda cute.")

time.sleep(2)

question = str(input("Wanna hang out sometime? Type in [y] for yes and [n] for no. "))

time.sleep(0.5)

#write a while loop that doesn't allow the user to exit unless it's a yes
if question == 'y':
  print("Aight, cool. We'll figure something out.")
else:
  print("Fine. Your loss.")

#writing anything besides y is a mistake in this game
#because the CCB is gonna kill u (cray cyber bitch)
