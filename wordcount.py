# Word count program
# Name: Chinmay PC
# USN: 1RUA25BCA0021
def word_count(text):
    words = text.split()
    return len(words)

text = input("Enter a sentence: ")
print("Number of words:", word_count(text))
