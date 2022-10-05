import textwrap

class Rotor():
    def __init__(self, selected_type, rotor_position):
        with open('./cyphers/rotors.txt', 'r') as file:
            rotors = {}
            for line in file:
                type, rotor = line.split(": ")
                rotors[type] = rotor.rstrip()
        
        self.selected_type = selected_type
        self.standard_mapping = rotors[selected_type]
        self.updated_mapping = rotors[selected_type]
        self.rotor_position = rotor_position

        # notch positions are fixed: https://en.wikipedia.org/wiki/Enigma_rotor_details#Turnover_notch_positions
        notch_positions = {
            "I"  : "Q",  # If rotor steps from Q to R, the next rotor is advanced
            "II" : "E",  # If rotor steps from E to F, the next rotor is advanced
            "III": "V",  # If rotor steps from V to W, the next rotor is advanced
            "IV" : "J",  # If rotor steps from J to K, the next rotor is advanced
            "V"  : "Z"   # If rotor steps from Z to A, the next rotor is advanced
        }

        self.notch_position = notch_positions[selected_type]
        print(f"Seleted rotor     {selected_type}: {self.updated_mapping}. Notch position {self.notch_position}")

    def get_input_mapping_index(self, input_letter):
        return ord(input_letter.upper()) - ord("A")

    def rotate_and_update_mapping(self, shift):
        new_mapping = ""
        self.updated_mapping =  self.standard_mapping[shift:] + self.standard_mapping[:shift]
        for x in self.updated_mapping:
            if ord(x) - shift < ord("A"):
                new_mapping += chr(ord(x) - shift + 26)
            else:
                new_mapping += chr(ord(x) - shift)
        self.updated_mapping = new_mapping

    def encrypt_forward(self, letter):
        """
        Encrypt a letter in the forward mannar (3rd rotor --> 1st)
        Runs before the reflector
        """
        letter = letter.upper()
        index = self.get_input_mapping_index(letter)
        mapped_to = self.updated_mapping[index]
        print(f"Rotor{self.selected_type:>5}: input {letter} - output {mapped_to}; mapping {self.updated_mapping}")
        return mapped_to

    def encrypt_backward(self, letter):
        """
        Encrypt a letter in the backward mannar (1rd rotor --> 3st)
        Runs after the reflector
        """
        letter = letter.upper()
        index = self.updated_mapping.index(letter.upper())
        mapped_to = chr(index + ord("A"))
        print(f"Rotor{self.selected_type:>5}: input {letter} - output {mapped_to}; mapping {self.updated_mapping}")
        return mapped_to


class Rotors():
    def __init__(self, order, rotor_positions):
        self.rotors = {}
        self.order = order
        for i, o in enumerate(order):
            self.rotors[i] = Rotor(o, rotor_positions[i])
        info = f"""
        Rotors           {1:>5} {2:>5} {3:>5}
        ---------------------------------------------------
        selected         {order[2]:>5} {order[1]:>5} {order[0]:>5}
        initial position {rotor_positions[2]:>5} {rotor_positions[1]:>5} {rotor_positions[0]:>5}
        """
        print(textwrap.dedent(info))

    def encrypt_forward(self, letter):
        for i in range(len(self.order)):
            letter = self.rotors[i].encrypt_forward(letter)
        return letter

    def encrypt_backward(self, letter):
        for i in range(len(self.order))[::-1]:
            letter = self.rotors[i].encrypt_backward(letter)
        return letter

    def rotate(self):
        print("Rotor rotating...")
        advance_next_flag = True
        
        for i, r in enumerate(self.order):
            print(f"Rotor{r:>5}: Advance: {advance_next_flag}")
            if advance_next_flag:
                shift = (self.rotors[i].get_input_mapping_index(self.rotors[i].rotor_position) + 1) % 26
                self.rotors[i].rotate_and_update_mapping(shift)
                print(f"-  rotated : {self.rotors[i].updated_mapping}, offset with next {shift}")

                if self.rotors[i].rotor_position != self.rotors[i].notch_position: # Advance the next rotor
                    advance_next_flag = False

                self.rotors[i].rotor_position = "A" if self.rotors[i].rotor_position == "Z" else chr(ord(self.rotors[i].rotor_position) + 1)
        
        # print(f"rotated_rotors: {advanced_rotor_position}")

