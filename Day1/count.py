def count_words(sentence):
    word = sentence.split()
    count = {}
    for words in word:
        if words in count:
            count[words] += 1
        else:
            count[words] = 1
    return count

sentence = "the cat and the dog and the bird"
print(count_words(sentence))



