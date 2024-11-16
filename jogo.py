import pygame as pg
import random

# Definindo cores como tuplas de RGB
branco = (255, 255, 255)
preto = (0, 0, 0)
verde = (34, 177, 76)
amarelo = (255, 223, 0)
vermelho = (255, 0, 0)
vermelho_escuro = (200, 0, 0)
cinza_claro = (128, 128, 128)
cinza_escuro = (88, 88, 88)

# Inicializa o Pygame
pg.init()

# Configurações da janela do jogo
window = pg.display.set_mode((1000, 600))
pg.display.set_caption("Jogo da Forca - Times de Futebol")
pg.font.init()

# Carregando o ícone da janela
icone = pg.image.load("imagens/icone.jpg")
pg.display.set_icon(icone)

# Definição de fontes para títulos, botões e textos
fonte_titulo = pg.font.SysFont("impact", 60)
fonte_rb = pg.font.SysFont("comicsansms", 40)
fonte_menor = pg.font.SysFont("comicsansms", 25)
fonte_conjuntos = pg.font.SysFont("comicsansms", 16)
fonte_pequena = pg.font.SysFont("comicsansms", 25)

# Listas de times de futebol que serão usadas nas perguntas
A = ['ATLETICO MINEIRO', 'CRUZEIRO', 'FLAMENGO', 'INTERNACIONAL', 'VASCO DA GAMA']
B = ['CORINTHIANS', 'GREMIO', 'PALMEIRAS', 'SANTOS', 'SAO PAULO', 'VASCO DA GAMA']
C = ['CORINTHIANS', 'CRUZEIRO', 'SANTOS', 'SAO PAULO', 'VASCO DA GAMA']

# Variáveis para controle do jogo
tentativas_de_letras = ['', '-']
palavra_escolhida = ''
palavra_camuflada = ''
end_game = True
chance = 0
letra = ''
click_last_status = False
jogo_iniciado = False
pergunta = ''
conjuntos_exibidos = False

# Função para desenhar o botão de sair
def Desenho_Sair_Button(window):
    pg.draw.rect(window, vermelho, (350, 350, 300, 75))
    pg.draw.rect(window, amarelo, (350, 350, 300, 75), 5)
    texto_sair = fonte_rb.render("Sair", True, branco)

    largura_texto = texto_sair.get_width()
    altura_texto = texto_sair.get_height()
    pos_x = (350 + 300 / 2) - largura_texto / 2
    pos_y = (350 + 75 / 2) - altura_texto / 2

    window.blit(texto_sair, (pos_x, pos_y))

# Função para verificar o clique no botão de sair
def Verificar_Botao_Sair(x, y, click, click_last_status):
    if 350 <= x <= 650 and 350 <= y <= 425:
        if click[0] and not click_last_status:
            pg.quit()
            exit()

# Função para desenhar a tela inicial do jogo
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

# Função para desenhar a forca
def Desenho_da_Forca(window, chance):
    imagem_fundo = pg.image.load('imagens/estadio.jpeg')
    imagem_fundo = pg.transform.scale(imagem_fundo, (1000, 600))
    window.blit(imagem_fundo, (0, 0))

    superficie_clara = pg.Surface((1000, 600))
    superficie_clara.fill((255, 255, 255))
    superficie_clara.set_alpha(100)
    window.blit(superficie_clara, (0, 0))

    x_base = 100
    y_base = 100

    tamanho_poste = 10
    tamanho_circulo = 50
    tamanho_linhas = 15
    deslocamento_y = 30

    altura_poste = 330
    comprimento_barra = 220
    comprimento_base = 140

    pg.draw.line(window, preto, (x_base, y_base + altura_poste), (x_base, y_base), tamanho_poste)
    pg.draw.line(window, preto, (x_base - comprimento_base / 2, y_base + altura_poste), 
                 (x_base + comprimento_base / 2, y_base + altura_poste), tamanho_poste)
    pg.draw.line(window, preto, (x_base, y_base), (x_base + comprimento_barra, y_base), tamanho_poste)
    pg.draw.line(window, preto, (x_base + comprimento_barra, y_base), 
                 (x_base + comprimento_barra, y_base + 60), tamanho_poste)

    if chance >= 1: pg.draw.circle(window, preto, (x_base + comprimento_barra, y_base + 100), tamanho_circulo, tamanho_linhas)
    if chance >= 2: pg.draw.line(window, preto, (x_base + comprimento_barra, y_base + 140), (x_base + comprimento_barra, y_base + 250), tamanho_linhas)
    if chance >= 3: pg.draw.line(window, preto, (x_base + comprimento_barra, y_base + 160), (x_base + comprimento_barra - 60, y_base + 250), tamanho_linhas)
    if chance >= 4: pg.draw.line(window, preto, (x_base + comprimento_barra, y_base + 160), (x_base + comprimento_barra + 60, y_base + 250), tamanho_linhas)
    if chance >= 5: pg.draw.line(window, preto, (x_base + comprimento_barra, y_base + 250), (x_base + comprimento_barra + 60, y_base + 320), tamanho_linhas)
    if chance >= 6: pg.draw.line(window, preto, (x_base + comprimento_barra, y_base + 250), (x_base + comprimento_barra - 60, y_base + 320), tamanho_linhas)

