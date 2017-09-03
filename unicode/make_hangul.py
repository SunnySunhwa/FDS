def make_hangul_unicode(cho, jung, jong):
    unicode = 0xAC00 +((cho * 21) + jung) * 28 + jong
    return chr(unicode)

print(make_hangul_unicode(11, 2, 21), end = '')
print(make_hangul_unicode(16, 1, 0), end = '')
print(make_hangul_unicode(18, 9, 4))
