from text_request import OnlineResource


def check_unicode(char):
    '''
    Checks is char is in range of [a-zA-Z] and returns uppercase [char, True].
    Otherwise it returns [None, False].
    '''
    unicode = ord(char)
    # [A-Z] codes
    if unicode >= 65 and unicode <= 90:
        return True, char
    # [a-z] codes
    if unicode >= 97 and unicode <= 122:
        return True, char.upper()
    return False, None


def count_letters(string):
    '''
    Counts the  occurrences of each character in the string.
    Returns the result as an unsorted map.
    '''
    freq_map = {}
    for character in string:
        is_char_alpha, character = check_unicode(character)
        if is_char_alpha:
            if character in freq_map:
                # increment the count by one
                freq_map[character] += 1
            else:
                # adds the new character to the map
                freq_map[character] = 1
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
        print('%c: %5.2f (%d), %s' %
              (letter, freq, letter_map[letter], ord(letter)))


if __name__ == "__main__":
    online_resource = OnlineResource(
        "https://www.gutenberg.org/files/100/100-0.txt")
    string = online_resource.text
    freq_map = count_letters(string)
    map_to_freq(freq_map, len(string))
