class Reflector():
    """ A class of the reflector

    Attributes:
        mapping (dict): a dictionary of encode/decode mapping
        selected_type (str): selected reflector type defined in file.

    Methods:
        encrypt(letter: str): encrypt a letter
    """
    def __init__(self, selected_type):
        """Initialize the Reflector Class and set the mapping

        Args:
            selected_type (str):
                selected reflector type defined in file. Support "A", "B", "C"
        """
        with open('./cyphers/reflectors.txt', 'r') as file:
            reflectors = {}
            for line in file:
                type, rotor = line.split(": ")
                reflectors[type] = rotor.rstrip()
        
        self.selected_type = selected_type
        self.mapping = reflectors[selected_type]
        print(f"Seleted reflector {selected_type}: {self.mapping}")

    def encrypt(self, letter):
        """
        Encrypt a letter with reflector. Return encrypted letter.

        Args:
            letter (str): input letter to encrypt

        Returns:
            str: output encrypted letter
        """
        index = ord(letter.upper()) - ord("A")
        mapped_to = self.mapping[index]
        print(f"Reflector{self.selected_type}: input {letter} - output {mapped_to}; mapping {self.mapping}")
        return mapped_to
