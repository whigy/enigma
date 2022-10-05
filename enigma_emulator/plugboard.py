class PlugBoard():
    def __init__(self, mapping = None):
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
        Encrypt a letter with plugboard
        """
        letter = letter.upper()
        if letter in self.mapping.keys():
            print(f"Plugboard map {letter} --> {self.mapping[letter]}")
            return self.mapping[letter]
        else:
            return letter
