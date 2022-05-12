# -*- coding: utf-8 -*-

import sys, pygame
from random import *


pygame.init()

SCREEN_SIZE=(800,500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Genius confusão")

#cores em RGB
BRANCO_COR= (255,255,255)
ROSA_COR = (255, 78, 183)
AMARELO_CLARO_COR= (255, 255, 27)
AZUL_COR=(55, 102, 253)
VERDE_COR=(55, 251, 49)
PRETO_COR=(0,0,0)
VERDE_LIMAO_COR=(169, 255, 36)

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()


#caminhos pastas
caminho_fontes = "fonts//"



#fontes
arial_font = pygame.font.SysFont('arial',40)
quickens_font = pygame.font.Font(caminho_fontes+"QUICKENS.ttf",55)
yogurt_mango_font = pygame.font.Font(caminho_fontes+"Yogurt Mango.ttf", 40)
yogurt_mango_font_maior = pygame.font.Font(caminho_fontes+"Yogurt Mango.ttf", 50)



#Vetores
vetor_cores=[ROSA_COR, AMARELO_CLARO_COR, AZUL_COR, VERDE_COR]
vetor_rects=[0,0,0,0]
vetor_cores_nomes=["Rosa", "Amarelo", "Azul", "Verde"]

#Flags
tela_inicio_jogo = True 
comeco_jogo = False


class Tela():
    
    tela_inicio_jogo = True 
    comeco_jogo = False
    valor = 125
    pos_x = 0
    pos_y = 0
    vetor_posicao_circulos = [225, 350, 475, 600]
    vetor_pos = [0,0]
    flag_colisao = False
    num_cor = 0
    num_cor_do_texto = 0
    sorteio = True
    cor_clicada = ""
    dic = {}
    pontos = 0
    
    # pos_x = (SCREEN_SIZE[0]-500)/2
    
    # def __init__(self):
    
    
    def inicializa_dicionario(self):
        
        dic = {vetor_cores_nomes[0]:"", vetor_cores_nomes[1]:"", vetor_cores_nomes[2]:"", vetor_cores_nomes[3]:""}
        

    def desenha_circulos(self):
        # self.pos_x = 225
        self.pos_y = 350
        i = 0
        for cor in vetor_cores:
            rect = pygame.draw.circle(screen, cor, (self.vetor_posicao_circulos[i], self.pos_y), 50)
            vetor_rects[i] = rect
            self.dic[vetor_cores_nomes[i]]=rect
              
            i+=1
            
            
   

    def checa_colisao(self):
        

        pygame.event.pump()
        click = pygame.mouse.get_pressed()
        
        if  click[0]:
            for rect in vetor_rects:
                
                point = pygame.mouse.get_pos()
                collide = rect.collidepoint(point)
                
                print(self.cor_clicada)
                
                if collide:
                    for item in self.dic.keys():
                        if (rect == self.dic[item]):
                            print("ACHEI")
                            print(f'chave:{item}')
                            
                            if (item == vetor_cores_nomes[self.num_cor]):
                                print ("MESMA COR!")
                                self.pontos+=1
                            
                            # ELE ESTA RECONHECENDO A COR ONDE EH CLICADO POR CONTA DO DICIONARIO QUE EU CRIEI. AGORA PRECISO APENAS ASSOCIAR COM A POSICAO SORTEADA NO INICIO 
                    
                    print("COLIDIU    " + str(point) )
                    
                    self.flag_colisao = True
                    self.sorteio = True
                    break
                
    
    
    def sorteiaCor(self):
        if self.sorteio:
            self.num_cor = randint(0, (len(vetor_cores_nomes)-1))
            self.num_cor_do_texto = randint(0, (len(vetor_cores_nomes))-1)
            self.sorteio = False
            
    def escreveCorNaTela(self):
        textofinal = quickens_font.render((vetor_cores_nomes[self.num_cor]), True, (vetor_cores[self.num_cor_do_texto]))
        screen.blit(textofinal, (350, 155))     
        
    def escrevePontosNaTela(self):
        textoPontos = yogurt_mango_font.render(str(self.pontos), True, BRANCO_COR)   
        screen.blit(textoPontos, (710,30))   
        
        
    def telaDeInicio(self):
        screen.fill(PRETO_COR)
        textoTitulo = yogurt_mango_font_maior.render("Troca-cor", True, VERDE_LIMAO_COR)
        screen.blit(textoTitulo, (300,230))
        
        
        pygame.event.pump()
        click = pygame.mouse.get_pressed()
        
        if  click[0]:
            print("CLICADO")
            self.tela_inicio_jogo = False
            self.comeco_jogo = True
        
            
    
            
    


running = True
tela_obj = Tela()
while running:
    
    #Carrega a tela de inicio e aguarda um clique para iniciar o jogo
    if tela_obj.tela_inicio_jogo:
        tela_obj.telaDeInicio()
    
    

    
   
    if tela_obj.comeco_jogo:
        screen.fill(PRETO_COR)
        tela_obj.escrevePontosNaTela()
        tela_obj.desenha_circulos()
        tela_obj.sorteiaCor()
        tela_obj.escreveCorNaTela()   
        tela_obj.checa_colisao()
    
    
    
        
       
       
 
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            running = False
    # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)


