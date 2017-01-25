
def longest_alphabetic_substring(s):
    """
    A program that prints the longest substring of s in which the letters occur in alphabetical order,
    where s is a string of lower case characters.
    :param s: String
    :return: String

    >>> s = 'abcd'
    >>> longest_alphabetic_substring(s)
    'abcd'
    >>> s = 'mspljehgdtrrxyropmrr'
    >>> longest_alphabetic_substring(s)
    'rrxy'

    """
    string = s
    index = 0
    lst = []
    while len(string) >= 2 and index < (len(string)-1):

        if string[index] <= string[index + 1]:
            index += 1
            if index == len(string)-1:
                lst.append(string)
        elif string[index] >= string[index + 1]:
            lst.append(string[:index + 1])
            string = string[index + 1 :]
            index = 0

    longest = ''
    for item in lst:
        if len(item) > len (longest):
            longest = item
    return(longest)



s = 'abcd'
longest_alphabetic_substring(s)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    s = 'abcd'
    longest_alphabetic_substring(s)

