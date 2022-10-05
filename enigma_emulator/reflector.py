class Reflector():
    def __init__(self, selected_type):
        with open('./cyphers/reflectors.txt', 'r') as file:
            reflectors = {}
            for line in file:
                type, rotor = line.split(": ")
                reflectors[type] = rotor.rstrip()
        
        self.selected_type = selected_type
        self.mapping = reflectors[selected_type]
        print(f"Seleted reflector {selected_type}: {self.mapping}")

    def get_input_mapping_index(self, input_letter):
        return ord(input_letter.upper()) - ord("A")

    def encrypt(self, letter):
        """
        Encrypt a letter with the reflector
        """
        index = self.get_input_mapping_index(letter)
        mapped_to = self.mapping[index]
        print(f"Reflector{self.selected_type}: input {letter} - output {mapped_to}; mapping {self.mapping}")
        return mapped_to
