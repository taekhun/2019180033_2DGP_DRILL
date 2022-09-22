from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('marathon_animation.png')

frame = 0
#  ready
for x in range(48, 50+1):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 200, 100, 100, x, 100)
    update_canvas()
    frame = (frame + 1) % 3
    delay(0.5)
    get_events()

frame = 0
# run
for x in range(50, 400 + 1, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 100, 100, 100, x, 100)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.1)
    get_events()

frame = 0
# jump
for x in range(400, 425 + 1, 5):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 100)
    update_canvas()
    frame = (frame + 1) % 6
    delay(0.1)
    get_events()

close_canvas()

