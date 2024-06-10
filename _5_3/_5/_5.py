import cv2

# Загружаем изображения
image1 = cv2.imread("img_1.png")
image2 = cv2.imread("img_2.png")

# Изменяем размер второго изображения, чтобы оно совпадало с размерами первого
image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Наложение изображений
result = cv2.addWeighted(image1, 0.5, image2, 0.3, 0)

# Отображение результата
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
