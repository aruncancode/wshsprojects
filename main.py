from RLE import *


encoding = open('encoding.txt', 'r+')
encode_string = encoding.read()
decoding = open('decoding.txt', 'r+')
decode_string = decoding.read()


print(RLE.RLEC(1, encode_string))
print(RLE.RLED(1, decode_string))
