from PIL import Image

import imagehash

path = r'path'

hash = imagehash.phash(Image.open(path))
print(hash)
