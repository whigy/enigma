class PlugBoard():
    """ A class of plugboard

    Attributes:
        mapping (dict): a dictionary of encode/decode mapping

    Methods:
        encrypt(letter: str): encrypt a letter
    """
    def __init__(self, mapping = None):
        """Initialize the PlugBoard Class and set the mapping

        Args:
            mapping (str):
                A string of plugboard settings. 
                Each pair is a set of two letters; pairs seperated with " "
                e.g. "AB CD EF GH"
        """
        if mapping is not None:
            print(f"Plugboard set: {mapping}")
            mapping = mapping.split(" ")
            encode_map = {}
            for m in mapping:
                encode_map[m[0]] = m[1]
                encode_map[m[1]] = m[0]
            self.mapping = encode_map
        else:
            print(f"Plugboard not set.")
            self.mapping = {}
            

    def encrypt(self, letter):
        """
        Encrypt a letter with plugboard. Return encrypted letter if the letter is with plugboard setting.
        Otherwise return the letter itself

        Args:
            letter (str): input letter to encrypt

        Returns:
            str: output encrypted letter
        """
        letter = letter.upper()
        if letter in self.mapping.keys():
            print(f"Plugboard map {letter} --> {self.mapping[letter]}")
            return self.mapping[letter]
        else:
            return letter
