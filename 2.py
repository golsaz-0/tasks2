result = ''

# eternal loop
while(True):
    word = input(f'Enter the word: ')

    if word == 'stop':
        break

    result += word + ' '

result = result[:-1]

print(result)