from plugboard import PlugBoard
from rotors import Rotors
from reflector import Reflector


def encrypt(
    string_to_encrypt,
    plugboard_settings,
    reflector_type,
    rotor_order,
    rotor_initial_positions,
    rotot_ring_positions
):
    plugboard = PlugBoard(plugboard_settings)
    reflector = Reflector(reflector_type)
    rotors = Rotors(rotor_order, rotor_initial_positions, rotot_ring_positions)

    print("===================== start =====================")
    string_encrypted = ""
    for l in string_to_encrypt:
        print("----------------------------------------------------")

        # going through plugboard
        l = plugboard.encrypt(l)
        rotors.rotate()
        print("                                        ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        # going through 3 rotors
        l = rotors.encrypt_forward(l)
        # reflector
        l = reflector.encrypt(l)
        # going back through 3 rotors
        l = rotors.encrypt_backward(l)
        # going through plugboard
        l = plugboard.encrypt(l)

        string_encrypted += l

    return string_encrypted


if __name__ == '__main__':
    initial_positions = ["A", "A", "A"]
    order = ["III", "II", "I"] # lower to upper
    ring_positions = ["B", "Z", "A"]
    plugs = "QA ED FG BO LP CS RT UJ HN ZW"

    string_to_encrypt = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
    string_encrypted = encrypt(
        string_to_encrypt,
        plugboard_settings=plugs,
        reflector_type="B",
        rotor_order=order,
        rotor_initial_positions=initial_positions,
        rotot_ring_positions=ring_positions
    )
    print(string_encrypted)
