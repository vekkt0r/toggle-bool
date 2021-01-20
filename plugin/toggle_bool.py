values = {
    'true': 'false',
    'on': 'off',
    'yes': 'no',
    '1': '0',
    'enable': 'disable',
    'enabled': 'disabled',
    'before': 'after',
    'first': 'last',
}


def format_value(word, toggleWord):
    if word.isupper():
        toggleWord = toggleWord.upper()
    elif word.istitle():
        toggleWord = toggleWord.title()
    return toggleWord


def get_word(word, key):
    idx = word.lower().find(key)
    return word[idx:idx+len(key)]


def toggle_bool_value(full_word):
    toggleWord = word = full_word
    for key in values.keys():
        if key in full_word.lower():
            word = get_word(full_word, key)
            toggleWord = values[key]
            toggleWord = format_value(word, toggleWord)
            break
        elif values[key] in full_word.lower():
            word = get_word(full_word, values[key])
            toggleWord = key
            toggleWord = format_value(word, toggleWord)
            break
    return full_word.replace(word, toggleWord)
