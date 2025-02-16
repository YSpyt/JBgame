import pygame
import sys
import os
import time

pygame.init()

# Определяем размеры окна
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('JBgame')

font = pygame.font.Font(None, 48)
lvls_font = pygame.font.Font(None, 100)
sky = pygame.image.load('photos/sky.png')

# Загружаем изображение фона
background_image = pygame.image.load('photos/menu.jpg')
settings_background_image = pygame.image.load('photos/menu.jpg')

# Загружаем и воспроизводим фоновую музыку
pygame.mixer.music.load('music/JBgame soundtrack(by Famour).mp3')
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
                    continue
                # Проверка нажатия кнопки "Настройки"
                if 300 <= mouse_x <= 500 and 350 <= mouse_y <= 450:
                    settings_menu()
                    continue

        # Отображаем фон главного меню
        screen.blit(background_image, (0, 0))

        # Рисуем кнопки
        draw_button("Играть", 300, 200, 200, 100, (8, 8, 17))
        draw_button("Настройки", 300, 350, 200, 100, (8, 8, 17))

        # Обновляем экран
        pygame.display.flip()


# Меню настроек
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
                    main_menu()  # Возвращаемся в главное меню

                # Проверка нажатия на первый уровень
                if 10 <= mouse_x <= 160 and 225 <= mouse_y <= 375:
                    first_lvl()  # Переход к первому уровню

        # Отображаем фон меню уровней
        screen.blit(background_image, (0, 0))

        draw_button('1', 10, 225, 150, 150, (8, 8, 17), lvls_font)
        draw_button('Назад', 10, 10, 150, 150, (8, 8, 17))

        # Обновляем экран
        pygame.display.flip()


# Функция для расчета столкновения с препятствием
def check_collision(center_x, center_y, i):  # i = (x0, y0, x1, y1)
    # Для удобства создаем переменную радиуса
    R = 26.5
    # Проверяем углы препятствия, используя теорему Пифагора
    if min(abs(center_x - i[0]), abs(center_x - i[2])) ** 2 + min(abs(center_y - i[1]),
                                                                  abs(center_y - i[3])) ** 2 <= R ** 2:
        return True

    # В случае, если мячик не касается края, то проверяем находится ли его нижняя часть между двумя краями препятствия
    # и касается ли она его по высоте

    if i[0] <= center_x <= i[2] and i[1] <= center_y + R and i[3] >= center_y + R:
        return True
    return False


