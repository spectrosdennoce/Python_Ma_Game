import pygame
from Game.Game import Game
from Game.Menu import Menu

#pyinstaller --onefile --noconsole .\main.py
#ne pas oublier le dossier ini et image avec le exe
menu_object = Menu()
game_object = Game()

while menu_object.Running:
    menu_object.HandleEvent()
    menu_object.Update()
while game_object.Running:
    game_object.HandleEvent()
    game_object.Update()
pygame.quit()