import re


def popular_things(text):
    splitter_words = text.lower().split()
    words = set(splitter_words)
    letters = re.sub(' ', '', text)

    words_count = {word: splitter_words.count(word) for word in words}
    popular_word = max(words_count, key=words_count.get)

    alphabet = set(letters)
    letters_count = {letter: letters.count(letter) for letter in alphabet}
    popular_letter = max(letters_count, key=letters_count.get)

    average_numbers = [str(key) + ': ' + str(value) for key, value in letters_count.items()]

    return 'the most popular word is: {0} \nthe most popular letter is: {1} \naverage numbers of occurrences: {d}'.format(
        popular_word, popular_letter, d=' '.join(average_numbers))


print(popular_things('python python C Ruby Kotlin Kotlin python'))
