def single_root_words(root_word, *other_words):
    same_words = []
    root_word.lower()
    # print(type(other_words))
    for i in other_words:
        if root_word in i.lower():
            same_words.append(i)
        if i.lower() in root_word.lower():
            same_words.append(i)
    return same_words
result1 = single_root_words('rich', 'richest', 'orichalcum', 'cheers', 'riches')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)