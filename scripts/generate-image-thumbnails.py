import glob
import os.path
from PIL import Image
import io

folders = ['./*.png']

for folder in folders:

	files = glob.glob(folder)

	for f in files:
        img = Image.open(f)
		img_thumb = img.resize( (200,200) ).crop( (50, 50, 150, 150) )
		img_thumb = img_thumb.save( os.path.splitext(f)[0]+'_thumb'+'.png' )
