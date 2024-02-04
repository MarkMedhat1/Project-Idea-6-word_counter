def word_counter(sentence):
    word_count = {}

    words = sentence.lower().split()

    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    print("Word count:")
    for word, count in word_count.items():
        print(f"{word}: {count} occurrences")

# Example usage
user_input = input("Enter a sentence: ")
word_counter(user_input)
