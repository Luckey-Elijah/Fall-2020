from text_request import OnlineTextResource
import re


def __check_unicode(char) -> (bool, chr):
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


def count_letter_frequency(string, desc=True, include_spaces=False, alphanum_only=True) -> dict:
    '''
    Counts the occurrences of each character in the string.
    Returns the result as an unsorted map.
    '''
    letter_map = {}
    for character in string:
        is_char_alpha, character = __check_unicode(character)
        if is_char_alpha:
            if character in letter_map:
                # increment the count by one
                letter_map[character] += 1
            else:
                # adds the new character to the map
                letter_map[character] = 1

    # Sorts the dictionary
    letter_map = {
        letter: count
        for letter, count in sorted(
            letter_map.items(),
            key=lambda letter_m: letter_m[1],
            reverse=desc
        )
    }
    return letter_map


class CharacterFrequencyAnalyzer():
    def __init__(self, source_string, include_spaces=False, alphanum_only=True):

        self.text = re.sub(r'\W+', '', source_string)
        self.length = len(self.text)
        self.map = count_letter_frequency(self.text)

    def print_frequency(self):
        """
        Prints a table in this style: \n
        ```txt
        +--------+-----------+--------+
        | letter | frequency | counts |
        +--------+-----------+--------+
        |      E |   8.36    | 481973 |
        |      T |   6.14    | 354387 |
        |      O |   5.77    | 333041 |
        |      A |   5.38    | 310094 |
        |   ect. |   X.XX    | ...... |
        |   .... |   ....    | ...... |
        ```
        """

        str_format = "| {0:>6} | {1:>6} | {2:^9.2f} |"
        h_line = "+--------+--------+-----------+"
        print(h_line)
        print("| LETTER | COUNTS | FREQUENCY |")
        print(h_line)

        # prints the list
        for letter in self.map:

            # letter count
            count = self.map[letter]

            # this index freq
            freq = round(count / self.length * 100, 2)
            print(str_format.format(letter, count, freq))

        print(h_line)


if __name__ == "__main__":
    online_resource = OnlineTextResource(
        "https://www.astrolog.org/labyrnth/novel.txt")

    if online_resource.status_code == 200:
        freq_analysis = CharacterFrequencyAnalyzer(online_resource.text)
        freq_analysis.print_frequency()
        print(freq_analysis.length)
    else:
        print("Server response is not good.")
        print("Status Code: {0}".format(online_resource.status_code))
