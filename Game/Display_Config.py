import pygame,glob
from configparser import ConfigParser
from pygame import mixer
from Level.Level import Level
class Display_Interface:
    def __init__(self):
        pygame.init()
        #music
        mixer.pre_init(44100, -16, 2, 2048)
        mixer.init()
        #icon
        Icon = pygame.image.load(r"./Image/icon.png")
        #init controler
        self.TOUCHE = self.get_Config('Klavier')
        #init display
        self.Running = True
        Screen_config = self.get_Config('Ecran')
        self.SCREEN_WIDTH = int(Screen_config["screen_width"])
        self.SCREEN_HEIGHT = int(Screen_config['screen_height'])
        self.Display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.Icon = pygame.display.set_icon(Icon)
        self.Name = pygame.display.set_caption("pygame by Knowledge Keeper")
        #init fps
        self.frames_per_second = 60

    def get_Config(self,section):
        config = ConfigParser()
        config.read('Config.ini')
        element = {}
        for key,value in config.items(section):
            element[key] = value
        return element
    