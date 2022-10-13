from pico2d import *
import game_framework
import logo_state
import title_state
import item_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.made = load_image('animation_sheet.png')
        self.delete = load_image('animation_sheet.png')
        self.item = None

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 400:
            self.dir = -1
            self.x = 400
        elif self.x < 0:
            self. dir = 1
            self.x = 0

    def draw(self):
        global i
        global boy
        if self.item == 'made':
            if self.dir == 1:
                self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x - 20, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x - 20, self.y)
        elif self.item == 'delete':
            if self.dir == 1:
                self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
            else:
                self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

        if self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key == SDLK_b:
                game_framework.push_state(item_state)


# 게임 초기화: 객체들을 생성
boy = None  # c NULL
grass = None


def world():
    grass.draw()
    boy.draw()


def enter():
    global boy
    global grass
    global running
    boy = Boy()
    grass = Grass()

# 게임 종료 - 객체를 소멸
def exit():
    global boy, grass
    del boy
    del grass

# 게임 월드 객체를 업데이트 - 게임 로직
def update():
    boy.update()


def draw():
    # 게임 월드 렌더링
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass


# 셀프 테스트
def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()


if __name__ == '__main__':  # 만약 단독 실행 상태이면,
    test_self()