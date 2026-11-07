import sys
from filters import blur
from image import Image

originalFileName = sys.argv[1]
blurredFileName = sys.argv[2]
 
ogFile = Image.read(originalFileName)
blurredFile = blur(ogFile)

blurredFile.write_pgm(blurredFileName)