# Função para desenhar o botão de voltar ao menu
def Desenho_Voltar_Menu_Button(window):
    pg.draw.rect(window, cinza_claro, (700, 175, 200, 65))
    pg.draw.rect(window, cinza_escuro, (700, 175, 200, 65), 5)

    texto_voltar_menu = fonte_rb.render("Voltar", True, branco)
    
    largura_texto_voltar = texto_voltar_menu.get_width()
    altura_texto_voltar = texto_voltar_menu.get_height()
    pos_x_voltar = (700 + 200 / 2) - largura_texto_voltar / 2
    pos_y_voltar = (175 + 65 / 2) - altura_texto_voltar / 2

    window.blit(texto_voltar_menu, (pos_x_voltar, pos_y_voltar))

# Função para verificar o clique no botão de voltar ao menu
def Voltar_Ao_Menu(x, y, click, click_last_status, jogo_iniciado):
    if 700 <= x <= 900 and 175 <= y <= 240 and not click_last_status and click[0]:
        jogo_iniciado = False
    return jogo_iniciado

# Função para mostrar as perguntas
def Mostrar_Pergunta(window, pergunta):
    texto_pergunta = fonte_pequena.render(pergunta, True, preto)
    window.blit(texto_pergunta, (20, 20))

# Função para desenhar o botão de restart
def Desenho_Restart_Button(window):
    pg.draw.rect(window, vermelho, (700, 100, 200, 65))
    pg.draw.rect(window, vermelho_escuro, (700, 100, 200, 65), 5)

    texto = fonte_rb.render('Restart', True, branco)
    largura_texto = texto.get_width()
    altura_texto = texto.get_height()
    pos_x = (700 + 200 / 2) - largura_texto / 2
    pos_y = (100 + 65 / 2) - altura_texto / 2
    window.blit(texto, (pos_x, pos_y))

# Função para quebrar o texto, evitando que ultrapasse o tamanho da janela
def quebrar_texto(texto, largura_maxima, fonte):
    palavras = texto.split(' ')
    linhas = []
    linha_atual = ""
    
    for palavra in palavras:
        if fonte.size(linha_atual + ' ' + palavra)[0] <= largura_maxima:
            linha_atual += (' ' + palavra) if linha_atual else palavra
        else:
            linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)
    
    return linhas

# Função para desenhar texto
def desenhar_texto(texto, pos_x, pos_y):
    texto_renderizado = fonte_conjuntos(texto, True, branco)
    window.blit(texto_renderizado, (pos_x, pos_y))

