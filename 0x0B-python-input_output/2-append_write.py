#!/usr/bin/python3
""" Module that contains a function that appends to the end of a text file """


def append_write(filename="", text=""):
    """ Function that appends to the end of a text file
    and returns the number of characters appended
    Args:
        filename: filename
        text: text to append
    Raises
        Exception: when the file can be opened
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
