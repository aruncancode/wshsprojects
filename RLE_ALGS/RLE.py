from conversion import *


class RLE():

    def RLEC(self, inputstream):
        last_char = ''
        compressed_data = []
        repeated_length = 0
        binary_string = ''

        for e in inputstream:
            if e == last_char:
                repeated_length += 1
                compressed_data.pop(-1)
                compressed_data.append(str(repeated_length) + '*' + e)
            elif e != last_char:
                repeated_length = 1
                compressed_data.append(str(repeated_length) + '*' + e)
            last_char = e

        for e in compressed_data:
            compressed_string = e.split('*')
            repeats = compressed_string[0]
            bit = compressed_string[1]
            binary_string += (Conversions.dec_bin(1,
                                                  int(repeats)) + bit)

        return binary_string

    def RLED(self, inputstream):
        string = ''
        repeated_length = ''
        repeated_char = ''
        output_string = ''

        for e in inputstream:
            string += e
            if len(string) == 9:
                repeated_length = Conversions.bin_dec(1, string[:8])
                repeated_char = string[-1]
                output_string += (int(repeated_length)*repeated_char)
                repeated_length = ''
                string = ''

        return output_string
