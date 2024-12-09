calls = 0

def count_calls():
    global calls
    calls += 1
def string_info(string):
    global calls
    calls += 1
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    global calls
    calls += 1
    string = string.lower()
    for i in  range(len(list_to_search)):
        list_to_search[i] = list_to_search[i].lower()
    if string in list_to_search:
        return (True)
    else:
        return (False)

print(string_info('Cats'))
print(string_info('World'))
print(string_info('Sky'))
print(is_contains('Newsagent', ['new', 'AgENt', 'newSAgent']))  # Urban ~ urBAN
print(is_contains('ability', ['inability', 'disability']))  # No matches
print(calls)
