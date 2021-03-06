from copy import copy, deepcopy
from os import removedirs
from Game.Display_Config import Display_Interface,pygame,ConfigParser,mixer,Level,glob
import random,sys,math
from Libs.Read_Raw import raw,Get_All_From_Folder
from Entity.Personage import Personnage
from Entity.Enemy import Enemy
from Entity.Bullet import Bullet
class Game(Display_Interface):
    def __init__(self):
        super().__init__()

    #get_Ressource
        ##get_image
        self.Image = {
            'Image_Bg_Lvl1' : Get_All_From_Folder("./Image/Background/",".png"),
            'Image_Player' : Get_All_From_Folder("./Image/Player/",".png"),
            'Image_Bullet' : Get_All_From_Folder("./Image/Bullet/Bullet/",".png"),
            'Image_Laser' : Get_All_From_Folder("./Image/Bullet/Laser/",".png"),
            'Image_Mob1' : Get_All_From_Folder("./Image/Mob/Sorcerer/",".png"),
            'Image_Mob2' : Get_All_From_Folder("./Image/Mob/TrucWip/",".png"),
            'Image_Mob3' : Get_All_From_Folder("./Image/Mob/Ship/",".png")
        }
        # self.Object = {
        #     'Level_1': Get_All_From_Folder("./Image/Object/Level1",".png")
        # }
        ##get_sound
        self.Sound = {
            'Music' : [raw("./Music/songamu1.mp3")],
            'Sfx' : raw("./sfx/gun.wav"),
            'Game_Over' : raw("./sfx/Game_over.wav")
        }
    #init var pause
        self.Pause = False
    #init player
        self.Player = Personnage(Image=self.Image['Image_Player'],Game=self,Position_Bullet_X=80,Position_Bullet_Y=40,Shoot_Entity=Bullet(self.Image['Image_Bullet'],self,self.Sound['Sfx']))
    #init spawner
        self.Spawner = (self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-350)
        self.Timer_Spawner = 1500
    #init enemy
        self.Enemy = []

    #init Level
        self.Level_Right = Level(self.Image['Image_Bg_Lvl1'],self,-self.SCREEN_WIDTH)
        self.Level_Left = Level(self.Image['Image_Bg_Lvl1'],self,self.SCREEN_WIDTH)
        self.Level = [Level(self.Image['Image_Bg_Lvl1'],self)]

    #init music
        mixer.music.load(self.Sound['Music'][self.Player.Level])
        mixer.music.set_volume(self.Music_Volume)
        if(self.Debug == False):
            mixer.music.play(-1)
        self.Rythme = 1200
        self.BPM = 60
        self.milliseconds_until_event = self.Rythme
        self.milliseconds_since_event = 0
        self.milliseconds_since_event_shooter = 0
        self.milliseconds_since_event_hit = 0
        self.milliseconds_since_event_spawner = 0

    def Create_Enemy(self,Number):
        if(Number == 0):
            x = Enemy(Image=self.Image['Image_Mob1'],Game=self,Vie=2,Position_Bullet_X=0,Position_Bullet_Y=40,Shoot_Entity=Bullet(self.Image['Image_Bullet'],self,self.Sound['Sfx'],Reverse=True),Pos_X=self.Spawner[0],Pos_Y=self.Spawner[1])
        elif(Number == 1):
            x = Enemy(Image=self.Image['Image_Mob2'],Position_Bullet_X=0,Vie=2,Position_Bullet_Y=20,Game=self,Shoot_Entity=Bullet(self.Image['Image_Bullet'],self,self.Sound['Sfx'],Reverse=True),Pos_X=self.Spawner[0],Pos_Y=self.Spawner[1])
        elif(Number == 2):
            x = Enemy(Image=self.Image['Image_Mob3'],Position_Bullet_X=0,Vie=2,Position_Bullet_Y=89,Game=self,Shoot_Entity=Bullet(self.Image['Image_Bullet'],self,self.Sound['Sfx']),Pos_X=self.Spawner[0],Pos_Y=self.Spawner[1])
        return x
        
    #init Controler
    def HandleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if (event.key == getattr(pygame, "K_"+self.TOUCHE["pause"])):
                    self.Pause = not self.Pause
                    if(self.Pause):
                        mixer.music.pause()
                    else:
                        mixer.music.unpause()

        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, "K_"+self.TOUCHE["escape"])]:
            sys.exit()

        if keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Is_Jump == False) & (self.Pause == False):
            self.Player.Is_Away_Jump = True
        # a coder et animer une fonction accroupire (vu que les collision perfect frame sa abaissera la boitre de collision)
        # if keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y < self.SCREEN_HEIGHT):
        #     self.Player.Pos_Y += self.Player.Vitesse
        # elif keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y > self.SCREEN_HEIGHT):
        #     self.Player.Pos_Y = self.SCREEN_HEIGHT-self.Player.Size_Y

        if (keys[getattr(pygame, "K_"+self.TOUCHE["droite"])]) & ((self.Player.Is_Away_Shot == False) & (self.Pause == False)):
            self.Player.Is_Move = True
            self.Player.Goto_Right()

        if (keys[getattr(pygame, "K_"+self.TOUCHE["gauche"])]) & ((self.Player.Is_Away_Shot == False) & (self.Pause == False)):
            self.Player.Is_Move = True
            self.Player.Goto_Left()

        if (keys[getattr(pygame, "K_"+self.TOUCHE["space"])]) & (self.Player.Is_Shooting == False) & (self.Player.Is_Action == True) & (self.Pause == False):
            self.Player.Is_Away_Shot = True
            self.Player.Etat = 0

        if (keys[getattr(pygame, "K_"+self.TOUCHE["second_fire"])]) & (self.Player.Is_Shooting == False) & (self.Player.Is_Action == True) & (self.Pause == False):
            self.Player.Is_Away_Shot_laser = True
            self.Player.Etat = 0

        if ((keys[getattr(pygame, "K_"+self.TOUCHE["reset"])]) & (self.Player.Vie == 0)):
            self.reset()
            
        if (keys[getattr(pygame, "K_l")]):
            if(self.Debug == True):
                self.Debug = False
            else:
                self.Debug = True

    def reset(self):
        self.__init__()

    #init Rythme_based
    def Rythme_fonc(self):

        #automatisme generation mob selon template
        if (self.milliseconds_since_event_spawner >= ((self.milliseconds_until_event-self.BPM)%self.Timer_Spawner)):
            self.milliseconds_since_event_spawner = 0
            if(len(self.Enemy) < 3):
                self.Enemy.append(self.Create_Enemy(random.randint(0,2)))

        if ((self.milliseconds_since_event >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Jump)) & (self.Player.Is_Away_Jump == True) & (self.Player.Is_Jump == False)):
            self.milliseconds_since_event = 0
            self.Player.Animate(5,10,False,lambda:self.Player.Set_Jump())

        if (((self.milliseconds_since_event >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Move)) & (self.Player.Is_Move == True)) | ((self.Player.Is_Animate == False) & (self.Player.Is_Move == True))):
            self.milliseconds_since_event = 0
            if(self.Player.Is_Jump == False) & (self.Player.Is_Away_Jump == False):
                self.Player.Is_Move = False
                self.Player.Animate(10,18,False,lambda:self.Player.Reset_Etat())

        if (self.milliseconds_since_event_hit >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Can_Hit)):
            self.milliseconds_since_event_hit = 0
            self.Player.Is_Hit = False

        if ((self.milliseconds_since_event_shooter >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Shoot)) & (self.Player.Is_Away_Shot == True) & (self.Player.Has_Shoot == False)):
            self.milliseconds_since_event_shooter = 0
            self.Player.Animate(2,4,True,lambda:self.Player.Shoot())
            self.Has_Shoot = True
            if(self.Player.Etat == 0):
                self.Player.Is_Away_Shot = False
            self.Player.Is_Action = False

        for Enemy_unique in self.Enemy:
            if ((self.milliseconds_since_event_shooter >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Shoot)) & (Enemy_unique.Is_Away_Shot == True) & (Enemy_unique.Has_Shoot == False)):
                self.milliseconds_since_event_shooter = 0
                Enemy_unique.Animate(0,len(Enemy_unique.Image)-2,False,lambda:Enemy_unique.Shoot())
                self.Has_Shoot = True
                if(Enemy_unique.Etat == 0):
                    Enemy_unique.Is_Away_Shot = False
                Enemy_unique.Is_Action = False

        if (self.milliseconds_since_event_shooter >= self.milliseconds_until_event-self.BPM):
            self.Player.Is_Action = True
            self.Player.Has_Shoot = False

            if self.milliseconds_since_event_shooter >= (self.milliseconds_until_event+self.BPM):
                self.milliseconds_since_event_shooter = 0
                for Enemy_unique in self.Enemy:
                    Enemy_unique.Is_Away_Shot = True
                    Enemy_unique.Etat = 0
                self.Player.Is_Action = False
            self.milliseconds_until_event = self.Rythme

    #init Update
    def Update(self):
        self.Player.Shoot_Entity.Etat = (self.Player.Shoot_Entity.Etat+1)%3
        #init black background
        self.Display.fill((0,0,0))
        #set image fonction level
        self.Display.blit(self.Level[self.Player.Level].Get_Image(),(0, 0))
        #set purple rect
        if ((self.milliseconds_since_event_shooter >= self.milliseconds_until_event-self.BPM)):
            pygame.draw.rect(self.Display,(255,0,255),pygame.Rect(self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-100,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))


