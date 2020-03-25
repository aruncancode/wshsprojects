class CaesarCipher():

    def encrypt(self, text, s):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        shitfted_alphabet = alphabet[s:] + alphabet[:s]
        output = ""

        for e in text:
            if e.isupper():
                index = alphabet.index(e)
                output += shitfted_alphabet[index]
            elif e.islower():
                index = alphabet.index(e.upper())
                output += (shitfted_alphabet[index]).lower()
            else:
                output += e
        return output

    def decrypt(self, text, s):
        alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                    "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        shitfted_alphabet = alphabet[s:] + alphabet[:s]
        output = ""

        for e in text:
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

print("ENCRYPTED", C.encrypt("test", 5))
print("DECRYPTED", C.decrypt("fyyfhp fy ifbs", -21))
