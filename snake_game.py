import pygame
import time
import random

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Размеры экрана
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Размер блока змейки и скорость
BLOCK_SIZE = 20
SPEED = 15

# Создание экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Загрузка шрифтов
font = pygame.font.SysFont(None, 35)


def message(msg, color, x, y):
    mesg = font.render(msg, True, color)
    screen.blit(mesg, [x, y])


class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * BLOCK_SIZE)) % SCREEN_WIDTH), (cur[1] + (y * BLOCK_SIZE)) % SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH // 2), (SCREEN_HEIGHT // 2))]
        self.direction = random.choice([(0, -1), (0, 1), (-1, 0), (1, 0)])
        game_over_sound.play()
        time.sleep(2)

    def draw(self, surface):
        for p in self.positions:
            pygame.draw.rect(surface, self.color, (p[0], p[1], BLOCK_SIZE, BLOCK_SIZE))

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn((0, -1))
                elif event.key == pygame.K_DOWN:
                    self.turn((0, 1))
                elif event.key == pygame.K_LEFT:
                    self.turn((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    self.turn((1, 0))
        return False


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // BLOCK_SIZE) - 1) * BLOCK_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // BLOCK_SIZE) - 1) * BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))


def main():
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()

    running = True
    while running:
        screen.fill(BLACK)
        running = not snake.handle_keys()
        snake.move()

        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()
            eat_sound.play()

        snake.draw(screen)
        food.draw(screen)

        message(f"Score: {snake.length - 1}", WHITE, 10, 10)
        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()


if __name__ == "__main__":
    eat_sound = pygame.mixer.Sound("eat.wav")
    game_over_sound = pygame.mixer.Sound("game_over.wav")
    main()
