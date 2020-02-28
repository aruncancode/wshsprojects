
class Conversions():

    def ascii_bin(self, ascii_input=""):  # converts ascii to bin
        output = ''
        for e in [bin(ord(x))[2:].zfill(8) for x in ascii_input]:
            output += e
        return output

    def bin_ascii(self, binary):  # converts bin to ascii
        string = ''
        bin_input = []
        for e in binary:
            string += e
            if len(string) == 8:
                bin_input.append(string)
                string = ''

        return ''.join([chr(int(x, 2)) for x in bin_input])

    def dec_bin(self, decimal):  # converts dec to bin
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal = decimal // 2
        binary = binary.zfill(8)
        return binary

    def bin_dec(self, n):  # converts bin to dec
        return int(n, 2)
