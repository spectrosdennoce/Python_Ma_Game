from Entity.Entity import Entity
class Enemy(Entity):
    def __init__(self,Image,Game,Pos_X,Pos_Y,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y):
        super().__init__(Image, Game,Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Size_X=80,Can_Shoot=True,Vie=1,Pos_X=Pos_X,Pos_Y=Pos_Y,Shoot_Entity=Shoot_Entity)