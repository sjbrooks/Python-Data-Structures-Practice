def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # Originally, I didn't realize there was a swapcase function and attempted
    # to swap letters manually using replace, but forgot that once I changed
    # the lowercase to uppercase I wouldn't have been able to find
    # the uppercase and vice versa:

    # if to_swap.isupper():
    #     phrase = phrase.replace(to_swap, to_swap.lower())
    #     phrase = phrase.replace(to_swap.lower(), to_swap)
    # else:
    #     phrase = phrase.replace(to_swap, to_swap.upper())
    #     phrase = phrase.replace(to_swap.upper(), to_swap)
    # return phrase

    to_swap = to_swap.lower()
    swapped_caps_phrase = ""

    for ltr in phrase:
        if ltr.lower() == to_swap:
            ltr = ltr.swapcase()
        swapped_caps_phrase += ltr
        # good to keep in mind that you can build a string letter by letter

    return swapped_caps_phrase
