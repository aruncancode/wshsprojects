# MAINLINE

from RLE import *  # imports rle algs and conversions


encoding = open('input.txt', 'r+')  # opens input.txt, in read/write form
input_string = encoding.read()  # input_string is set to file data


output = RLE.RLED(1, input_string)

# output = Conversions.bin_ascii(1, RLE.RLED(
#     1, input_string))


print("INPUT: %s \nLENGTH: %s" %
      (input_string, str(len(input_string))))
print("OUPUT: %s \nLENGTH: %s" %
      (output, str(len(output))))
print('EFFICIENY: ' + str(1 - len(output)/len(input_string)))
