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
        try:
            self.TOUCHE = self.get_Config('Klavier')
        except:
            print('cannot open Klvaier')
            self.TOUCHE = {
            'Haut':'z',
            'Bas':'s',
            'Gauche':'q',
            'Droite':'d',
            'Space':'SPACE',
            'Escape':'ESCAPE',
            'Enter':'RETURN'
            }
            self.Write_all_Config('Klavier',self.TOUCHE)
        #init display
        self.Debug = True
        self.Running = True
        try:
            Screen_config = self.get_Config('Ecran')
            self.SCREEN_WIDTH = int(Screen_config['screen_width'])
            self.SCREEN_HEIGHT = int(Screen_config['screen_height'])
        except:
            print('cannot open Ecran')
            self.SCREEN_WIDTH = 1200
            self.SCREEN_HEIGHT = 800
            self.Write_Config('Ecran','SCREEN_WIDTH',self.SCREEN_WIDTH)
            self.Write_Config('Ecran','SCREEN_HEIGHT',self.SCREEN_HEIGHT)
        self.Display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.Icon = pygame.display.set_icon(Icon)
        self.Name = pygame.display.set_caption("Tempo of the psycho")
        #init fps
        self.frames_per_second = 60
        #get sound information (all is between 0 and 100)
        try:
            Audio_config = self.get_Config('Music')
            self.Music_Volume = float(Audio_config['music_volume'])/100
            self.SFX_Volume = float(Audio_config['sfx_volume'])/100
        except:
            print('cannot open Music')
            self.Music_Volume = 0.2
            self.SFX_Volume = 0.1
            self.Write_Config('Music','Music_Volume',int(self.Music_Volume*100))
            self.Write_Config('Music','SFX_Volume',int(self.SFX_Volume*100))

    def get_Config(self,section):
        config = ConfigParser()
        config.read('Config.ini')
        element = {}
        for key,value in config.items(section):
            element[key] = value
        return element

    def Write_Config(self,section,line,value):
        config = ConfigParser()
        #respect case
        config.optionxform = str
        config.read('Config.ini')
        if(config.has_section(str(section)) == False):
            config.add_section(str(section))
        if(config.has_option(str(section), str(line)) == False):
            config.set(str(section), str(line), str(value))
        with open('Config.ini', 'w') as configfile:
            config.write(configfile)
    def Write_all_Config(self,section,dict_value):
        for key in dict_value:
            self.Write_Config(section,key,dict_value[key])