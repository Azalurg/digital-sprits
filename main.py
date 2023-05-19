# Author: Azalurg
# Description: Image generator inspired by Sprite-Generator by @MaartenGr

# Mask code: -1 = transparent, 0 = black, 1 = white, other = colors

from src import spirit
from src import mask

size = 8
mask_key = 112
spirit_key = 102
name = f"{size}_{mask_key}_{spirit_key}"

print('Generating mask...')
generated_mask, mask_key = mask.generate(mask_key, width=size//2, height=size)
print('Generating spirit...')
result_code = spirit.generate(generated_mask, spirit_key, name)
if result_code == 0:
    print('Done!')
