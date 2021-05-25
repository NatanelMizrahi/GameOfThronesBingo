from PIL import Image, ImageOps
from random import shuffle
from math import ceil

NUM_CARDS = 50
NUM_CHARS = 28
N = 5

src = "./icons/out"
dest = "./bingos"
original = Image.open("all2.jpg")

width, height = original.size   
x_step, y_step = width/10, height/10
width, height = ceil(N*x_step), ceil(N*y_step)

mask = Image.new('RGB', (width,height), (255, 255, 255))

icons = [Image.open("{}/{}.jpg".format(src,i)) for i in range(NUM_CHARS)]

for k in range(NUM_CARDS):
	new_img = Image.new('RGB', (width, height))
	shuffle(icons)
	for i in range(N):
		for j in range(N):
			new_img.paste(icons[N*i+j], (round(i*x_step),round(j*y_step)))
	new_img = Image.blend(new_img, mask, alpha=0.3)
	new_img = ImageOps.expand(new_img,border=3,fill='black')
	new_img.save("{}/{}.jpg".format(dest,k))