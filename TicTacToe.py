#Tic Tac Toe

Plansza = [' -',' -',' -',
        ' -',' -',' -',
        ' -',' -',' -']
ObecnyGracz = 'X'
Zwyciezca = None
TrwajacaGra = True

#Plansza do gry

def PlanszaDoGry(Plansza):
    print('│' + Plansza[0] + ' │' + Plansza[1] + ' │' + Plansza[2] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[0] + ' │' + Plansza[1] + ' │' + Plansza[2] + ' │')
    print('├───┼───┼───┤')
    print('│' + Plansza[0] + ' │' + Plansza[1] + ' │' + Plansza[2] + ' │') 
     
PlanszaDoGry(Plansza)

#Wpisanie danych przez gracza

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis

#Zmiana gracza

#Sprawdzenie czy dany ruch daje zwyciestwo lub remis