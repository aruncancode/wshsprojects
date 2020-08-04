class CaesarCipher():

    def caesar_e(self, plaintext, keyvalue):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        shitfted_alphabet = alphabet[keyvalue:] + alphabet[:keyvalue]
        output = ""

        for e in plaintext:
            if e.isupper():
                index = alphabet.index(e)
                output += shitfted_alphabet[index]
            elif e.islower():
                index = alphabet.index(e.upper())
                output += (shitfted_alphabet[index]).lower()
            else:
                output += e
        return output

    def caesar_d(self, ciphertext, keyvalue):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        shitfted_alphabet = alphabet[keyvalue:] + alphabet[:keyvalue]
        output = ""

        for e in ciphertext:
            if e.isupper():
                index = shitfted_alphabet.index(e)
                output += shitfted_alphabet[index]
            elif e.islower():
                e = e.upper()
                index = shitfted_alphabet.index(e)
                output += (alphabet[index]).lower()
            else:
                output += e
        return output


C = CaesarCipher()

print("ENCRYPTED:", C.caesar_e('arun234', 5))
print("DECRYPTED:", C.caesar_d("yjxy", 5))
