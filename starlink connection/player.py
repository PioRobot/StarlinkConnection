import pygame
class Player():
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotAng = 0
        self.img = None
        self.finalPlayer = None
    def main(self, display):
        playerRect = pygame.draw.ellipse(display, (0, 0, 255), (self.x, self.y, self.width, self.height))
        if self.img is None:
            self.img = pygame.image.load('images/player.png').convert()
        rotated_player = pygame.transform.rotate(self.img, self.rotAng)
        rotated_rect = rotated_player.get_rect(center=playerRect.center)
        display.blit(rotated_player, rotated_rect)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotAng += 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotAng -= 1