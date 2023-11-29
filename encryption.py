from typing import Type


def create_decryption_dictionary(encrypted_dict: dict[str, str]):
    decrypted_dictionary = {}
    for k, v in encrypted_dict.items():
        decrypted_dictionary[v] = k
    return decrypted_dictionary


def create_encryption_dictionary(counted_dict: dict[str, int]):
    offset = 0
    # A random way I thought up of to make a dynamic "encryption algorithm"
    # It's basically just the ROT cipher
    for v in counted_dict.values():
        if v % 2 == 0:
            offset -= v
        else:
            offset += v

    offset_list: list[tuple[str, int]] = list(counted_dict.items())
    encryption_dict: dict[str, str] = {}
    iteration = 0
    for k in counted_dict.keys():
        new_value = offset_list[(offset + iteration) % len(offset_list)][0]
        encryption_dict[k] = new_value
        iteration += 1
    return encryption_dict


def encrypt_str(input_str: str, encryption_dict: dict[str, str]):
    result: str = ""
    for char in input_str:
        result += encryption_dict[char]
    return result


def decrypt_str(input_str: str, decryption_dict: dict[str, str]):
    result: str = ""
    for char in input_str:
        result += decryption_dict[char]
    return result


def encryption(readfile, enfile, counted_dictionary):
    f = open(readfile, 'r')
    raw_str = f.read()
    f.close()
    encryption_dict = create_encryption_dictionary(counted_dictionary)
    encrypted_str = encrypt_str(raw_str, encryption_dict)
    f = open(enfile, 'w')
    f.write(encrypted_str)
    f.close()

    return encryption_dict


def count_chars(readfile: str):
    f = open(readfile, 'r')
    lines = f.read()
    f.close()
    """
        Counts all chars in a line, this is where the file should be fed to first
    """
    dictionary = {}
    for char in lines:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def decryption(readfile, enfile, defile, counted_dictionary):
    encryption_dict = encryption(readfile, enfile, counted_dictionary)
    decryption_dict = create_decryption_dictionary(encryption_dict)
    f = open(enfile, 'r')
    raw_str = f.read()
    f.close()
    decrypted_str = decrypt_str(raw_str, decryption_dict)
    f = open(defile, 'w')
    f.write(decrypted_str)
    f.close()
