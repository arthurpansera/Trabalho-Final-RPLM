import pygame as pg
import random

branco = (255, 255, 255)
preto = (0, 0, 0)

pg.init()
window = pg.display.set_mode((1000, 600))
pg.display.set_caption("Jogo da Forca - Times de Futebol")
pg.font.init()

fonte = pg.font.SysFont("Courier New", 50)
fonte_rb = pg.font.SysFont("Courier New", 30)

times = ['CRUZEIRO', 'INTERNACIONAL', 'ATLETICO MINEIRO', 'GREMIO', 'SAO PAULO', 'VASCO DA GAMA', 'XV DE PIRACICABA', 'FLAMENGO', 'FERROVIARIA', 'SAO CAETANO', 'IBIS', 'PORTUGUESA', 'CORINTHIANS', 'CUIABA', 'MANAUS', 'BRASIL DE PELOTAS', 'AMERICA DE NATAL', 'REMO', 'PAYSANDU', 'CORITIBA', 'ATHLETICO PARANAENSE', 'RB BRAGANTINO', 'FLUMINENSE', 'JUVENTUDE', 'ATLETICO GOIANIENSE', 'SANTOS', 'MIRASSOL', 'SPORT', 'OPERARIO FERROVIARIO', 'VITORIA', 'GREMIO NOVORIZONTINO', 'SPORT RECIFE']

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ' '
click_last_status = False

def Desenho_da_Forca(window, chance):
    pg.draw.rect(window, branco, (0, 0, 1000, 600))
    pg.draw.line(window, preto, (100, 500), (100, 100), 10)
    pg.draw.line(window, preto, (50, 500), (150, 500), 10)
    pg.draw.line(window, preto, (100, 100), (300, 100), 10)
    pg.draw.line(window, preto, (300, 100), (300, 150), 10)
    if chance >= 1: pg.draw.circle(window, preto, (300, 200), 50, 10)
    if chance >= 2: pg.draw.line(window, preto, (300, 250), (300, 350), 10)
    if chance >= 3: pg.draw.line(window, preto, (300, 260), (225, 350), 10)
    if chance >= 4: pg.draw.line(window, preto, (300, 260), (375, 350), 10)
    if chance >= 5: pg.draw.line(window, preto, (300, 350), (375, 450), 10)
    if chance >= 6: pg.draw.line(window, preto, (300, 350), (225, 450), 10)

def Desenho_Restart_Button(window):
    pg.draw.rect(window, preto, (700, 100, 200, 65))
    texto = fonte_rb.render('Restart', True, branco)
    window.blit(texto, (740, 120))

def Sorteando_Palavra(times, end_game):
    if end_game:
        palavra_escolhida = random.choice(times)
        end_game = False
        return palavra_escolhida, end_game
    return '', end_game

def Camuflando_Palavra(palavra_escolhida, tentativas_de_letras):
    palavra_camuflada = ''
    for letra in palavra_escolhida:
        if letra in tentativas_de_letras:
            palavra_camuflada += letra
        else:
            palavra_camuflada += '#'
    return palavra_camuflada

def Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    return tentativas_de_letras, chance

def Palavra_do_Jogo(window, palavra_camuflada):
    palavra = fonte.render(palavra_camuflada, True, preto)
    window.blit(palavra, (200, 500))

def Restart_do_Jogo(end_game, chance, tentativas_de_letras, click_last_status, click, x, y):
    if 700 <= x <= 900 and 100 <= y <= 165 and not click_last_status and click[0]:
        tentativas_de_letras = [' ', '-']
        end_game = True
        chance = 0
    return end_game, chance, tentativas_de_letras

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

        if event.type == pg.KEYDOWN and not end_game:
            letra = event.unicode.upper()
            tentativas_de_letras, chance = Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance)

    x, y = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    Desenho_da_Forca(window, chance)
    Desenho_Restart_Button(window)

    if end_game:
        palavra_escolhida, end_game = Sorteando_Palavra(times, end_game)
        tentativas_de_letras = [' ', '-']

    palavra_camuflada = Camuflando_Palavra(palavra_escolhida, tentativas_de_letras)

    Palavra_do_Jogo(window, palavra_camuflada)

    end_game, chance, tentativas_de_letras = Restart_do_Jogo(
        end_game, chance, tentativas_de_letras, click_last_status, click, x, y)

    click_last_status = click[0]

    pg.display.update()