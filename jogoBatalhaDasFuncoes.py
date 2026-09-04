import pygame # importando a biblioteca pygame
pygame.init() # inicializando o pygame
LARGURA = 900
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA)) # definir o tamanho da tela
pygame.display.set_caption("Batalha das Funções") # definindo o título da tela

AZUL_ESCURO = (8, 18, 45) # definindo a cor azul escuro
BRANCO = (245, 245, 245) # definindo a cor branca

fonte = pygame.font.SysFont("arial", 40, bold=True) # definindo a fonte do texto 
titulo = fonte.render(
    "BATALHA DAS FUNÇÕES",
    True,
    BRANCO
)
#fonte para o texto da missão
fonte_texto = pygame.font.SysFont(
    "arial",
    24
)
# texto da missão
missao = fonte_texto.render(
    "Reconecte a rede de energia!",
    True,
    BRANCO
)

# Carrega a imagem
fundo = pygame.image.load("imagens/background.png").convert()

# Ajusta para o tamanho da janela
fundo = pygame.transform.scale(fundo, (LARGURA, ALTURA))


rodando = True # loop principal do jogo

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    tela.fill(AZUL_ESCURO) # preenchendo a tela com a cor azul
    tela.blit(fundo, (0, 0)) # Coloca a imagem no fundo
    tela.blit(titulo, (230, 100))# desenhando o título na tela
    tela.blit(missao, (290, 170)) # desenhando a missão na tela
    pygame.display.flip() # atualizando a tela
pygame.quit()