#--------------------------------------------------------------------------------------

        for Enemy_unique in self.Enemy:
            if(self.Pause == False):
                if(Enemy_unique.Pos_X > 0 - Enemy_unique.Size_X):
                    Enemy_unique.Pos_X -= Enemy_unique.Vitesse
                else:
                    self.Enemy.remove(Enemy_unique)
                if self.Player.IS_Overlaps(Enemy_unique):
                    if(self.Player.Is_Hit == False):
                        self.Player.Vie -= Enemy_unique.Degat
                        self.Player.Is_Hit = True
                    if(self.Debug):
                        print('Player collide enemy!' + " : " +  str(Enemy_unique.Vie))
            if(self.Debug):
                print(len(self.Enemy))

#--------------------------------------------------------------------------------------

            #shoot enemy collider
            if(self.Pause == False):
                if (Enemy_unique.Is_Shooting == True):
                    for Enemy_Bullet in Enemy_unique.Bullet:
                        if Enemy_Bullet.IS_Overlaps(self.Player):
                            self.Player.Vie -= Enemy_Bullet.Degat
                            Enemy_unique.Bullet.remove(Enemy_Bullet)
                            if(self.Debug):
                                print('enemy bullet collide player')

#--------------------------------------------------------------------------------------

            #player shoot collider
            if(self.Pause == False):
                if (self.Player.Is_Shooting == True):
                    for Player_Bullet in self.Player.Bullet:
                        if Player_Bullet.IS_Overlaps(Enemy_unique):
                            self.Player.Bullet.remove(Player_Bullet)
                            self.Player.Is_Shooting = False
                            #erreur de cible les entit?? ne sont pas identifier correctemement
                            Enemy_unique.Vie = Enemy_unique.Vie - Player_Bullet.Degat
                            if(self.Debug):
                                print('player bullet collide enemy' + " : " +  str(Enemy_unique.Vie))

