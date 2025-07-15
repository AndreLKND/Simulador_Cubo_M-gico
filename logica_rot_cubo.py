'''
Esse código define as rotações de um cubo mágico 3x3x3 e suas permutações.
O cubo é representado por uma lista de 54 posições, onde cada posição
corresponde a um sticker(adesivo) do mesmo.

As rotações são definidas por listas de permutações, onde cada índice representa
uma posição do cubo e o valor nesse índice indica a nova posição desse sticker

A função `aplicar_rot` recebe o estado atual do cubo e uma rotação,
e retorna uma nova lista de 54 cores (adesivos), permutadas conforme a rotação especificada.
'''

# Rotação U (Horario)
rot_U = list(range(54))
rot_face_U = {0:2, 1:5, 2:8, 3:1, 4:4, 5:7, 6:0, 7:3, 8:6}
for i_orig, i_dest in rot_face_U.items():
    rot_U[i_dest] = i_orig
# Rotação U_adj
bordas_adj_U = [(18, 27, 36, 9), (19, 28, 37, 10), (20, 29, 38, 11)]
for (f, r, b, l) in bordas_adj_U:
    rot_U[f] = r
    rot_U[r] = b
    rot_U[b] = l
    rot_U[l] = f
# Rotação U' (Anti-horario)
rot_Ui = list(range(54))
for i_orig, i_dest in rot_face_U.items():
    rot_Ui[i_orig] = i_dest
# Rotação U'_adj
for (f, r, b, l) in bordas_adj_U:
    rot_Ui[f] = l
    rot_Ui[r] = f
    rot_Ui[b] = r
    rot_Ui[l] = b

# Rotação L (Horario)
rot_L = list(range(54))
rot_face_L = {9:11, 10:14, 11:17, 12:10, 13:13, 14:16, 15:9, 16:12, 17:15}
for i_orig, i_dest in rot_face_L.items():
    rot_L[i_dest] = i_orig
# Rotação L_adj
bordas_adj_L = [(0, 44, 45, 18), (3, 41, 48, 21), (6, 38, 51, 24)]
for (u, b, d, f) in bordas_adj_L:
    rot_L[u] = b
    rot_L[b] = d
    rot_L[d] = f
    rot_L[f] = u
# Rotação L' (Anti-horario)
rot_Li = list(range(54))
for i_orig, i_dest in rot_face_L.items():
    rot_Li[i_orig] = i_dest
# Rotação L'_adj
for (u, b, d, f) in bordas_adj_L:
    rot_Li[u] = f
    rot_Li[f] = d
    rot_Li[d] = b
    rot_Li[b] = u

# Rotação F (Horario)
rot_F = list(range(54))
rot_face_F = {18:20, 19:23, 20:26, 21:19, 22:22, 23:25, 24:18, 25:21, 26:24}
for i_orig, i_dest in rot_face_F.items():
    rot_F[i_dest] = i_orig
# Rotação F_adj
bordas_adj_F = [(6, 17, 47, 27), (7, 14, 46, 30), (8, 11, 45, 33)]
for (u, l, d, r) in bordas_adj_F:
    rot_F[u] = l
    rot_F[l] = d
    rot_F[d] = r
    rot_F[r] = u
# Rotação F' (Anti-horario)
rot_Fi = list(range(54))
for i_orig, i_dest in rot_face_F.items():
    rot_Fi[i_orig] = i_dest
# Rotação F'_adj
for (u, l, d, r) in bordas_adj_F:
    rot_Fi[u] = r
    rot_Fi[r] = d
    rot_Fi[d] = l
    rot_Fi[l] = u

# Rotação R (Horario)
rot_R = list(range(54))
rot_face_R = {27:29, 28:32, 29:35, 30:28, 31:31, 32:34, 33:27, 34:30, 35:33}
for i_orig, i_dest in rot_face_R.items():
    rot_R[i_dest] = i_orig
# Rotação R_adj
bordas_adj_R = [(8, 26, 53, 36), (5, 23, 50, 39), (2, 20, 47, 42)]
for (u, f, d, b) in bordas_adj_R:
    rot_R[u] = f
    rot_R[f] = d
    rot_R[d] = b
    rot_R[b] = u
# Rotação R' (Anti-horario)
rot_Ri = list(range(54))
for i_orig, i_dest in rot_face_R.items():
    rot_Ri[i_orig] = i_dest
# Rotação R'_adj
for (u, f, d, b) in bordas_adj_R:
    rot_Ri[u] = b
    rot_Ri[b] = d
    rot_Ri[d] = f
    rot_Ri[f] = u

# Rotação B (Horario)
rot_B = list(range(54))
rot_face_B = {36:38, 37:41, 38:44, 39:37, 40:40, 41:43, 42:36, 43:39, 44:42}
for i_orig, i_dest in rot_face_B.items():
    rot_B[i_dest] = i_orig
# Rotação B_adj
bordas_adj_B = [(2, 35, 51, 9), (1, 32, 52, 12), (0, 29, 53, 15)]
for (u, r, d, l) in bordas_adj_B:
    rot_B[u] = r
    rot_B[r] = d
    rot_B[d] = l
    rot_B[l] = u
# Rotação B' (Anti-horario)
rot_Bi = list(range(54))
for i_orig, i_dest in rot_face_B.items():
    rot_Bi[i_orig] = i_dest
# Rotação B'_adj
for (u, r, d, l) in bordas_adj_B:
    rot_Bi[u] = l
    rot_Bi[l] = d
    rot_Bi[d] = r
    rot_Bi[r] = u

# Rotação D (Horario)
rot_D = list(range(54))
rot_face_D = {45:47, 46:50, 47:53, 48:46, 49:49, 50:52, 51:45, 52:48, 53:51}
for i_orig, i_dest in rot_face_D.items():
    rot_D[i_dest] = i_orig
# Rotação D_adj
bordas_adj_D = [(24, 15, 42, 33), (25, 16, 43, 34), (26, 17, 44, 35)]
for (f, l, b, r) in bordas_adj_D:
    rot_D[f] = l
    rot_D[l] = b
    rot_D[b] = r
    rot_D[r] = f
# Rotação D' (Anti-horario)
rot_Di = list(range(54))
for i_orig, i_dest in rot_face_D.items():
    rot_Di[i_orig] = i_dest
# Rotação D'_adj
for (f, l, b, r) in bordas_adj_D:
    rot_Di[f] = r
    rot_Di[r] = b
    rot_Di[b] = l
    rot_Di[l] = f


# Dicionário geral de todos os movimentos e suas permutações
PERMUTACOES = {
    "U":  rot_U,
    "U'": rot_Ui,
    "D":  rot_D,
    "D'": rot_Di,
    "F":  rot_F,
    "F'": rot_Fi,
    "B":  rot_B,
    "B'": rot_Bi,
    "L":  rot_L,
    "L'": rot_Li,
    "R":  rot_R,
    "R'": rot_Ri
}

# Função para aplicar uma rotação ao estado do cubo e retornar um novo estado.
def aplicar_rot(cubo_estado, rot):
    """
    Retorna uma lista nova de 54 cores, permutadas conforme o vetor rot (de 54 elementos).
    cubo_estado: lista de 54 strings (cores atuais).
    rot: lista de 54 inteiros (nova ordem).
    """
    return [cubo_estado[i_origem] for i_origem in rot]

