import random 


words = ['big', 'red', 'funny', 'baby', 'yellow', 'wait', 'python', 'Joseph']
def main():
    numbers = [16.2, 75.1, 52.3]
    words_list = []
    print(numbers)
    append_random_numbers(numbers)
    print(numbers)
    append_random_numbers(numbers, 3)

    append_random_words(words_list)
    print(words_list)
    append_random_words(words_list, 3)
    print(words_list)

    

def append_random_words(w_list, quantity=1):
    for _ in range(quantity):
        w_list.append(random.choice(words))


def append_random_numbers(num_list, quantity=1):
    for _ in range(quantity):
        num = random.uniform(0, 100)
        num = round(num, 1)
        num_list.append(num)


if __name__ == "__main__":
    main()