kolor = input('Jaki kolor lubisz?\n').lower()
if kolor == 'czerwony':
    print('Ja też lubię czerwony')
else:
    print(f'Nie lubie koloru {kolor}, wolę kolor czerwony')

rainy = input("Is it raining?\n").lower()
if rainy == 'yes':
    windy = input('Is it windy?\n').lower()
    if windy == 'yes':
        print('It`s too windy for umbrella.')
    elif windy == 'no':
        print('Take your umbrella.')
elif rainy == 'no':
    print('Enjoy your day!')

name = input("What`s your name?\n")
print(len(name))

name = input("What`s your name?\n")
surname = input("What`s your surname?\n")
name_surname = name + ' ' + surname
print(name_surname, len(name_surname))

name = input("What`s your name(in lower case)?\n").title()
surname = input("What`s your surname(in lower case)?\n").title()
name_surname = name + ' ' + surname
print(name_surname)

first_name = input('What`s your first name?')
if len(first_name) < 5:
    surname = input('What`s your first name?')
    name = first_name + surname
    print(name.upper())
else:
    print(first_name.lower())

answer = input('Podaj jakiś tekst: ')
answer_len = len(answer)
start_num = int(input("Podaj liczbę od 1 do {}".format(answer_len + 1)))
end_num = int(input("Podaj liczbę od {} do {}".format(start_num + 1, answer_len + 1)))
print(answer[start_num - 1: end_num - 1])

word = input("say a word: ")
vowel = ['a', 'e', 'o', 'u', 'i', 'y']
if word[0] in vowel:
    print(word + 'way')
else:
    pig_word = word[1:len(word)] + word[0] + 'ay'
    print(pig_word)

lista_miats = ['Wrocław', 'Warszawa', 'Londyn', 'Poznan']
wycinek1 = lista_miats[1:3]
wycinek2 = lista_miats[1:]
print(lista_miats)
print(wycinek1)
print(wycinek2)
#a

male_miasta = str(lista_miats)
print(male_miasta.lower())