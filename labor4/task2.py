import re

def find_common_word_in_sentences(file_path):
    with open(file_path, encoding='utf-8') as file: text = file.read()

    sentences = re.split(r'[.!?]', text)
    words_lists = [re.findall(r'\b\w+\b', sentence) for sentence in sentences]

    print(words_lists)
    common_word = set(words_lists[0])
    for words in words_lists[1:-1]: 
        common_word = common_word.intersection(set(words))
        

    if common_word: return common_word
    return "Совпадающее слово не найдено в каждом предложении."

file_path = "text2.txt"
result = find_common_word_in_sentences(file_path)
print(result)