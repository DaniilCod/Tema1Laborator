produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]

reducere_curenta = 0
vmeniu = 1
vmeniu2 = 1

def afisare(produse, preturi, stoc):
    for i in range(len(produse)):
        print(f"{i}. {produse[i]} Pret: {preturi[i]} lei Stoc: {stoc[i]}")

def adaugareprodus(produse, preturi, stoc, cant_comanda):
    print("Introdu indexul produsului:")
    produs=input()
    produs=int(produs)
    print("Introdu cantitatea:")
    cantitate=input()
    cantitate=int(cantitate)
    if(produs<=len(produse) and cantitate<=stoc[produs]):
        cant_comanda[produs]=cantitate
        print("Cosul dumneavoastra a fost modificat")
    elif(produs>len(produse)):
        print("Produsul pe care l-ati introdus nu exista")
    elif(cantitate>stoc[produs]):
        print("Nu esta stoc suficient pentru cantitatea introdusa de dumneavoastra")
    return

def scadere(produse, preturi, stoc, cant_comanda):
    print("Introdu indexul produsului:")
    produs = input()
    produs = int(produs)
    print("Introdu cantitatea:")
    cantitate = input()
    cantitate = int(cantitate)
    if (produs <= len(produse) and cantitate <= cant_comanda[produs]):
        cant_comanda[produs] -= cantitate
        print("Cosul dumneavoastra a fost modificat")
    elif (produs > len(produse)):
        print("Produsul pe care l-ati introdus nu exista")
    elif (cantitate > cant_comanda[produs]):
        cant_comanda[produs] = 0
        print("Cosul dumneavoastra a fost modificat")
    return

def total(produse, preturi, stoc, cant_comanda):
    valtotal=0
    p=0
    for p in range(len(preturi)):
        if cant_comanda[p]>0:
            valtotal+=preturi[p]*stoc[p]
    aplreducere(produse, preturi, stoc, cant_comanda, valtotal)

def aplreducere(produse, preturi, stoc, cant_comanda, valtotal):
    global reducere_curenta
    if valtotal==0:
        print("Comanda este goala")
        reducere_curenta=0
        return
    print("1. Student \n 2. Happy\n 3. Cupon\n 4. Fara reducere\n 5. Inapoi")
    ales=input()
    totalfinal=valtotal
    if ales=="1":
        if valtotal>=30:
            reducere_curenta=0.1*valtotal
        else:
            reducere_curenta=0
            print("Totalul este insuficient")
    return


while vmeniu==1:
    if vmeniu2 == 1:
        print(f"1. Afisare meniu produse\n2. Adaugare produs in comanda\n3. Scadere/eliminare produs din comanda\n4. Aplicare reducere\n5. Finalizare comanda\n6. Anulare comanda\n7. Afisare cantitate produse din cos\n0. Iesire")
        vmeniu2 = 0
        cin=input()
        if cin=="1":
            afisare(produse,preturi,stoc)
        elif cin=="2":
            adaugareprodus(produse, preturi, stoc, cant_comanda)
        elif cin=="3":
            scadere(produse, preturi, stoc, cant_comanda)
        elif cin=="4":
            total(produse, preturi, stoc, cant_comanda)
        elif cin=="7":
            print(cant_comanda)
        vmeniu2 = 1