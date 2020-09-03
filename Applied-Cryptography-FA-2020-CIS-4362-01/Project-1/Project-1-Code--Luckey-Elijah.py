import sys

alphabet_to_val = {'a':  0, 'b':  1, 'c':  2, 'd':  3, 'e':  4, 'f':  5, 'g':  6, 'h':  7, 'i':  8, 'j':  9, 'k': 10, 'l': 11,
                   'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}
alphabet_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
test_cases = [
    'AHEALTHYATTITUDEISCONTAGIOUSBUTDONTWAITTOCATCHITFROMOTHERS',
    'IFYOUCARRYYOURCHILDHOODWITHYOUYOUNEVERBECOMEOLDER',
    'FROMPRINCIPLESISDERIVEDPROBABILITYBUTTRUTHORCERTAINTYISOBTAINEDONLYFROMFACTS',
]


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


def test():
    # Driver code
    for test in test_cases:
        message = test.lower()
        cipher = encrypt(message, 'elijah')
        print(message.upper() + ": " + cipher.upper())


def print_how_to_use():
    print('Run the test cases:')
    print('\t' + sys.argv[0] + ' test')
    print('\nUse your own message (default key is \'luckey\'):')
    print('\t' + sys.argv[0] + ' message')
    print('\nUse your own message and key:')
    print('\t' + sys.argv[0] + ' message key')
    print('\nPrint this message:')
    print('\t' + sys.argv[0])


if __name__ == "__main__":
    num_arg = len(sys.argv) - 1

    if (num_arg == 0):
        # no arguments given, user needs help
        print_how_to_use()

    elif(num_arg == 1 and sys.argv[1] == 'test'):
        # User wants test cases
        test()

    elif(num_arg == 1):
        # User is passing in only a message, using default key
        cipher = encrypt(sys.argv[1], 'luckey')
        print(cipher)

    elif(num_arg == 2):
        # User is passing in their own message and key
        cipher = encrypt(sys.argv[1], sys.argv[2])
        print(cipher)

    else:
        print_how_to_use()
