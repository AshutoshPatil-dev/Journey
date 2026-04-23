from collections import Counter
file = open("testt","r")
text = file.read().lower()
file.close()

words = text.split()
word_count = Counter(words)

#Sort by frequency (decending)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse = True)
print("Word frequencies: ")
for word, count in sorted_words:
    print(f"{word}:{count}")