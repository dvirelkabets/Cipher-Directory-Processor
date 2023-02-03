import os
import json
abcSize = 26

class CaesarCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintxt: str):
        newStr = ""
        for letter in plaintxt:
            if letter.isalpha():
                if letter.isupper():
                    newStr += chr((ord(letter) - ord('A') + self.key) % abcSize + ord('A'))
                elif letter.islower():
                    newStr += chr((ord(letter) - ord('a') + self.key) % abcSize + ord('a'))
            else:
                newStr += letter
        return newStr

    def decrypt(self, plaintxt: str):
        self.key = -self.key
        decryptStr = self.encrypt(plaintxt)
        self.key = -self.key
        return decryptStr


class VigenereCipher:
    def __init__(self, numArray):
        self.numArray = numArray
        self.keyArray = []
        for number in numArray:
            self.keyArray.append(CaesarCipher(number))

    def encrypt(self, plaintxt: str):
        newStr = ""
        index = 0
        for letter in plaintxt:
            if letter.isalpha():
                newStr += self.keyArray[index].encrypt(letter)
                index = (index + 1) % len(self.keyArray)
            else:
                newStr += letter

        return newStr

    def decrypt(self, plaintxt: str):
        for index, number in enumerate(self.numArray):
            self.keyArray[index] = CaesarCipher(-number)

        decryptStr = self.encrypt(plaintxt)

        for index, number in enumerate(self.numArray):
            self.keyArray[index] = CaesarCipher(-number)

        return decryptStr


def getVigenereFromStr(keyString):
    array = []
    for letter in keyString:
        if letter.isalpha():
            if letter.islower():
                array.append(ord(letter) - ord('a'))
            elif letter.isupper():
                array.append(ord(letter) - ord('A') + abcSize)
        elif letter.isdigit():
            array.append(int(letter))
    return VigenereCipher(array)


def processDirectory(dir_path: str):
    with open(os.path.join(dir_path, 'config.json')) as file:
        data = json.load(file)

    if data['type'] == 'Caesar':
        encryptType = CaesarCipher(int(data['key']))
    elif data['type'] == 'Vigenere':
        if (isinstance(data['key'], list)):
            encryptType=VigenereCipher(data['key'])
        else:
            encryptType = getVigenereFromStr(data['key'])

    files = os.listdir(dir_path)
    files = [f for f in files if os.path.isfile(os.path.join(dir_path, f))]

    if data['mode'] == 'encrypt':
        for file in files:
            if file.endswith('.txt'):
                fileNameTuple = os.path.splitext(file)
                with open(os.path.join(dir_path, file), 'r') as rootFile:
                    rawData = rootFile.read()
                with open(os.path.join(dir_path, (fileNameTuple[0]+'.enc')), 'w') as encryptedFile:
                    encryptedText = encryptType.encrypt(rawData)
                    encryptedFile.write(encryptedText)

    elif data['mode'] == 'decrypt':
        for file in files:
            if file.endswith('.enc'):
                fileNameTuple = os.path.splitext(file)
                with open(os.path.join(dir_path, file), 'r') as rootFile:
                    rawData = rootFile.read()
                with open(os.path.join(dir_path, (fileNameTuple[0]+'.txt')), 'w') as  decryptedFile:
                    decryptedFile.write(encryptType.decrypt(rawData))

def main():
    processDirectory(r'C:\Users\alkdv\Documents\homework\testFolder')


if __name__ == "__main__":
    main()