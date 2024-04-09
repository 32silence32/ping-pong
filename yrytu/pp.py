
from random import *
from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг Понг")
color = (255,0,0)

run = True
clock = time.Clock()
FPS = 120


class Game(sprite.Sprite):
    def __init__(self,pimage, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (200,200))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Game2(sprite.Sprite):
    def __init__(self,pimage, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (100,70))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
        
class Player(Game):
    def update(self):
        keys = key.get_pressed()
        if keys [K_UP] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys [K_DOWN] and self.rect.y <= 300:
            self.rect.y += self.speed
        
class Player2(Game):
    def update(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y <= 300:
            self.rect.y += self.speed
        
        
tester2  = Player2('121.png', 0 , 150, 1)
tester = Player('121.png', 500, 150, 1)

ball = Game2('images.png', 300, 175,1)

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
        
                
    
    window.fill(color)
    if ball.rect.y <= 430:
        ball.rect.x+=ball.speed
        ball.rect.y+=ball.speed
     
    tester.reset()
    tester2.reset()
    ball.reset()
    tester.update()
    tester2.update()
    display.update()
    clock.tick(FPS)
