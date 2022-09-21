from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
angle = -90

while(1):
    while(x < 700):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x,y)
         x = x + 2
         delay(0.001)
         
    while(y < 550):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x, y)
         y = y + 2
         delay(0.001)
         
    while(x > 70):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x, y)
         x = x - 2
         delay(0.001)

    while(y > 90):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x, y)
         y = y - 2
         delay(0.001)

    while(x < 400):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x,y)
         x = x + 2
         delay(0.001)
         
    while(angle < 270):
         clear_canvas_now()
         grass.draw_now(400,30)
         character.draw_now(x, y)
         x = 400 + (270 * math.cos(angle/360 * 2 * math.pi))
         y = 310 + (270 * math.sin(angle/360 * 2 * math.pi))
         angle = angle + 2
         delay(0.001)
    angle = -90
    x = 0
    y = 90
    
