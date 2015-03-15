from functools import cmp_to_key


def is_pangram(sentence):
    letters = 'абвгдежзийклмнопрстуфхцчшщъьюя'
    for letter in letters:
        if not letter in sentence.lower():
            return False
    return True


def char_histogram(text):
    result = {}
    for symbol in text:
        result[str(symbol)] = text.count(symbol)
    return result


def sort_by(func, arguments):
    return sorted(arguments, key = cmp_to_key(func))


def group_by_type(dictionary):
    result = {}
    for key in dictionary:
        if not type(key) in result:
            result[type(key)] = {key: dictionary[key]}
        else:
            result[type(key)][key] = dictionary[key]
    return result


def is_anagram(word1, word2):
    return sorted(list(word1)) == sorted(list(word2))


def word_anagram(word, words_list):
    result = []
    for second_word in words_list:
        if is_anagram(word, second_word):
            result.append(second_word)
    return result


def anagrams(words):
    result = []
    for word in words:
        if not word_anagram(word, words) in result:
            result.append(word_anagram(word, words))
    return result
