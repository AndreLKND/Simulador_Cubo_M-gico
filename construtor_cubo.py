'''
Esse código define as funções necessárias para construir e manipular um cubo mágico 3x3x3,
incluindo a representação 2D e 3D, bem como as operações de rotação e manipulação do cubo.

Além disso, ele inclui a lógica para desenhar as faces do cubo em 2D e 3D, 
utilizando as bibliotecas Pygame e OpenGL.
'''

import pygame
import random
from OpenGL.GL import *
from OpenGL.GLU import *
from logica_rot_cubo import aplicar_rot, PERMUTACOES


# Predefinições
iniciais_2d = (
    ['branco'] * 9 + 
    ['laranja'] * 9 + 
    ['verde'] * 9 + 
    ['vermelho'] * 9 + 
    ['azul'] * 9 + 
    ['amarelo'] * 9
)
cubo_2d = iniciais_2d.copy()
iniciais_3d = (
    ['branco'] * 9 + 
    ['laranja'] * 9 + 
    ['verde'] * 9 + 
    ['vermelho'] * 9 + 
    ['azul'] * 9 + 
    ['amarelo'] * 9
)
cubo_3d = iniciais_3d.copy()

historico = []
indice_movimento = -1
copiado = False
tempo_copiado = 0
retangulos_hist = []

TMH_PECA = 30
MARGEM = 2

POS_CORES = {
    "branco": (255, 255, 255),
    "amarelo": (255, 255, 0),
    "vermelho": (255, 0, 0),
    "laranja": (255, 120, 0),
    "verde": (0, 240, 0),
    "azul": (0, 0, 255),
    None: (50, 50, 50),
}

CORES_RGB = {k: tuple(c/255 for c in v) for k, v in POS_CORES.items()}

POS_FACES_2D = {
    "U": (300, 120),
    "L": (200, 220),
    "F": (300, 220),
    "R": (400, 220),
    "B": (500, 220),
    "D": (300, 320),    
}

# Classe para as peças 3D
class Peca3D:
    def __init__(self, pos):
        self.pos = pos
        self.faces = [None]*6

    def set_face_color(self, face, cor):
        idx = {'U':0, 'L':1, 'F':2, 'R':3, 'B':4, 'D':5}[face]
        self.faces[idx] = cor

# Função para construir as peças 3D a partir do estado do cubo
def construir_pecas(cubo):
    pecas = []
    posicoes_pecas = [(x, y, z)
                      for x in (-1, 0, 1)
                      for y in (-1, 0, 1)
                      for z in (-1, 0, 1)
                      if (x, y, z) != (0, 0, 0)]

    face_idx = {
        'U':  0,
        'L':  9,
        'F': 18,
        'R': 27,
        'B': 36,
        'D': 45
    }

    for x, y, z in posicoes_pecas:
        peca = Peca3D((x, y, z))

        if y == 1:
            linha  = z + 1 
            coluna = x + 1
            idx    = linha*3 + coluna
            peca.set_face_color('U', cubo[face_idx['U'] + idx])

        if y == -1:
            linha  = 1 - z 
            coluna = x + 1
            idx    = linha*3 + coluna
            peca.set_face_color('D', cubo[face_idx['D'] + idx])

        if x == -1:
            linha  = 1 - y
            coluna = z + 1       
            idx    = linha*3 + coluna
            peca.set_face_color('L', cubo[face_idx['L'] + idx])

        if x == 1:
            linha  = 1 - y
            coluna = 1 - z
            idx    = linha*3 + coluna
            peca.set_face_color('R', cubo[face_idx['R'] + idx])

        if z == 1:
            linha  = 1 - y
            coluna = x + 1
            idx    = linha*3 + coluna
            peca.set_face_color('F', cubo[face_idx['F'] + idx])

        if z == -1:
            linha  = 1 - y
            coluna = 1 - x
            idx    = linha*3 + coluna
            peca.set_face_color('B', cubo[face_idx['B'] + idx])

        pecas.append(peca)

    return pecas

