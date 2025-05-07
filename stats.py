def word_count(file_contents):
    num_words = 0
    num_words = len(file_contents.split())

    return num_words

def count_char(file_contents):
    char_dict = {}
    word_list = file_contents.split()
    for word in word_list:
        word = word.lower()
        for letter in word:
            if letter in char_dict:
               char_dict[letter] += 1
            else:
               char_dict[letter] = 1 

    return char_dict

def sort_on(dict):
    return dict["num"]

def create_sorted_list(char_dict):
    sorted_char_list = []
    for char in char_dict:
        num = char_dict[char]
        sorted_char_list.append({
            "char": char,
            "num": num
        })

    sorted_char_list.sort(reverse=True, key=sort_on)
    #print(sorted_char_list)
    return sorted_char_list

def print_report(input_list):
    for item in input_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")