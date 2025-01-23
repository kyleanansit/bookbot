with open('./books/frankenstein.txt', encoding='utf-8') as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_frequency = {}

    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    print("\nCharacter Count (including whitespaces):", sum(char_frequency.values()))
    
    # del hash below to Print full sorted character frequency (includes spaces and punctuation)
    # print("\nCharacter Frequency Breakdown:\n")
    # for char, count in sorted(char_frequency.items()):
    #     display_char = char if char.isprintable() else repr(char)
    #     print(f"'{display_char}': {count}")

    print("\nCharacter Count Report (Only Alphanumeric Characters):\n")
    for char, count in sorted(char_frequency.items()):
        if char.isalnum():  # Only count letters and numbers for the report
            print(f"The '{char}' character was found {count} times")

    return char_frequency

# Optional: Uncomment this line to print the full book
# print(file_contents) 

word_count = count_words(file_contents)
print("\nWord Count:", word_count)

char_count = count_characters(file_contents)  # Generates the report
