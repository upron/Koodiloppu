import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os

TIEDOSTO = "yhteystiedot.txt" # Tiedoston nimi, johon yhteystiedot tallennetaan

# --- PÄÄIKKUNA ---
root = tk.Tk()
root.title("Yhteystietosovellus")


# Aseta pääikkunan koko ja keskitä se näytölle
ikkuna_leveys = 1280
ikkuna_korkeus = 720
näyttö_leveys = root.winfo_screenwidth()  # Näytön leveys
näyttö_korkeus = root.winfo_screenheight()  # Näytön korkeus
x = (näyttö_leveys // 2) - (ikkuna_leveys // 2)  # Lasketaan ikkunan sijainti
y = (näyttö_korkeus // 2) - (ikkuna_korkeus // 2)
root.geometry(f"{ikkuna_leveys}x{ikkuna_korkeus}+{x}+{y}")  # Asetetaan ikkuna keskelle
root.minsize(800, 600)  # Määritetään minimikoko
root.configure(bg="#d4d0c8")


# --- IKKUNAN APUFUNKTIO ---
def avaa_keskitetty_ikkuna(ikkuna, leveys, korkeus):
    """Avaa uusi ikkuna ja keskitä se pääikkunaan."""
    ikkuna.geometry(f"{leveys}x{korkeus}")
    ikkuna.update_idletasks()  # Päivittää ikkunan asettelut
    x = root.winfo_x() + (root.winfo_width() // 2) - (leveys // 2)
    y = root.winfo_y() + (root.winfo_height() // 2) - (korkeus // 2)
    ikkuna.geometry(f"+{x}+{y}")  # Sijoittaa ikkunan keskelle


# --- LISÄÄ YHTEYSTIETO ---
def lisaa_yhteystieto():
    """Avaa ikkuna, jossa käyttäjä voi lisätä yhteystiedon."""
    ikkuna = tk.Toplevel(root)  # Luo uusi ikkuna pääikkunan päälle
    ikkuna.title("Lisää yhteystieto")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)  # Keskittää ikkunan
    ikkuna.configure(bg="#d4d0c8")  # Asetetaan taustaväri
    ikkuna.transient(root)  # Ikkuna pysyy pääikkunan päällä
    ikkuna.grab_set()  # Estää pääikkunan käytön, kun tämä ikkuna on auki

    # Tekstikentät ja napit yhteystiedon syöttämistä varten
    tk.Label(ikkuna, text="Etunimi:", bg="#d4d0c8", fg="black").pack(pady=5)
    etunimi_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    etunimi_entry.pack()

    tk.Label(ikkuna, text="Sukunimi:", bg="#d4d0c8", fg="black").pack(pady=5)
    sukunimi_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    sukunimi_entry.pack()

    tk.Label(ikkuna, text="Puhelin:", bg="#d4d0c8", fg="black").pack(pady=5)
    puhelin_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    puhelin_entry.pack()

    tk.Label(ikkuna, text="Sähköposti:", bg="#d4d0c8", fg="black").pack(pady=5)
    email_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    email_entry.pack()

    def tallenna():
        etunimi = etunimi_entry.get()
        sukunimi = sukunimi_entry.get()
        puhelin = puhelin_entry.get()
        email = email_entry.get()
        if not etunimi or not sukunimi:
            messagebox.showerror("Virhe", "Etunimi ja sukunimi ovat pakollisia.")
            return
        id_numero = random.randint(1, 9)
        id = f"{etunimi[:2].upper()}{sukunimi[:2].upper()}{id_numero}"
        with open(TIEDOSTO, "a") as f:
            f.write(f"{id},{etunimi},{sukunimi},{puhelin},{email}\n")
        messagebox.showinfo("Tallennettu", f"Yhteystieto lisätty. ID: {id}")
        ikkuna.destroy()

    tk.Button(ikkuna, text="Tallenna", command=tallenna, bg="#ece9d8", fg="black", activebackground="#316ac5", activeforeground="white", relief="raised", bd=2).pack(pady=10)

# --- NÄYTÄ KAIKKI ---
def nayta_yhteystiedot():
    ikkuna = tk.Toplevel(root)
    ikkuna.title("Kaikki yhteystiedot")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)
    ikkuna.configure(bg="#d4d0c8") 
    ikkuna.transient(root)
    ikkuna.grab_set()

    teksti = tk.Text(ikkuna, bg="#d4d0c8", fg="black", relief="sunken", bd=1)
    teksti.pack(expand=True, fill="both")

    try:
        with open(TIEDOSTO, "r") as f:
            rivit = f.readlines()
            if not rivit:
                teksti.insert("1.0", "Ei yhteystietoja.")
            else:
                for rivi in rivit:
                    id, etu, suku, puh, email = rivi.strip().split(",")
                    teksti.insert("end", f"ID: {id}, Nimi: {etu} {suku}, Puh: {puh}, Sähköposti: {email}\n")
    except FileNotFoundError:
        teksti.insert("1.0", "Tiedostoa ei löydy.")

# --- HAE ---
def hae_yhteystieto():
    ikkuna = tk.Toplevel(root)
    ikkuna.title("Hae yhteystieto")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)
    ikkuna.configure(bg="#d4d0c8") 
    ikkuna.transient(root)
    ikkuna.grab_set()

    # Hakukenttä ja nappi rinnakkain
    hakurivi = tk.Frame(ikkuna, bg="#d4d0c8")
    hakurivi.pack(pady=10)

    tk.Label(hakurivi, text="Anna hakusana:", bg="#d4d0c8", fg="black").pack(side="left", padx=(0, 5))
    haku_entry = tk.Entry(hakurivi, bg="white", fg="black", relief="sunken", bd=1)
    haku_entry.pack(side="left", padx=(0, 5))
    tk.Button(hakurivi, text="Hae", command=lambda: hae(), bg="#ece9d8", fg="black", activebackground="#316ac5", activeforeground="white", relief="raised", bd=2).pack(side="left")

    # Tulokset
    tulokset = tk.Text(ikkuna, bg="#d4d0c8", fg="black", relief="sunken", bd=1)
    tulokset.pack(expand=True, fill="both", padx=10, pady=5)

    def hae():
        hakusana = haku_entry.get().strip().lower()
        tulokset.delete("1.0", "end")
        if not hakusana:
            tulokset.insert("1.0", "Anna hakusana.")
            return
        try:
            with open(TIEDOSTO, "r") as f:
                rivit = f.readlines()
                osumat = [rivi for rivi in rivit if hakusana in rivi.lower()]
                if osumat:
                    for r in osumat:
                        tulokset.insert("end", r)
                else:
                    tulokset.insert("1.0", "Ei osumia.")
        except FileNotFoundError:
            tulokset.insert("1.0", "Tiedostoa ei löydy.")

# --- MUOKKAA ---
def muokkaa_yhteystietoa():
    ikkuna = tk.Toplevel(root)
    ikkuna.title("Muokkaa yhteystietoa")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)
    ikkuna.configure(bg="#d4d0c8") 
    ikkuna.transient(root)
    ikkuna.grab_set()

    tk.Label(ikkuna, text="Anna muokattavan ID:", bg="#d4d0c8", fg="black").pack(pady=5)
    id_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    id_entry.pack()

    etunimi_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    sukunimi_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    puhelin_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)
    email_entry = tk.Entry(ikkuna, bg="white", fg="black", relief="sunken", bd=1)

    def hae():
        muokattava_id = id_entry.get().strip()
        if not muokattava_id:
            messagebox.showerror("Virhe", "Anna ID ennen hakua.")
            return
        try:
            with open(TIEDOSTO, "r") as f:
                rivit = f.readlines()
            loytyi = False
            for rivi in rivit:
                if rivi.startswith(muokattava_id + ","):
                    loytyi = True
                    _, etu, suku, puh, email = rivi.strip().split(",")
                    etunimi_entry.delete(0, "end")
                    etunimi_entry.insert(0, etu)
                    sukunimi_entry.delete(0, "end")
                    sukunimi_entry.insert(0, suku)
                    puhelin_entry.delete(0, "end")
                    puhelin_entry.insert(0, puh)
                    email_entry.delete(0, "end")
                    email_entry.insert(0, email)
                    break
            if not loytyi:
                messagebox.showerror("Virhe", "ID:tä ei löytynyt.")
        except FileNotFoundError:
            messagebox.showerror("Virhe", "Tiedostoa ei löydy.")

    tk.Button(ikkuna, text="Hae ID", command=hae, bg="#ece9d8", fg="black", activebackground="#316ac5", activeforeground="white", relief="raised", bd=2).pack(pady=5)
    tk.Label(ikkuna, text="Etunimi:", bg="#d4d0c8", fg="black").pack()
    etunimi_entry.pack()
    tk.Label(ikkuna, text="Sukunimi:", bg="#d4d0c8", fg="black").pack()
    sukunimi_entry.pack()
    tk.Label(ikkuna, text="Puhelin:", bg="#d4d0c8", fg="black").pack()
    puhelin_entry.pack()
    tk.Label(ikkuna, text="Sähköposti:", bg="#d4d0c8", fg="black").pack()
    email_entry.pack()

    def tallenna():
        id = id_entry.get().strip()
        etunimi = etunimi_entry.get().strip()
        sukunimi = sukunimi_entry.get().strip()
        puhelin = puhelin_entry.get().strip()
        email = email_entry.get().strip()

        if not id or not etunimi or not sukunimi:
            messagebox.showerror("Virhe", "ID, etunimi ja sukunimi ovat pakollisia kenttiä.")
            return
        
        uudet = f"{id},{etunimi},{sukunimi},{puhelin},{email}\n"

        try:
            with open(TIEDOSTO, "r") as f:
                rivit = f.readlines()
            for i, rivi in enumerate(rivit):
                if rivi.startswith(id + ","):
                    rivit[i] = uudet
                    with open(TIEDOSTO, "w") as f:
                        f.writelines(rivit)
                messagebox.showinfo("Päivitetty", "Yhteystieto päivitetty.")
                ikkuna.destroy()
                return
            messagebox.showerror("Virhe", "ID:tä ei löytynyt.")
        except FileNotFoundError:
            messagebox.showerror("Virhe", "Tiedostoa ei löydy.")

    tk.Button(ikkuna, text="Tallenna muutokset", command=tallenna, bg="#ece9d8", fg="black", activebackground="#316ac5", activeforeground="white", relief="raised", bd=2).pack(pady=10)

