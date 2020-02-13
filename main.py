# RLE encoder and decoder

string = 'aaaaaaaaaaabbbbbbbbbbbbcccccccccdddddddddddde'


def rel_test(input_string):

    iter_char = ''
    repeated_length = 0
    repeated_char = ''
    output_string = ''

    first_run = True
    compressed_data = []

    for e in input_string:
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

    return input_string, output_string


print(rel_test(string))
