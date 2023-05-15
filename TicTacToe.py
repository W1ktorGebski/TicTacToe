#Tic Tac Toe

Plansza = [' -',' -',' -',
        ' -',' -',' -',
        ' -',' -',' -']
ObecnyGracz = ' X'
Zwyciezca = None
TrwaGra = True

#Plansza do gry

def PlanszaDoGry(Plansza):
    print('│' + Plansza[0] + ' │' + Plansza[1] + ' │' + Plansza[2] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[3] + ' │' + Plansza[4] + ' │' + Plansza[5] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[6] + ' │' + Plansza[7] + ' │' + Plansza[8] + ' │') 

#Wpisanie koordynatow przez gracza

def WprowadzLiczbe(Plansza):
    i = int(input('Wprowadz liczbe w zakresie 1-9: '))
    if i >= 1 and i <= 9 and Plansza[i-1] == ' -':
        Plansza[i-1] = ObecnyGracz
    else:
        print('Podana liczba nie jest w zakresie od 1-9 lub podana liczba jest juz zajeta')

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis

#Zmiana gracza

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis

while TrwaGra:
    PlanszaDoGry(Plansza)
    WprowadzLiczbe(Plansza)