# Função para desenhar os conjuntos
def Desenho_Conjuntos(window, A, B, C):
    conjunto_box_width = 340
    conjunto_box_height = 300

    pos_x = 650
    pos_y = 260
    pos_y_c = 0
    pos_y_a = 0
    pos_y_b = 0

    conjunto_box = pg.Surface((conjunto_box_width, conjunto_box_height))
    conjunto_box.fill((200, 200, 200))
    conjunto_box.set_alpha(180)
    window.blit(conjunto_box, (pos_x, pos_y))

    texto_conjunto_A = f"Foram bem no Brasileirão: A = [{', '.join(A)}]"
    texto_conjunto_B = f"Foram bem na Copa do Brasil: B = [{', '.join(B)}]"
    texto_conjunto_C = f"Forma bem na Libertadores: C = [{', '.join(C)}]"

    linhas_A = quebrar_texto(texto_conjunto_A, conjunto_box_width - 60, fonte_conjuntos)
    linhas_B = quebrar_texto(texto_conjunto_B, conjunto_box_width - 40, fonte_conjuntos)
    linhas_C = quebrar_texto(texto_conjunto_C, conjunto_box_width - 80, fonte_conjuntos)

    margin_x = 20
    margin_y = 10
    gap_between_lines = 25

    total_linhas_A = len(linhas_A)
    total_linhas_B = len(linhas_B)
    total_linhas_C = len(linhas_C)

    total_altura_ocupada = (total_linhas_A + total_linhas_B + total_linhas_C) * gap_between_lines

    espacamento_extra = conjunto_box_height - total_altura_ocupada
    espacamento_entre_conjuntos = espacamento_extra // 4

    pos_y_offset = pos_y + margin_y + espacamento_entre_conjuntos

    pos_y_a = 270
    for i, linha in enumerate(linhas_A):
        window.blit(fonte_conjuntos.render(linha, True, preto), (pos_x + margin_x, pos_y_a + i * gap_between_lines))


    pos_y_offset += total_linhas_A * gap_between_lines + espacamento_entre_conjuntos
    pos_y_b = 370
    for i, linha in enumerate(linhas_B):
        window.blit(fonte_conjuntos.render(linha, True, preto), (pos_x + margin_x, pos_y_b + i * gap_between_lines))

    pos_y_offset += total_linhas_B * gap_between_lines + espacamento_entre_conjuntos
    pos_y_c += 475
    for i, linha in enumerate(linhas_C):
        window.blit(fonte_conjuntos.render(linha, True, preto), (pos_x + margin_x, pos_y_c + i * gap_between_lines))

    pos_y_final = pos_y + conjunto_box_height - margin_y - gap_between_lines
    if pos_y_offset + (total_linhas_C * gap_between_lines) < pos_y_final:
        espacamento_final = pos_y_final - (pos_y_offset + (total_linhas_C * gap_between_lines))
        pos_y_offset += espacamento_final

# Função para gerar as perguntas e respostas
def Gerar_Pergunta():
    perguntas = [
        ("Qual time foi bem no Brasileirão e na Copa do Brasil?", list(set(A) & set(B))),
        ("Qual time foi bem no Brasileirão, mas não na Copa do Brasil?", list(set(A) - set(B))),
        ("Qual time foi bem na Copa do Brasil, mas não no Brasileirão?", list(set(B) - set(A))),
        ("Qual time foi bem no Brasileirão e na Libertadores?", list(set(A) & set(C))),
        ("Qual time foi bem no Brasileirão, na Copa do Brasil e na Libertadores?", list(set(A) & set(B) & set(C))),
        ("Qual time foi bem na Copa do Brasil, mas não na Libertadores?", list(set(B) - set(C))),
        ("Qual time foi bem na Copa do Brasil ou Libertadores, mas não no Brasileirão?", list((set(B) | set(C)) - set(A))),
        ("Qual time não foi bem na Copa do Brasil?", list((set(A) | set(C)) - set(B))),
        ("Qual time não foi bem no Brasileirão e na Libertadores?", list(set(B) - set(A) - set(C))),
        ("Qual time não foi bem na Copa do Brasil e na Libertadores?", list(set(A) - set(B) - set(C))),
    ]

    pergunta, resposta = random.choice(perguntas)

    if not resposta:
        return Gerar_Pergunta()

    palavra_escolhida = random.choice(resposta)

    return pergunta, palavra_escolhida

# Função para camuflar a resposta
def Camuflando_Palavra(palavra_escolhida, tentativas_de_letras):
    palavra_camuflada = ''
    for letra in palavra_escolhida:
        if letra in tentativas_de_letras:
            palavra_camuflada += letra
        else:
            palavra_camuflada += '#'
    return palavra_camuflada

