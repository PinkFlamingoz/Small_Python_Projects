# Words in dictionary
words = set()


#Return true if word is in dictionary else false
def check(word):
    if word.lower() in words:
        return True
    else:
        return False


# Load dictionary into memory, returning true if successful else false
def load(dictionary):
    file = open(dictionary, "r")
    for line in file:
        word = line.rstrip() #-- Remove the las \0 character of the word
        words.add(word)
    file.close()
    return True


# Returns number of words in dictionary if loaded else 0 if not yet loaded
def size():
    return len(words)