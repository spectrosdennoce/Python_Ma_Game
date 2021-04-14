from Entity.Entity import Entity
class Personnage(Entity):
    def __init__(self,Image,Game,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y):
        super().__init__(Image, Game,Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Can_Shoot=True,Vie=10,Pos_X=Game.SCREEN_WIDTH/2,Pos_Y=Game.SCREEN_HEIGHT/2,Shoot_Entity=Shoot_Entity)
        self.Level = 0