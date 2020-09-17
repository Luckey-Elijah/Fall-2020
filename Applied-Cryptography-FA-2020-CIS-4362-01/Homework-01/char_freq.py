char_map_template = {
    'A': 0,
    'B': 0,
    'C': 0,
    'D': 0,
    'E': 0,
    'F': 0,
    'G': 0,
    'H': 0,
    'I': 0,
    'J': 0,
    'K': 0,
    'L': 0,
    'M': 0,
    'N': 0,
    'O': 0,
    'P': 0,
    'Q': 0,
    'R': 0,
    'S': 0,
    'T': 0,
    'U': 0,
    'V': 0,
    'W': 0,
    'X': 0,
    'Y': 0,
    'Z': 0,
}

test = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZ" + \
    "VUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSX" + \
    "EPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"


if __name__ == "__main__":
    string = test
    freq_map = {}
    for letter in string:
        if letter in freq_map:
            # increment the count by one
            freq_map[letter] += 1
        else:
            freq_map[letter] = 1

    print('P: ', freq_map['P'])
    print('Z: ', freq_map['Z'])
    print('S: ', freq_map['S'])
    print('W: ', freq_map['W'])
    print(freq_map)
