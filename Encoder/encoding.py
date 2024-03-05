"""

"""
__all__ = ['encode']

DEFAULT_KEYWORD = "Депрессия"
ALPHABET = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3,
            'Д': 4, 'Е': 5, 'Ё': 6, 'Ж': 7,
            'З': 8, 'И': 9, 'Й': 10, 'К': 11,
            'Л': 12, 'М': 13, 'Н': 14, 'О': 15,
            'П': 16, 'Р': 17, 'С': 18, 'Т': 19,
            'У': 20, 'Ф': 21, 'Х': 22, 'Ц': 23,
            'Ч': 24, 'Ш': 25, 'Щ': 26, 'Ъ': 27,
            'Ы': 28, 'Ь': 29, 'Э': 30, 'Ю': 31,
            'Я': 32,
            'а': 33, 'б': 34, 'в': 35, 'г': 36,
            'д': 37, 'е': 38, 'ё': 39, 'ж': 40,
            'з': 41, 'и': 42, 'й': 43, 'к': 44,
            'л': 45, 'м': 46, 'н': 47, 'о': 48,
            'п': 49, 'р': 50, 'с': 51, 'т': 52,
            'у': 53, 'ф': 54, 'х': 55, 'ц': 56,
            'ч': 57, 'ш': 58, 'щ': 59, 'ъ': 60,
            'ы': 61, 'ь': 62, 'э': 63, 'ю': 64,
            'я': 65,
            '.': 66, ',': 67, '!': 68, '?': 69, ' ': 70, '-': 71}


def encode(message: str, keyword: str = DEFAULT_KEYWORD, alphabet: dict[str, int] = ALPHABET) -> str:
    rev_alphabet = {v: k for k, v in alphabet.items()}
    cont_symbols = len(alphabet)
    result = ""
    counter = 0
    for sym in message:
        if sym == '\n':
            result += sym
            continue
        key_sym = keyword[counter]

        diff = alphabet[sym] - alphabet[key_sym]
        diff = (diff + cont_symbols) % cont_symbols
        result += rev_alphabet[diff]

        counter = (counter + 1) % len(keyword)

    return result
