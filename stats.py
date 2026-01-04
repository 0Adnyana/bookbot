def get_num_words(text: str) -> int:
    words = text.split()
    word_count = len(words)
    return word_count

def get_char_count_dict(text: str) -> dict:
    text = text.lower()
    charDict = dict[str, int]()
    for char in text:
        if (char in charDict):
            charDict[char] += 1
        else:
            charDict[char] = 1

    return charDict

def get_char_list(char_dict: dict) -> list:
    char_list = []
    for key in char_dict:
        item = {
            "char": key,
            "num": char_dict[key]
        }
        char_list.append(item)
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def get_alpha_char_list(char_dict: list) -> list:
    char_list = []
    for key in char_dict:
        if key.isalpha():
            item = {
                "char": key,
                "num": char_dict[key]
            }
            char_list.append(item)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(items):
    return items["num"]