def count_letters(sentence):
    words = sentence
    count = {}
    for word in range(len(words)):
        wordss = words[word]
        if wordss in count:
            count[wordss] += 1
        else:
           count[wordss] = 1
    return count
sentence = "banana"
print(count_letters(sentence))