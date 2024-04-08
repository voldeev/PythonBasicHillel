def popular_words(text, words):
    words_in_text = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = words_in_text.count(word.lower())
    return word_count

assert popular_words('''When I was One I had just begun When I was Two I was nearly new 
''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
