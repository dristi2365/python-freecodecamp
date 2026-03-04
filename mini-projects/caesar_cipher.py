# Caesar Cipher - FreeCodeCamp Mini Project

def caesar(text, shift, encrypt=True):
    # Validate shift type
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    # Ensure shift is within valid Caesar Cipher range
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # If decrypting, reverse the shift
    if not encrypt:
        shift = -shift

    # Create shifted alphabet
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    # Create translation table including uppercase letters
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    # Translate the text
    encrypted_text = text.translate(translation_table)

    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


# Encryption Example
encrypt_text = encrypt('freeCodeCamp', 3)
print(encrypt_text)

# Decryption Example
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)