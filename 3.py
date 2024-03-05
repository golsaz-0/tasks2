word = input('Enter the word: ')

for sym in word:
    if sym == 'ф' or sym == 'Ф':
        print("Ого! Это редкое слово!")

        break
else:
    print('Эх, это не очень редкое слово...')