def str_alt(str1=''):
    alt = str1.replace('{', '')
    alt = alt.replace('}', '')
    alt = alt.replace('"', '')
    alt = alt.replace(',', '')
    return alt
