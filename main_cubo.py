'''
Esse é o código principal para a execução do cubo mágico 3x3x3, integrando as representações 2D e 3D.

Ele utiliza os dados e funções definidas em `logica_rot_cubo.py` e `construtor_cubo.py`
para manipular o estado do cubo, aplicar rotações e renderizar as faces do cubo em Pygame e OpenGL.

Lembre-se de colocar os arquivos `logica_rot_cubo.py` e `construtor_cubo.py` no mesmo diretório.
'''

import pygame
import time
import pyperclip
from OpenGL.GL import *
from OpenGL.GLU import *
import construtor_cubo as c
import logica_rot_cubo as r

# Setup Pygame
pygame.init()
tela = pygame.display.set_mode((1300, 600), pygame.DOUBLEBUF | pygame.OPENGL)
pygame.display.set_caption("Rubik's Cube 3x3 - Representações 2D e 3D")
clock = pygame.time.Clock()
FONTE = pygame.font.SysFont("arial", 18)

fonte_entrada = pygame.font.SysFont("arial", 20)
entrada_texto = ""
campo_ativo = False
retangulo_entrada = pygame.Rect(50, 470, 600, 30)
contador_cursor = 0

botoes = {
    "embaralhar": pygame.Rect(75, 520, 100, 40),
    "reiniciar": pygame.Rect(225, 520, 100, 40),
    "voltar": pygame.Rect(375, 520, 100, 40),
    "avancar": pygame.Rect(525, 520, 100, 40)
}

