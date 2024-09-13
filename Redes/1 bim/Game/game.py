import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./CS2/Game/characters/fagames.png')
        self.rect = self.image.get_rect(center=(640,360)) 
        self.image = pygame.transform.rotate(self.image, 60)
        
group_player = pygame.sprite.Group()
group_player.add(Player())
# x_player_pos = group_player

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if pressed_keys[K_w]:
            # group_player.move_ip()

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    group_player.draw(screen)
    
    
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()