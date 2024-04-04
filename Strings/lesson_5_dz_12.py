user_input = input("Введіть рядок: ")

words = [''.join(char for char in word if char.isalnum()) for word in user_input.split()]

hashtag = '#' + ''.join(word.capitalize() for word in words)

hashtag = hashtag[:140]

print(hashtag)
