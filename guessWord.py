import random

ime= input("Kako se zoves?")

print("Srecno! ", ime)


reci= ['mesec', 'python', 'fudbal', 'arsenal', 'radisa']


nasumicna_rec= random.choice(reci)

print('Pogadjaj karaktere')

pokusaji=''
broj_pokusaja= 12


while broj_pokusaja>0:
    broj_promasaja=0

    for char in nasumicna_rec:
        if char in pokusaji:
            print(char, end=" ")
        else:
            print("_")
            broj_promasaja+=1
    if broj_promasaja==0:
        print("Pobedio si")
        print("Rec je: ", nasumicna_rec)
        break


    print()
    pokusaj=input('Unesi karakter:')
    pokusaji+=pokusaj
    if pokusaj not in nasumicna_rec:
        broj_pokusaja-=1
        print('Pogresan karakter')
        print('Imas jos', +broj_pokusaja, 'pokusaja')

        if broj_pokusaja==0:
            print('Izgubio si')
