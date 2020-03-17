def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

# Originally, I converted the string into an array so I could use .reverse(),
# removed the blank spaces using a list comprehension,
# and then created a copy of that list that would get reversed
# # Finally, compared the lists to check if the phrase was the same reversed

#     phrase_list = list(phrase.lower())
#     phrase_list = [letter for letter in phrase_list if letter != ' ']

#     phrase_list_reversed = phrase_list.copy()
#     phrase_list_reversed.reverse()

#     if phrase_list == phrase_list_reversed:
#         return True
#     return False


# Answer includes slice, which I forgot you could use on strings
# in addition to lists
    normalized = phrase.lower().replace(' ', '')
    return normalized == normalized[::-1]
