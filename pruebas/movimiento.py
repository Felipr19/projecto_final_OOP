import pygame
import sys

pygame.init()

# Definir dimensiones de la ventana
ANCHO = 800
ALTO = 600

# Crear la ventana
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ventana de Pygame")
reloj = pygame.time.Clock()

surface = pygame.Surface((100,100))
surface.fill('white')
player = surface.get_rect(topleft =(50,50))

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        teclas=pygame.key.get_pressed()

        if teclas[pygame.K_d]:
             player.x+=5
        elif teclas[pygame.K_a]:
             player.x-=5
        
        if teclas[pygame.K_w]:
             player.y-=5
        elif teclas[pygame.K_s]:
             player.y+=5


    ventana.fill('Black')
    ventana.blit(surface, player)


    pygame.display.update()
    pygame.display.flip()
