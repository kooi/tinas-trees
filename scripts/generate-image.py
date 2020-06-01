import glob
import os.path
from PIL import Image
import io

folders = ['./tree.py']

for folder in folders:

	files = glob.glob(folder)

	for f in files:
		  exec(open(f).read())
		  ps = tina.getscreen().getcanvas().postscript()
		  img = Image.open(io.BytesIO(ps.encode('utf-8')))
		  img.save(os.path.splitext(f)[0]+'.png')
		  turtle.clearscreen()
