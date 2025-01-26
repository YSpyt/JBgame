import pygame
import sys

pygame.init()

# Определяем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('JBgame')

font = pygame.font.Font(None, 48)
lvls_font = pygame.font.Font(None, 100)

# Загружаем изображение фона
background_image = pygame.image.load('photos/menu.jpg')
settings_background_image = pygame.image.load('photos/menu.jpg')

# Загружаем и воспроизводим фоновую музыку
pygame.mixer.music.load('music/test music.mp3')
pygame.mixer.music.set_volume(0.5)  # Установка начальной громкости
pygame.mixer.music.play(-1)  # Воспроизводим музыку в бесконечном цикле

# Переменная для хранения громкости
volume = 0.5  # Начальная громкость (от 0.0 до 1.0)


# Функция для отрисовки кнопки
def draw_button(text, x, y, width, height, color, font=font):
    pygame.draw.rect(screen, color, (x, y, width, height))
    text_surface = font.render(text, True, (130, 115, 192))
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)


# Функция для отображения текущей громкости
def display_volume():
    volume_text = f"Громкость: {int(volume * 100)}%"
    text_surface = font.render(volume_text, True, (130, 115, 192))
    screen.blit(text_surface, (width // 2 - text_surface.get_width() // 2, 100))


# Основная функция
def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Проверка нажатия кнопки "Играть"
                if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
                    lvls()
                # Проверка нажатия кнопки "Настройки"
                if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 450:
                    settings_menu()

        # Отображаем фон главного меню
        screen.blit(background_image, (0, 0))

        # Рисуем кнопки
        draw_button("Играть", 300, 200, 200, 100, (8, 8, 17))
        draw_button("Настройки", 300, 350, 200, 100, (8, 8, 17))

        # Обновляем экран
        pygame.display.flip()


def settings_menu():
    global volume  # Используем глобальную переменную для громкости
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Проверка нажатия кнопки "Назад"
                if 300 <= mouse_x <= 500 and 450 <= mouse_y <= 550:
                    return  # Возвращаемся в главное меню

                # Проверка нажатия кнопки "Увеличить громкость"
                if 300 <= mouse_x <= 500 and 200 <= mouse_y <= 300:
                    if volume < 1.0:  # Проверяем, чтобы не превышать 1.0
                        volume = min(round(volume + 0.1, 2), 1.0)  # Увеличиваем громкость
                        pygame.mixer.music.set_volume(volume)

                # Проверка нажатия кнопки "Уменьшить громкость"
                if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 450:
                    if volume > 0.0:  # Проверяем, чтобы не опускаться ниже 0.0
                        volume = max(round(volume - 0.1, 2), 0.0)  # Уменьшаем громкость
                        pygame.mixer.music.set_volume(volume)

        # Отображаем фон меню настроек
        screen.blit(settings_background_image, (0, 0))

        # Рисуем кнопку "Назад"
        draw_button("Назад", 300, 450, 200, 100, (8, 8, 17))
        # Рисуем кнопку "Увеличить громкость"
        draw_button("Увеличить громкость", 200, 150, 400, 100, (8, 8, 17))
        # Рисуем кнопку "Уменьшить громкость"
        draw_button("Уменьшить громкость", 200, 300, 400, 100, (8, 8, 17))

        # Отображаем текущую громкость
        display_volume()

        # Обновляем экран
        pygame.display.flip()


# Уровни
def lvls():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Проверка нажатия кнопки "Назад"
                if 10 <= mouse_x <= 160 and 10 <= mouse_y <= 160:
                    return  # Возвращаемся в главное меню

                # Проверка нажатия на первый уровень
                if 10 <= mouse_x <= 160 and 225 <= mouse_y <= 375:
                    level_one()  # Переход к первому уровню

        # Отображаем фон меню уровней
        screen.blit(background_image, (0, 0))

        draw_button('1', 10, 225, 150, 150, (8, 8, 17), lvls_font)
        draw_button('Назад', 10, 10, 150, 150, (8, 8, 17))

        # Обновляем экран
        pygame.display.flip()


# Функция для первого уровня
def level_one():
    pygame.init()
    pygame.display.set_caption('Jump Ball')
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    background = pygame.image.load('photos/phon.png')
    background = pygame.transform.scale(background, (width, height))

    running = True
    y_ball = 200
    v0 = 0
    v = v0
    g = 10 * 10
    clock = pygame.time.Clock()

    # Позиция фона
    background_x = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Обработка нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            background_x += 1  # Двигаем фон влево
        if keys[pygame.K_RIGHT]:
            background_x -= 1  # Двигаем фон вправо

        # Отрисовка фона
        screen.blit(background, (background_x, 0))

        ball_size = 40, 40
        ball_a_size = 30, 50
        ball_d_size = 50, 30
        ball_x = 180 + int((ball_size[0] - ball_a_size[0]) / 2 * abs(v) / 296)
        ball_y = int(y_ball) + int((ball_size[1] - ball_a_size[1]) / 2 * abs(v) / 148)
        ball_x_size = int(ball_size[0] - 10 * abs(v) / 296)
        ball_y_size = int(ball_size[1] + 10 * abs(v) / 148)

        # Отрисовка шарика
        pygame.draw.ellipse(screen, (0, 255, 0), (ball_x, ball_y, ball_x_size, ball_y_size), 0)

        t = clock.tick() / 1000
        t = min(t, 0.05)
        v += g * t
        y_ball += v * t

        pygame.display.flip()

        if y_ball > height - ball_y_size - 0.01 * int(v):
            v = -v

    pygame.quit()


main_menu()
