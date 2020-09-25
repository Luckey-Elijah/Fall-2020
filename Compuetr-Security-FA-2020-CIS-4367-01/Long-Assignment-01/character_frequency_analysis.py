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


def count_letters(string):
    '''
    Counts the occurrences of each character in the string.
    Returns the result as an unsorted map.
    '''
    freq_map = {}
    for letter in string:
        if letter in freq_map:
            # increment the count by one
            freq_map[letter] += 1
        else:
            freq_map[letter] = 1
    return freq_map


def map_to_freq(letter_map, string_length):
    '''
    Takes a letter map {(letter, count)} and
    '''
    # Orders the list
    letter_map = {k: v for k, v in sorted(
        letter_map.items(), key=lambda item: item[1], reverse=True)}

    # prints the list
    for letter in letter_map:
        # calculates the frequency
        freq = round(letter_map[letter] / string_length * 100, 2)
        print('%c: %5.2f (%d)' % (letter, freq, letter_map[letter]))


if __name__ == "__main__":
    string = test
    freq_map = count_letters(string)
    map_to_freq(freq_map, len(string))
