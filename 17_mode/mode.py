def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # import frequency counter (or make one here)

    from collections import Counter

    # invoke frequency counter with nums as argument

    num_frequency_count = Counter(nums)

    # find the key with the largest value 
    # (https://kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python)

    mode = max(num_frequency_count, key=num_frequency_count.get)
    return mode