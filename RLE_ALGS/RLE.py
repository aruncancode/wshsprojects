from conversion import *


class RLE():

    def RLEC(self, inputstream):
        last_char = ''
        compressed_data = []
        repeated_length = 0
        binary_string = ''

        for e in inputstream:
            if e == last_char:
                repeated_length += 1  # adds one to run length
                compressed_data.pop(-1)  # removes last element from list
                # adds new run length, with repeated bit
                compressed_data.append(str(repeated_length) + '*' + e)
            elif e != last_char:
                repeated_length = 1  # sets run length to 1
                compressed_data.append(
                    str(repeated_length) + '*' + e)  # adds bit to list
            last_char = e  # sets last bit

        for e in compressed_data:  # takes the compressed data and converts to bitstream
            # splits list at * to get separate the run length and bit
            compressed_string = e.split('*')
            repeats = compressed_string[0]  # sets run length and bit
            bit = compressed_string[1]
            # converts the run length to bin and adds it to output string, along with bit
            binary_string += (Conversions.dec_bin(1, int(repeats)) + bit)

        return binary_string  # returns compressed bitstream

    def RLED(self, inputstream):
        string = ''
        repeated_length = ''
        repeated_char = ''
        output_string = ''

        for e in inputstream:
            string += e  # adds bit to string
            if len(string) == 9:  # if string is length 9
                # takes the first 8 chars and converts them to dec
                repeated_length = Conversions.bin_dec(1, string[:8])
                # takes the last char and sets it to repeated char
                repeated_char = string[-1]
                # takes run length and multiplys it by repeated char
                output_string += (int(repeated_length)*repeated_char)
                string = ''  # resets string

        return output_string  # returns uncompressed bitstream

    def RLE_ALPHANUMERIC(self, alphanumericstream):
        binary_stream = ''
        for e in alphanumericstream:
            # converts ascii text to binary
            binary_stream += Conversions.ascii_bin(1, e)
        # parses uncompressed bitstream into RLEC, and returns the compressed bitstream
        return RLE.RLEC(1, binary_stream)
