
LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]
    

def word_in_file(word, filename, case_sensitive=False):
    with open(filename, 'r') as file:
        for line in file:
            if case_sensitive:
                if word == line.strip():
                    return True
            else:
                if word.lower() == line.strip().lower():
                    return True 
    return False


def word_has_character(word, character_list):
    for i in range(0, len(word)):
        if word[i] in character_list:
            return True
    return False


def word_complexity(word):
    complexity = 0
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
   

    if word_in_file(password, 'wordlist.txt'):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    if word_in_file(password, 'toppasswords.txt', True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1

        
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password")
        return 5
    
    return word_complexity(password) + 1


def main():
    password = input("Enter a password or q|Q to quit:  ")
    while password[0].lower() != 'q':
        strength = password_strength(password)
        print("Password Strength: {0}".format(strength))
        password = input("Enter a password or q|Q to quit:  ")

        
if __name__ == "__main__":
    main()