# Author: Azalurg
# Description: Image generator inspired by Sprite-Generator by @MaartenGr

# Mask code: -1 = transparent, 0 = black, 1 = white, other = colors

from src import spirit
from src import mask


spirit_key = 102
mask_key = 112

print('Generating mask...')
generated_mask, mask_key = mask.generate(mask_key, width=32//2, height=32)
print('Generating spirit...')
result_code = spirit.generate(generated_mask, spirit_key, mask_key)
if result_code == 0:
    print('Done!')