# Função para verificar se uma letra está na resposta
def Tentando_uma_Letra(tentativas_de_letras, palavra_escolhida, letra, chance):
    if letra.isalpha() and letra not in tentativas_de_letras:
        tentativas_de_letras.append(letra)
        if letra not in palavra_escolhida:
            chance += 1
    return tentativas_de_letras, chance

# Função para desenhar a palavra camuflada
def Palavra_do_Jogo(window, palavra_camuflada):
    palavra = fonte_rb.render(palavra_camuflada, True, preto)
    window.blit(palavra, (30, 460))

pergunta_gerada = False

# Função para recomeçar o jogo
def Restart_do_Jogo(end_game, chance, tentativas_de_letras, click_last_status, click, x, y, pergunta_gerada):
    if 700 <= x <= 900 and 100 <= y <= 165 and not click_last_status and click[0]:
        tentativas_de_letras = [' ', '-']
        end_game = True
        chance = 0
        pergunta_gerada = False
    return end_game, chance, tentativas_de_letras, pergunta_gerada

# Função para desenhar as letras tentadas
def Desenho_Letras_Tentadas(window, tentativas_de_letras):
    tentativas_filtradas = [letra for letra in tentativas_de_letras if letra not in [' ', '-']]
    letras = 'Letras tentadas: ' + ', '.join(tentativas_filtradas)
    texto_tentativas = fonte_menor.render(letras, True, preto)
    window.blit(texto_tentativas, (20, 550))

# Função para desenhar a tela de game over
def Desenho_Tela_Game_Over(window, resposta, x, y, click, click_last_status):
    if resposta == 'CRUZEIRO':
        imagem_fundo = pg.image.load('imagens/cruzeiroperdeu.jpg')
    if resposta == 'SANTOS':
        imagem_fundo = pg.image.load('imagens/santosperdeu.jpeg')
    if resposta == 'INTERNACIONAL':
        imagem_fundo = pg.image.load('imagens/interperdeu.jpg')
    if resposta == 'VASCO DA GAMA':
        imagem_fundo = pg.image.load('imagens/vascoperdeu.jpg')
    if resposta == 'ATLETICO MINEIRO':
        imagem_fundo = pg.image.load('imagens/galoperdeu.jpg')
    if resposta == 'FLAMENGO':
        imagem_fundo = pg.image.load('imagens/flamengoperdeu.jpg')
    if resposta == 'CORINTHIANS':
        imagem_fundo = pg.image.load('imagens/corinthiansperdeu.jpg')
    if resposta == 'GREMIO':
        imagem_fundo = pg.image.load('imagens/gremioperdeu.jpg')
    if resposta == 'PALMEIRAS':
        imagem_fundo = pg.image.load('imagens/palmeirasperdeu.jpeg')
    if resposta == 'SAO PAULO':
        imagem_fundo = pg.image.load('imagens/saopauloperdeu.jpg')

    imagem_fundo = pg.transform.scale(imagem_fundo, (1000, 600))
    window.blit(imagem_fundo, (0, 0))

    superficie_escura = pg.Surface((1000, 600))
    superficie_escura.fill((0, 0, 0))
    superficie_escura.set_alpha(150)
    window.blit(superficie_escura, (0, 0))

    texto_titulo = fonte_titulo.render("Você perdeu!", True, vermelho)
    largura_texto_titulo = texto_titulo.get_width()
    pos_x_titulo = (1000 - largura_texto_titulo) / 2
    pos_y_titulo = 100
    window.blit(texto_titulo, (pos_x_titulo, pos_y_titulo))

    texto_resposta = fonte_rb.render(f"A resposta era: {resposta}", True, branco)
    largura_texto_resposta = texto_resposta.get_width()
    pos_x_resposta = (1000 - largura_texto_resposta) / 2
    pos_y_resposta = 200
    window.blit(texto_resposta, (pos_x_resposta, pos_y_resposta))

    pg.draw.rect(window, cinza_claro, (50, 450, 300, 60))
    pg.draw.rect(window, cinza_escuro, (50, 450, 300, 60), 5)
    texto_voltar_menu = fonte_rb.render("Voltar ao Menu", True, branco)
    largura_texto_voltar = texto_voltar_menu.get_width()
    altura_texto_voltar = texto_voltar_menu.get_height()
    pos_x_voltar = (50 + 300 / 2) - largura_texto_voltar / 2
    pos_y_voltar = (450 + 60 / 2) - altura_texto_voltar / 2
    window.blit(texto_voltar_menu, (pos_x_voltar, pos_y_voltar))

    pg.draw.rect(window, verde, (650, 450, 300, 60))
    pg.draw.rect(window, amarelo, (650, 450, 300, 60), 5)
    texto_nova_rodada = fonte_rb.render("Nova Rodada", True, branco)
    largura_texto_nova_rodada = texto_nova_rodada.get_width()
    altura_texto_nova_rodada = texto_nova_rodada.get_height()
    pos_x_nova_rodada = 650 + (300 / 2) - (largura_texto_nova_rodada / 2)
    pos_y_nova_rodada = (450 + 60 / 2) - (altura_texto_nova_rodada / 2)
    window.blit(texto_nova_rodada, (pos_x_nova_rodada, pos_y_nova_rodada))

    voltar_menu = False
    nova_rodada = False

    if 50 <= x <= 350 and 450 <= y <= 510 and not click_last_status and click[0]:
        voltar_menu = True

    if 650 <= x <= 950 and 450 <= y <= 510 and not click_last_status and click[0]:
        nova_rodada = True

    return True, nova_rodada, voltar_menu

