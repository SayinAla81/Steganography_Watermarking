import cv2
import numpy as np


image = cv2.imread('Encode_Flower.png')
plain_text = ""

def solve(image, plain_text):
    counter, binary_char = 0, 0
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if counter == 8:
                plain_text += chr(binary_char)
                if(chr(binary_char) == '#'):
                    return plain_text
                counter, binary_char = 0, 0
            binary_char = binary_char * 2 + (image[i, j, 0] & 1)
            counter += 1
            
print(solve(image, plain_text))
