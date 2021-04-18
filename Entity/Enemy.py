from Entity.Entity import Entity
class Enemy(Entity):
    def __init__(self,Image,Game,Pos_X,Pos_Y,Shoot_Entity,Position_Bullet_X,Position_Bullet_Y,Vie=10,Reverse=False):
        super().__init__(Image, Game,Reverse,Position_Bullet_X=Position_Bullet_X,Position_Bullet_Y=Position_Bullet_Y,Size_X=80,Can_Shoot=True,Vie=Vie,Pos_X=Pos_X,Pos_Y=Pos_Y,Shoot_Entity=Shoot_Entity)