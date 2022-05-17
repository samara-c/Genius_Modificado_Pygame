# -*- coding: utf-8 -*-

import sys, pygame
from random import *


pygame.init()

SCREEN_SIZE=(800,500)
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Troca-cor")

#cores em RGB
BRANCO_COR= (255,255,255)
ROSA_COR = (255, 78, 183)
ROSA_ESCURO_COR = (204, 0, 122)
AMARELO_CLARO_COR= (255, 255, 27)
AMARELO_ESCURO_COR= (204, 204, 0)
AZUL_COR=(55, 102, 253)
AZUL_ESCURO_COR = (2, 49, 202)
VERDE_COR=(55, 251, 49)
VERDE_ESCURO_COR=(11, 200, 4)
PRETO_COR=(0,0,0)
VERDE_LIMAO_COR=(169, 255, 36)

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()


#caminhos pastas
caminho_fontes = "fonts//"
caminho_figuras_animais="figs//"



#fontes
arial_font = pygame.font.SysFont('arial',40)
quickens_font = pygame.font.Font(caminho_fontes+"QUICKENS.ttf",55)
yogurt_mango_font = pygame.font.Font(caminho_fontes+"Yogurt Mango.ttf", 40)
yogurt_mango_font_maior = pygame.font.Font(caminho_fontes+"Yogurt Mango.ttf", 50)



#Vetores
vetor_cores=[ROSA_COR, AMARELO_CLARO_COR, AZUL_COR, VERDE_COR]
vetor_animais_nomes = ["GATO","RATO","PATO","SAPO"]
vetor_cores_escuras=[ROSA_ESCURO_COR, AMARELO_ESCURO_COR, AZUL_ESCURO_COR, VERDE_ESCURO_COR]
vetor_rects=[0,0,0,0]
vetor_cores_nomes=["Rosa", "Amarelo", "Azul", "Verde"]

#Flags
tela_inicio_jogo = True 
comeco_jogo = False


#Figuras animais
figura_gato = "gato_corpo_contorno.png"
figura_rato = "rato_corpo_contorno.png"
figura_pato = "pato_corpo_contorno.png"
figura_sapo = "sapo_corpo_contorno.png"

#Tamanhos



