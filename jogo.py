import pygame as pg
import random

branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (34, 177, 76)
amarelo = (255, 223, 0)
vermelho = (255, 0, 0)

pg.init()
window = pg.display.set_mode((1000, 600))
pg.display.set_caption("Jogo da Forca - Times de Futebol")
pg.font.init()

icone = pg.image.load("imagens/icone.jpg")
pg.display.set_icon(icone)

fonte_titulo = pg.font.SysFont("impact", 60)
fonte_rb = pg.font.SysFont("comicsansms", 40)

A = ['CRUZEIRO', 'INTERNACIONAL', 'ATLETICO MINEIRO', 'VASCO DA GAMA', 'FLAMENGO']
B = ['GREMIO', 'SAO PAULO', 'VASCO DA GAMA', 'CORINTHIANS', 'SANTOS']
C = ['CORINTHIANS', 'SÃO PAULO', 'CRUZEIRO']

tentativas_de_letras = [' ', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ' '
click_last_status = False
jogo_iniciado = False

def Desenho_Sair_Button(window):
    pg.draw.rect(window, vermelho, (350, 350, 300, 75))
    pg.draw.rect(window, amarelo, (350, 350, 300, 75), 5)
    texto_sair = fonte_rb.render("Sair", True, branco)

    largura_texto = texto_sair.get_width()
    altura_texto = texto_sair.get_height()
    pos_x = (350 + 300 / 2) - largura_texto / 2
    pos_y = (350 + 75 / 2) - altura_texto / 2

    window.blit(texto_sair, (pos_x, pos_y))

def Verificar_Botao_Sair(x, y, click, click_last_status):
    if 350 <= x <= 650 and 350 <= y <= 425:
        if click[0] and not click_last_status:
            pg.quit()
            exit()

def Desenho_Tela_Inicial(window):
    imagem_fundo = pg.image.load('imagens/bola.jpg')
    imagem_fundo = pg.transform.scale(imagem_fundo, (1000, 600))
    window.blit(imagem_fundo, (0, 0))

    superficie_escura = pg.Surface((1000, 600))
    superficie_escura.fill((0, 0, 0))
    
    superficie_escura.set_alpha(150)

    window.blit(superficie_escura, (0, 0))

    texto_titulo = fonte_titulo.render("Jogo da Forca - Times de Futebol", True, branco)

    largura_texto_titulo = texto_titulo.get_width()
    pos_x_titulo = (1000 - largura_texto_titulo) / 2
    pos_y_titulo = 100

    window.blit(texto_titulo, (pos_x_titulo, pos_y_titulo))

    pg.draw.rect(window, verde, (350, 250, 300, 75))
    pg.draw.rect(window, amarelo, (350, 250, 300, 75), 5)
    texto_start = fonte_rb.render("Jogar", True, branco)

    largura_texto = texto_start.get_width()
    altura_texto = texto_start.get_height()
    pos_x = (350 + 300 / 2) - largura_texto / 2
    pos_y = (250 + 75 / 2) - altura_texto / 2

    window.blit(texto_start, (pos_x, pos_y))

    Desenho_Sair_Button(window)

    texto_creditos = "Feito por: Arthur Rodrigues Pansera, Jean Inácio Praes Moura, João Gabriel de Lima Coltre e Stefany Carlos de Oliveira"
    fonte_creditos = pg.font.SysFont("comicsansms", 25)
    texto_creditos_renderizado = fonte_creditos.render(texto_creditos, True, branco)

    def quebrar_texto(texto, max_largura):
        palavras = texto.split(' ')
        linhas = []
        linha_atual = ""
        
        for palavra in palavras:
            if fonte_creditos.size(linha_atual + ' ' + palavra)[0] <= max_largura:
                linha_atual += ' ' + palavra
            else:
                linhas.append(linha_atual)
                linha_atual = palavra

        if linha_atual:
            linhas.append(linha_atual)
        
        return linhas

    max_largura = 1000 - 210

    linhas_creditos = quebrar_texto(texto_creditos, max_largura)

    pos_y_creditos = 500

    for linha in linhas_creditos:
        texto_creditos_renderizado = fonte_creditos.render(linha, True, branco)
        largura_texto_creditos = texto_creditos_renderizado.get_width()
        pos_x_creditos = (1000 - largura_texto_creditos) / 2
        window.blit(texto_creditos_renderizado, (pos_x_creditos, pos_y_creditos))
        pos_y_creditos += fonte_creditos.get_height() + 5

def Desenho_da_Forca(window, chance):
    imagem_fundo = pg.image.load('imagens/estadio.jpeg')
    imagem_fundo = pg.transform.scale(imagem_fundo, (1000, 600))

    window.blit(imagem_fundo, (0, 0))

    superficie_clara = pg.Surface((1000, 600))
    superficie_clara.fill((255, 255, 255))
    superficie_clara.set_alpha(100)

    window.blit(superficie_clara, (0, 0))

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
    palavra = fonte_rb.render(palavra_camuflada, True, preto)
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

        if event.type == pg.KEYDOWN and not end_game and jogo_iniciado:
            letra = event.unicode.upper()
            tentativas_de_letras, chance = Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance)

    x, y = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()

    if not jogo_iniciado:
        Desenho_Tela_Inicial(window)

        if 350 <= x <= 650 and 250 <= y <= 325 and click[0] and not click_last_status:
            jogo_iniciado = True
            palavra_escolhida, end_game = Sorteando_Palavra(A, end_game)
            tentativas_de_letras = [' ', '-']

        Verificar_Botao_Sair(x, y, click, click_last_status)
        
    if jogo_iniciado:
        Desenho_da_Forca(window, chance)
        Desenho_Restart_Button(window)

        if end_game:
            palavra_escolhida, end_game = Sorteando_Palavra(A, end_game)
            tentativas_de_letras = [' ', '-']

        palavra_camuflada = Camuflando_Palavra(palavra_escolhida, tentativas_de_letras)
        Palavra_do_Jogo(window, palavra_camuflada)

        end_game, chance, tentativas_de_letras = Restart_do_Jogo(end_game, chance, tentativas_de_letras, click_last_status, click, x, y)

    click_last_status = click[0]

    pg.display.update()