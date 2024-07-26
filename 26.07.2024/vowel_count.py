words = input("Enter words separated by spaces: ").split()
for word in words:
    vowel_count = sum(1 for letter in word if letter.lower() in 'aeiou')
    print(f"{word}: {vowel_count}")
