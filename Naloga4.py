def izpisi_trikotnik(visina):
    for i in range(1, visina + 1):
        print('*' * i)


visina = int(input("Vnesite višino trikotnika: "))
izpisi_trikotnik(visina)