def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    letter_count = 0

    for char in word:
        if char.lower() == letter.lower():
            letter_count += 1
    return letter_count


single_letter_count('awesome', 'e')

# Rithm Solution:

# def single_letter_count(word, letter):

#   return word.lower().count(letter.lower())
