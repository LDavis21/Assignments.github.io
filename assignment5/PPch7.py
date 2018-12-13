'hello'.upper()
'Happy Birthday!'.lower()
'WeeeEEEeeeEEEeee'.swapcase()
'ABC123'.isupper()
'aeiouAEIOU'.count('a')
'hello'.endswith('o')
'hello'.startswith('H')
'Hello {0}'.format('Python')
'Hello {0}! Hello {1}!'.format('Python', 'World')

print('tomato'.count('o'))
print('tomato'.find('o'))
print('tomato'.find('o', 'tomato'.find('o') +1))
print('avocado'.find('o', 'avocado'.find('o') + 1))
print('runner'.replace('n', 'b'))
print('strip')


print('I love {0}!'.format('season'))
'The sides have lengths {0}, {1}, and {2}'.format('side1', 'side2', 'side3')


def total_occurrences(s1, s2, ch):
    """(ster, ster, ster) ->  int

    Precondition: len(ch) == 1
    
    Return the toal number of times that ch occurs is s1 and s2.

    total_occurrences('color', 'yellow', 'l')
    3
    total_occurrences('red', 'blue', 'l')
    1
    total_occurrences('green', 'purple', 'b')
    0
    """
    return s1.count(ch) + s2.count(ch)

