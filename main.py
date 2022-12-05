def translit():
    eng_rus = {
        "q": "й",
        "w": "ц",
        "e": "у",
        "r": "к",
        "t": "е",
        "y": "н",
        "u": "г",
        "i": "ш",
        "o": "щ",
        "p": "з",
        "a": "ф",
        "s": "ы",
        "d": "в",
        "f": "а",
        "g": "п",
        "h": "р",
        "j": "о",
        "k": "л",
        "l": "д",
        "z": "я",
        "x": "ч",
        "c": "с",
        "v": "м",
        "b": "и",
        "n": "т",
        "m": "ь",
        "[": "х",
        "]": "ъ",
        "{": "х",
        "}": "ъ",
        ";": "ж",
        "'": "э",
        ":": "ж",
        "\"": "э",
        ",": "б",
        ".": "ю",
        "<": "б",
        ">": "ю",
    }

    with open(file='eng.txt') as f:
        for text in f:
            for key in eng_rus:
                text = text.replace(key, eng_rus[key])
            return text


print(translit())
