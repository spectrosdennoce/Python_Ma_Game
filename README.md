# Tempo Of the Psycho
Ceci est un jeu inspirer du offline T-Rex game

Toute les images, music et bruitage sont crée par moi meme.

# Installation

Pour compiler le jeu il faut installer pygame et pyinstaller en global 
et lancer le script build un zip ce créera alors avec les asset et l'executable.

# Gameplay
les actions disponible sont ce deplacer par default zqsd (changeable dans le config.ini crée apres le lancement du jeu si le menu option encore WIP)

Le but est de rester en vie le plus longtemp possible avec des enemie qui tire des projectiles
vous avez toute les x secondes la possibilité de retiré de la vie au enemie une fois tout les enemie tuer de la zone (compteur indiqué)
vous changerez de niveau visible par le fond.

# Fonctionnalité
-Gestion d'animation avec dossier d'image.
-Gestion de changement de touche.
-Gestion de l'audio
-Gestion d'entité
-Gestion de niveau
-Gestion d'evenement
-Gestion du temps

# RoadMap futur
-Faire une base de donnée contenant la progression du joueur
-Une Boutique d'arme et de bonus avec une notion monetaire pour chaque enemie tuer X niveau actuel
-Faire en sorte que les enemie inflige des malus.
(ex sorcier qui inverse les touches du joueur ou alien qui inflige paranoia qui fait voir des enemie au joueur qui n'existe pas)
-un vrai gestionaire hud avec la v2 du gestionaire interface qui comprendra une simplification de l'ajout de bouton et de texte
-un module de distortion des sons(a valider)
-IA v2
-Class enemy v2
-HandleEvent v2
-plus de niveau (fonctionnalité faite mais manque le passage de l'un a l'autre)

# Code
## Librairie
### Read_Raw
Librairie Read_Raw permet de recuperer des contenu de repertoire ou un fichier particulier pour les affectés a un object.
Les images sont ranger par rapport au tri ascii.
### Pygame
Pygame est une librairie d'interface utilisant sdl2 qui est une librairie C/C++ afin de gerer les fenetre windows a destination des jeux
### Glob
Glob est une librairie de fichier je m'en sert pour recuperer des chemins de fichier automatiquemement
### Shutil
Shutil est une librairie de gestion de fichier dans ce projet il sert a copier les assets pour l'executable et crée une archive zip du build final.
### Os
Os est uen librairies qui permet d'avoir un acces plus global au variable de la machine
### Pyinstaller
Pyinstaller est ce qui permet de transformer le code source en executable
### Sprite
Sprite est une classe que j'ai crée en librairie elle me permet de generer des objets utilisable par les outils de pygame comme celle des collision entre masque

## Display_config
Display_config est le parrent de l'objet jeu et menu qui s'occupe d'init tout ce que le jeu a besion :
les assets les variable commune les fonction de prelancemement et l'apelle de toute les librairies.

## Game
Game est le coeur du jeu il a un gestionaire d'event (handle_event) un gestionaire de temp (rythme_fonc)
le premier est la gestion des action du type sauter tirer ce deplacer
le dexieme permet de faire des action en fontion du temps qui est passer grace au milliseconds
dans le cadre actuel il permet de gerer la fonction de tir des entités qui le peuvent

## Entity 
Entity est un des pilliers du jeu il gere les proprieté de toute les entité
possedant les images associer et les sprites qui on recuperer les images qui permet donc de travailler sur du materiel modifiable et en meme temps du materiel d'origine.
Cette classe contient le gestionaire d'animation qui permet de choisir un range d'image, le choix de si on reverse l'animation une fois executé et une fonction executable pour l'executé apres la premiere passe d'animation (comme pour le tir qui ce passe aux milieu de l'animation).

# Organization

L'organisation c'est fait de maniere a d'abord elaborer l'idée donc un jeu ressemblant au t-rex mais en plus aboutie avec l'ajout d'arme et d'un panel d'entité possible.
La seconde idée etais de dessiné moi meme les sprites et de faire moi meme la musique(Indulgence pour la musique :) )


# Outils Utiliser

-Visual studio code

-Github

-BeepBox (https://www.beepbox.co)

-BFRX (https://www.bfxr.net/)

-Studio One

-Krita

-Pixel studio for pixel art

```
MMMMMMMMMMMMMMMMMMMMMMMMddMMyMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMddMMsMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMhmMMsMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMyNMMsMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMsMMMyMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMNmhyymMMMMMMMMMyMMMsMMMMMMMMMMMMMMMMMMMMM
MMMMMmddyyyyyysNMMMMMMmmyMMMohdMMMMMMMMMMMMMMMMMMM
MMMdyyyyyyyyyyyNMMMMMMmmms+odmmNMMMMMMMMMMMMMMMMMM
MMMyyyyyyyssddNMMMMMMMMMy...:mMMMMMMMMMMMMMMMMMMMM
MMMNdhyysssmMMMMMMMMMMMm......hMMMMMMMMMMMMMMMMMMM
MMMMMMMMhosmhMMMMMMMMMN-.......oMMMMMMMMMMMMMMMMMM
MMMMMMMMm++o+dMMMMMMMM/..-.--...:NMMMMMMMMMMMMMMMM
MMMMMMMMy+++++oMMMMMM+.-+/-/:+...-dMMMMMMMMMMMMMMM
MMMMMNh+//////oMMMMMs.:..o   `--...yMMMMMMMMMMMMMM
MMMNs/////////mMMMMd.:  oN`    `--..oMMMMMMMMMMMMM
MMM+//:+o///:+dNMMm-.:` oN`     -:.../NMMMMMMMMMMM
MMN+/:-odNm:::/hMd-...:-:s   .-:-.....:mNMMMMMMMMM
MMMNy//:-sN/-:/ss/.....:-+:+::-......./dmdddddmMMM
MMMMMNhyhshmssymh:.-.....--..............ymmmNmhdh
MMMMMMMMMMdhhhd/...-...hy+::ohs....-......yMMmhNNh
MMMMMMMMMMMMMMy......-.yho//oh+.-..........+dmNyhN
MMMMMMMMMMMMMm........--........-......-...ymNNdhM
MMMMMMMMMMMMMy::-------+-.....-:.......-.....+mNMM
MMMMMMMMMMMMMMMMMMMMMhhhhNNNmhyhoddddddddddhsmMMMM
MMMMMMMMMMMMMMMddNMMhhhyMMMMM+m+MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMoNyddydoMyhmMydsNMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMmhNhhd+MMyNhhydhMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMmymh+NMMNhNdm+MMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMmmMMMMMNyhsmMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
```
