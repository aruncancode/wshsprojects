from RLE import *


encoding = open('input.txt', 'r')
uncompressed_string = encoding.read()


output = RLE.RLED(1, uncompressed_string)


<<<<<<< HEAD
print("INPUT:  %s  LENGTH: %s" %
      (uncompressed_string, str(len(uncompressed_string))))

print("OUPUT: %s LENGTH: %s" %
      (output, str(len(output))))

print('EFFICIENY: ' + str(1 - len(output)/len(uncompressed_string) * 100))
=======
print(RLE.RLEC(1, encode_string))
# print(RLE.RLED(1, decode_string))

# RLE.RLE_ASCII(1, encode_string)




print(1- (len(decode_string) / len(encode_string)))
>>>>>>> 7397ce9ca658d219870869857e34aa52d19bf720
