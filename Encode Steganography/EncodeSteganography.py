import cv2
import numpy as np


image = cv2.imread('Flower.jpg')
plain_text = "Salam Khoobi?#"
binary_plain_text = list()
counter = 0

for i in range(len(plain_text) - 1, -1, -1):
    temp = ord(plain_text[i])
    for _ in range(8):
        binary_plain_text.append(temp % 2)
        temp //= 2
binary_plain_text = list(reversed(binary_plain_text))

for i in range(image.shape[0]):
    for j in range(image.shape[1]):
        if(counter == len(binary_plain_text)):
            break
        for k in range(image.shape[2]):
            image[i, j, k] ^= abs(binary_plain_text[counter] - (image[i, j, k] & 1))
        counter += 1

cv2.imwrite('Encode_Flower.png', image)