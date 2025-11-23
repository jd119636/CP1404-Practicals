"""
Word Occurrences
Estimate: 20 minutes
Actual:   30 minutes
"""

sentence = input("Enter a sentence: ").lower()
split_sentence = sentence.split()

word_counts = {}

for word in split_sentence:
    length: int = len(word)
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

for word, count in word_counts.items():
    print(f"{word:{length}} {count:3}")