# Função para desenhar a tela de vitória
def Desenho_Tela_Vitoria(window, resposta, x, y, click, click_last_status):
    if resposta == 'CRUZEIRO':
        imagem_fundo = pg.image.load('imagens/cruzeiroganhou.jpg')
    if resposta == 'SANTOS':
        imagem_fundo = pg.image.load('imagens/santosganhou.jpeg')
    if resposta == 'INTERNACIONAL':
        imagem_fundo = pg.image.load('imagens/interganhou.jpg')
    if resposta == 'VASCO DA GAMA':
        imagem_fundo = pg.image.load('imagens/vascoganhou.jpg')
    if resposta == 'ATLETICO MINEIRO':
        imagem_fundo = pg.image.load('imagens/galoganhou.jpg')
    if resposta == 'FLAMENGO':
        imagem_fundo = pg.image.load('imagens/flamengoganhou.jpeg')
    if resposta == 'CORINTHIANS':
        imagem_fundo = pg.image.load('imagens/corinthiansganhou.jpg')
    if resposta == 'GREMIO':
        imagem_fundo = pg.image.load('imagens/gremioganhou.jpg')
    if resposta == 'PALMEIRAS':
        imagem_fundo = pg.image.load('imagens/palmeirasganhou.jpeg')
    if resposta == 'SAO PAULO':
        imagem_fundo = pg.image.load('imagens/saopauloganhou.jpg')

    imagem_fundo = pg.transform.scale(imagem_fundo, (1000, 600))
    window.blit(imagem_fundo, (0, 0))

    superficie_escura = pg.Surface((1000, 600))
    superficie_escura.fill((0, 0, 0))
    superficie_escura.set_alpha(150)
    window.blit(superficie_escura, (0, 0))

    texto_titulo = fonte_titulo.render("Você ganhou!", True, verde)
    largura_texto_titulo = texto_titulo.get_width()
    pos_x_titulo = (1000 - largura_texto_titulo) / 2
    pos_y_titulo = 100
    window.blit(texto_titulo, (pos_x_titulo, pos_y_titulo))

    texto_resposta = fonte_rb.render(f"A resposta era: {resposta}", True, branco)
    largura_texto_resposta = texto_resposta.get_width()
    pos_x_resposta = (1000 - largura_texto_resposta) / 2
    pos_y_resposta = 200
    window.blit(texto_resposta, (pos_x_resposta, pos_y_resposta))

    pg.draw.rect(window, cinza_claro, (50, 450, 300, 60))
    pg.draw.rect(window, cinza_escuro, (50, 450, 300, 60), 5)
    texto_voltar_menu = fonte_rb.render("Voltar ao Menu", True, branco)
    largura_texto_voltar = texto_voltar_menu.get_width()
    altura_texto_voltar = texto_voltar_menu.get_height()
    pos_x_voltar = (50 + 300 / 2) - largura_texto_voltar / 2
    pos_y_voltar = (450 + 60 / 2) - altura_texto_voltar / 2
    window.blit(texto_voltar_menu, (pos_x_voltar, pos_y_voltar))

    pg.draw.rect(window, verde, (650, 450, 300, 60))
    pg.draw.rect(window, amarelo, (650, 450, 300, 60), 5)
    texto_nova_rodada = fonte_rb.render("Nova Rodada", True, branco)
    largura_texto_nova_rodada = texto_nova_rodada.get_width()
    altura_texto_nova_rodada = texto_nova_rodada.get_height()
    pos_x_nova_rodada = 650 + (300 / 2) - (largura_texto_nova_rodada / 2)
    pos_y_nova_rodada = (450 + 60 / 2) - (altura_texto_nova_rodada / 2)
    window.blit(texto_nova_rodada, (pos_x_nova_rodada, pos_y_nova_rodada))

    voltar_menu = False
    nova_rodada = False

    if 50 <= x <= 350 and 450 <= y <= 510 and not click_last_status and click[0]:
        voltar_menu = True

    if 650 <= x <= 950 and 450 <= y <= 510 and not click_last_status and click[0]:
        nova_rodada = True

    return True, nova_rodada, voltar_menu