#--------------------------------------------------------------------------------------

            if(Enemy_unique.Vie == 0):
                self.Enemy.remove(Enemy_unique)
            else:
                if(self.Debug):
                    pygame.draw.rect(self.Display,(255,255,0,255),Enemy_unique.Get_Rect())
                Enemy_unique.Print_Screen()

            if(self.Pause == False):
                if (Enemy_unique.Is_Shooting == True) & (Enemy_unique.Is_Animate == False):
                    #show enemy bullet image
                    for Enemy_Bullet in Enemy_unique.Bullet:
                        self.Display.blit(Enemy_Bullet.Get_Image(),Enemy_Bullet.Get_Pos())
                        if Enemy_Bullet.Pos_X > 0:
                            Enemy_Bullet.Pos_X -= Enemy_Bullet.Vitesse
                        else:
                            Enemy_unique.Bullet.remove(Enemy_Bullet)

#--------------------------------------------------------------------------------------

        #check jump player
        if(self.Pause == False):
            if(self.Player.Is_Jump == True):
                self.Player.jump()

        #print bullet
        if(self.Pause == False):
            if (self.Player.Is_Shooting == True):
                for Player_Bullet in self.Player.Bullet:
                    if(Player_Bullet.Reverse == False):
                        #show player bullet image
                        if (Player_Bullet.Pos_X < self.SCREEN_WIDTH):
                            Player_Bullet.right(self.Player)
                            self.Display.blit(Player_Bullet.Get_Image(),Player_Bullet.Get_Pos())
                            #show player bullet masque
                            if(self.Debug):
                                self.Display.blit(Player_Bullet.Get_Mask_Surface(),Player_Bullet.Get_Pos())
                                pygame.draw.rect(self.Display,(255,255,0,255),Player_Bullet.Get_Rect())
                        else:
                            self.Player.Bullet.remove(Player_Bullet)
                            self.Player.Is_Shooting = False
                    else:
                        #show player bullet image
                        if (Player_Bullet.Pos_X > 0):
                            Player_Bullet.left(self.Player)
                            self.Display.blit(Player_Bullet.Get_Image(),Player_Bullet.Get_Rect())
                            #show  player bullet masque
                            if(self.Debug):
                                pygame.draw.rect(self.Display,(255,255,0,255),Player_Bullet.Get_Rect())
                                self.Display.blit(Player_Bullet.Get_Mask_Surface(),Player_Bullet.Get_Rect())
                        else:
                            self.Player.Bullet.remove(Player_Bullet)
                            self.Player.Is_Shooting = False

