from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH // 2
y = 200
frame = 0
dir = 0
updown = 0
show = 3

def handle_events():
    global running
    global dir
    global updown
    global show

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                show = 1
            elif event.key == SDLK_LEFT:
                dir -= 1
                show = 0
            elif event.key == SDLK_UP:
                updown += 1
            elif event.key == SDLK_DOWN:
                updown -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
                #show = 3
            elif event.key == SDLK_LEFT:
                dir += 1
                #show = 2
            elif event.key == SDLK_UP:
                updown -= 1
            elif event.key == SDLK_DOWN:
                updown += 1
    pass


while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100 * show, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame = (frame + 1) % 8

    x += dir * 5
    if x > TUK_WIDTH - 20:
        x = 1260
    elif x < 20:
        x = 20
    y += updown * 5
    if y > TUK_HEIGHT - 120:
        y = 904
    elif y < 130:
        y = 130
    delay(0.01)


close_canvas()