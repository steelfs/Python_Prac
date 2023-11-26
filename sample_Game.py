import pygame
import sys

pygame.init()

# 화면 크기 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Pygame Example")

# 색상 정의
RED = (255, 0, 0)

# 사각형의 초기 위치와 크기 설정
rect_x, rect_y = 300, 300
rect_width, rect_height = 50, 50

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 화면을 검은색으로 채움
    screen.fill((0, 0, 0))

    # 사각형 그리기
    pygame.draw.rect(screen, RED, [rect_x, rect_y, rect_width, rect_height])

    # 화면 업데이트
    pygame.display.flip()

    # 프레임 속도 조절
    pygame.time.Clock().tick(60)

# Pygame 종료
pygame.quit()
sys.exit()