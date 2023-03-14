import pygame,sys
pygame.init()

screen = pygame.display.set_mode((274,396))
pygame.display.set_caption('Simple Calculator')

Num_font = pygame.font.Font('img/digital-7.ttf',30)

calculator_screen = pygame.image.load('img/screen.png')
calculator_keyboard = pygame.image.load('img/keyboard.png')

Button_0_rect    = pygame.Rect(24,331,41,28)
Button_1_rect    = pygame.Rect(24,291,41,28)
Button_4_rect    = pygame.Rect(24,251,41,28)
Button_7_rect    = pygame.Rect(24,211,41,28)
Button_2_rect    = pygame.Rect(71,291,41,28)
Button_5_rect    = pygame.Rect(71,251,41,28)
Button_8_rect    = pygame.Rect(71,211,41,28)
Button_3_rect    = pygame.Rect(118,291,41,28)
Button_6_rect    = pygame.Rect(118,251,41,28)
Button_9_rect    = pygame.Rect(118,211,41,28)
Button_cong_rect = pygame.Rect(165,291,41,28)
Button_nhan_rect = pygame.Rect(165,251,41,28)
Button_bang_rect = pygame.Rect(212,331,41,28)
Button_tru_rect  = pygame.Rect(212,291,41,28)
Button_chia_rect = pygame.Rect(212,251,41,28)
Button_DEL_rect  = pygame.Rect(165,211,41,28)
Button_AC_rect   = pygame.Rect(212,211,41,28)

Num_list = []
x_pos = 36
memory = ''
result = 0

while True:
    screen.blit(calculator_screen,(0,0))
    screen.blit(calculator_keyboard,(0,197))

    for Num,pos in Num_list:
        screen.blit(Num,pos)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if Button_0_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('0',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='0'
            elif Button_1_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('1',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='1'
            elif Button_2_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('2',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='2'
            elif Button_3_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('3',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='3'
            elif Button_4_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('4',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='4'
            elif Button_5_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('5',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='5'
            elif Button_6_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('6',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='6'
            elif Button_7_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('7',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='7'
            elif Button_8_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('8',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='8'
            elif Button_9_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('9',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='9'
            elif Button_cong_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('+',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='+'
            elif Button_tru_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('-',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='-'
            elif Button_nhan_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('*',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='*'
            elif Button_chia_rect.collidepoint(pygame.mouse.get_pos()):
                Num = Num_font.render('/',True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
                memory+='/'
            elif Button_DEL_rect.collidepoint(pygame.mouse.get_pos()):
                x_pos-=14
                if len(memory)>0:
                    Num_list.remove(Num_list[-1])
                    memory.replace(memory[-1],'')
            elif Button_AC_rect.collidepoint(pygame.mouse.get_pos()):
                Num_list,memory = [],''
                x_pos = 36
            elif Button_bang_rect.collidepoint(pygame.mouse.get_pos()):
                for count in range(len(memory)):
                    if (ord(memory[count])<ord('0')) or (ord(memory[count])>ord('9')):
                        if memory[count] =='+':
                            result = int(memory[:count])+int(memory[count+1:])
                        elif memory[count] =='-':
                            result = int(memory[:count])-int(memory[count+1:])
                        elif memory[count] =='*':
                            result = int(memory[:count])*int(memory[count+1:])
                        else:
                            result = int(memory[:count])//int(memory[count+1:])
                Num = Num_font.render('='+str(result),True,(41,28,41))
                screen.blit(Num,(x_pos,107))
                Num_list.append((Num,(x_pos,107)))
                x_pos+=14
        
    pygame.display.update()