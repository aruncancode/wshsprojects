# RLE encoder and decoder
class RLE():

    # these algs are for compressing and decompressing binary data.
    # they're also able to process alphanumeric strings, without binary conversion.
    # ASCII_CONVERSION is able to convert alphanumeric strings into ascii and ba

    def RLEC(self, inputstream):

        iter_char = ''
        repeated_length = 0
        repeated_char = ''
        output_string = ''
        first_run = True
        run = 0
        compressed_data = []

        for e in inputstream:
            if first_run == True:
                iter_char = e
                repeated_length = 1
                compressed_data.append(e)
                first_run = False

            elif e == iter_char:
                repeated_char = e
                repeated_length += 1
                compressed_data.pop(-1)
                if len(compressed_data) != 0:
                    if compressed_data[-1].isnumeric() == True:
                        compressed_data.append(',')
                compressed_data.append(
                    str(repeated_length) + '*' + str(repeated_char))

            elif e != iter_char:
                compressed_data.append(e)
                repeated_length = 1
                repeated_char = ''
                iter_char = e

            run += 1
            # print(compressed_data)

        for e in compressed_data:
            output_string += e
            # output_string += ' '

        return output_string

    def RLED(self, inputstream):

        multiply = ''
        output_string = ''
        stop = False
        compressed_data = []
        possible_numbers = ''
        iter_list = iter(inputstream)
        run = 0

        for e in iter_list:

            if e.isnumeric() == True and stop == False:
                if run != 0:
                    if compressed_data[-1] == possible_numbers:
                        compressed_data.pop(-1)
                possible_numbers += e
                multiply += e
                compressed_data.append(possible_numbers)

            elif e.isalpha() == True and stop == False:
                compressed_data.append(e)
                possible_numbers = ''
                multiply = ''

            elif stop == True:
                compressed_data.pop(-1)
                compressed_data.append(int(multiply) * e)
                possible_numbers = ''
                multiply = ''
                stop = False

            elif e == ',':
                multiply = ''
                possible_numbers = ''

            elif e == '*':
                stop = True

            run += 1

        for e in compressed_data:
            output_string += e

            # print(compressed_data)

        return output_string
