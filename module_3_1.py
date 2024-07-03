calls = 0


def count_calls():
    global calls
    calls = 4


count_calls()


def string_info(string):
    i = (len(string), string.upper(), string.lower())
    return i


def is_contains(string, list_to_search):
    for e in list_to_search:
        if e.lower() in string.lower():
            return True
    return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
