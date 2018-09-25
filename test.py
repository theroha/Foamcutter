# Test Foamcutter Interface
# by Jared Strain

import sys, pygame
from subprocess import run
from pathlib import Path    

pygame.init()

# Set UI
size = width, height = [640, 489]
white = (255,255,255)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

'''

'''
class ICON:
    def __init__(self, image, svgFile):
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.svgFile = svgFile

    def clickCheck(self, mouse):
        #if mouse[0] >= self.rect.topleft[0] and mouse[1] >= self.rect.topleft[1] and mouse[0] <= self.rect.bottomright[0] and mouse[1] <= self.rect.bottomright[1]:
        if self.collidepoint(mouse): 
            run(['python', '/usr/share/inkscape/extensions/makeict_foamcutter.py', self.svgFile])
        else:
            return False
        return True


swirl = ICON('/home/pi/test.png', '/home/pi/test.svg')

# Main loop
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = mouseX, mouseY = pygame.mouse.get_pos()
            print(str(mouse[0]) + ' ' + str(mouseX))
            swirl.clickCheck(mouse)
            
    screen.fill(white)
    screen.blit(swirl.image, swirl.rect)
    pygame.display.flip()
