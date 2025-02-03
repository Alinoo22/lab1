def reverse():
   sentence = input("Your sentense, please: ")
   split_to_words = sentence.split()
   split_to_words.reverse()
   reversed_sentence = ' '.join(split_to_words)
   return reversed_sentence
print(reverse())