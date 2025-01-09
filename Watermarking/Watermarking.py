from PIL import Image

def transparent(image_path, position, counter):
    watermark = Image.open("./masters/"+ str(counter) + ".png").convert("RGBA")
    image = Image.open(image_path)
    watermark = watermark.resize((position[2] - position[0], position[3] - position[1]))
    transparent_layer = Image.new("RGBA", image.size, (0, 0, 0, 0))
    transparent_layer.paste(watermark, position, mask=watermark)
    watermarked_image = Image.alpha_composite(image.convert("RGBA"), transparent_layer)
    watermarked_image.save("output.png")

transparent("image.jpg",  (50, 30, 70, 50), 22)
list_position = [(98, 35, 118, 55),(97, 55, 117, 75),(135, 16, 155, 36),(162, 40, 182, 60),
(161, 60, 181, 80),(227, 60, 247, 80),(246, 41, 266, 61),(246, 21, 266, 41),
(268, 68, 288, 88),(282, 51, 301, 71),(304, 125, 321, 142),(304, 108, 321, 125),
(321, 66, 336, 81),(321, 81, 336, 96),(160, 125, 180, 145),(159, 145, 179, 165),
(268, 134, 288, 154),(94, 125, 114, 145),(93, 145, 113, 165),(216, 118, 236, 138),
(236, 147, 256, 167)]

counter = 1
for i in list_position:
    transparent("output.png", i, counter)
    counter += 1