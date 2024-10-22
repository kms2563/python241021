import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)  # 블록 경계선 색상

# 테트로미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # J
    [[0, 0, 1], [1, 1, 1]],  # L
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 0], [1, 1, 1]],  # T
]

# 색상 매핑
SHAPE_COLORS = [CYAN, YELLOW, BLUE, ORANGE, GREEN, RED, MAGENTA]

# 그리드 생성
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE

# 그리드 설정
grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]


class Tetromino:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = SHAPE_COLORS[SHAPES.index(self.shape)]
        self.x = GRID_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

    def draw(self, screen):
        for i, row in enumerate(self.shape):
            for j, value in enumerate(row):
                if value == 1:
                    # 블록 내부 그리기
                    pygame.draw.rect(
                        screen,
                        self.color,
                        pygame.Rect(
                            (self.x + j) * BLOCK_SIZE,
                            (self.y + i) * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                    )
                    # 블록 경계선 그리기
                    pygame.draw.rect(
                        screen,
                        GRAY,
                        pygame.Rect(
                            (self.x + j) * BLOCK_SIZE,
                            (self.y + i) * BLOCK_SIZE,
                            BLOCK_SIZE,
                            BLOCK_SIZE,
                        ),
                        1  # 테두리 두께
                    )


def check_collision(tetromino, offset_x=0, offset_y=0):
    for i, row in enumerate(tetromino.shape):
        for j, value in enumerate(row):
            if value:
                new_x = tetromino.x + j + offset_x
                new_y = tetromino.y + i + offset_y
                if (
                    new_x < 0
                    or new_x >= GRID_WIDTH
                    or new_y >= GRID_HEIGHT
                    or grid[new_y][new_x] != BLACK
                ):
                    return True
    return False


def merge_tetromino(tetromino):
    for i, row in enumerate(tetromino.shape):
        for j, value in enumerate(row):
            if value:
                grid[tetromino.y + i][tetromino.x + j] = tetromino.color


def clear_lines():
    global grid
    new_grid = [row for row in grid if BLACK in row]
    cleared_lines = GRID_HEIGHT - len(new_grid)
    new_grid = [[BLACK for _ in range(GRID_WIDTH)] for _ in range(cleared_lines)] + new_grid
    grid = new_grid
    return cleared_lines


def draw_grid(screen):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(
                screen,
                grid[y][x],
                pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
            )
            # 그리드 경계선 그리기
            pygame.draw.rect(
                screen,
                GRAY,
                pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                1  # 경계선 두께
            )


def run_game():
    clock = pygame.time.Clock()
    tetromino = Tetromino()
    drop_speed = 500  # ms
    drop_timer = 0
    score = 0
    game_over = False

    while not game_over:
        screen.fill(BLACK)

        # 시간 처리
        current_time = pygame.time.get_ticks()
        if current_time - drop_timer > drop_speed:
            if not check_collision(tetromino, offset_y=1):
                tetromino.y += 1
            else:
                merge_tetromino(tetromino)
                score += clear_lines() * 10
                tetromino = Tetromino()
                if check_collision(tetromino):
                    game_over = True
            drop_timer = current_time

        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not check_collision(tetromino, offset_x=-1):
                    tetromino.x -= 1
                if event.key == pygame.K_RIGHT and not check_collision(tetromino, offset_x=1):
                    tetromino.x += 1
                if event.key == pygame.K_DOWN and not check_collision(tetromino, offset_y=1):
                    tetromino.y += 1
                if event.key == pygame.K_SPACE:  # 스페이스바를 누르면 즉시 바닥으로 떨어짐
                    while not check_collision(tetromino, offset_y=1):
                        tetromino.y += 1
                    merge_tetromino(tetromino)
                    score += clear_lines() * 10
                    tetromino = Tetromino()
                    if check_collision(tetromino):
                        game_over = True
                if event.key == pygame.K_UP:
                    tetromino.rotate()
                    if check_collision(tetromino):
                        tetromino.rotate()  # 충돌 시 회전 취소

        draw_grid(screen)
        tetromino.draw(screen)

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    print(f"Game Over! Your score: {score}")


if __name__ == "__main__":
    run_game()
