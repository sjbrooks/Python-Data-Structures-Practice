def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    return (len([elem for elem in lst if isinstance(elem, list)]) == len(lst))

    # Alternate possibilities: use all() with a generator comprehension,
    # though that isn't something we've covered yet:
    #
    # return all(isinstance(item, list) for item in lst)

    # OR the OG solution:
    # for item in lst:
    #     if not isinstance(item, list):
    #         return False

    # return True
