



sentence = input("Enter a sentence: ") 
words = sentence.split() 
longest = max(words, key=len) 
print("Words:", words) 
print("Longest word:", longest)