# Loop principal do jogo
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
            pergunta, palavra_escolhida = Gerar_Pergunta()
            pergunta_gerada = True
            tentativas_de_letras = [' ', '-']
            chance = 0
            end_game = False

        Verificar_Botao_Sair(x, y, click, click_last_status)
        
    if jogo_iniciado:
        Desenho_da_Forca(window, chance)
        Desenho_Restart_Button(window)
        Desenho_Voltar_Menu_Button(window)
        Desenho_Letras_Tentadas(window, tentativas_de_letras)
        Mostrar_Pergunta(window, pergunta)

        if end_game:
            if not pergunta_gerada:
                pergunta, palavra_escolhida = Gerar_Pergunta()
                pergunta_gerada = True
                tentativas_de_letras = [' ', '-']
                chance = 0
                end_game = False

        palavra_camuflada = Camuflando_Palavra(palavra_escolhida, tentativas_de_letras)
        Palavra_do_Jogo(window, palavra_camuflada)

        Desenho_Conjuntos(window,
                        ['ATLETICO MINEIRO', 'CRUZEIRO', 'FLAMENGO', 'INTERNACIONAL', 'VASCO DA GAMA'],
                        ['CORINTHIANS', 'GREMIO', 'PALMEIRAS', 'SANTOS', 'SAO PAULO', 'VASCO DA GAMA'],
                        ['CORINTHIANS', 'CRUZEIRO', 'SÃO PAULO', 'VASCO DA GAMA'])

        if palavra_camuflada == palavra_escolhida:
            end_game = True
            resposta = palavra_escolhida
            game_victory, nova_rodada, voltar_menu = Desenho_Tela_Vitoria(window, resposta, x, y, click, click_last_status)

            if nova_rodada:
                pergunta, palavra_escolhida = Gerar_Pergunta()
                pergunta_gerada = True
                tentativas_de_letras = [' ', '-']
                chance = 0
                end_game = False

            if voltar_menu:
                jogo_iniciado = False
                tentativas_de_letras = ['', '-']
                chance = 0
                pergunta_gerada = False

        end_game, chance, tentativas_de_letras, pergunta_gerada = Restart_do_Jogo(end_game, chance, tentativas_de_letras, click_last_status, click, x, y, pergunta_gerada)

        jogo_iniciado = Voltar_Ao_Menu(x, y, click, click_last_status, jogo_iniciado)

    if chance == 6:
        resposta = palavra_escolhida
        game_over, nova_rodada, voltar_menu = Desenho_Tela_Game_Over(window, resposta, x, y, click, click_last_status)

        if voltar_menu:
            jogo_iniciado = False
            tentativas_de_letras = ['', '-']
            chance = 0
            pergunta_gerada = False
        
        if nova_rodada:
            pergunta, palavra_escolhida = Gerar_Pergunta()
            pergunta_gerada = True
            tentativas_de_letras = [' ', '-']
            chance = 0
            end_game = False

    click_last_status = click[0]

    pg.display.update()