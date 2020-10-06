# !/usr/bin/python3

from vigenere_cipher import VigenereCipher
from text import TextResource
from character_frequency_analysis import CharacterFrequencyAnalyzer
import sys

assert sys.version_info >= (3, 6, 0), "Python version too low."


if __name__ == "__main__":\

    v = VigenereCipher(
        "elijah", plaintext="Used to perform vigenere encryption, vigenere decryption, and analysis on text.")
    v.encrypt()
    # resource = TextResource("example_literature/shakespeare.txt")
    freq_analysis_c = CharacterFrequencyAnalyzer(v.cipher_text)
    freq_analysis_p = CharacterFrequencyAnalyzer(v.plaintext)
    freq_analysis_c.print_frequency()
    freq_analysis_p.print_frequency()
    print(v.cipher_text)
    print(v.plaintext)
