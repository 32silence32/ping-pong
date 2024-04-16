
from random import *
from pygame import *
window = display.set_mode((1200, 800))
display.set_caption("Пинг Понг")
color = (255,0,0)

run = True
clock = time.Clock()
FPS = 120


class Game(sprite.Sprite):
    def __init__(self,pimage, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (50,125))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        
class Game2(sprite.Sprite):
    def __init__(self,pimage, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(pimage), (50,50))
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
        if keys [K_DOWN] and self.rect.y <= 670:
            self.rect.y += self.speed
        
class Player2(Game):
    def update(self):
        keys = key.get_pressed()
        if keys [K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys [K_s] and self.rect.y <= 670:
            self.rect.y += self.speed
        
        
tester2  = Player2('121.png', 0 , 300, 4)
tester = Player('121.png', 1150, 300, 4)
ball = Game2('images.png', 500, 300,1)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Player 1 - Lose!!!', True, (180, 0, 0))
lose2 = font.render('Player 2 - Lose!!!', True, (180, 0, 0))

speed_x = 4
speed_y = 4

while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    ball.rect.x+= speed_x
    ball.rect.y+= speed_y           
    
    window.fill(color)
    if ball.rect.y >= 750:
        speed_y *= -1
        speed_x *= 1
        
    if sprite.collide_rect(tester2, ball) or sprite.collide_rect(tester, ball):
        speed_x *= -1
        speed_y *= 1
    if ball.rect.y <= 0:
        speed_y *= -1
        speed_x *= 1
       
    if ball.rect.x >= 1150:
        speed_x *= 0
        speed_y *= 0
        window.blit(lose2, (500,200))
        game_over = True
        
    if ball.rect.x <= 0:
        speed_x *= 0
        speed_y *= 0
        window.blit(lose1, (500,200))
        game_over = True
        
    
        
    
        
    
        
    tester.reset()
    tester2.reset()
    ball.reset()
    tester.update()
    tester2.update()
    display.update()
    clock.tick(FPS)
