import cv2
import numpy as np
import random

def generate_captcha(width, height, length):

    # Генерируем случайную строку для капчи
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', k=length))
    # captcha_text = "hello"
    # Создаем изображение для капчи
    image = np.ones((height, width, 3), np.uint8) * 255

    # Устанавливаем шрифт и его параметры
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.5
    font_thickness = 2

    # Рассчитываем позицию для отображения текста на капче
    text_size = cv2.getTextSize(captcha_text, font, font_scale, font_thickness)[0]
    letter_width = text_size[0]//len(captcha_text)
    text_x = (width - text_size[0]) // 2 - letter_width
    text_y = (height + text_size[1]) // 2

    # Рисуем текст по буквам на изображении капчи
    for letter in captcha_text:
        text_x += letter_width + random.randint(-10, 0)
        text_y += random.randint(-10, 10)
        cv2.putText(image, letter, (text_x, text_y), font, font_scale, (0, 0, 0), font_thickness)

    for _ in range(3):
        x1 = random.randint(-width, -width // 2)
        y1 = random.randint(-height//2, height + height//2)
        x2 = random.randint(width, width * 2)
        y2 = random.randint(-height//2, height + height//2)

        cv2.line(image, (x1, y1), (x2, y2), (0, 0, 0), thickness=2)

    cv2.imshow('Captcha', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return captcha_text

# Задаем размерность капчи
captcha_width = 200
captcha_height = 80

# Задаем длину текста на капче
captcha_length = 6

captcha_text = generate_captcha(captcha_width, captcha_height, captcha_length)
print('Captcha text:', captcha_text)
