
string = int(input('Введите длину списка :'))

words = []
words_length = []
for i in range(string):
  word = input("Введите слова :")
  words.append(word)
for i in words:
  words_length.append(len(i))
print(words)  
print(words_length)