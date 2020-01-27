import pygame,random,time


white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
rect1=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
matrix=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
pygame.init()
screen_height=400
screen_width=500
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TicTacToe")
fps=30
clock=pygame.time.Clock()

font=pygame.font.Font(None,25)

def msgToScrn(msg,color,mx,my):
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[mx,my])
def displayMove(msg,color,mx,my):
    screen_text = font.render(msg, True, color)
    window.blit(screen_text, [mx, my])


def drawTemplate(disp_x,disp_y):

    rect1[0] =pygame.draw.rect(window, white, [100, 50, 100, 100], 1)
    rect1[1] =pygame.draw.rect(window, white, [200, 50, 100, 100], 1)
    rect1[2] =pygame.draw.rect(window, white, [300, 50, 100, 100], 1)

    rect1[3] =pygame.draw.rect(window, white, [100, 150, 100, 100], 1)
    rect1[4] =pygame.draw.rect(window, white, [200, 150, 100, 100], 1)
    rect1[5] =pygame.draw.rect(window, white, [300, 150, 100, 100], 1)

    rect1[6] =pygame.draw.rect(window, white, [100, 250, 100, 100], 1)
    rect1[7] =pygame.draw.rect(window, white, [200, 250, 100, 100], 1)
    rect1[8] =pygame.draw.rect(window, white, [300, 250, 100, 100], 1)

    for i in range(0,3):
        for j in range(0,3):
            if(matrix[i][j]==-1):
                displayMove("", white, disp_x[i][j],disp_y[i][j])
            elif(matrix[i][j]==0):
                displayMove("0",white, disp_x[i][j], disp_y[i][j])
            elif (matrix[i][j] == 1):
                displayMove("X", white, disp_x[i][j], disp_y[i][j])


def gameLoop():
    turn=1
    played=0
    game_exit=False
    winner=-1
    disp_x=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]
    disp_y=[[-1,-1,-1],[-1,-1,-1],[-1,-1,-1]]

    stop=0
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                break

            elif event.type==pygame.MOUSEBUTTONDOWN and stop==0:

                mouse_x,mouse_y = pygame.mouse.get_pos()
                if mouse_x in range(100,400):
                    if mouse_y in range(50,350):
                        if mouse_x in range (100,200):
                            if mouse_y in range(50,150) and matrix[0][0]==-1:
                                matrix[0][0]=turn
                                disp_x[0][0]=150
                                disp_y[0][0]=100
                                played=1

                            elif mouse_y in range(150, 250)and matrix[0][1]==-1:
                                matrix[0][1] = turn
                                disp_x[0][1] = 150
                                disp_y[0][1]= 200
                                played=1

                            elif mouse_y in range(250, 350)and matrix[0][2]==-1:
                                matrix[0][2] = turn
                                disp_x[0][2] = 150
                                disp_y[0][2] = 300
                                played=1

                        elif mouse_x in range(200, 300):
                            if mouse_y in range(50,150)and matrix[1][0]==-1:
                                matrix[1][0]=turn
                                disp_x[1][0] = 250
                                disp_y[1][0]= 100
                                played=1

                            elif mouse_y in range(150, 250)and matrix[1][1]==-1:
                                matrix[1][1] = turn
                                disp_x[1][1]= 250
                                disp_y[1][1]= 200
                                played=1

                            elif mouse_y in range(250, 350)and matrix[1][2]==-1:
                                matrix[1][2] = turn
                                disp_x[1][2]= 250
                                disp_y[1][2] = 300
                                played=1
                        elif mouse_x in range(300, 400):
                            if mouse_y in range(50,150) and matrix[2][0]==-1:
                                matrix[2][0]=turn
                                disp_x[2][0] = 350
                                disp_y[2][0] = 100
                                played=1
                            elif mouse_y in range(150, 250) and matrix[2][1]==-1:
                                matrix[2][1] = turn
                                disp_x[2][1] = 350
                                disp_y[2][1] = 200
                                played=1
                            elif mouse_y in range(250, 350)and matrix[2][2]==-1:
                                matrix[2][2] = turn
                                disp_x[2][2] = 350
                                disp_y[2][2] = 300
                                played=1
                if played==1:
                    if turn==1:
                        turn=0
                    elif turn==0:
                        turn=1
                played=0
                break



        drawTemplate(disp_x,disp_y)

        pygame.display.update()

        for i in range(0,3):
            c0=0
            c1=0
            for j in range(0,3):
                if matrix[i][j]==0:
                    c0=c0+1
                    if(c0==3):
                        winner=0
                elif matrix[i][j]==1:
                    c1=c1+1
                    if(c1==3):
                        winner=1
        for i in range(0,3):
            c0=0
            c1=0
            for j in range(0,3):
                if matrix[j][i]==0:
                    c0=c0+1
                    if(c0==3):
                        winner=0
                elif matrix[j][i]==1:
                    c1=c1+1
                    if(c1==3):
                        winner=1
        if matrix[0][0]==matrix[1][1]==matrix[2][2]==0 or matrix[0][2]==matrix[1][1]==matrix[2][0]==0:
            winner=0
        elif matrix[0][0]==matrix[1][1]==matrix[2][2]==1 or matrix[0][2]==matrix[1][1]==matrix[2][0]==1:
            winner=1


        if winner!=-1:
            stop=1

            if winner==0:
                msgToScrn("0 winner",white,400,360)
            else:
                msgToScrn("X winner", white, 400, 360)
            pygame.display.update()
        #pygame.draw.rect(window,white,[100,0,300,500])
        clock.tick(fps)
    pygame.quit()
    quit()

gameLoop()

