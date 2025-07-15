========================================================================================================================
				  SIMULADOR DE CUBO MÁGICO INTERATIVO USANDO PYTHON
========================================================================================================================

Projeto para obtenção do título de Graduação em Licenciatura em Matemática 
Universidade Federal do Delta do Parnaíba (UFDPar)

Tema do Trabalho: Rubik's Cube: Uma Abordagem Computacional Usando Python

Desenvolvido por: 
André Luis Araújo Oliveira  

Orientado por: 
Prof. Dr. Paulo Sérgio Marques dos Santos

------------------------------------------------------------------------------------------------------------------------

Visão Geral:

Este projeto implementa um simulador de Cubo Mágico 3x3 em Python, com visualizações 2D e 3D interativas construídas 
usando as bibliotecas PyOpenGL e Pygame para as manipulações e representações gráficas.
Tem como objetivo unir conceitos de:

- Teoria dos Grupos e Análise Combinatória (movimentação e permutações do cubo).  
- Programação em Python, incluindo boas práticas e modularização de código.  
- Gráficos 3D com OpenGL e integração com pygame para renderização em tempo real.

------------------------------------------------------------------------------------------------------------------------

Principais Objetivos:

1. Modelagem Computacional  
   – Representar e manipular o estado do cubo (faces, peças e orientações) de forma estruturada e eficiente.  
2. Visualização Gráfica 3D  
   – Renderizar o cubo em 3D com OpenGL, permitindo rotações de câmera e visualização instantânea de cada movimento.  
3. Interatividade  
   – Controlar rotações do cubo (U, D, L, R, F, B e suas inversas) via botões, teclado ou campo de texto.  
   – Funções de desfazer/refazer movimentos, embaralhamento e reset do estado inicial.  
4. Aprendizado e Ensino  
   – Servir de base prática para demonstrações em aulas de matemática abstrata, programação e computação gráfica.  
5. Manutenção e Extensão  
   – Arquitetura modular (separação clara entre lógica de permutações, construção de peças 3D e interface) para permitir 
futuras melhorias (algoritmos de resolução automática, exportação de vídeo, modos de jogo).

------------------------------------------------------------------------------------------------------------------------

Estruturas do Programa:

- Representação 2D e 3D:
Divididas ao meio da tela do programa (esquerda 2D, direita 3D)

- Instruções:
Canto superior esquerdo, explica de forma resumida os controles do programa.

- Histórico de Movimentos:
Localizado à esquerda da representação 2D, a cada 10 movimentos pula uma linha.

- Campo Ativo:
Localizado abaixo da representação 2D, recebe os algoritmos de movimentos e suas variantes (ex.: U, U', U2) 
separados por espaço.

- Botões:
	- Embaralhar:
	Aplica 20 movimentos aleatórios usando a biblioteca random.
	- Reiniciar:
	Volta o cubo pro estado resolvido.
	- Voltar:
	Volta 1 movimento já realizado.
	- Avançar:
	Avança um movimento que foi voltado.

------------------------------------------------------------------------------------------------------------------------

- Controles e Como Utilizar:
	- Teclas válidas: u, l, f, r, b, d, 1, 2, espaço, setas do teclado
	
	- Formas de usar:

	- Um toque duplo nas letras (u, l, f, r, b, d) Realiza um movimento horário na face correspondente
	- Um toque único nas letras (u, l, f, r, b, d) seguido de um toque único no número 1 Realiza um movimento 
	anti-horário na fase correspondente. 
	- Um toque único nas letras (u, l, f, r, b, d) seguido de um toque único no número 2 Realiza um movimento 
	duplo na fase correspondente.

	- A tecla espaço ativa e desativa a rotação automática do cubo 3D. 
	- As teclas de setas do teclado desativam a rotação automática e realizam a rotação manual do cubo

	- O mouse ativa os botões e o Campo ativo
	- Quando o Campo ativo está selecionado, as teclas do teclado não funcionam, para voltar a funcionar, basta
	clicar fora do Campo ativo.

------------------------------------------------------------------------------------------------------------------------

1. Pré-requisitos: 
	- Python 3.8 ou superior   
	- pygame 
	- PyOpenGL 
	- pyperclip

2. Instalação  
   ```bash
   git clone https://github.com/AndreLKND/Simulador_Cubo_Magico.git
   cd Simulador_Cubo_Magico
   pip install -r requirements.txt
   ```

3. Execução  
   ```bash
   python main_cubo.py
   ```

------------------------------------------------------------------------------------------------------------------------

Contribuições

Contribuições são muito bem‑vindas! Sinta‑se à vontade para:

- Abrir issues para bugs ou sugestões.  
- Enviar pull requests com novos recursos ou melhorias.  
- Discutir no discussions sobre métodos de resolução, interfaces ou performance.

Antes de submeter, por favor siga as diretrizes de estilo no arquivo CONTRIBUTING.md.

------------------------------------------------------------------------------------------------------------------------

Referências

- ARAUJO OLIVEIRA, André Luis. Rubik's Cube: Uma Abordagem Computacional Usando Python. Monografia 
(Licenciatura em Matemática) - Universidade Federal do Delta do Parnaíba, Parnaíba, 2025. Disponível em: 
https:. Acesso em: 15 jul. 2025.

