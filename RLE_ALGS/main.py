from RLE import *


encoding = open('input.txt', 'r+')
input_string = encoding.read()


# output = RLE.RLE_ALPHANUMERIC(1, input_string)

# output = Conversions.bin_ascii(1, RLE.RLED(
#     1, input_string))

print("INPUT: %s \nLENGTH: %s" %
      (input_string, str(len(input_string))))

print("OUPUT: %s \nLENGTH: %s" %
      (output, str(len(output))))


print('EFFICIENY: ' + str(1 - len(output)/len(input_string)))