#--------------------------------------------------------------------------------------

        #get image du joueur
        self.Display.blit(self.Player.Get_Image(),self.Player.Get_Pos())
        #get line shoot

        plotPoints = []
        for x in range(self.Player.Get_Shoot_Point()[0], self.SCREEN_WIDTH):
            y=int(math.sin((x-self.Player.Get_Shoot_Point()[0])/50.0) * 100 + self.Player.Get_Shoot_Point()[1])
            plotPoints.append([x, y])
        if(plotPoints):
            pygame.draw.lines(self.Display, (0,255,0,255), False, plotPoints, 1)
        plotPoints = []
        for x in range(self.Player.Get_Shoot_Point()[0], self.SCREEN_WIDTH):
            y=int(-math.sin((x-self.Player.Get_Shoot_Point()[0])/50.0) * 100 + self.Player.Get_Shoot_Point()[1])
            plotPoints.append([x, y])
        if(plotPoints):
            pygame.draw.lines(self.Display, (0,255,0,255), False, plotPoints, 1)
            pygame.draw.line(self.Display,(0,255,0,255),self.Player.Get_Shoot_Point(),(self.SCREEN_WIDTH,self.Player.Get_Shoot_Point()[1]))

        plotPoints = []
        for x in range(0, self.Player.Get_Shoot_Point()[0]):
            y=int(math.sin((x-self.Player.Get_Shoot_Point()[0])/50.0) * 100 + self.Player.Get_Shoot_Point()[1])
            plotPoints.append([x, y])
        if(plotPoints):
            pygame.draw.lines(self.Display, (0,0,255,255), False, plotPoints, 1)
            pygame.draw.line(self.Display,(0,0,255,255),self.Player.Get_Shoot_Point(),(0,self.Player.Get_Shoot_Point()[1]))

        #get life player
        self.Player.print_life()
        #get masque du joueur
        if(self.Debug):
            pygame.draw.rect(self.Display,(255,255,0,255),self.Player.Get_Rect())
            self.Display.blit(self.Player.Get_Mask_Surface(),self.Player.Get_Pos())

        if(self.Player.Vie == 0):
            self.Pause = True
            self.Display.fill((0,0,0))
            self.Write_Text((self.SCREEN_WIDTH/2,self.SCREEN_HEIGHT/2),(240,20,20),"u die")
            mixer.music.stop()
            mixer.music.load(self.Sound['Game_Over'])
            if(self.Debug == False):
                mixer.music.play(0)
        elif(self.Pause):
            self.Write_Text((self.SCREEN_WIDTH/2,self.SCREEN_HEIGHT/2),(255,255,255),"PAUSE")

        #for time event and flip
        if(self.Pause == False):
            self.milliseconds_since_event += pygame.time.Clock().tick(self.frames_per_second)
            self.milliseconds_since_event_shooter +=  pygame.time.Clock().tick(self.frames_per_second)
            self.milliseconds_since_event_hit +=  pygame.time.Clock().tick(self.frames_per_second)
            self.milliseconds_since_event_spawner  +=  pygame.time.Clock().tick(self.frames_per_second)
        pygame.display.flip()
