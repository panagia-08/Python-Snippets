import base64 

imager = r'path'

image = open(imager, 'rb')
image_read = image.read()
image_64_encode = base64.encodestring(image_read)
image_64_decode = base64.decodestring(image_64_encode) 
image_result = open('deer_decode.gif', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)

print (image_64_encode)
