import random

# Tämä ohjelma hallitsee yhteystietojen lisäämistä, näyttämistä, hakemista, muokkaamista ja poistamista.
# Se käyttää tiedostoa tietojen tallentamiseen ja lukemiseen.
# Ohjelma kysyy käyttäjältä valintoja ja suorittaa niihin liittyvät toiminnot.

def kysy_valinta():
    # Kysytään käyttäjältä valinta.
    return int(input("Valitse toiminto:\n" \
    "1: Lisää yhteystieto\n" \
    "2: Näytä kaikki yhteystiedot\n" \
    "3: Hae yhteystieto\n" \
    "4: Muokkaa yhteystietoa\n" \
    "5: Poista yhteystieto\n" \
    "6: Hae puutteelliset yhteystiedot\n" \
    "7: Poistu ohjelmasta\n" \
    "Valintasi: "))

def main():
    # Pääohjelma, joka hallitsee yhteystietojen käsittelyä.
    valinta = kysy_valinta()
    while valinta != 7:  # Updated exit condition
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
        elif valinta == 6:
            hae_puutteelliset_yhteystiedot()  # New option
        else:
            print("Virheellinen valinta, yritä uudelleen.")
        
        valinta = kysy_valinta()
    print("Poistutaan ohjelmasta.")

def lisaa_yhteystieto():
    # Kysytään käyttäjältä yhteystiedot ja tallennetaan ne tiedostoon.
    etunimi = input("Anna etunimesi: ")
    sukunimi = input("Anna sukunimesi: ")
    puhelin = input("Anna puhelinnumerosi: ")
    email = input("Anna sähköpostiosoitteesi: ")
    id_numero = random.randint(1, 9)
    id = f"{etunimi[:2].upper()}{sukunimi[:2].upper()}{id_numero}"
    
    with open("yhteystiedot.txt", "a") as tiedosto:
        tiedosto.write(f"{id},{etunimi},{sukunimi},{puhelin},{email}\n")
    
    print(f"Yhteystieto lisätty onnistuneesti. ID: {id}")

def nayta_yhteystiedot():
    # Näytetään kaikki yhteystiedot tiedostosta.
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        if not yhteystiedot:
            print("Ei yhteystietoja näytettäväksi.")
            return
        
        print("Kaikki yhteystiedot:")
        for rivi in yhteystiedot:
            id, etunimi, sukunimi, puhelin, email = rivi.strip().split(",")
            print(f"ID: {id}, Nimi: {etunimi} {sukunimi}, Puhelin: {puhelin}, Sähköposti: {email}")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def hae_yhteystieto():
    # Haetaan tietty yhteystieto hakusanalla.
    hakusana = input("Anna hakusana: ").lower()
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        osumat = []
        for rivi in yhteystiedot:
            if hakusana in rivi.lower():
                osumat.append(rivi.strip())
        
        if osumat:
            print("Löydetyt yhteystiedot:")
            for osuma in osumat:
                print(osuma)
        else:
            print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def muokkaa_yhteystietoa():
    # Muokataan olemassa olevaa yhteystietoa.
    muokattava_id = input("Anna muokattavan henkilön ID: ")
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        for i, rivi in enumerate(yhteystiedot):
            if rivi.startswith(muokattava_id):
                etunimi = input("Anna uusi etunimi: ")
                sukunimi = input("Anna uusi sukunimi: ")
                puhelin = input("Anna uusi puhelinnumero: ")
                email = input("Anna uusi sähköpostiosoite: ")
                
                yhteystiedot[i] = f"{muokattava_id},{etunimi},{sukunimi},{puhelin},{email}\n"
                
                with open("yhteystiedot.txt", "w") as tiedosto:
                    tiedosto.writelines(yhteystiedot)
                
                print("Yhteystieto päivitetty onnistuneesti.")
                return
        print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def poista_yhteystieto():
    # Poistetaan yhteystieto tiedostosta.
    poistettava_id = input("Anna poistettavan henkilön ID: ")
    
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        for i, rivi in enumerate(yhteystiedot):
            if rivi.startswith(poistettava_id):
                del yhteystiedot[i]
                
                with open("yhteystiedot.txt", "w") as tiedosto:
                    tiedosto.writelines(yhteystiedot)
                
                print("Yhteystieto poistettu onnistuneesti.")
                return
        print("Yhteystietoa ei löytynyt.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

def hae_puutteelliset_yhteystiedot():
    # Haetaan yhteystiedot, joissa on puutteellisia kenttiä.
    try:
        with open("yhteystiedot.txt", "r") as tiedosto:
            yhteystiedot = tiedosto.readlines()
        
        puutteelliset = []
        for rivi in yhteystiedot:
            kentat = rivi.strip().split(",")
            if len(kentat) < 5 or any(not kentta.strip() for kentta in kentat):
                puutteelliset.append(rivi.strip())
        
        if puutteelliset:
            print("Puutteelliset yhteystiedot:")
            for puutteellinen in puutteelliset:
                print(puutteellinen)
        else:
            print("Ei puutteellisia yhteystietoja.")
    except FileNotFoundError:
        print("Yhteystietotiedostoa ei löydy.")

if __name__ == "__main__":
    main()