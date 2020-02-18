

class Conversions():

    def ascii_bin(self, ascii_input=""):
        output = ''
        for e in [bin(ord(x))[2:].zfill(8) for x in ascii_input]:
            output += e
        return output

    def bin_ascii(self, bin_input=None):
        return ''.join([chr(int(x, 2)) for x in bin_input])


# print(ascii_bin('4*04*1'))

# print(bin_ascii(ascii_bin('4*04*1')))

print(Conversions.bin_ascii(1, ['00010001', '01000010']))
