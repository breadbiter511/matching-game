import pygame


pygame.init()
HEIGHT = 900
WIDTH = 600
pygame.display.set_caption("MATCHING GAME")
screen = pygame.display.set_mode((WIDTH,HEIGHT))
screen.fill("blue")
pygame.display.update()
subwayimg = pygame.image.load("match the things/subway surfer.png")
screen.blit(subwayimg,(110,100))
templeimg = pygame.image.load("match the things/temple run.png")
screen.blit(templeimg,(110,250))
candyimg = pygame.image.load("match the things/candy crush.jpg")
screen.blit(candyimg,(110,400))
ludoimg = pygame.image.load("match the things/ludo.png")
screen.blit(ludoimg,(110,550))
mineimg = pygame.image.load("match the things/minecraft.webp")
screen.blit(mineimg,(110,700))


font = pygame.font.SysFont("Arial",32)
text1 = font.render("LUDO",True,"orange")
screen.blit(text1,(280,120))
text2 = font.render("CANDY CRUSH",True,"orange")
screen.blit(text2,(280,270))
text3 = font.render("SUBWAY SURFERS",True,"orange")
screen.blit(text3,(280,420))
Text4 = font.render("TEMPLE RUN",True,"orange")
screen.blit(Text4,(280,570))
Text5 = font.render("MINECRAFT",True,"orange")
screen.blit(Text5,(280,720))

pygame.display.update()
while True :
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(screen,"green",(pos),10,0)
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
            pygame.draw.line(screen,"green",(pos),(pos2),5)
            pygame.draw.circle(screen,"green",(pos2),10,0)
            pygame.display.update()
        
        
        
        