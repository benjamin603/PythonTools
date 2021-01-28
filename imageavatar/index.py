from PIL import Image, ImageDraw, ImageFont

font_size = 7
text = "我喜欢你！"
img_path = "D://20210128210942.jpg" 

img_raw = Image.open(img_path)
img_array = img_raw.load()

#字体和字体大小
img_new = Image.new("RGB", img_raw.size, (0, 0, 0))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)

def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]

ch_gen = character_generator(text)

#字体颜色并写入
for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font, fill=img_array[x, y], direction=None)

#输出成品
img_new.convert('RGB').save("D://image-avatar.jpg")