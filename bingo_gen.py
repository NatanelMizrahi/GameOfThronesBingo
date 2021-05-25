from PIL import Image, ImageOps
from random import shuffle
from math import ceil
from config import CHARACTER_MOSAIC_PATH, NUM_CARDS, OUT_PATH, CHARACTER_MOSAIC_LENGTH, BINGO_CARD_ROW_SIZE as N
from pathlib import Path

def split_mosaic_to_character_images(character_mosaic_path):
    width, height, x_step, y_step = get_bingo_dims_from_image(character_mosaic_path)
    original = Image.open(character_mosaic_path)
    character_images = []
    for i in range(CHARACTER_MOSAIC_LENGTH):
        for j in range(CHARACTER_MOSAIC_LENGTH):
            box = (i * x_step, j * y_step, (i + 1) * x_step, (j + 1) * y_step)
            character_crop_region = original.crop(box)
            character_images.append(character_crop_region)
    return character_images


def get_bingo_dims_from_image(character_mosaic_path):
    original = Image.open(character_mosaic_path)
    original_width, original_height = original.size
    x_step, y_step = original_width / CHARACTER_MOSAIC_LENGTH, original_height / CHARACTER_MOSAIC_LENGTH
    width, height = ceil(N * x_step), ceil(N * y_step)
    return width, height, x_step, y_step


def style_bingo_card(bingo_card_img, mask):
    img_with_opacity = Image.blend(bingo_card_img, mask, alpha=0.3)
    img_with_border = ImageOps.expand(img_with_opacity, border=3, fill='black')
    return img_with_border


def create_output_path():
    Path(OUT_PATH).mkdir(exist_ok=True)


def generate_bingo(character_mosaic_path):
    create_output_path()
    icons = split_mosaic_to_character_images(character_mosaic_path)
    width, height, x_step, y_step = get_bingo_dims_from_image(character_mosaic_path)
    mask = Image.new('RGB', (width, height), (255, 255, 255))
    for k in range(NUM_CARDS):
        new_img = Image.new('RGB', (width, height))
        shuffle(icons)
        for i in range(N):
            for j in range(N):
                new_img.paste(icons[N * i + j], (round(i * x_step), round(j * y_step)))
        styled_bingo_card = style_bingo_card(new_img, mask)
        styled_bingo_card.save(f"{OUT_PATH}/{k}.jpg")


if __name__ == "__main__":
    generate_bingo(CHARACTER_MOSAIC_PATH)
