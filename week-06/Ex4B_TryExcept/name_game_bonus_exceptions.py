def get_valid_name(name):
    # I use try/except and validation so blank names or one-letter names do not break the song logic.
    try:
        name = str(name).strip()
        if len(name) < 2:
            raise ValueError('Name must have at least two characters.')
        if not name.replace(' ', '').isalpha():
            raise TypeError('Name should only contain letters and spaces.')
        return name
    except ValueError as e:
        print(f"ValueError: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")
    return None


def trunc_name(name):
    name = name.strip().lower()
    vowels = 'aeiou'
    if name[0] in vowels:
        return name
    elif len(name) > 1 and name[1] not in vowels:
        return name[2:]
    else:
        return name[1:]


def name_game(name):
    valid_name = get_valid_name(name)
    if valid_name is None:
        raise SystemExit(0)
    clean_name = valid_name.title()
    t = trunc_name(valid_name)
    yield f"{clean_name}, {clean_name}, bo-b{t}"
    yield f"banana fana fo-f{t}"
    yield f"me my mo-m{t}"
    yield f"{clean_name}!"

for sample in ['Mohamed', 'A', '', 'John3']:
    try:
        for line in name_game(sample):
            print(line)
    except SystemExit:
        print('Stopping this invalid example and moving to the next one.')
    print()

# raise SystemExit(0) means stop the program with exit code 0, which usually means no error.
# It can be used instead of break when I want to end the whole script, not just one loop.
# It may produce unexpected results in notebooks because it can stop the running cell/kernel behavior.
