caesar_map = {
    ' ': ' ',
    'A': 'X',
    'B': 'Y',
    'C': 'Z',
    'D': 'A',
    'E': 'B',
    'F': 'C',
    'G': 'D',
    'H': 'E',
    'I': 'F',
    'J': 'G',
    'K': 'H',
    'L': 'I',
    'M': 'J',
    'N': 'K',
    'O': 'L',
    'P': 'M',
    'Q': 'N',
    'R': 'O',
    'S': 'P',
    'T': 'Q',
    'U': 'R',
    'V': 'S',
    'W': 'T',
    'X': 'U',
    'Y': 'V',
    'Z': 'W'
}

test = 'DORIAN STRUCK THE NORTHERN BAHAMAS AS A CATEGORY FIVE HURRICANE'

if __name__ == "__main__":
    cipher = ''
    for letter in test:
        mapped_letter = caesar_map[letter]
        cipher += mapped_letter
    print(cipher)
