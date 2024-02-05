def countWords(sentences):
    word_count = 0
    
    for char in sentences:
        
        if char == ' ':
            word_count += 1
    
    return word_count + 1


user_sentence = input("Enter a sentence: ")


result = countWords(user_sentence)
print(f"Number of words: {result}")
