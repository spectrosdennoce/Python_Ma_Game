from Game.Display_Config import Display_Interface,pygame,ConfigParser,mixer,Level,glob
import random
from Libs.Read_Raw import raw,Get_All_From_Folder
from Entity.Personage import Personnage
from Entity.Enemy import Enemy
from Entity.Bullet import Bullet
class Game(Display_Interface):
    def __init__(self):
        super().__init__()


    #get_Ressource
        ##get_image
        Image_Bg_Lvl1 = Get_All_From_Folder("./Image/Background/",".png")
        Image_Player = Get_All_From_Folder("./Image/Player/",".png")
        Image_Bullet = Get_All_From_Folder("./Image/Bullet/Bullet/",".png")
        Image_Laser = Get_All_From_Folder("./Image/Bullet/Laser/",".png")
        Image_Mob1 = Get_All_From_Folder("./Image/Mob/Sorcerer/",".png")
        Image_Mob2 = Get_All_From_Folder("./Image/Mob/TrucWip/",".png")
        Image_Mob3 = Get_All_From_Folder("./Image/Mob/Ship/",".png")
        
        ##get_sound
        
        Music = [raw("./Music/songamu1.mp3")]
        Sfx = raw("./sfx/gun.wav")

    
    #init player
        self.Player = Personnage(Image=Image_Player,Game=self,Position_Bullet_X=80,Position_Bullet_Y=40,Shoot_Entity=Bullet(Image_Bullet,self,Sfx))
    #init spawner
        self.Spawner = (self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-350)
    #init enemy
        self.Enemy_Type = [
            Enemy(Image=Image_Mob1,Game=self,Vie=2,Position_Bullet_X=0,Position_Bullet_Y=40,Shoot_Entity=Bullet(Image_Bullet,self,Sfx,Reverse=True),Pos_X=self.Spawner[0],Pos_Y=self.Spawner[1]),
            Enemy(Image=Image_Mob2,Position_Bullet_X=0,Vie=2,Position_Bullet_Y=20,Game=self,Shoot_Entity=Bullet(Image_Bullet,self,Sfx,Reverse=True),Pos_X=self.SCREEN_WIDTH/2-self.SCREEN_WIDTH/3,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/3),
            Enemy(Image=Image_Mob3,Position_Bullet_X=0,Vie=2,Position_Bullet_Y=89,Game=self,Shoot_Entity=Bullet(Image_Laser,self,Sfx),Pos_X=self.SCREEN_WIDTH-self.SCREEN_WIDTH/2,Pos_Y=self.SCREEN_HEIGHT-self.SCREEN_HEIGHT/2)
        ]
        self.Enemy = [self.Enemy_Type[0],self.Enemy_Type[1],self.Enemy_Type[2]]

    #init Level
        self.Level_Right = Level(Image_Bg_Lvl1,self,-self.SCREEN_WIDTH)
        self.Level_Left = Level(Image_Bg_Lvl1,self,self.SCREEN_WIDTH)
        self.Level = [Level(Image_Bg_Lvl1,self)]

    #init music
        mixer.music.load(Music[self.Player.Level])
        mixer.music.set_volume(self.Music_Volume)
        if(self.Debug == False):
            mixer.music.play(-1)
        self.Rythme = 1200
        self.BPM = 60
        self.milliseconds_until_event = self.Rythme
        self.milliseconds_since_event = 0
        self.milliseconds_since_event_shooter = 0
    #init Controler
    def HandleEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.Running = False
        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, "K_"+self.TOUCHE["escape"])]:
            self.Running = False

        if keys[getattr(pygame, "K_"+self.TOUCHE["haut"])] & (self.Player.Is_Jump == False):
            self.Player.Is_Away_Jump = True

        # if keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y < self.SCREEN_HEIGHT):
        #     self.Player.Pos_Y += self.Player.Vitesse
        # elif keys[getattr(pygame, "K_"+self.TOUCHE["bas"])] & (self.Player.Pos_Y+self.Player.Size_Y > self.SCREEN_HEIGHT):
        #     self.Player.Pos_Y = self.SCREEN_HEIGHT-self.Player.Size_Y

        if (keys[getattr(pygame, "K_"+self.TOUCHE["droite"])]) & (self.Player.Is_Shooting == False) & ((self.Player.Is_Away_Shot == False) ):
            self.Player.Is_Move = True
            self.Player.Goto_Right()

        if (keys[getattr(pygame, "K_"+self.TOUCHE["gauche"])]) & (self.Player.Is_Shooting == False) & ((self.Player.Is_Away_Shot == False) ):
            self.Player.Is_Move = True
            self.Player.Goto_Left()

        if (keys[getattr(pygame, "K_"+self.TOUCHE["space"])]) & (self.Player.Is_Shooting == False) & (self.Player.Is_Action == True):
            self.Player.Is_Away_Shot = True
            self.Player.Etat = 0

    #init Rythme_based
    def Rythme_fonc(self):
        
        if ((self.milliseconds_since_event >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Jump)) & (self.Player.Is_Away_Jump == True)):
            self.milliseconds_since_event = 0
            self.Player.Animate(4,12,True,lambda:self.Player.Set_Jump())

        if ((self.milliseconds_since_event >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Jump)) & (self.Player.Is_Move == True)):
            self.milliseconds_since_event = 0
            if(self.Player.Is_Jump == False) & (self.Player.Is_Away_Jump == False):
                self.Player.Animate(12,24,False)
                self.Player.Is_Move = False

        if ((self.milliseconds_since_event_shooter >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Shoot)) & (self.Player.Is_Away_Shot == True) & (self.Player.Has_Shoot == False)):
            self.milliseconds_since_event_shooter = 0
            self.Player.Animate(1,3,True,lambda:self.Player.Shoot())
            self.Has_Shoot = True
            if(self.Player.Etat == 0):
                self.Player.Is_Away_Shot = False
            
            self.Player.Is_Action = False
            # for Enemy_unique in self.Enemy:
            #     if(Enemy_unique.Can_Shoot == True):
            #         #Enemy_unique.Shoot()
            #         Enemy_unique.Animate(1,len(Enemy_unique.Image),False,lambda:Enemy_unique.Shoot())
        
        for Enemy_unique in self.Enemy:
            if ((self.milliseconds_since_event_shooter >= ((self.milliseconds_until_event-self.BPM)%self.Player.Speed_Shoot)) & (Enemy_unique.Is_Away_Shot == True) & (Enemy_unique.Has_Shoot == False)):
                        self.milliseconds_since_event_shooter = 0
                        Enemy_unique.Animate(1,len(Enemy_unique.Image),False,lambda:Enemy_unique.Shoot())
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
        #init black background
        self.Display.fill((0,0,0))
        #set image fonction level
        self.Display.blit(self.Level[self.Player.Level].Get_Image(),(0, 0))
        #set purple rect
        if ((self.milliseconds_since_event_shooter >= self.milliseconds_until_event-self.BPM)):
            pygame.draw.rect(self.Display,(255,0,255),pygame.Rect(self.SCREEN_WIDTH-100,self.SCREEN_HEIGHT-100,self.SCREEN_WIDTH,self.SCREEN_HEIGHT))

