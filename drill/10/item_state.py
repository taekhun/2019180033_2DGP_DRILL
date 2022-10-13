from pico2d import *
import game_framework
import play_state

image = None


def enter():
    global image
    image = load_image('add_delete_boy.png')


def exit():
    global image
    del image


def update():
    pass

def draw():
    clear_canvas()
    play_state.world()
    image.draw(400, 300)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_1:  # + 버튼이 입력이 안되서 1로 대체
                    play_state.boy.item = 'made'
                    game_framework.pop_state()
                case pico2d.SDLK_MINUS:
                    play_state.boy.item = 'delete'
                    game_framework.pop_state()

# 셀프 테스트
def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':  # 만약 단독 실행 상태이면,
    test_self()