class Tela():
    
    tamanho_figura_x = 75
    tamanho_figura_y = 75
    tela_inicio_jogo = True 
    comeco_jogo = False
    valor = 125
    pos_x = 0
    pos_y = 0
    vetor_posicao_circulos = [190, 315, 440, 565]
    vetor_pos = [0,0]
    flag_colisao = False
    num_cor = 0
    num_cor_do_texto = 0
    sorteio = True
    cor_clicada = ""
    dic = {}
    pontos = 0
    circulo_nao_clicado = True
    figuras_tela = []
    animal_nao_clicado = True
    nivel = 1
    sorteio_var = 5
    continuar = True
    vetor_sorteio = [0]
    # pos_x = (SCREEN_SIZE[0]-500)/2
    
    def __init__(self):
        gato_figura_tela = pygame.image.load(caminho_figuras_animais+figura_gato).convert_alpha()
        gato_figura_tela = pygame.transform.scale(gato_figura_tela, (self.tamanho_figura_x, self.tamanho_figura_y))
        
        rato_figura_tela = pygame.image.load(caminho_figuras_animais+figura_rato).convert_alpha()
        rato_figura_tela = pygame.transform.scale(rato_figura_tela, (self.tamanho_figura_x, self.tamanho_figura_y))
        
        pato_figura_tela = pygame.image.load(caminho_figuras_animais+figura_pato).convert_alpha()
        pato_figura_tela = pygame.transform.scale(pato_figura_tela, (self.tamanho_figura_x, self.tamanho_figura_y))
        
        sapo_figura_tela = pygame.image.load(caminho_figuras_animais+figura_sapo).convert_alpha()
        sapo_figura_tela = pygame.transform.scale(sapo_figura_tela, (self.tamanho_figura_x, self.tamanho_figura_y))
        
        self.figuras_tela.append(gato_figura_tela)
        self.figuras_tela.append(rato_figura_tela)
        self.figuras_tela.append(pato_figura_tela)
        self.figuras_tela.append(sapo_figura_tela)
    
    def inicializa_dicionario(self):
        
        dic = {vetor_animais_nomes[0]:"", vetor_animais_nomes[1]:"", vetor_animais_nomes[2]:"", vetor_animais_nomes[3]:""}
        
        
        
    def monta_tela(self):
        screen.fill(BRANCO_COR)
       
            

    def desenha_animais(self):
        self.pos_y = 295
        i = 0
        
        
        
        if self.animal_nao_clicado:
            for animal in vetor_animais_nomes:
                rect = screen.blit(self.figuras_tela[i], (self.vetor_posicao_circulos[i], self.pos_y))
                vetor_rects[i] = rect
                self.dic[vetor_animais_nomes[i]] = rect
                i+=1
    
    def desenha_circulos(self):
        # self.pos_x = 225
        self.pos_y = 350
        i = 0
        
        if self.circulo_nao_clicado:
            
            for cor in vetor_cores:
                rect = pygame.draw.circle(screen, cor, (self.vetor_posicao_circulos[i], self.pos_y), 50)
                vetor_rects[i] = rect
                self.dic[vetor_cores_nomes[i]]=rect
                  
                i+=1
        else:
            self.circulo_nao_clicado = True
            for cor in vetor_cores_escuras:
                rect = pygame.draw.circle(screen, cor, (self.vetor_posicao_circulos[i], self.pos_y), 50)
                vetor_rects[i] = rect
                self.dic[vetor_cores_nomes[i]]=rect
                  
                i+=1   
            
    
    
    
    def define_nivel(self, nivel):
        
        if (nivel > 0 and nivel < 6):
            self.sorteio_var = nivel
            self.continuar = True
        else:
            self.continuar = False    
        
        
        
                

    def checa_colisao(self):
        

        pygame.event.pump()
        click = pygame.mouse.get_pressed()
        
        if  click[0]:
            self.circulo_nao_clicado = False
            for rect in vetor_rects:
                
                point = pygame.mouse.get_pos()
                collide = rect.collidepoint(point)
                
                
                if collide:
                    for item in self.dic.keys():
                        if (rect == self.dic[item]):
                            print("ACHEI")
                            print(f'chave:{item}')
                            
                            
                            if (item == vetor_animais_nomes[self.num_cor]):
                                print ("MESMA COR!")
                                self.pontos+=1
                                vetor_tamanho = len(self.vetor_sorteio)
                                self.sorteio = True
                            
                            # ELE ESTA RECONHECENDO A COR ONDE EH CLICADO POR CONTA DO DICIONARIO QUE EU CRIEI. AGORA PRECISO APENAS ASSOCIAR COM A POSICAO SORTEADA NO INICIO 
                    
                    print("COLIDIU    " + str(point) )
                    self.flag_colisao = True
                    
                    break
                
    
    
    def sorteiaCor(self):
        if self.sorteio:
            self.num_cor = randint(0, (len(vetor_cores_nomes)-1))
            self.num_cor_do_texto = randint(0, (len(vetor_cores_nomes))-1)
            self.sorteio = False
            
    def sorteiaAnimal(self):
        i = 0
        if self.sorteio:
                self.num_cor = randint(0, (len(vetor_animais_nomes)-1))
                print(self.num_cor)
                self.num_cor_do_texto = randint(0, (len(vetor_cores_nomes))-1)
                self.vetor_sorteio[i] = self.num_cor
                i+=1
                print ("sorteado")
                self.sorteio = False        
            
    def escreveAnimalNaTela(self):
        
        pos_1 = 350
        pos_2 = 155
        
        
        for num in self.vetor_sorteio:
            try:
                textofinal = quickens_font.render((vetor_animais_nomes[self.num_cor]), True, PRETO_COR)
                screen.blit(textofinal, (pos_1, pos_2))
                pos_1+=150
            except:
                print("DEU ERRO" + str(self.vetor_sorteio))
                print(vetor_animais_nomes)     
        
    def escrevePontosNaTela(self):
        textoPontos = yogurt_mango_font.render(str(self.pontos), True, PRETO_COR)   
        screen.blit(textoPontos, (710,30))   
        
        
    def telaDeInicio(self):
        screen.fill(PRETO_COR)
        textoTitulo = yogurt_mango_font_maior.render("Bichos", True, VERDE_LIMAO_COR)
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
        
        tela_obj.monta_tela()
        tela_obj.escrevePontosNaTela()
        tela_obj.sorteiaAnimal()
        tela_obj.desenha_animais()
        tela_obj.escreveAnimalNaTela()   
        tela_obj.checa_colisao()
    
    
    
        
       
       
 
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            running = False
    # Flip the display
    pygame.display.flip()
    fpsClock.tick(FPS)


