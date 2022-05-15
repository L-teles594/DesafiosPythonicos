def validation(a, b):
    if len(a) > 1 and len(b) > 1:
        return True
    else:
        return False

if validation(a, b):
    else:
    return "We coundn't mixed-up"

test(mix_up, ('x', 'y'), "We coundn't mixed-up")
    test(mix_up, ('xx', 'y'), "We coundn't mixed-up")
    test(mix_up, ('x', 'yy'), "We coundn't mixed-up")
    test(mix_up, ('xx', 'yy'), 'yy xx')