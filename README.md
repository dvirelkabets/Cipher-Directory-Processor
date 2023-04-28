# Caesar and Vigenere Cipher

## Overview

This Python script contains implementations of the Caesar and Vigenere ciphers. It allows the user to encrypt or decrypt files in a specified directory using either cipher.

## Usage

### Installation

1. Install Python 3.x (if not already installed) from the [official Python website](https://www.python.org/downloads/).
2. Clone or download this repository.
3. Navigate to the project directory.

### Configuration

1. Open the `config.json` file located in the project directory.
2. Set the `type` field to either "Caesar" or "Vigenere", depending on which cipher you want to use.
3. Set the `key` field to the encryption key you want to use. If using the Caesar cipher, this should be an integer. If using the Vigenere cipher, this can be a list of integers or a string containing letters and/or numbers.

### Running the Script

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the command `python caesar_vigenere_cipher.py`.

### Caesar Cipher

The Caesar Cipher is a simple substitution cipher in which each letter in the plaintext is shifted a certain number of places down the alphabet.

The `CaesarCipher` class in this script takes an encryption key (an integer) when instantiated. The `encrypt()` and `decrypt()` methods can then be used to encrypt and decrypt strings using the Caesar Cipher.

### Vigenere Cipher

The Vigenere Cipher is a more complex polyalphabetic substitution cipher in which the encryption key is a series of letters, which are used to perform multiple Caesar Cipher shifts at different points in the plaintext.

The `VigenereCipher` class in this script takes an array of integers as the encryption key when instantiated. The `encrypt()` and `decrypt()` methods can then be used to encrypt and decrypt strings using the Vigenere Cipher.

### File Processing

The `processDirectory()` function in this script takes a directory path as an argument and processes all the files in the directory according to the configuration specified in `config.json`. If the configuration specifies encryption mode, all `.txt` files in the directory will be encrypted and saved with a `.enc` extension. If the configuration specifies decryption mode, all `.enc` files in the directory will be decrypted and saved with a `.txt` extension.

## Contributors

-[Dvir Elkabets](https://github.com/dvirelkabets)

