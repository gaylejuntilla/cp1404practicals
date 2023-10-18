"""
Word Occurrences
Estimate: 40 minutes
Actual: 47 minutes
"""


text = input("Text: ")
word_to_count = {}
words = text.split()

for word in words:
    try:
        word_to_count[word] += 1
    except KeyError:
        word_to_count[word] = 1

ordered_words = sorted(word_to_count.keys())
max_word_length = max(len(word) for word in words)
for word in ordered_words:
    print(f"{word:{max_word_length}} : {word_to_count[word]}")