# Setup OpenGL
glViewport(600, 0, 600, 600)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
gluPerspective(45, 1, 0.1, 100.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()
glTranslatef(0, 0, 20)
glEnable(GL_DEPTH_TEST)

angulo = 0
velocidade_auto = 0.3
rotacao_manual = [0, 0]
auto_rotacao = True

ultima_tecla = None
tempo_ultima = 0

# Loop principal
rodar = True
while rodar:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodar = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            campo_ativo = retangulo_entrada.collidepoint(evento.pos)
            for rect in c.retangulos_hist:
                if rect.collidepoint(evento.pos):
                    pyperclip.copy(" ".join(c.historico[:c.indice_movimento+1]))
                    copiado = True
                    tempo_copiado = time.time()
            # Botões
            for nome, botao in botoes.items():
                if botao.collidepoint(evento.pos):
                    if nome == "embaralhar": c.embaralhar()
                    elif nome == "reiniciar": c.reiniciar()
                    elif nome == "voltar": c.desfazer_movimento()
                    elif nome == "avancar": c.refazer_movimento()

        elif evento.type == pygame.TEXTINPUT and campo_ativo:
            ch = evento.text.upper()
            if ch in "UDFBLR'2, ":
                entrada_texto += ch

        elif evento.type == pygame.KEYDOWN:
            key = pygame.key.name(evento.key)
            mods = pygame.key.get_mods()
            teclas = {'u','d','f','b','l','r'}

            if evento.key == pygame.K_SPACE:
                auto_rotacao = not auto_rotacao

            elif evento.key == pygame.K_LEFT:
                rotacao_manual[1] -= 5
                auto_rotacao = False
            elif evento.key == pygame.K_RIGHT:
                rotacao_manual[1] += 5
                auto_rotacao = False
            elif evento.key == pygame.K_UP:
                rotacao_manual[0] -= 5
                auto_rotacao = False
            elif evento.key == pygame.K_DOWN:
                rotacao_manual[0] += 5
                auto_rotacao = False

            if campo_ativo and evento.key == pygame.K_v and (mods & pygame.KMOD_CTRL):
                clip = pyperclip.paste().replace('\r','')
                for h in clip.upper():
                    if h in "UDFBLR'2, ":
                        entrada_texto += h
                continue

            if campo_ativo:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_texto = entrada_texto[:-1]
                elif evento.key == pygame.K_RETURN:
                    seq = [m.strip() for m in entrada_texto.split(" ") if m.strip()]
                    for mov in seq:
                        m = mov.upper()
                        if m in r.PERMUTACOES:
                            c.aplicar_movimento(m)
                        elif len(m) == 2 and m[1] == '2' and m[0] in 'UDFBLR':
                            c.aplicar_movimento(m[0])
                            c.aplicar_movimento(m[0])
                    entrada_texto = ""
                continue

            if key in teclas:
                now = time.time()
                if key == ultima_tecla and now - tempo_ultima < 0.5:
                    m = key.upper()
                    if m in r.PERMUTACOES:
                        c.aplicar_movimento(m)
                    ultima_tecla = None
                else:
                    ultima_tecla = key
                    tempo_ultima = now

            elif key in {'1','2'} and ultima_tecla in teclas:
                face = ultima_tecla.upper()
                if key == '1' and face + "'" in r.PERMUTACOES:
                    c.aplicar_movimento(face + "'")
                elif key == '2' and face in r.PERMUTACOES:
                    c.aplicar_movimento(face)
                    c.aplicar_movimento(face)
                ultima_tecla = None

    # Reconstruir peças 3D com estado atual do cubo
    pecas3d = c.construir_pecas(c.cubo_3d)

    # Limpa tela (2D parte esquerda)
    tela_2d = pygame.Surface((700, 600))
    tela_2d.fill((30, 30, 30))

    c.desenhar_instrucoes(tela_2d, FONTE)
    current = c.historico[:c.indice_movimento+1]
    grupos = [current[i:i+10] for i in range(0, len(current), 10)]
    c.retangulos_hist.clear()
    for i, grupo in enumerate(grupos):
        linha = " ".join(grupo)
        texto = FONTE.render(linha, True, (255, 255, 255))
        x, y = 20, 100 + i * 22
        tela_2d.blit(texto, (x, y))
        c.retangulos_hist.append(pygame.Rect(x, y, texto.get_width(), texto.get_height()))

    c.desenhar_botoes(tela_2d, FONTE, botoes)
    order = ['U', 'L', 'F', 'R', 'B', 'D']
    indices = [0,9,18,27,36,45]
    for face, idx in zip(order, indices):
        c.desenhar_face(tela_2d, c.cubo_2d[idx:idx+9], c.POS_FACES_2D[face])

    pygame.draw.rect(tela_2d, (255,255,255), retangulo_entrada, 2)
    surf = fonte_entrada.render(entrada_texto, True, (255,255,255))
    tela_2d.blit(surf, (retangulo_entrada.x+5, retangulo_entrada.y+5))
    if campo_ativo:
        contador_cursor += 1
        if (contador_cursor//30)%2 == 0:
            x = retangulo_entrada.x+5+surf.get_width()
            y = retangulo_entrada.y+5
            pygame.draw.line(tela_2d, (255,255,255), (x, y), (x, y+20), 2)
    else:
        contador_cursor = 0

    instr = FONTE.render("Digite movimentos separados por espaço e pressione Enter", True, (200, 200, 200))
    tela_2d.blit(instr, (retangulo_entrada.x + 110, retangulo_entrada.y - 22))

    if c.copiado and time.time() - tempo_copiado < 1:
        msg = FONTE.render("Copiado!", True, (200, 255, 200))
        tela_2d.blit(msg, (550, 90))
    elif c.copiado:
        c.copiado = False

    # Render 3D (direita)
    glViewport(700, 0, 600, 600)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0, 0, -20)
    if auto_rotacao:
        angulo += velocidade_auto
        glRotatef(angulo, 1, 1, 0)
    else:
        glRotatef(rotacao_manual[0], 1, 0, 0)
        glRotatef(rotacao_manual[1], 0, 1, 0)

    for peca in pecas3d:
        c.desenhar_peca(peca)

    # Render 2D (esquerda)
    glViewport(0, 0, 700, 600)
    glDisable(GL_DEPTH_TEST)
    data = pygame.image.tostring(tela_2d, "RGB", True)
    glWindowPos2d(0, 0)
    glDrawPixels(tela_2d.get_width(), tela_2d.get_height(), GL_RGB, GL_UNSIGNED_BYTE, data)
    glEnable(GL_DEPTH_TEST)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
