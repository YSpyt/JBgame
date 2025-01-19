import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('JBgame')

font = pygame.font.Font(None, 48)

# Загружаем изображение фона
background_image = pygame.image.load('photos/menu.jpg')

# Функция для отрисовки кнопки
def draw_button(text, x, y, width, height, color):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (130, 115, 192))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


# Главный игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            # Проверка нажатия кнопки "Играть"
            if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
                pass
            # Проверка нажатия кнопки "Настройки"
            if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 450:
                pass

    # Отображаем фон
    screen.blit(background_image, (0, 0))

    # Рисуем кнопки
    draw_button("Играть", 300, 200, 200, 100, (8, 8, 17))
    draw_button("Настройки", 300, 350, 200, 100, (8, 8, 17))

    # Обновляем экран
    pygame.display.flip()

# Завершение работы Pygame
pygame.quit()
sys.exit()