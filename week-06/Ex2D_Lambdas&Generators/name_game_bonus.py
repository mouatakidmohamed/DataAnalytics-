def trunc_name(name):
    # I make the name lowercase so the logic works even if the user uses capitals.
    name = name.strip().lower()
    vowels = 'aeiou'
    if len(name) == 0:
        return ''
    if name[0] in vowels:
        return name
    elif len(name) > 1 and name[1] not in vowels:
        return name[2:]
    else:
        return name[1:]


def name_game(name):
    # This is a generator because it yields one song line at a time.
    clean_name = name.strip().title()
    t = trunc_name(name)
    yield f"{clean_name}, {clean_name}, bo-b{t}"
    yield f"banana fana fo-f{t}"
    yield f"me my mo-m{t}"
    yield f"{clean_name}!"

for sample_name in ['Mohamed', 'carly', 'CHARLIE', 'Aidan', 'Braden', 'Billy Bob']:
    for line in name_game(sample_name):
        print(line)
    print()

# Observation: names with spaces still work, but a real song version may need more rules.
