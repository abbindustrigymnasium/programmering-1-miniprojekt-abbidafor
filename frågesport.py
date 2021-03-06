# importerar en random funktion
import random

# frågorna definerade till kortare variabler 
Fråga1 = "Vem gav 1755 ut kokboksklassikern Hjelpreda I hushållningen för unga Fruentim(b)er?"
Fråga2 = "När tillverkades första JAS gripen?"
Fråga3 = "Vad heter björnen i djungelboken?"
Fråga4 = "Är norrland ett land?"

# vi har 0 poäng från början
poäng = 0

# dictionary/lista över frågorna, svarsalternativ och svar 
frågor = [
    {
        'Fråga': Fråga1,
        'Alternativ': [
            "Selma Lagerlöv",
            "Cajsa Warg",
            "Lisa Ajax"
        ],
        'Svar': 'Cajsa Warg'
    },
    {
        'Fråga': Fråga2,        
        'Alternativ': [
            "1985",
            "1978",
            "1982"
        ],
        'Svar': '1982'
    },
    {
        'Fråga': Fråga3,
        'Alternativ': [
            "Shere Khan",
            "Bagheera",
            "Baloo"
        ],
        'Svar': 'Baloo'
    },
    { 
        'Fråga': Fråga4,
        'Alternativ': [
            "Ja",
            "På sätt o vis",
            "Nej"
        ],
        'Svar': 'Nej'
    }
]

# skriver ut välkommen frasen
print('Välkommen till Quizmas!')

# randomar frågorna 
random.shuffle(frågor)

# random funktion för svarsalternativen
    # loopar igenom listan frågor och shufflar/randomar alternativen i dictionary
for fråga in frågor:    
    random.shuffle(fråga['Alternativ'])

# kollar vilket alternativ som är rätt 
# hämtar index i listan med alternativ och kollar om det är 1 x eller 2
    index = fråga['Alternativ'].index(fråga['Svar'])
    if index == 0:
        fråga['RättAlternativ']  = '1'
    elif index == 1:
        fråga['RättAlternativ']  = 'X'
    else:
        fråga['RättAlternativ']  = '2'

# skriver ut frågan och salternativ
    print(fråga['Fråga'])
    print('Alternativ: ')

# skriver ut 1, X eller 2 + svarsalternativ
    print('1: ' + fråga['Alternativ'][0])
    print('X: ' + fråga['Alternativ'][1])
    print('2: ' + fråga['Alternativ'][2])

# kollar om inputen (det personen tror är rätt) stämmer med svaret. om den gör det skrivs rätt ut annars skrivs fel ut
#.upper() gör att alla bokstäver blir stora
    val = input("Skriv ditt val: ")
    if val.upper() == fråga['RättAlternativ']:
        poäng = poäng + 1
        print("Rätt!")
    else:
        print("Fel!")
    
print("Du fick " + str(poäng) + " poäng!")
