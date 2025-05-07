from stats import word_count, count_char, create_sorted_list, print_report
import sys

def get_book_text(path_to_file):
    #print(path_to_file)
    file_contents = ""
    
    with open(path_to_file) as f:
        file_contents = f.read()
    
    return file_contents

def main():
    #rel_path = "books/frankenstein.txt"

    try:
        rel_path = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        raise

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {rel_path}...")

    print("----------- Word Count ----------")
    num_words = (word_count(get_book_text(rel_path)))
    #print(f"{num_words} words found in the document")
    print(f"Found {num_words} total words")
    
    print("--------- Character Count -------")
    dict1 = count_char(get_book_text(rel_path))
    #print(dict1)
    
    sorted_list = create_sorted_list(dict1)
    print_report(sorted_list)

    print("============= END ===============")

main()