# --- POISTA ---
def poista_yhteystieto():
    ikkuna = tk.Toplevel(root)
    ikkuna.title("Poista yhteystieto")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)
    ikkuna.configure(bg="#d4d0c8") 
    ikkuna.transient(root)
    ikkuna.grab_set()

    tk.Label(ikkuna, text="Anna muokattavan ID:", bg="#d4d0c8", fg="black").pack(pady=5)
    id_entry = tk.Entry(ikkuna)
    id_entry.pack()

    tiedot_text = tk.Text(ikkuna, height=5, width=40)
    tiedot_text.pack(pady=10)

    def hae():
        id_input = id_entry.get().strip()
        tiedot_text.delete("1.0", "end")

        if not id_input:
            messagebox.showerror("Virhe", "Anna ID.")
            return

        try:
            with open(TIEDOSTO, "r") as f:
                rivit = f.readlines()

            for rivi in rivit:
                if rivi.startswith(id_input + ","):
                    tiedot_text.insert("1.0", f"Poistettava yhteystieto:\n{rivi}")
                    return
            tiedot_text.insert("1.0", "ID:tä ei löytynyt.")
        except FileNotFoundError:
            tiedot_text.insert("1.0", "Tiedostoa ei löydy.")

    def poista():
        id_input = id_entry.get().strip()
        if not id_input:
            messagebox.showerror("Virhe", "Anna ID.")
            return

        try:
            with open(TIEDOSTO, "r") as f:
                rivit = f.readlines()

            uusi_lista = []
            poistettava_rivi = None

            for rivi in rivit:
                if rivi.startswith(id_input + ","):
                    poistettava_rivi = rivi
                else:
                    uusi_lista.append(rivi)

            if not poistettava_rivi:
                messagebox.showerror("Virhe", "ID:tä ei löytynyt.")
                return

            vastaus = messagebox.askyesno("Vahvista poisto", f"Haluatko varmasti poistaa seuraavan henkilön?\n\n{poistettava_rivi.strip()}")
            if vastaus:
                with open(TIEDOSTO, "w") as f:
                    f.writelines(uusi_lista)
                messagebox.showinfo("Poistettu", "Yhteystieto poistettu onnistuneesti.")
                ikkuna.destroy()
        except FileNotFoundError:
            messagebox.showerror("Virhe", "Tiedostoa ei löydy.")

    tk.Button(ikkuna, text="Hae ID", command=hae).pack(pady=5)
    tk.Button(ikkuna, text="Poista yhteystieto", command=poista).pack(pady=5)