# Função para desenhar uma peça 3D
def desenhar_peca(peca):
    x, y, z = [i * 2.1 for i in peca.pos]
    glPushMatrix()
    glTranslatef(x, y, z)

    faces = [
        ([(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)], peca.faces[2]), 
        ([(1,-1,1),(1,-1,-1),(1,1,-1),(1,1,1)], peca.faces[3]),
        ([(1,-1,-1),(-1,-1,-1),(-1,1,-1),(1,1,-1)], peca.faces[4]),
        ([(-1,-1,-1),(-1,-1,1),(-1,1,1),(-1,1,-1)], peca.faces[1]),
        ([(-1,1,1),(1,1,1),(1,1,-1),(-1,1,-1)], peca.faces[0]),
        ([(-1,-1,-1),(1,-1,-1),(1,-1,1),(-1,-1,1)], peca.faces[5])
    ]

    for quad, cor in faces:
        if cor is None:
            glColor3f(0.1,0.1,0.1)
        else:
            glColor3fv(CORES_RGB[cor])
        glBegin(GL_QUADS)
        for v in quad:
            glVertex3f(*v)
        glEnd()
    glPopMatrix()
    
# Funções 2D (desenho de faces e interface)
def desenhar_face(tela, face_cores, origem):
    for idx in range(9):
        i, j = divmod(idx, 3)
        cor = POS_CORES.get(face_cores[idx], (100, 100, 100))
        x = origem[0] + j * (TMH_PECA + MARGEM)
        y = origem[1] + i * (TMH_PECA + MARGEM)
        pygame.draw.rect(tela, cor, (x, y, TMH_PECA, TMH_PECA))
        pygame.draw.rect(tela, (0, 0, 0), (x, y, TMH_PECA, TMH_PECA), 1)

def desenhar_instrucoes(tela, fonte):
    instrucoes = [
        "Controles: Duplo toque na tecla da face = (U, F, R, L, B, D)",
        "Toque único + 1 = (U', F', R', L', B', D') | Toque único + 2 = (U2, F2, R2, L2, B2, D2)",
        "==========================================================================",
        "Histórico:",
    ]
    for idx, linha in enumerate(instrucoes):
        text = fonte.render(linha, True, (255, 255, 255))
        tela.blit(text, (20, 10 + idx * 22))

def desenhar_botoes(tela, fonte, botoes):
    mouse_pos = pygame.mouse.get_pos()
    for nome, botao in botoes.items():
        sobre = botao.collidepoint(mouse_pos)
        cor_fundo = (80, 230, 230) if sobre else (100, 255, 255)
        pygame.draw.rect(tela, cor_fundo, botao, border_radius=8)
        texto = fonte.render(nome.capitalize(), True, (0, 0, 0))
        texto_x = botao.x + (botao.width - texto.get_width()) // 2
        texto_y = botao.y + (botao.height - texto.get_height()) // 2
        tela.blit(texto, (texto_x, texto_y))

# Funções gerais de movimentos
def aplicar_movimento(mov):
    global cubo_2d, cubo_3d, historico, indice_movimento
    cubo_2d = aplicar_rot(cubo_2d, PERMUTACOES[mov])
    cubo_3d = aplicar_rot(cubo_3d, PERMUTACOES[mov])
    historico = historico[:indice_movimento + 1] + [mov]
    indice_movimento += 1

def inverter_movimento(mov):
    return mov + "'" if "'" not in mov else mov[0]

def desfazer_movimento():
    global cubo_2d, cubo_3d, indice_movimento
    if indice_movimento >= 0:
        mov = historico[indice_movimento]
        cubo_2d = aplicar_rot(cubo_2d, PERMUTACOES[inverter_movimento(mov)])
        cubo_3d = aplicar_rot(cubo_3d, PERMUTACOES[inverter_movimento(mov)])
        indice_movimento -= 1

def refazer_movimento():
    global cubo_2d, cubo_3d, indice_movimento
    if indice_movimento + 1 < len(historico):
        indice_movimento += 1
        cubo_2d = aplicar_rot(cubo_2d, PERMUTACOES[historico[indice_movimento]])
        cubo_3d = aplicar_rot(cubo_3d, PERMUTACOES[historico[indice_movimento]])

def embaralhar():
    for _ in range(20):
        aplicar_movimento(random.choice(list(PERMUTACOES.keys())))

def reiniciar():
    global cubo_2d, cubo_3d, historico, indice_movimento
    cubo_2d = iniciais_2d.copy()
    cubo_3d = iniciais_3d.copy()
    historico.clear()
    indice_movimento = -1