#--------------------------------------------------------------------------------------

        for Enemy_unique in self.Enemy:
            if(len(self.Enemy) < 4):
                randomized_mod = random.randint(1,3)
                if randomized_mod == 1:
                    self.Enemy.append(self.Enemy_Type[0])
                elif randomized_mod == 2:
                    self.Enemy.append(self.Enemy_Type[1])
                elif randomized_mod == 3:
                    self.Enemy.append(self.Enemy_Type[2])
            if self.Player.IS_Overlaps(Enemy_unique):
                print('Player collide enemy!' + " : " +  str(Enemy_unique.Vie))
            
#--------------------------------------------------------------------------------------

            #shoot enemy collider
            if (Enemy_unique.Is_Shooting == True):
                for Enemy_Bullet in Enemy_unique.Bullet:
                    if Enemy_Bullet.IS_Overlaps(self.Player):
                        self.Player.Vie -= Enemy_Bullet.Degat
                        Enemy_unique.Bullet.remove(Enemy_Bullet)
                        if(self.Debug):
                            print('enemy bullet collide player')

#--------------------------------------------------------------------------------------

            #player shoot collider
            if (self.Player.Is_Shooting == True):
                for Player_Bullet in self.Player.Bullet:
                    if Player_Bullet.IS_Overlaps(Enemy_unique):
                        self.Player.Bullet.remove(Player_Bullet)
                        self.Player.Is_Shooting = False
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
        if(self.Player.Is_Jump == True):
            self.Player.jump()

        #print bullet
        if (self.Player.Is_Shooting == True):
            for Player_Bullet in self.Player.Bullet:
                if(Player_Bullet.Reverse == False):
                    #show player bullet image
                    if (Player_Bullet.Pos_X < self.SCREEN_WIDTH):
                        Player_Bullet.Pos_X += Player_Bullet.Vitesse
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
                        Player_Bullet.Pos_X -= Player_Bullet.Vitesse
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
        #get masque du joueur
        if(self.Debug):
            pygame.draw.rect(self.Display,(255,255,0,255),self.Player.Get_Rect())
            self.Display.blit(self.Player.Get_Mask_Surface(),self.Player.Get_Pos())

        #for time event and flip
        self.milliseconds_since_event += pygame.time.Clock().tick(self.frames_per_second)
        self.milliseconds_since_event_shooter +=  pygame.time.Clock().tick(self.frames_per_second)
        pygame.display.flip()
