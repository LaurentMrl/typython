class Sprite:
    def __init__(self, sp_img_path, sp_animation, sp_pos = [0,0]):
        self.sp_name = sp_img_path
        self.sp_animation = sp_animation
        self.sp_pos = sp_pos
   
    def printListOfSprites(self):
        for sprite in self.listOfSprites:
            print(f"Sprite {sprite.name}")