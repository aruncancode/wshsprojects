from RLE import *


encoding = open('input.txt', 'r')
uncompressed_string = encoding.read()


output = RLE.RLEC(1, uncompressed_string)


print("INPUT:  %s  LENGTH: %s" %
      (uncompressed_string, str(len(uncompressed_string))))

print("OUPUT: %s LENGTH: %s" %
      (output, str(len(output))))

print('EFFICIENY: ' + str(1 - len(output)/len(uncompressed_string) * 100))
