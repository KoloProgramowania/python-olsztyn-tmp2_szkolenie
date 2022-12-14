import pgzrun
from random import randint

# wymiary okna
WIDTH = 640
HEIGHT = 427
TITLE = "Moja gra"


class Bohater:
    def __init__(self, hero, keyb, krok):
        self.my_actor = hero
        self.u, self.l, self.d, self.r = tuple(keyb)
        self.step = krok
        self.my_actor.pos = (randint(krok, WIDTH), randint(krok, HEIGHT))

    def draw(self):
        self.my_actor.draw()

    def move(self, key_keyboard):
        if key_keyboard == self.u:
            self.my_actor.y -= self.step
        if key_keyboard == self.d:
            self.my_actor.y += self.step
        if key_keyboard == self.l:
            self.my_actor.x -= self.step
        if key_keyboard == self.r:
            self.my_actor.x += self.step

        if self.my_actor.x > WIDTH:
            self.my_actor.x -= self.step * 2
        if self.my_actor.x < 20:
            self.my_actor.x += self.step * 2
        if self.my_actor.y > HEIGHT:
            self.my_actor.y -= self.step * 2
        if self.my_actor.y < 20:
            self.my_actor.y += self.step * 2


santa = Bohater(Actor("santa-claus.png"), "wasd", 10)
snowman = Bohater(Actor("snowman3.png"), "ijkl", 5)
ball = Bohater( Actor("ball.png"), "tfgh", 15)

aktorzy = (santa, snowman, ball)


def on_key_down(key):
    key_str = str(key)[-1:].lower()
    for aktor in aktorzy:
        aktor.move(key_str)


def update():
    for aktor in aktorzy:
        aktor.draw()
    pass


def draw():
    screen.blit("snow.jpg", (0, 0))
    for aktor in aktorzy:
        aktor.draw()
    pass


pgzrun.go()
