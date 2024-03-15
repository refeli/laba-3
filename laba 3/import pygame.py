import pygame
import random
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.speed_x = 0
        self.speed_y = 0

    def update(self):
        self.speed_x = 0
        self.speed_y = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speed_x = -5
        if keystate[pygame.K_RIGHT]:
            self.speed_x = 5
        if keystate[pygame.K_UP]:
            self.speed_y = -5
        if keystate[pygame.K_DOWN]:
            self.speed_y = 5
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(HEIGHT - self.rect.height)


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

coins = pygame.sprite.Group()
for i in range(10):
    c = Coin()
    all_sprites.add(c)
    coins.add(c)

enemies = pygame.sprite.Group()
for i in range(5):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)


level = 1
score = 0


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Пригоди Маленького Лицаря")
clock = pygame.time.Clock()


def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    all_sprites.update()

    
    hits = pygame.sprite.spritecollide(player, coins, True)
    for hit in hits:
        score += 10  

   
    hits = pygame.sprite.spritecollide(player, enemies, False)
    if hits:
        
        running = False

    # Рендерінг
    screen.fill(WHITE)
    all_sprites.draw(screen)
    draw_text(screen, f"Рівень: {level}", 18, 100, 10)
    draw_text(screen, f"Рахунок: {score}", 18, 100, 30)
    pygame.display.flip()

    
    clock.tick(FPS)

pygame.quit()
sys.exit()
