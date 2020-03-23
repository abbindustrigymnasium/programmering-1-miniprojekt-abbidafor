# importerar en random funktion
import random

# frågorna definerade till kortare variabler 
Fråga1 = "Vem gav 1755 ut kokboksklassikern Hjelpreda I hushållningen för unga Fruentim(b)er?"
Fråga2 = "När tillverkades första JAS gripen?"
Fråga3 = "Vad heter björnen i djungelboken?"
Fråga4 = "Är norrland ett land?"

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

print('Välkommen till någon pun om frågesport!')

# randomar frågorna 
random.shuffle(frågor)

# random funktion för svarsalternativen
    # loopar igenom listan frågor och shufflar/randomar alternativen i dictionary
for fråga in frågor:    
    random.shuffle(fråga['Alternativ'])

    # print('fråga')
    print(fråga['Fråga'])
    print('Alternativ: ')

    print('1: ' + fråga['Alternativ'][0])
    print('X: ' + fråga['Alternativ'][1])
    print('2: ' + fråga['Alternativ'][2])

    val = input("Skriv ditt val: ")


