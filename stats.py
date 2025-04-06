def get_word_count(book_text):
    return len(book_text.split())

def get_number_of_letters(book_text):
    book_text = book_text.lower()
    lettersDict = {}
    for letter in book_text:
        if letter in lettersDict:
            lettersDict[letter] += 1
        else:
            lettersDict[letter] = 1
    return lettersDict

def myFunc(e):
    return e['count'] 

def dict_to_dictList(item):
    dictList = []

    for char, count in item.items():
        dictList.append({"char": char, "count": count})
    
    return dictList

def sort_item(item):
    newList = dict_to_dictList(item)
    newList.sort(key=myFunc, reverse=True)
    return newList