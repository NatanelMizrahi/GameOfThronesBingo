import glob
import shutil
from pathlib import Path
next_id = 0
out = "./icons/out"
Path(out).mkdir(exist_ok=True)
for filename in glob.glob('./icons/*.jpg'):
	shutil.copy(filename,'{}/{}.jpg'.format(out,next_id))
	next_id += 1
