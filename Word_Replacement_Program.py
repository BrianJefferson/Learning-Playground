#Word Replacement Program

def replace_word():
    str = "Hey there! My name is Brian, what is your name? "
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")
    print(str.replace(word_to_replace, word_replacement))

replace_word()
