def ordinal(num):
    """
    Take number and return the ordinal st, nd, th.
    :num: int
    :return: str
    """
    num_str = str(num)

    SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}
    # Check for 11-14 because those are abnormal
    if int(num_str[-2:]) > 10 and int(num_str[-2:]) < 14:
        return 'th'
    else:
        suffix = SUFFIXES.get(int(num_str[-1:]), 'th')
    return suffix
