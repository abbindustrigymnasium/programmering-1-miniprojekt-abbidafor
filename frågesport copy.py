# importerar en random funktion
import random

import requests

# frågorna definerade till kortare variabler 
Fråga1 = "Vem gav 1755 ut kokboksklassikern Hjelpreda I hushållningen för unga Fruentim(b)er?"
Fråga2 = "När tillverkades första JAS gripen?"
Fråga3 = "Vad heter björnen i djungelboken?"
Fråga4 = "Är norrland ett land?"

# vi har 0 poäng från början
poäng = 0

# skapar en lista för highscore 
highscore_lista = []

# en url till api för att hämta frågorna
url ='https://opentdb.com/api.php?amount=10&type=multiple'

# skapar en lista för frågorna
frågor = []

# get funktionen gör anropet mot api:t
r = requests.get(url)
response_dictionary = r.json()

# loppar igenom alla frågor som hämtats av api:t
for result in response_dictionary['results']:
    fråga = { } 
    fråga['Fråga'] = result['question']
    fråga['Alternativ'] = result['incorrect_answers']
    fråga['Alternativ'].append(result['correct_answer'])
    fråga['Svar'] = result['correct_answer']
    frågor.append(fråga)  


# skriver ut välkommen frasen
print('Välkommen till Quizmas!')

# randomar frågorna 
random.shuffle(frågor)

# random funktion för svarsalternativen
    # loopar igenom listan frågor och shufflar/randomar alternativen i dictionary
for fråga in frågor:    
    random.shuffle(fråga['Alternativ'])

    # kollar vilket alternativ som är rätt 
    # hämtar index i listan med alternativ och kollar vilket som är rätt
    index = fråga['Alternativ'].index(fråga['Svar'])
    
    fråga['RättAlternativ']  = index + 1

    # skriver ut frågan och alternativ
    print(fråga['Fråga'])
    print('Alternativ: ')
    for index, alternativ in enumerate(fråga['Alternativ']):
        print(str(index + 1) + ": " + alternativ)

# kollar om inputen (det personen tror är rätt) stämmer med svaret. om den gör det skrivs rätt ut annars skrivs fel ut
#.upper() gör att alla bokstäver blir stora
    val = input("Skriv ditt val: ")
    if val.upper() == str(fråga['RättAlternativ']):
        poäng = poäng + 1
        print("Rätt!")
    else:
        print("Fel!")


# highscorelistan öppnas
highscore = open("HIGHSCORE.txt", "r+")
# if highscore.mode == 'r':
#     contents =highscore.read()
#     print(contents)

# contents = highscore.read()
# print(contents + "hej")

# läser raderna och läser in actuell lista till programmet
fl = highscore.readlines()
for x in fl:
    highscore_lista.append(int(x))

# sorterar highscore listan från störst till minst 
highscore_lista.sort(reverse = True)

# kollar om min poäng är lägre än det minsta värdet i highscorelistan
# raderar sista positionen i listan
if poäng > min(highscore_lista):
    del highscore_lista[-1]
    highscore_lista.append(poäng)
    highscore_lista.sort(reverse = True)
    highscore.seek(0)
    for p in highscore_lista:
        highscore.write(str(p) + "\n")
    print("Du kom med på HIGHSCORE listan!")

# stänger highscorelistan-fil
highscore.close()
    
print("Du fick " + str(poäng) + " poäng!")

print("HIGHSCORE lista:")
for n in highscore_lista:
    print(str(n) + " poäng")