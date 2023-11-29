from bargraph import bargraph
from encryption import encryption, decryption, count_chars


def main():
    visual = "visual.txt"
    readfile = "normal.txt"
    enfile = "Encrypted.txt"
    defile = "Decrypted.txt"
    bargraph(readfile, visual)

    counted_dictionary = count_chars(readfile)
    encryption(readfile, enfile, counted_dictionary)
    decryption(readfile, enfile, defile, counted_dictionary)


main()
