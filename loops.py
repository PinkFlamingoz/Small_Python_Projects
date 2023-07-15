text = "In the great green room"
words = text.split()


# Round 1 print each word
print("Round 1")
for word in words:
    print(word)
print()


# Round 1.1 print each word without a new line
print("Round 1.1")
for word in words:
    print(word, end=" ")
print()
print()


# Round 2 print each letter in each word 
print("Round 2")
for word in words:
    for c in word:
        print(c)
print()


# Round 3 only print words that contain the letter "g"
print("Round 3")
for word in words:
    if "g" in word:
        print(word)
print()


# Round 4 start from the 2cond word
print("Round 4")
for word in words[2:]:
    print(word)
print()


# Round 4.1 start from the 2cond word and end till the 4th word
print("Round 4.1")
for word in words[2:4]:
    print(word)
print()


# Round 5 print Goodnight Moon as many times as there are words in the list
print("Round 5")
for _ in words:
    print("Goodnight Moon")
print()