
from random import *
from pygame import *
window = display.set_mode((700, 500))
display.set_caption("Пинг Понг")
color = (255,0,0)

run = True
clock = time.Clock()
FPS = 120

font.init()
font2 = font.Font(None, 36)
font3 = font.Font(None, 56)

score = 0
lost = 0                

class Game(sprite.Sprite):
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
        if keys [K_UP] and self.rect.x <= 640:
            self.rect.x += self.speed
        if keys [K_DOWN] and self.rect.x >= 5:
            self.rect.x -= self.speed

lost = 0
class Enemy(Game):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
            lost += 1

class Enemy2(Game):
    def update(self):
        self.rect.y += self.speed
        
        self.rect.x -= self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            

class Enemy2(Game):
    def update(self):
        self.rect.y += self.speed
        
        self.rect.x -= self.speed

        
        global lost
        if self.rect.y > 500:
            self.rect.y = 0
           
            

tester2  = Player('121.png',330, 440, 10)
tester = Player('121.png', 330, 440, 10)



monsters = sprite.Group()
bullets = sprite.Group()
asteroids = sprite.Group()

for i in range(0,6):
    test1 = Enemy('images.png', randint(0,650), 0, randint(1,4) )
    monsters.add(test1)
    
    

top = 0

finish = False
while run: 
    for e in event.get():
        if e.type == QUIT:
            run = False
        
                
  
    window.fill(color)
   
    display.update()
    clock.tick(FPS)
