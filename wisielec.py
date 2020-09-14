import random

slownik=['kot','piesek','slon','zyrafa','zolw','mrowka','kon','mysz','krowa','swinia']
czy_zgadnal=False
ilosc_zyc=10
koniec_gry='nie'

wylosowany_wyraz=random.choice(slownik)
#print("Developer help: "+wylosowany_wyraz)
print('Zgadnij wyraz zwierzę: *bez polskich liter')

wyrazx=[]
i=0
while len(wylosowany_wyraz)>i:
    wyrazx.append("_")
    i=i+1

def narysuj_obrazek():
    if ilosc_zyc==9:
        print('          ')
        print('          ')
        print('          ')
        print('          ')
        print('==========')
    if ilosc_zyc==8:
        print('       I  ')
        print('       I  ')
        print('       I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==7:
        print('   |---I  ')
        print('       I  ')
        print('       I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==6:
        print('   |---I  ')
        print('   :   I  ')
        print('       I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==6:
        print('   |---I  ')
        print('  :)   I  ')
        print('       I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==5:
        print('   |---I  ')
        print('  :)   I  ')
        print('   I   I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==4:
        print('   |---I  ')
        print('  :)   I  ')
        print('   I\  I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==3:
        print('   |---I  ')
        print('  :)   I  ')
        print('  /I\  I  ')
        print('       I  ')
        print('==========')
    if ilosc_zyc==2:
        print('   |---I  ')
        print('  :)   I  ')
        print('  /I\  I  ')
        print('    \  I  ')
        print('==========')
    if ilosc_zyc==1:
        print('   |---I  ')
        print('  :)   I  ')
        print('  /I\  I  ')
        print('   /\  I  ')
        print('==========')
    if ilosc_zyc==0:
        print('   |---I  ')
        print('  :o   I  ')
        print('  \I/  I  ')
        print('   /\  I  ')
        print('==========')
    print('Masz '+str(ilosc_zyc)+' żyć!')

while True:
    # wypisanie wyrazuX (nieznanego)
    j = 0
    while len(wyrazx) > j:
        print(wyrazx[j], end="")
        j = j + 1
    print('')
    #zgadywanie
    a=input('Zgadnij literę albo hasło:')

    #sprawdzenie czy litera jest w slowie i zgadnął
    i = 0
    while len(wylosowany_wyraz)>i:
        if wylosowany_wyraz[i]==a:
            #print('Jest w miejscu',i)
            wyrazx[i]=a
            czy_zgadnal=True
        i = i + 1

    #sprawdzenie czy zgadął wyraz
    if a==wylosowany_wyraz:
        print('Zgadłeś wyraz! Wygrales!' + ' Haslo to: "' + wylosowany_wyraz + '".')
        czy_zgadnal = True
        koniec_gry = 'tak'

    #sprawdzenie czy przeglales (plus zaczcie nowej gry)
    if czy_zgadnal==False:
        ilosc_zyc=ilosc_zyc-1
        print('Nie zgadłeś!')
        narysuj_obrazek()
        if ilosc_zyc==0:
            print('Przegrales!' + ' Haslo to: "' + wylosowany_wyraz + '"')
            koniec_gry='tak'

    #sprawdzenie czy wygrales (plus zaczcie nowej gry)
    if ''.join(wyrazx) == wylosowany_wyraz:
        print('Zgadłeś literę! Wygrales!' + ' Haslo to: "' + wylosowany_wyraz + '"')
        koniec_gry = 'tak'

    #czy koniec jest gry?
    if koniec_gry=='tak':
        input('Czy chcesz grac dalej? (enter-tak)')
        #restart danych
        czy_zgadnal=False
        ilosc_zyc=10
        koniec_gry = 'nie'
        wylosowany_wyraz = random.choice(slownik)
        wyrazx = []
        i = 0
        while len(wylosowany_wyraz) > i:
            wyrazx.append("_")
            i = i + 1

    czy_zgadnal=False
