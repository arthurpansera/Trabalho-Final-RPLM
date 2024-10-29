import pygame as pg
import random

branco = (255,255,255)
preto = (0,0,0)

window = pg.display.set_mode((1000, 600))

pg.font.init()

fonte = pg.font.SysFont("Courier New", 50)
fonte_rb = pg.font.SysFont("Courier New", 30)

times = ['CRUZEIRO', 'GREMIO', 'SAO PAULO', 'INTERNACIONAL', 'ATLETICO MINEIRO']
campeonatos = ['SERIE A', 'SERIE B', 'SULAMERICANA', 'LIBERTADORES', 'COPA DO BRASIL']
jogadores = ['DIOGO BARBOSA', 'WESLEY', 'PATRICK', 'RAFAEL', 'EDENILSON']

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ''
click_last_status = False

def Desenho_da_Forca(window, chance):
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10) 
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)

    if chance >= 1:
        pg.draw.circle(window, preto, (300, 200), 50, 10)
    if chance >= 2:
        pg.draw.line(window, preto, (300, 250), (300, 350), 10)
    if chance >= 3:
        pg.draw.line(window, preto, (300, 260), (225, 350), 10)
    if chance >= 4:
        pg.draw.line(window, preto, (300, 260), (375, 350), 10)
    if chance >= 5:
        pg.draw.line(window, preto, (300, 350), (375, 450), 10)
    if chance >= 6:
        pg.draw.line(window, preto, (300, 350), (225, 450), 10)