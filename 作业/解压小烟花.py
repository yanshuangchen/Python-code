import pygame
import random

# 初始化 pygame 库
pygame.init()

# 设置屏幕尺寸
screen = pygame.display.set_mode((800, 600))

# 设置标题
pygame.display.set_caption("Fireworks Animation")

# 设置时钟
clock = pygame.time.Clock()

# 定义颜色
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
orange = (255, 165, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
purple = (128, 0, 128)

# 定义粒子类
class Particle:
    def __init__(self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.vx = random.randint(-10, 10) / 10
        self.vy = random.randint(-10, 10) / 10
        self.alpha = 255
        self.gravity = 0.05

    def draw(self):
        pygame.draw.circle(screen, (self.color[0], self.color[1], self.color[2], self.alpha), (int(self.x), int(self.y)), self.size)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += self.gravity
        self.alpha -= 5
        if self.alpha <= 0:
            particles.remove(self)

# 定义爆炸函数
def explode(x, y, color):
    num_particles = random.randint(50, 100)
    for i in range(num_particles):
        particles.append(Particle(x, y, random.randint(2, 5), color))

# 主循环
running = True
particles = []

while running:
    # 处理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            color = random.choice([red, yellow, orange, green, blue, purple])
            explode(*event.pos, color)

    # 更新粒子系统
    for particle in particles:
        particle.update()

    # 绘制屏幕
    screen.fill(white)
    for particle in particles:
        particle.draw()

    # 更新屏幕
    pygame.display.update()

    # 限制帧速率
    clock.tick(60)

# 退出游戏
pygame.quit()
