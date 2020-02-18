def ascii_to_binary(ascii_char_2):
    ascii_dec = ascii_to_dec(ascii_char_2)
    ascii_bin_num = dec_to_bin(ascii_dec)
    byte = int(len(ascii_bin_num)) / int(8) + ((len(ascii_bin_num)) % 8 > 0)
    print("Your binary number is " + str(ascii_bin_num))
    print("It is " + str(round(int(byte))) + " bytes")

ascii_list = [" ", "!", "", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", "0", "1", "2", "3", "4", "5", "6",
                  "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G","H", "I", "J", "K", "L", "M", "N", "O",
                  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i"
                  , "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]

def binary_to_ascii(binary_char_2):
    binary_dec = bin_to_dec(binary_char_2)
    dec_ascii_num = dec_to_ascii(binary_dec)
    print(dec_ascii_num)

def dec_to_ascii(decimal_char):
    ascii = decimal_char - 32 #If the pattern to find the decimal value is to add 32 then this just takes 32 to get the position in the list.
    ascii_char = ascii_list[ascii] #the square brackets just finds the position in the list
    print(str(ascii_char) + " is your ASCII character.") #prints the answer.