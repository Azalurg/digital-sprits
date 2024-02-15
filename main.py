# Author: Azalurg
# Description: Image generator inspired by Sprite-Generator by @MaartenGr

# Mask code: -1 = transparent, 0 = black, 1 = white, other = colors

from src import spirit
from src.mask import Mask
from src.spirit import Spirit

print("Generating mask...")
mask = Mask(16, 16, 2, axes=1, salt=2)
mask.generate()
print("Generating spirit...")
Spirit(mask)
