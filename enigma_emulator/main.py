from plugboard import PlugBoard
from rotors import Rotors
from reflector import Reflector


def encrypt(
    input_letter,
    plugboard,
    reflector,
    rotors
):
    l = input_letter

    # going through plugboard
    # l = plugboard.encrypt(l)
    rotors.rotate()
    print("                                        ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    # going through 3 rotors
    l = rotors.encrypt_forward(l)
    # reflector
    l = reflector.encrypt(l)
    # going back through 3 rotors
    l = rotors.encrypt_backward(l)
    # going through plugboard
    # l = plugboard.encrypt(l)

    return l

# def main():


if __name__ == '__main__':
    initial_positions = ["A", "A", "A"]
    order = ["III", "II", "I"] # lower to upper
    ring_positions = ["A", "A", "A"]
    plugs = "QA ED FG BO LP CS RT UJ HN ZW"

    string_to_encrypt = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    # string_to_encrypt = "THE"
    string_encrypted = ""

    plugboard = PlugBoard(plugs)
    reflector = Reflector("B")
    rotors = Rotors(order, initial_positions)

    print("===================== start =====================")
    for l in string_to_encrypt:
        print("----------------------------------------------------")
        l = plugboard.encrypt(l)
        l = encrypt(
            l, plugboard, reflector, rotors)
        l = plugboard.encrypt(l)
        string_encrypted += l

    print(string_encrypted)