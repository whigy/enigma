# Enigma workshop


## `enigma_emulator`
An Enigma emulator that encode/decode text message according to initial settings. The initial settings include:
- Pl

## `ciphers/`

Contains cyphers for all rotors and reflectors

## `data/`

Contains test data in the following format:

```
# I:1 II:1 III:1 - QA ED FG BO LP CS RT UJ HN ZW
THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG
VAUFLPVWMQIVFWNPCGPGVPIMKUWZREEDTTQ
I:1 II:2 III:10
```

Where the first line contains the rotors, their starting position and the plugboard settings (if any). The second line is the input text. The third line is the encrypted text. The last line is the rotors and their position after the message was entered.
