#Tic Tac Toe

Plansza = [' -',' -',' -',
        ' -',' -',' -',
        ' -',' -',' -']
ObecnyGracz = ' X'
Zwyciezca = None
TrwaGra = True

#Plansza do gry

def PlanszaDoGry(Plansza):
    print('┌───┬───┬───┐')
    print('│' + Plansza[0] + ' │' + Plansza[1] + ' │' + Plansza[2] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[3] + ' │' + Plansza[4] + ' │' + Plansza[5] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[6] + ' │' + Plansza[7] + ' │' + Plansza[8] + ' │')
    print('└───┴───┴───┘')

#Wpisanie koordynatow przez gracza

def WprowadzLiczbe(Plansza):
    i = int(input('Wprowadz liczbe w zakresie 1-9: '))
    if i >= 1 and i <= 9 and Plansza[i-1] == ' -':
        Plansza[i-1] = ObecnyGracz
    else:
        print('Podana liczba nie jest w zakresie od 1-9 lub podana liczba jest juz zajeta')

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis

def WygranaWPoziomie(Plansza):
    global Zwyciezca
    if Plansza[0] == Plansza[1] == Plansza[2] and Plansza[0] != ' -':
        Zwyciezca = Plansza[0]
        return True
    elif Plansza[3] == Plansza[4] == Plansza[5] and Plansza[3] != ' -':
        Zwyciezca = Plansza[3]
        return True
    elif Plansza[6] == Plansza[7] == Plansza[8] and Plansza[6] != ' -':
        Zwyciezca = Plansza[6]
        return True

def WygranaWPionie(Plansza):
    global Zwyciezca
    if Plansza[0] == Plansza[3] == Plansza[6] and Plansza[0] != ' -':
        Zwyciezca = Plansza[0]
        return True
    elif Plansza[1] == Plansza[4] == Plansza[7] and Plansza[1] != ' -':
        Zwyciezca = Plansza[1]
        return True
    elif Plansza[2] == Plansza[5] == Plansza[8] and Plansza[2] != ' -':
        Zwyciezca = Plansza[2]
        return True

def WygranaPoskosie(Plansza):
    global Zwyciezca
    if Plansza[0] == Plansza[4] == Plansza[8] and Plansza[0] != ' -':
        Zwyciezca = Plansza[0]
        return True
    elif Plansza[2] == Plansza[4] == Plansza[6] and Plansza[2] != ' -':
        Zwyciezca = Plansza[0]
        return True

def Remis(Plansza):
    global TrwaGra
    if ' -' not in Plansza:
        PlanszaDoGry(Plansza)
        print('Remis!')
        TrwaGra = False

#Zmiana gracza

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis

while TrwaGra:
    PlanszaDoGry(Plansza)
    WprowadzLiczbe(Plansza)
