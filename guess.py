import random
import math

od_broja = int(input("Unesi dornju granicu broja: "))
do_broja = int(input("Unesi gornju granicu broja: "))

nasumican_broj= random.randint(od_broja,do_broja)

maksimalan_broj_pokusaja = math.ceil(math.log(do_broja - od_broja + 1, 2))

print("\n\tImas ", maksimalan_broj_pokusaja, " pokusaja da pogodis broj!\n")

broj_pokusaja=0;
kraj_igre=False

while broj_pokusaja<=maksimalan_broj_pokusaja:
    broj_pokusaja+=1

    korisnikov_broj= int(input("Unesi broj: "))

    if nasumican_broj==korisnikov_broj:
        print("Ma bravo brate, pogodio si broj! Tacan broj je: ", korisnikov_broj, "\n\tPogodio si ga iz" ,broj_pokusaja, "pokusaja")
        kraj_igre=True
        break  
    elif nasumican_broj<korisnikov_broj:
        print("Tacan broj je manji od navedenog")
      
    
    else:
        print('Broj je veci od navedenog')
   

if not kraj_igre:
     print("\nBroj je %d" % nasumican_broj);
     print("\tVise srece sledeci put!")