# 1. Создайте программу для игры в ""Крестики-нолики"" при помощи виртуального окружения и PIP
import pygame as pg
import sys
import time
from pygame.locals import *
  
width = 400 # ширина игрового окна
height = 400 # высота игрового окна

# название диалогового окна
pg.display.set_caption('Игра "Крестики-нолики"')

# задаем размеры окна
screen = pg.display.set_mode((width, height + 100), 0, 32)

# начальное окно игры
initiating_window = pg.image.load("krestiki-noliki.jpg")
x_img = pg.image.load("X_modified.png")
o_img = pg.image.load("o_modified.png")

initiating_window = pg.transform.scale(initiating_window, (width, height+100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(o_img, (80, 80))
 
XO = 'x'
winner = None
draw = None # ничья
white = (255, 255, 255) # белый фон
line_color = (47, 79, 79) # цвет линий для отрисовки поля
board = [[None]*3, [None]*3, [None]*3] # доска три на три
fps = 30 # кадровая частота

# Создание диалогового окна
pg.init()
# для отслежки времени
CLOCK = pg.time.Clock()
 
def game_initiating_window():
     
    screen.blit(initiating_window, (0,0)) # отображение на экране
     
    # обновление экрана
    pg.display.update()
    time.sleep(3)                   
    screen.fill(white)
  
    # отрисовка вертикальных линий поля
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
  
    # отрисовка горизонтальных линий поля
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()
  
# отрисовка сообщения для пользователей внизу игрового поля
def draw_status():
    global draw
     
    if winner is None:
        message = XO.upper() + " ходит"
    else:
        message = winner.upper() + " выиграл!"
    if draw:
        message = "Ничья!"

    font = pg.font.Font(None, 30)
    text = font.render(message, 1, (0, 0, 0))
  
    screen.fill ((255, 255, 255), (0, 400, 500, 100))
    text_rect = text.get_rect(center =(width / 2, 500-50))
    screen.blit(text, text_rect)
    pg.display.update()
     
# проверка на выигрыш
def check_win():
    global board, winner, draw
  
    # проверка строк
    for row in range(0, 3):
        if((board[row][0] == board[row][1] == board[row][2]) and (board [row][0] is not None)):
            winner = board[row][0]
            pg.draw.line(screen, (255, 0, 255),
                         (0, (row + 1)*height / 3 -height / 6),
                         (width, (row + 1)*height / 3 - height / 6 ),
                         10)
            break
  
    # проверка столбцов
    for col in range(0, 3):
        if((board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None)):
            winner = board[0][col]
            pg.draw.line (screen, (255, 0, 255), ((col + 1)* width / 3 - width / 6, 0), \
                          ((col + 1)* width / 3 - width / 6, height), 10)
            break
  
    # проверка диагонали
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
         
        # слева направо
        winner = board[0][0]
        pg.draw.line (screen, (255, 0, 255), (50, 50), (350, 350), 10)
         
    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
         
        # справа налево
        winner = board[0][2]
        pg.draw.line (screen, (255, 0, 255), (350, 50), (50, 350), 10)
  
    # ничья
    if(all([all(row) for row in board]) and winner is None ):
        draw = True
    draw_status()
     
def drawXO(row, col):
    global board, XO
     
    # вычисление сдвигов картинки относительно поля игры
    if row == 1:
        posx = 30
    elif row == 2:
        posx = width / 3 + 30
    elif row == 3:
        posx = width / 3 * 2 + 30
  
    if col == 1:
        posy = 30  
    elif col == 2:
        posy = height / 3 + 30
    elif col == 3:
        posy = height / 3 * 2 + 30
    
    # запоминание хода
    board[row-1][col-1] = XO
    
    # выбор подставляемой картинки
    if(XO == 'x'):
        screen.blit(x_img, (posy, posx))
        XO = 'o'
    else:
        screen.blit(o_img, (posy, posx))
        XO = 'x'

    pg.display.update()

# вычисляем координаты нажатия мышкой
def user_click():
    # координаты клика
    x, y = pg.mouse.get_pos()
  
    # проверка в какой строке
    if(x<width / 3):
        col = 1
     
    elif (x<width / 3 * 2):
        col = 2
     
    elif(x<width):
        col = 3
     
    else:
        col = None
  
    # проверка в каком столбце
    if(y<height / 3):
        row = 1
     
    elif (y<height / 3 * 2):
        row = 2
     
    elif(y<height):
        row = 3
     
    else:
        row = None
       
    #отрисовка в этой строке и столбце картинки х/о
    if(row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row, col)
        check_win()
         
# перезапуск игры
def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]
  

# ОСНОВНАЯ ПРОГРАММА
game_initiating_window() 
while(True):
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if(winner or draw):
                reset_game()
    pg.display.update()
    CLOCK.tick(fps)