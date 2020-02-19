
class Conversions():

    def ascii_bin(self, ascii_input=""):
        output = ''
        for e in [bin(ord(x))[2:].zfill(8) for x in ascii_input]:
            output += e
        return output

    def bin_ascii(self, binary):
        string = ''
        bin_input = []
        for e in binary:
            string += e
            if len(string) == 8:
                bin_input.append(string)
                string = ''

        return ''.join([chr(int(x, 2)) for x in bin_input])
