from RLE import *


encoding = open('input.txt', 'r+')
input_string = encoding.read()


output = RLE.RLEC(1, input_string)


print("INPUT: %s \nLENGTH: %s" %
      (input_string, str(len(input_string))))

print("OUPUT: %s \nLENGTH: %s" %
      (output, str(len(output))))


print('EFFICIENY: ' + str(1 - len(output)/len(input_string)))
