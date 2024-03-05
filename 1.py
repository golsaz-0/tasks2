n = int(input('Enter n: '))

result = ''

for i in range(0, n):
    word = input(f'Enter the {i + 1} word: ')
    result += word + ' '

result = result[:-1]

print(result)