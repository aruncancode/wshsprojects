# RLE encoder and decoder

encoding = open('encoding.txt', 'r+')
encode_string = encoding.read()

decoding = open('decoding.txt', 'r+')


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
            if e.isnumeric() == True:
                compressed_data.append(
                    str(repeated_length) + "*" + repeated_char+',')
            else:
                compressed_data.append(str(repeated_length) + repeated_char)

        elif e != iter_char:
            if e.isnumeric() == True:
                compressed_data.append(e + ',')
            else:
                compressed_data.append(e)
            repeated_length = 1
            repeated_char = ''
            iter_char = e

    for e in compressed_data:
        output_string += e
        if e == ',':
            pass

    return compressed_data


def RLED(inputstream):

    multiply = ''
    output_string = ''
    stop = False

    for e in inputstream:
        if e.isnumeric() == True and stop != True:
            multiply += e

        elif e == '*':
            stop = True

        elif e.isalpha() == True:
            if multiply != '':
                output_string += int(multiply) * e
            else:
                output_string += e
            multiply = ''

        elif e == ',':
            multiply = ''

        elif stop == True:
            output_string += int(multiply) * e
            multiply = ''
            stop = False

    return output_string


# decoding.write(RLEC(encode_string))

# decoding = decoding.read()
# print(RLED(decoding))

print(RLEC(encode_string))
