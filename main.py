# RLE encoder and decoder

string = 'AAAAAAAABBBBBBBBBBCCCCCCCCC'
compressed_string = '8A10B9C'


def RLEC(inputstream):

    iter_char = ''
    repeated_length = 0
    repeated_char = ''
    output_string = ''
    first_run = True
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
            compressed_data.append(str(repeated_length)+repeated_char)

        elif e != iter_char:
            compressed_data.append(e)
            repeated_length = 1
            repeated_char = ''
            iter_char = e

    for e in compressed_data:
        output_string += e

    return inputstream, output_string


# print(RLEC(string))


def RLED(inputstream):

    multiply = 0
    output_string = ''

    for e in inputstream:
        if e.isalpha() == False:
            multiply = int(e)
            print(multiply)
        elif e.isalpha() == True:
            output_string += multiply * e
            multiply = 0

    return output_string


print(RLED(compressed_string))
