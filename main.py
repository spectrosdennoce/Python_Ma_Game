import pygame
from Game.Game import Game
from Game.Menu import Menu

#pyinstaller --onefile --noconsole .\main.py
#ne pas oublier le dossier ini image Music et sfx avec le exe
menu_object = Menu()
game_object = Game()
while menu_object.Running:
    menu_object.HandleEvent()
    menu_object.Update()
while game_object.Running:
    game_object.HandleEvent()
    game_object.Rythme_fonc()
    game_object.Update()
pygame.quit()




#MMMMMMMMMMMMMMMMMMMMMMMMddMMyMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMddMMsMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMhmMMsMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMyNMMsMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMsMMMyMMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMNmhyymMMMMMMMMMyMMMsMMMMMMMMMMMMMMMMMMMMM
#MMMMMmddyyyyyysNMMMMMMmmyMMMohdMMMMMMMMMMMMMMMMMMM
#MMMdyyyyyyyyyyyNMMMMMMmmms+odmmNMMMMMMMMMMMMMMMMMM
#MMMyyyyyyyssddNMMMMMMMMMy...:mMMMMMMMMMMMMMMMMMMMM
#MMMNdhyysssmMMMMMMMMMMMm......hMMMMMMMMMMMMMMMMMMM
#MMMMMMMMhosmhMMMMMMMMMN-.......oMMMMMMMMMMMMMMMMMM
#MMMMMMMMm++o+dMMMMMMMM/..-.--...:NMMMMMMMMMMMMMMMM
#MMMMMMMMy+++++oMMMMMM+.-+/-/:+...-dMMMMMMMMMMMMMMM
#MMMMMNh+//////oMMMMMs.:..o   `--...yMMMMMMMMMMMMMM
#MMMNs/////////mMMMMd.:  oN`    `--..oMMMMMMMMMMMMM
#MMM+//:+o///:+dNMMm-.:` oN`     -:.../NMMMMMMMMMMM
#MMN+/:-odNm:::/hMd-...:-:s   .-:-.....:mNMMMMMMMMM
#MMMNy//:-sN/-:/ss/.....:-+:+::-......./dmdddddmMMM
#MMMMMNhyhshmssymh:.-.....--..............ymmmNmhdh
#MMMMMMMMMMdhhhd/...-...hy+::ohs....-......yMMmhNNh
#MMMMMMMMMMMMMMy......-.yho//oh+.-..........+dmNyhN
#MMMMMMMMMMMMMm........--........-......-...ymNNdhM
#MMMMMMMMMMMMMy::-------+-.....-:.......-.....+mNMM
#MMMMMMMMMMMMMMMMMMMMMhhhhNNNmhyhoddddddddddhsmMMMM
#MMMMMMMMMMMMMMMddNMMhhhyMMMMM+m+MMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMoNyddydoMyhmMydsNMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMmhNhhd+MMyNhhydhMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMmymh+NMMNhNdm+MMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMmmMMMMMNyhsmMMMMMMMMMMMMMMMMMMMM
#MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

#Created by L'archimagus (Mikail Chambellant)