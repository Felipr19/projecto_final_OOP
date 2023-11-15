from Caracter import *
from InterfazGrafica import ALTO, ANCHO
import pygame


class Personaje(Caracter):
    def __init__(self, nombre, salud, velocidad):
        super().__init__(nombre, salud, velocidad)


    def mostrar_estado(self):
        super().mostrar_estado()

    def input(self):
        teclas=pygame.key.get_pressed()

        if teclas[pygame.K_d]:
            self.vel_x=self.velocidad

        elif teclas[pygame.K_a]:
            self.vel_x=-self.velocidad
        else:
            self.vel_x=0

        if teclas[pygame.K_w]:
            self.vel_y=-self.velocidad
            self.vel_y=0

    def mover(self)->None:
        self.rect.move_ip(self.vel_x, self.vel_y)
        if self.rect.bottom>ALTO:
            self.rect.bottom=ALTO
        if self.rect.top<0:
            self.rect.top=0
        if self.rect.left<0:
            self.rect.left=0
        if self.rect.right>ANCHO:
            self.rect.right=ANCHO

    def update(self):
        self.input()
        self.mover()

    def draw(self, surface_1:pygame.surface):
        surface_1.blit(self.image, self.rect)
    
