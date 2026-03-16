produse = ["espresso", "latte", "cappuccino", "ceai", "ciocolata calda", "croissant"]
preturi = [8.0, 12.0, 11.0, 7.0, 10.0, 9.0]
stoc = [20, 15, 18, 30, 12, 10]
cant_comanda = [0, 0, 0, 0, 0, 0]
reducere_curenta = 0
vmeniu = 1
vmeniu2 = 1

def afisare(produse, preturi, stoc):
    for i in range(len(produse)):
        print(f"{i}. {produse[i]} : {preturi[i]} lei : Stoc disponibil: {stoc[i]}")

def adaugareprodus(produse, preturi, stoc, cant_comanda):
    print("Introdu indexul produsului:")
    p = int(input())
    print("Introdu cantitatea:")
    c = int(input())
    if p < len(produse) and c <= (stoc[p] - cant_comanda[p]):
        cant_comanda[p] += c
        print("Cosul dumneavoastra a fost modificat")
    elif p >= len(produse):
        print("Produsul pe care l-ati introdus nu exista")
    else:
        print("Nu este stoc suficient")

def scadere(produse, preturi, stoc, cant_comanda):
    print("Introdu indexul produsului:")
    p = int(input())
    print("Introdu cantitatea:")
    c = int(input())
    if p < len(produse) and c <= cant_comanda[p]:
        cant_comanda[p] -= c
        print("Cosul tau a fost modificat")
    elif p >= len(produse):
        print("Produsul nu exista")
    else:
        cant_comanda[p] = 0
        print("Cosul a fost modificat")

def total(produse, preturi, stoc, cant_comanda):
    vt = 0
    for i in range(len(preturi)):
        vt += preturi[i] * cant_comanda[i]
    aplreducere(vt)

def aplreducere(vt):
    global reducere_curenta
    if vt == 0:
        print("Comanda este goala")
        reducere_curenta = 0
        return
    print("1. student\n   2. happy\n  3. cupon\n4. fara reducere\n5. inapoi")
    ales = input()
    if ales == "1":
        if vt >= 30: reducere_curenta = 0.1 * vt
        else:
            reducere_curenta = 0
            print("Totalul e insuficient")
    elif ales == "2":
        if vt >= 50: reducere_curenta = 0.15 * vt
        else:
            reducere_curenta = 0
            print("Totalul este insuficient")
    elif ales == "3":
        if vt >= 25: reducere_curenta = 7.0
        else:
            reducere_curenta = 0
            print("Totalul este insuficient")
    elif ales =="4": reducere_curenta = 0


def finalizare(produse, preturi, stoc, cant_comanda):
    global reducere_curenta
    vb = sum(preturi[i] * cant_comanda[i] for i in range(len(preturi)))
    if vb == 0:
        print("Nu exista produse in comanda ta")
        return
    print("\nBon fiscal")
    for i in range(len(produse)):
        if cant_comanda[i] > 0:
            subtotal_produs = cant_comanda[i] * preturi[i]
            print(f"{produse[i]} x {cant_comanda[i]} = {subtotal_produs} lei")
    r = min(reducere_curenta, vb)
    print(f"Subtotal: {vb} lei")
    print(f"Reducere: {r} lei")
    print(f"Total Final: {vb - r} lei")
    print(" ")
    for i in range(len(stoc)):
        stoc[i] -= cant_comanda[i]
        cant_comanda[i] = 0
    reducere_curenta = 0

def anulare(cant_comanda):
    global reducere_curenta
    for i in range(len(cant_comanda)): cant_comanda[i] = 0
    reducere_curenta = 0
    print("Comanda anulata")

while vmeniu == 1:
    if vmeniu2 == 1:
        print(f"1. Afisare meniu produse\n2. Adaugare produs in comanda\n3. Scadere/eliminare produs din comanda\n4. Aplicare reducere\n5. Finalizare comanda\n6. Anulare comanda\n7. Afisare cantitate produse din cos\n0. Iesire")
        vmeniu2 = 0
        cin = input()
        if cin == "1":
            afisare(produse, preturi, stoc)
        elif cin == "2":
            adaugareprodus(produse, preturi, stoc, cant_comanda)
        elif cin == "3":
            scadere(produse, preturi, stoc, cant_comanda)
        elif cin == "4":
            total(produse, preturi, stoc, cant_comanda)
        elif cin == "5":
            finalizare(produse, preturi, stoc, cant_comanda)
        elif cin == "6":
            anulare(cant_comanda)
        elif cin == "7":
            print(cant_comanda)
        elif cin == "0":
            vmeniu = 0
        vmeniu2 = 1
