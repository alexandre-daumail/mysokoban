import pygame

from modules.player import Player


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.player = Player(100, 100)
        self.all_sprites: pygame.sprite.Group[Player] = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            keys = pygame.key.get_pressed()
            self.player.update(keys)
            self.screen.fill((255, 255, 255))
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