# Функция для первого уровня
def first_lvl():
    pygame.init()
    pygame.display.set_caption('Jump Ball')

    background = pygame.image.load('photos/phon.png')

    back_to_lvls = pygame.image.load('photos/back_to_lvls.png')

    win_window = pygame.image.load('photos/win_window.png')

    running = True
    y_ball = height - 189
    v0 = 0
    v = v0
    g = 10 * 10
    clock = pygame.time.Clock()
    ball_x = 180
    ball_y = int(y_ball)
    x = ball_x
    s = []  # Создаем список координат препятствий
    s1 = [] # Создаем список координат шипов

    # Координаты препятствий
    s.append((379, 359, 414, 480))  # x0, y0, x1, y1
    s.append((494, 239, 529, 480))
    s.append((609, 133, 644, 480))
    s.append((803, 308, 1603, 343))
    s.append((1763, 344, 2038, 480))
    s.append((2179, 344, 2454, 480))
    s.append((2631, 345, 2906, 481))

    # Координаты шипов
    s1.append((1056, 218, 1146, 308))
    s1.append((1349, 216, 1396, 308))
    s1.append((1876, 252, 1918, 344))
    s1.append((2319, 257, 2352, 343))
    s1.append((2753, 260, 2787, 345))
    s1.append((644, 344, 811, 480))
    s1.append((1598, 350, 1763, 480))
    s1.append((2037, 353, 2196, 480))
    s1.append((2471, 354, 2630, 480))


    # Создаем анимированный спрайт мячика
    ball_sprite = load_image("ball_anim.png")
    all_sprites = pygame.sprite.Group()
    ball = AnimatedSprite(ball_sprite, 22, 1, ball_x, ball_y, frame_delay=20, scale_factor=1)
    all_sprites.add(ball)
    flag = True

    # Позиция фона
    background_x = 0

    start_time = time.time()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                # Проверка нажатия кнопки назад к уровням
                if 10 <= mouse_x <= 46 and 10 <= mouse_y <= 54 and flag:
                    lvls()  # Возвращаемся в меню уровней
                    continue

                # Проверка нажатия кнопки к уровням
                if 192 <= mouse_x <= 294 and 281 <= mouse_y <= 383:
                    lvls()  # Возвращаемся в меню уровней
                    continue

                # Проверка нажатия кнопки пройти заново
                if 349 <= mouse_x <= 449 and 281 <= mouse_y <= 383:
                    first_lvl()  # Запускаем уровень заново
                    continue

                # Проверка нажатия кнопки перейти к следующему уровнью
                if 349 <= mouse_x <= 449 and 281 <= mouse_y <= 383:
                    pass
                    # second_lvl()  # Запускаем второй уровень

        if flag:
            # Обработка нажатий клавиш
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and background_x < 0:
                # Двигаем фон влево
                background_x += 0.75
                # Записываем изменение координат шарика
                x -= 0.75
            if keys[pygame.K_RIGHT] and background_x > width - 3500:
                # Двигаем фон вправо
                background_x -= 0.75
                # Записываем изменение координат шарика
                x += 0.75

            # Отрисовка фона
            screen.blit(sky, (0, 0))
            screen.blit(background, (background_x, 0))

            # Отрисовка кнопки возврата к уровням
            screen.blit(back_to_lvls, (10, 10))

            # Обновляем физику мяча
            t = clock.tick() / 1000
            t = min(t, 0.05)
            v += g * t
            y_ball += v * t

            # Победа после пересечения определенной границы по x
            if x >= 2850:
                flag = False
                # отрисовываем всё как было и рисуем окно победы
                screen.blit(sky, (0, 0))
                screen.blit(background, (background_x, 0))
                screen.blit(win_window, (0, 0))
                elapsed_time = time.time() - start_time
                with open("best_time.txt.txt") as f:
                    lines = f.readlines()
                if lines[0] == '\n':
                    lines[0] = f'{elapsed_time:.2f}'
                else:
                    lines[0] = str(min(float(lines[0][:-1]), float(f"{elapsed_time:.2f}"))) + '\n'
                print(f'Текущее время: {f'{elapsed_time:.2f}'}\nЛучшее время: {lines[0]}')
                start_time = None
                with open("best_time.txt", "w") as f:
                    f.writelines(lines)
                continue

            # Проверка на столкновение с полом
            if y_ball + 69 > height - 120:
                v = -167
                # Запуск звука удара
                pygame.mixer.Sound("music/ball punch.mp3").play()
                # Начало анимации
                ball.animation_complete = False  # Сброс флага завершения анимации
                y_ball = height - 189  # Установка мяча на пол

                # Сброс анимации к первому кадру
                ball.reset_animation()

            # Проверка касания шипа
            for i in s1:
                if check_collision(x + 31, y_ball + 34.5, i):
                    first_lvl()
                    continue

            # Проверка касания препятствия
            for i in s:
                if check_collision(x + 31, y_ball + 34.5, i):
                    v = -167
                    # Запуск звука удара
                    pygame.mixer.Sound("music/ball punch.mp3").play()
                    # Начало анимации
                    ball.animation_complete = False  # Сброс флага завершения анимации
                    y_ball = i[1] - 69  # Установка мяча на верх препятствия

                    # Сброс анимации к первому кадру
                    ball.reset_animation()

            # Обновляем координаты мяча
            ball.rect.topleft = (ball_x, y_ball)

            # Обновляем и отрисовываем спрайты
            all_sprites.update()
            all_sprites.draw(screen)

        pygame.display.flip()

    pygame.quit()


# Функция для загрузки изображения
def load_image(name, colorkey=None):
    fullname = os.path.join('photos', name)
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


# Класс анимированного спрайта
class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, frame_delay=5, scale_factor=1):
        super().__init__()
        self.frames = []
        self.scale_factor = scale_factor
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.counter = 0
        self.frame_delay = frame_delay
        self.animation_complete = False

    # Функция для нарезания анимации на кадры
    def cut_sheet(self, sheet, columns, rows):
        frame_width = sheet.get_width() // columns
        frame_height = sheet.get_height() // rows
        for j in range(rows):
            for i in range(columns):
                frame_location = (frame_width * i, frame_height * j)
                frame = sheet.subsurface(pygame.Rect(frame_location, (frame_width, frame_height)))

                if self.scale_factor != 1:
                    frame = pygame.transform.scale(frame, (
                    int(frame_width * self.scale_factor), int(frame_height * self.scale_factor)))

                self.frames.append(frame)

    # Функция для сброса анимации
    def reset_animation(self):
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]

    # Функция для обновления кадра анимации
    def update(self):
        # Проверяем, завершена ли анимация
        if not self.animation_complete:
            # Увеличиваем счетчик кадров
            self.counter += 1

            # Проверяем, достиг ли счетчик задержки для смены кадра
            if self.counter >= self.frame_delay:
                # Сбрасываем счетчик
                self.counter = 0

                # Переходим к следующему кадру анимации
                self.cur_frame += 1

                # Если текущий кадр превышает количество доступных кадров, сбрасываем его на 0
                if self.cur_frame >= len(self.frames):
                    self.cur_frame = 0

                # Обновляем изображение текущим кадром анимации
                self.image = self.frames[self.cur_frame]


main_menu()
