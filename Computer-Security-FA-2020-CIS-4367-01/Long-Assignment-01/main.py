from character_frequency_analysis import CharacterFrequencyAnalyzer
from text import OnlineTextResource, LocalResource
import sys

if sys.version_info[0] < 3 and sys.version_info[1] < 6:
    print("Python version is not supported. Please use version 3.6 or higher.")
    exit()

if __name__ == "__main__":
    resource = LocalResource("example_literature/shakespeare.txt")
    freq_analysis = CharacterFrequencyAnalyzer(resource.text)
    freq_analysis.print_frequency()
    print(freq_analysis.length)
