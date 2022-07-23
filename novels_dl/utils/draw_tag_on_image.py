from PIL import Image, ImageDraw, ImageFont
from novels_dl.assets import get_asset


def draw_tag_on_image(img: Image, text: str):
    draw = ImageDraw.Draw(img)
    font_path = get_asset("fonts", "OpenSans-Regular.ttf")
    font = ImageFont.truetype(font_path, 40, encoding="utf-8")

    font_width, font_height = font.getsize(text)
    font_width += 10
    font_height += 10

    point_a = (img.width - font_width) / 2, img.height * (8.5/9) - font_height
    point_b = (img.width - font_width) / 2 + font_width, img.height * (8.5/9)

    draw.rectangle((*point_a, *point_b), fill=(35, 35, 35))
    draw.text((point_a[0] + 3, point_a[1] + 2), text, fill='white', font=font)
