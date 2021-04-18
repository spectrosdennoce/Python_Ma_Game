from Entity.Entity import Entity
class Personnage(Entity):
    def __init__(self,Image,Game,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y,Reverse=False):
        super().__init__(Image, Game,Reverse,
        #bullet
        Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Can_Shoot=True,Shoot_Entity=Shoot_Entity,
        #information
        Vie=10,Pos_X=Game.SCREEN_WIDTH/2,Vitesse = 7,Pos_Y=Game.SCREEN_HEIGHT/2)
        self.Level = 0