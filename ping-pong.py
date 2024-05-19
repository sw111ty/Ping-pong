from pygame import *
font.init()
font1 = font.Font(None,80)
win1 = font1.render('PLAYER 1 WIN', True, (255,255,255))
lose1 = font1.render('PLAYER 1 LOSE', True, (255,255,255))
win2 = font1.render('PLAYER 2 WIN', True, (255,255,255))
lose2 = font1.render('PLAYER 2 LOSE', True, (255,255,255))

font2 = font.Font(None,36)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x,player_y, size_x, size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

win_width = 600
win_heigth = 500
display.set_caption('Ping-pong')
window = display.set_mode((win_width, win_heigth))
background = transform.scale(image.load('background.jpg'), (win_width, win_heigth))

ball = GameSprite('balll.png', 225,190, 80, 100, 10)
rectangle1 = Player('pngwing.png', 5, 190, 80, 100 ,10)
rectangle2 = Player('pngwing.png', 450, 190, 80, 100 ,10)

finish = False
run = True

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
        
    if not finish:
        window.blit(background, (0,0))

        ball.update()
        rectangle1.update()
        rectangle2.update()
        ball.reset()
        rectangle1.reset()
        rectangle2.reset()
    display.update()
