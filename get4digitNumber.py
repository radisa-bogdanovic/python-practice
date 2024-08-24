import random

cetvorocifreni_broj = str(random.randrange(1000, 10000))
korisnicki_input = input('Unesi ?etvorocifreni broj: ')

if korisnicki_input == cetvorocifreni_broj:
    print("Bravo hakeru")
else:
    globalni_broj_pokusaja = 0

    while korisnicki_input != cetvorocifreni_broj:
        globalni_broj_pokusaja += 1
        broj_pogodjenih = 0
        tacno = ["X"] * 4

        for i in range(4):
            if korisnicki_input[i] == cetvorocifreni_broj[i]:
                broj_pogodjenih += 1
                tacno[i] = korisnicki_input[i]

        if broj_pogodjenih == 0:
            print('Ni jedna od cifara ne odgovara broju')
        else:
            print('Nije ceo broj, ali imas', broj_pogodjenih, 'ta?nih cifara:', ''.join(tacno))
        
        korisnicki_input = input("Upisi sledeci redosled cifara: ")

    print(f"Pogodio si tacan broj! Trebalo ti je {globalni_broj_pokusaja + 1} pokusaja.")