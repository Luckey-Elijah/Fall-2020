import sys

alphabet_to_val = {}
alphabet_list = []


def gen_full_key(plaintext, key):
    '''
    Generates the full-length key give the `key` and `plaintext` cipher.
    '''
    if len(key) == len(plaintext):
        return key
    for letter in range(len(plaintext) - len(key)):
        key = key + key[letter % len(key)]
    return key


def encrypt_letter(char, key):
    '''
    E = (P + K) mod 26
    '''
    p = alphabet_to_val[char]
    k = alphabet_to_val[key]
    e = (p + k) % 26
    char = alphabet_list[e]
    return char


def encrypt(plaintext, key):
    '''
    Use this function to vigenere encrypt.
    Pass a `plaintext` as the the message
    and the `key` to encrypt it.
    '''
    # Cipher starts empty.
    cipher = ''

    # Gets the *full key* (as in length).
    key = gen_full_key(plaintext, key)

    for letter_index in range(len(plaintext)):
        # Obtain just the letter of the given iteration.
        key_l = key[letter_index]
        plaintext_l = plaintext[letter_index]

        # Sends the letter of this `letter_index` to `encrypt_letter`.
        letter = encrypt_letter(plaintext_l, key_l)

        # Append to the new *encrypted* letter to the cipher.
        cipher = cipher + letter

    return cipher


if __name__ == "__main__":
    print("Hello, World!")