# --- HAE PUUTTEELLISET ---
def hae_puutteelliset_yhteystiedot():
    ikkuna = tk.Toplevel(root)
    ikkuna.title("Puutteelliset yhteystiedot")
    avaa_keskitetty_ikkuna(ikkuna, 400, 400)
    ikkuna.configure(bg="#d4d0c8") 
    ikkuna.transient(root)
    ikkuna.grab_set()

    teksti = tk.Text(ikkuna, bg="#d4d0c8", fg="black")
    teksti.pack(expand=True, fill="both")

    try:
        with open(TIEDOSTO, "r") as f:
            rivit = f.readlines()
            puutteelliset = []
            for rivi in rivit:
                kentat = rivi.strip().split(",")
                if len(kentat) < 5 or any(not k.strip() for k in kentat):
                    puutteelliset.append(rivi.strip())
            if puutteelliset:
                for r in puutteelliset:
                    teksti.insert("end", r + "\n")
            else:
                teksti.insert("1.0", "Ei puutteellisia tietoja.")
    except FileNotFoundError:
        teksti.insert("1.0", "Tiedostoa ei löydy.")

# --- PAINIKEVALIKKO ---
kehys = tk.Frame(root, bg="#d4d0c8")
kehys.pack(padx=10, pady=10, expand=True)

painikkeet = [
    ("Lisää yhteystieto", lisaa_yhteystieto),
    ("Näytä kaikki yhteystiedot", nayta_yhteystiedot),
    ("Hae yhteystieto", hae_yhteystieto),
    ("Muokkaa yhteystietoa", muokkaa_yhteystietoa),
    ("Poista yhteystieto", poista_yhteystieto),
    ("Hae puutteelliset yhteystiedot", hae_puutteelliset_yhteystiedot),
    ("Poistu", root.quit)
]

for teksti, komento in painikkeet:
    tk.Button(
        kehys,
        text=teksti,
        width=30,  # Suurempi leveys
        height=3,  # Suurempi korkeus
        command=komento,
        bg="#ece9d8",  # nappien tausta
        fg="black",  # nappien teksti
        activebackground="#316ac5",  # aktiivinen nappi XP-tyyliin
        activeforeground="white",
        relief="raised",  # antaa 3D-tyylisen napin
        bd=2  # border depth
    ).pack(pady=15, padx=15)  # Napit keskittyvät kehykseen ja niille annetaan tilaa

root.mainloop()