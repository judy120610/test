import pygame
import random
import time

# 초기화
pygame.init()

# 화면 설정 (전체 화면으로 설정하거나 특정 크기로 설정 가능)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.display.set_caption("System Update")

# 색상 정의
BLACK = (0, 0, 0)
GREEN = (0, 255, 70)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLUE = (66, 133, 244) # 구글 로고 색상 중 하나

# 폰트 설정
font_size = 20
matrix_font = pygame.font.SysFont("consolas", font_size)
error_font = pygame.font.SysFont("arial", 50, bold=True)
google_font = pygame.font.SysFont("arial", 25)

# 매트릭스 숫자 설정을 위한 변수
columns = width // font_size
drops = [0] * columns

def draw_matrix():
    """숫자가 아래로 떨어지는 효과"""
    # 배경을 완전히 지우지 않고 투명도 있는 검은색을 덧칠해 잔상 효과를 줌
    s = pygame.Surface((width, height))
    s.set_alpha(30)
    s.fill(BLACK)
    screen.blit(s, (0,0))

    for i in range(len(drops)):
        char = str(random.randint(0, 9))
        x = i * font_size
        y = drops[i] * font_size
        
        msg = matrix_font.render(char, True, GREEN)
        screen.blit(msg, (x, y))

        if y > height and random.random() > 0.975:
            drops[i] = 0
        drops[i] += 1

def draw_error_message():
    """5초 동안 뜰 에러 메시지"""
    pygame.draw.rect(screen, RED, (width//4, height//2 - 50, width//2, 100))
    error_text = error_font.render("CRITICAL ERROR: SYSTEM COMPROMISED", True, WHITE)
    text_rect = error_text.get_rect(center=(width//2, height//2))
    screen.blit(error_text, text_rect)

def draw_google_alert():
    """구글 알림창 메시지"""
    box_w, box_h = 450, 200
    box_x, box_y = (width - box_w) // 2, (height - box_h) // 2
    
    # 알림창 배경
    pygame.draw.rect(screen, WHITE, (box_x, box_y, box_w, box_h), border_radius=10)
    pygame.draw.rect(screen, (200, 200, 200), (box_x, box_y, box_w, box_h), 2, border_radius=10)

    # 구글 텍스트 (간단하게 구현)
    g_text = error_font.render("Google", True, BLUE)
    screen.blit(g_text, (box_x + 20, box_y + 20))

    # 메시지 내용
    alert_text1 = google_font.render("보안 경고: 계정이 위험합니다!", True, BLACK)
    alert_text2 = google_font.render("'해킹당하고 있습니다!'", True, RED)
    screen.blit(alert_text1, (box_x + 20, box_y + 80))
    screen.blit(alert_text2, (box_x + 20, box_y + 120))

# 메인 루프 변수
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # ESC 누르면 종료
                running = False

    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000 # 초 단위 계산

    # 시간대별 화면 전환 로직
    if 0 <= elapsed_time < 5:
        # 1단계: 숫자 낙하 (5초)
        draw_matrix()
    elif 5 <= elapsed_time < 10:
        # 2단계: 에러 메시지 (5초 동안 유지)
        # 배경에 숫자는 멈춘 상태로 메시지만 띄움
        draw_error_message()
    elif 10 <= elapsed_time < 15:
        # 3단계: 다시 숫자 낙하 (5초)
        draw_matrix()
    elif 15 <= elapsed_time < 20:
        # 4단계: 구글 알림창 (5초)
        draw_google_alert()
    else:
        # 5단계: 다시 숫자 낙하 (무한)
        draw_matrix()

    pygame.display.flip()
    clock.tick(30) # 프레임 속도 제어

pygame.quit()
