from PIL import Image
out = "./icons" 
original = Image.open("all_characters.jpg")
width, height = original.size   
x_step, y_step  = width/10, height/10
f_name = None 
for i in range(10):
	for j in range(10):
		box = (i*x_step, j*y_step, (i+1)*x_step, (j+1)*y_step)
		crop = original.crop(box)
		f_name = "{}/{}.jpg".format(out,(10*i+j))
		crop.save(f_name)