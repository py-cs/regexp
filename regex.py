def one_char_match(reg_exp, input_str, esc):
    return not reg_exp or (reg_exp == '.' and not esc) or reg_exp == input_str


def same_len_match(reg_exp, input_str):
    esc = False
    if not reg_exp:
        return True
    if reg_exp.startswith('\\'):
        esc = True
        reg_exp = reg_exp[1:]
    if not esc and reg_exp == '$':
        return not input_str
    if not esc and reg_exp.startswith('?'):
        reg_exp = reg_exp[1:]
    if one_char_match(reg_exp[0] if reg_exp else '',
                      input_str[0] if input_str else '', esc):
        if len(reg_exp) > 1 and reg_exp[1] in '*+':
            input_str = input_str.lstrip(input_str[0])
            return same_len_match(reg_exp[2:], input_str)
        return same_len_match(reg_exp[1:], input_str[1:])
    else:
        if len(reg_exp) > 1 and reg_exp[1] in '?*':
            return same_len_match(reg_exp[2:], input_str[0:])
    return False


def variable_len_match(reg_exp, input_str):
    i = 0
    if reg_exp and reg_exp[0] == '^':
        return same_len_match(reg_exp[1:], input_str)
    while len(input_str) >= i:
        if same_len_match(reg_exp, input_str[i:]):
            return True
        i += 1
    return False


reg_exp, input_str = input().split('|')
print(variable_len_match(reg_exp, input_str))
