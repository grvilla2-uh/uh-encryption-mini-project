def sorted_dict(dictionary):
    """
        Sorts the provided dictionary Highest to lowest, this is given
    """
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def num_symbols(value, sorted_dictionary):
    # This gets the largest value from the dict using an iterator
    largest_value = next(iter(sorted_dictionary.values()))
    scaling_factor = 25.9 / float(largest_value)
    number_of_symbols = scaling_factor * float(value)
    return int(number_of_symbols)


def print_graph(file_name, sorted_dictionary):
    result: str = ""
    for (k, v) in sorted_dictionary.items():
        count: int = num_symbols(v, sorted_dictionary)
        # Pythonic way to do it, but its easy, gives us the amount of symbols the bar will need
        symbols = "X" * count

        """
            This combines everything into one line, first is the actual character
            Next is the seperator, followed by the `count` amount of symbols, a seperator, the number of instances
            of said char and then finally a newline
        """
        # Handles that one special edge case with newlines
        if k == "#!":
            result += "{} | {} {}\n".format(k, symbols, str(v))
        else:
            result += "{}  | {} {}\n".format(k, symbols, str(v))

    file = open(file_name, 'w')
    file.write(result)
    file.close()


def count_chars(readfile: str):
    f = open(readfile, 'r')
    lines = f.read()
    f.close()
    """
        Counts all chars in a line, this is where the file should be fed to first
    """
    dictionary = {}
    for char in lines:
        # to conform to the specification in the document
        # This also helps with making the chart later
        if char == '\n':
            char = "#!"

        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def bargraph(readfile, visual):
    dictionary = count_chars(readfile)
    sorted_dictionary: dict[str, int] = sorted_dict(dictionary)
    print_graph(visual, sorted_dictionary)
