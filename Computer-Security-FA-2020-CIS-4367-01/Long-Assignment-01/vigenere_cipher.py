import sys


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
    # TODO: use all characters
    p = ord(char)
    k = ord(key)
    e = (p + k) % 26

    # TODO: Test evaluations
    while e < 65:
        e = e + 26
    while e > 122:
        e = e - 26
    enc_char = chr(e)
    return enc_char


def decrypt_letter(char, key):
    '''
    P = (E - K + 26) mod 26
    '''
    e = ord(char)
    k = ord(key)
    p = (e - k + 26) % 26

    while p < 65:
        p = p + 26
    while p > 122:
        p = p + 26
    return chr(p)


def encrypt(plaintext, key):
    '''
    Use this function to vigenere encrypt.
    Pass a `plaintext` as the the message
    and the `key` to encrypt it.
    '''
    # Cipher starts empty.
    cipher_str = ''

    # Gets the *full key* (as in length).
    key = gen_full_key(plaintext, key)
    plaintext = plaintext.upper()
    for char_index in range(len(plaintext)):
        # Obtain just the letter of the given iteration.
        key_char = key[char_index]
        plaintext_char = plaintext[char_index]

        # Sends the letter of this `letter_index` to `encrypt_letter`.
        cipher_char = encrypt_letter(plaintext_char, key_char)

        # Append to the new *encrypted* letter to the cipher.
        cipher_str = cipher_str + cipher_char

    return cipher_str


def decrypt(ciphertext, key):
    plaintext_str = ''

    key = gen_full_key(ciphertext, key)
    ciphertext = ciphertext.upper()

    for char_index in range(len(ciphertext)):
        # get the current values at the current index
        key_char = key[char_index]
        ciphertext_char = ciphertext[char_index]

        # decrypt the current index key
        plaintext_char = decrypt_letter(ciphertext_char, key_char)

        # append the decrypt character to the string
        plaintext_str = plaintext_str + plaintext_char

    return plaintext_str


if __name__ == "__main__":
    plaintext = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    key = 'HELP'
    print('PLAINTEXT: {}\n'.format(plaintext))
    ciphertext = encrypt(plaintext, key)
    print('CIPHERTEXT: {}\n'.format(ciphertext))
    decrypted_plaintext = decrypt(ciphertext, key)
    print('DECRYPTED: {}\n'.format(decrypted_plaintext))
