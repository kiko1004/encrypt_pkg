import string


def rot13(message, idx=13):
    get_l = lambda letters, l: letters[(letters.index(l) + idx) % len(letters)]
    ls = string.ascii_lowercase
    uls = string.ascii_uppercase
    code = []
    for l in message:
        if l in ls:
            code.append(get_l(ls, l))
        elif l in uls:
            code.append(get_l(uls, l))
        else:
            code.append(l)

    return "".join(code)
