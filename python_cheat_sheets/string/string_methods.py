# To get more string methods, please visit this site: https://docs.python.org/3/library/stdtypes.html#string-methods
test_str = 'Hollo World'

test_str.lower()

test_str.upper()

test_str.title()

test_str.casefold()
# Return a casefolded copy of the string. Casefolded strings may be used for caseless matching.
# Casefolding is similar to lowercasing but more aggressive because it is intended to remove all case distinctions in a string. 
# For example, the German lowercase letter 'ß' is equivalent to "ss". 
# Since it is already lowercase, lower() would do nothing to 'ß'; casefold() converts it to "ss".

test_str.lstrip()
# Return a copy of the string with leading characters removed
test_str.rstrip()
# Return a copy of the string with trailing characters removed.
test_str.strip()
# Return a copy of the string with the leading and trailing characters removed.

test_str.split(',')

data =('ab', 'cd', 'ef')
'--'.join(data)
# This will return ab--cd--ef

'x' in 'xyz'
# Finding substring

test_str.startswith('He')
test_str.endswith('ld')

test_str.index('world') # return error if not found
test_str.find('world') # return -1 if not found