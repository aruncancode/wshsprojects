def encrypt(text, s):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    shitfted_alphabet = alphabet[s:] + alphabet[:s]
    output = ""

    for e in text:
        if e.isupper():
            index = alphabet.index(e) + s
            output += shitfted_alphabet[index]
        else:
            e = e.upper()
            index = alphabet.index(e) + s
            output += (shitfted_alphabet[index]).lower()

    return output


def decrypt(text, s):
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    shitfted_alphabet = alphabet[s:] + alphabet[:s]
    output = ""

    for e in text:
        if e.isupper():
            index = shitfted_alphabet.index(e) - s
            output += shitfted_alphabet[index]
        else:
            e = e.upper()
            index = shitfted_alphabet.index(e) - s
            output += (alphabet[index]).lower()

    return output


print(decrypt("EvyrTewwASVH", 2))
