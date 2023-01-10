from colorama import Fore, Back, Style
import sys, time, random

velocita_testo = input(Fore.YELLOW + Style.BRIGHT + Back.BLACK + "Scegli la velocità del testo a schermo. \n"
                                                                         "Type: 'lento', 'normale' o 'veloce': ").lower()
if velocita_testo == "lento":
    velocita_testo = 0.5
elif velocita_testo == "normale":
    velocita_testo = 1
elif velocita_testo == "veloce":
    velocita_testo = 4
else:
    velocita_testo = 1

lista_personaggi = ['testo', 'tommy', 'giulio', 'samuel', 'agron', 'andrea']
personaggi = {
    "testo": [Fore.WHITE, Style.NORMAL],
    "tommy": [Fore.MAGENTA, Style.BRIGHT],
    "giulio": [Fore.RED, Style.NORMAL],
    "samuel": [Fore.GREEN, Style.NORMAL],
    "agron": [Fore.BLUE, Style.NORMAL],
    "andrea": [Fore.CYAN, Style.NORMAL]
}

def printslow(t, s, p):
    global lista_personaggi
    for pers in lista_personaggi:
        if pers == p:
            for l in t:
                sys.stdout.write(personaggi[p][0] + personaggi[p][1] + Back.BLACK + l)
                sys.stdout.flush()
                time.sleep(random.random() * 10.0 / (s * velocita_testo))
    print()