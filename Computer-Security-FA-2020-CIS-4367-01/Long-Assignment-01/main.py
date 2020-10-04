from character_frequency_analysis import CharacterFrequencyAnalyzer
from text_request import OnlineTextResource
import sys

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

    if sys.argv[1] == "file":
        # TODO: file runner
        pass
    else:
        # TODO: string runner
        # use the argument as the string itself
        pass
