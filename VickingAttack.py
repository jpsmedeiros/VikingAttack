__author__ = 'João Pedro Sá Medeiros' , 'Ian Lanza'
from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from random import  randint
from PPlay.collision import *
from PPlay.animation import *
from PPlay.sound import  *
from pygame import *
#Subprogramas
def inimigo1():
    soldado1 = Sprite("imagens\soldado1\.teste2.png", 9)
    larguraSol1 = soldado1.width
    alturaSol1 = soldado1.height
    soldado1.set_sequence(0, 5)
    soldado1.set_total_duration(1000)
    soldado1.set_position(0, 140-alturaSol1)
    #Troca de animação dependendo da direção do movimento(A fazer...)
    return soldado1
def movimentacao(posX, posY, objeto):
    #Condições diferentes para cada cenário, tais coordenadas valem para o cenário 1.3.5
    if (int(posX) < 390) and (int(posY) in range(90, 150)):
        objeto.move_x(1)
        objeto.move_y(0)
    if int(posX) in range(390, 395) and int(posY) in range(90, 330):
        objeto.move_x(0)
        objeto.move_y(1)
    if int(posX) in range(423, 60, -1) and int(posY) in range(250, 265):
        objeto.move_x(-1)
        objeto.move_y(0)
    if (int(posX) < 90) and int(posY) in range(250, 500):
        objeto.move_x(0)
        objeto.move_y(1)
    if (int(posX) in range(70, 630)) and (int(posY) in range(415, 500)):
        objeto.move_x(1)
        objeto.move_y(0)
    if (int(posX) in range(630, 635)) and int(posY) in range(475, 255, -1):
        objeto.move_x(0)
        objeto.move_y(-1)
    if int(posX) in range(630, 460, -1) and int(posY) in range(250, 260):
        objeto.move_x(-1)
        objeto.move_y(0)
    if int(posX) in range(460, 465) and int(posY) in range(258, 90, -1):
        objeto.move_x(0)
        objeto.move_y(-1)
    if int(posX) in range(460, 660) and int(posY) in range(90, 95):
        objeto.move_x(1)
        objeto.move_y(0)
    if int(posX) in range(660, 670) and int(posY) in range(90, 100):
        print("PERDEU")
    return
#Fundo
background = GameImage("imagens\cenarios\cenario1.3.5.png")
background.set_position(0, 0)
larguraFundo = background.width
alturaFundo = background.height
#Janela
larguraJanela = 800
alturaJanela = 608
janela = Window(larguraFundo, alturaFundo)
janela.set_title("Viking Attack")
janela.set_background_color((0, 0, 0))

#Define o ícone obs:(Não funciona completamente)
icone = pygame.image.load("imagens\icone.jpg").convert_alpha()
pygame.display.set_icon(icone)
#Inimigos
soldado1 = inimigo1()
#Musica
kingarthur = Sound("musicas\kingarthur.ogg")
kingarthur.set_volume(10)
#GameLoop
while True:
    janela.set_background_color((0, 0, 0))
    background.draw()
    #Inimigos
    #Soldado1
    soldado1.move_x(0)
    soldado1.move_y(0)
    soldado1.update()
    soldado1.draw()
    #Movimentacao
    posXSol1 = soldado1.x
    posYSol1 = soldado1.y
    print(posXSol1)
    print(posYSol1)
    movimentacao(posXSol1, posYSol1, soldado1)
    #Musica
    kingarthur.play()
    janela.update()