VOWELS = set("aeiou")


def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # freq_count = {}
    # vowels = 'aeiou'

    # phrase = phrase.lower()

    # for letter in phrase:
    #     if letter in vowels:
    #         exists = freq_count.get(letter, 0)
    #         if exists == 0:
    #             freq_count[letter] = 0
    #     freq_count[letter] += 1
    
    # return freq_count

    phrase = phrase.lower()
    counter = {}

    for ltr in phrase:
        if ltr in VOWELS:
            counter[ltr] = counter.get(ltr, 0) + 1

    return counter

