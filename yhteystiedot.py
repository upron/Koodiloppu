def kysy_valinta():
    return int(input("Valitse toiminto:\n" \
    "1: Lisää yhteystieto\n" \
    "2: Näytä kaikki yhteystiedot\n" \
    "3: Hae yhteystieto\n" \
    "4: Muokkaa yhteystietoa\n" \
    "5: Poista yhteystieto\n" \
    "6: Poistu ohjelmasta\n" \
    "Valintasi: "))

def main():
    valinta = kysy_valinta()
    while valinta != 6:
        if valinta == 1:
            lisaa_yhteystieto()
        elif valinta == 2:
            nayta_yhteystiedot()
        elif valinta == 3:
            hae_yhteystieto()
        elif valinta == 4:
            muokkaa_yhteystietoa()
        elif valinta == 5:
            poista_yhteystieto()
        else:
            print("Virheellinen valinta, yritä uudelleen.")
        
        valinta = kysy_valinta()
    print("Poistutaan ohjelmasta.")

def lisaa_yhteystieto():
    nimi = input("Anna nimesi: ")
    puhelin = input("Anna puhelinnumerosi: ")
    email = input("Anna sähköpostiosoitteesi: ")
    
    with open("yhteystiedot.txt", "a") as tiedosto:
        tiedosto.write(f"{nimi},{puhelin},{email}\n")
    
    print("Yhteystieto lisätty onnistuneesti.")

def nayta_yhteystiedot():
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        if not yhteystiedot:
            print("Ei yhteystietoja näytettäväksi.")
            return
        
        print("Kaikki yhteystiedot:")
        for rivi in yhteystiedot:
            nimi, puhelin, email = rivi.strip().split(",")
            print(f"Nimi: {nimi}, Puhelin: {puhelin}, Sähköposti: {email}")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def hae_yhteystieto():
    nimi = input("Anna haettavan henkilön nimi: ")
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        for rivi in yhteystiedot:
            if rivi.startswith(nimi):
                print(f"Löydetty yhteystieto: {rivi.strip()}")
                return
        print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def muokkaa_yhteystietoa():
    nimi = input("Anna muokattavan henkilön nimi: ")
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        for i, rivi in enumerate(yhteystiedot):
            if rivi.startswith(nimi):
                uusi_nimi = input("Anna uusi nimi: ")
                uusi_puhelin = input("Anna uusi puhelinnumero: ")
                uusi_email = input("Anna uusi sähköpostiosoite: ")
                
                yhteystiedot[i] = f"{uusi_nimi},{uusi_puhelin},{uusi_email}\n"
                
                with open("yhteystiedot.txt", "w") as tiedosto:
                    tiedosto.writelines(yhteystiedot)
                
                print("Yhteystieto päivitetty onnistuneesti.")
                return
        print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def poista_yhteystieto():
    nimi = input("Anna poistettavan henkilön nimi: ")
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        for i, rivi in enumerate(yhteystiedot):
            if rivi.startswith(nimi):
                del yhteystiedot[i]
                
                with open("yhteystiedot.txt", "w") as tiedosto:
                    tiedosto.writelines(yhteystiedot)
                
                print("Yhteystieto poistettu onnistuneesti.")
                return
        print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

if __name__ == "__main__":
    main()