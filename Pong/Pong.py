from pygame import *
from time import time as timer
#classes |
#        |
#        V
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

img_paddle = 'racket.png'
img_ball = 'tenis_ball.png'

back = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('Pong')
window.fill(back)

score = 0

game = True
finish = False
clock = time.Clock()
FPS = 60

paddle = Player(img_paddle, 10, win_height - 40, 150, 50, 8)
ball = GameSprite(img_ball, 200, 100, 50, 50, 4)

font.init()
font = font.Font(None, 70)
lose = font.render('You Lost', 1, (180,0,0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill(back)
        paddle.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(paddle, ball):
            speed_y *= -1
            speed_x += 0.5
            speed_y += -0.5
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            speed_x *= -1
        if ball.rect.x > win_width - 50:
            speed_x *= -1
        if ball.rect.y > win_height -50:
            finish = True
            window.blit(lose, (200, 200))
        paddle.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)