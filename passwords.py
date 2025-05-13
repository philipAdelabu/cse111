#


def word_in_file(word, filename, case_sensitive=False):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if case_sensitive:
                if word == line:
                    return True
            else:
                if word.lower() == line.lower():
                    return True 
    return False


def word_has_character(word, character_list):
    for ch in range(0, len(word)):
        if ch in character_list:
            return True
    return False


def word_complexity(word):
    complexity = 0
    LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    DIGITS=["0","1","2","3","4","5","6","7","8","9"]
    SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity


def password_strength(password, min_length=10, strong_length=16):
    complexity = word_complexity(password)

    if len(password) == len(min_length):
        

    if len(password) >= len(strong_length):
        print("Password is long, length trumps complexity this is a good password")
        return 1
    return 0