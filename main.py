import pygame
import random
import time


class SnakeGame:
    def __init__(self, width=4, height=4, cell_size=30):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.snake = [(0, 0), (0, 1), (0, 2)]
        self.food = None
        self._generate_food()
        self.direction = (1, 0)

        pygame.init()
        self.screen = pygame.display.set_mode((self.width * self.cell_size, self.height * self.cell_size))
        self.clock = pygame.time.Clock()

    def _generate_food(self):
        while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.snake:
                self.food = (x, y)
                break

    def _draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if (x, y) == self.snake[0]:
                    pygame.draw.rect(self.screen, (0, 255, 0), rect)  # green for snake head
                elif (x, y) in self.snake[1:]:
                    pygame.draw.rect(self.screen, (0, 128, 0), rect)  # dark green for snake body
                elif (x, y) == self.food:
                    pygame.draw.rect(self.screen, (255, 0, 0), rect)  # red for food
                else:
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)  # black for empty cells

    def move(self):
        dx, dy = self.direction
        new_head = (self.snake[0][0] + dx, self.snake[0][1] + dy)

        if new_head not in self.snake and 0 <= new_head[0] < self.width and 0 <= new_head[1] < self.height:
            if new_head == self.food:
                self.snake.insert(0, new_head)
                self._generate_food()
            else:
                self.snake.insert(0, new_head)
                self.snake.pop()
        else:
            print("Game Over!")
            pygame.quit()
            exit()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 1):
                        self.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -1):
                        self.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and self.direction != (1, 0):
                        self.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-1, 0):
                        self.direction = (1, 0)

            self.screen.fill((255, 255, 255))  # white background
            self._draw_grid()
            self.move()
            pygame.display.flip()
            self.clock.tick(1)  # limit game to 1 FPS for simplicity


if __name__ == "__main__":
    game = SnakeGame(width=16, height=16, cell_size=16)
    game.play()
