from colorama import Fore, Back, Style
from printing import printslow
from Finali import finale_soldi
from Orologio import orologio
import GlVar
import random

# Percent calculator
def percentuale(num1, num2):
    return ((num1 * num2) / 100)

# minigioco compravendita
def compravendita():
    mio_piatto = []
    keep_hustling = True
    while keep_hustling:
        printslow("Apri marketplace. Chissà quale piatto goloso ci capiterà?", 150, 'testo')
        # selettore di marca
        marca_list = ["Sergio's", "Constantinople", "Constantinople", "Zildjian", "Zildjian", "Zildjian", "Ufip",
                      "Ufip", "Ufip", "Ufip"]
        marca_chooser = random.choice(marca_list)
        marca = {
            # [costo, percentuale di ricarico]
            "Sergio's": [150, 40],
            "Constantinople": [100, 20],
            "Zildjian": [70, 14],
            "Ufip": [40, 7]
        }
        # selettore di condizione
        condizione_list = ["vintage", "nuovo", "nuovo"]
        condizione_chooser = random.choice(condizione_list)
        condizione = {
            "vintage": [100, 20],
            "nuovo": [50, 10]
        }
        # selettore di tipologia
        tipologia_list = ["crash", "charlestone", "ride"]
        tipologia_chooser = random.choice(tipologia_list)
        tipologia = {
            "crash": 30,
            "charlestone": 50,
            "ride": 70
        }
        # generatore di costo + acquisto
        costo = round(marca[marca_chooser][0] + condizione[condizione_chooser][0] + tipologia[tipologia_chooser] + (
                    random.random() * random.randint(2, 10)), 2)
        acquista = (input(
            Fore.MAGENTA + Back.BLACK + f"Ah! un {tipologia_chooser} {marca_chooser} {condizione_chooser} a {costo} euro! Quasi quasi...\n" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + f"Hai {GlVar.soldi} euro, vuoi comprare il piatto? Y o N: ")).lower()
        if acquista == "y":
            if GlVar.soldi < costo:
                printslow("- Mi sa che devo chiedere un prestito a babbo, ma mi ha già dato i soldi per i Radiohead.",
                          120, 'tommy')
                keep_hustling = False
                keep_going = input(
                    Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "continuo?" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + " Y o N: ").lower()
                if keep_going == "y":
                    GlVar.timer += 0.5
                    if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                        GlVar.final = orologio()
                        if GlVar.final == 'a':
                            another_shot = False
                            keep_hustling = False
                            keep_going = False
                            return True
                    printslow(f"Sono le {orologio()}.", 150, 'testo')
                    keep_hustling = True
            else:
                GlVar.soldi = round(GlVar.soldi - costo, 2)
                printslow(f"Ora hai {GlVar.soldi} euro", 150, 'testo')
                mio_piatto.clear()
                mio_piatto.extend([tipologia_chooser, marca_chooser, condizione_chooser])
                # generatore di condizioni di vendita
                another_shot = True
                while another_shot:
                    richiesta_mercato = [random.choice(tipologia_list), random.choice(marca_list),
                                         random.choice(condizione_list)]
                    printslow(f"- Uhm, a quanto pare tutti stanno cercando un "
                              f"\n{richiesta_mercato[0]} {richiesta_mercato[1]} {richiesta_mercato[2]}. \n"
                              f"Forse dovrei vendere il mio "
                              f"\n{mio_piatto[0]} {mio_piatto[1]} {mio_piatto[2]} \n"
                              f"e prendere qualcos'altro, vediamo a quanto posso venderlo!", 300, 'tommy')
                    # calcolatore di prezzo di vendita
                    prezzo_finale = costo + (percentuale(costo, random.randint(-5, 5)))
                    counter = -1
                    # TODO concatena le clause
                    for tipo1 in mio_piatto:
                        counter += 1
                        if tipo1 == richiesta_mercato[counter]:
                            corrispondenza = counter
                            if corrispondenza == 0:
                                prezzo_finale += 10
                            elif corrispondenza == 1:
                                prezzo_finale += (percentuale(costo, marca[marca_chooser][1]))
                            elif corrispondenza == 2:
                                prezzo_finale += (percentuale(costo, condizione[condizione_chooser][1]))
                        prezzo_finale = round(prezzo_finale, 2)
                    vendi = input(
                        Fore.MAGENTA + Back.BLACK + f"- Posso vendere il piatto a {prezzo_finale} euro, che faccio?" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + " \nY = vendi, N = aspetta ").lower()
                    if vendi == "y":
                        GlVar.soldi = round(GlVar.soldi + prezzo_finale, 2)
                        printslow(f"Ora hai {GlVar.soldi} euro", 150, 'testo')
                        x = finale_soldi(GlVar.soldi)
                        if x == 'a':
                            return True
                        GlVar.timer += 0.5
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                another_shot = False
                                keep_hustling = False
                                keep_going = False
                                return True
                        printslow(f"Sono le {orologio()}.", 150, 'testo')
                        another_shot = False
                        ci_ricaschi = input(
                            Fore.MAGENTA + Back.BLACK + "- Magari dò un'altra occhiatina!" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + " Y o N: ").lower()
                        if ci_ricaschi == "y":
                            keep_hustling = True
                        else:
                            printslow("- Ok dai, per oggi basta.\n", 150, 'tommy')
                            keep_hustling = False
                    else:
                        printslow("- Magari riprovo tra poco.\n", 150, 'tommy')
                        printslow("*Mezz'ora dopo...*\n", 100, 'testo')
                        GlVar.timer += 0.5
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                another_shot = False
                                keep_hustling = False
                                keep_going = False
                                return True
                        GlVar.final = orologio()
                        if GlVar.final == 'a':
                            another_shot = False
                            keep_hustling = False
                            keep_going = False
                            return True
                        printslow(f"Sono le {orologio()}.", 150, 'testo')
        else:
            trillionaire_grindset = input(
                Fore.MAGENTA + Back.BLACK + "- Beh, magari potrei cercare un altro bell'affare, ho bisogno di nuovi suoni..." + Fore.YELLOW + Back.BLACK + " Y o N: ").lower()
            if trillionaire_grindset == "y":
                keep_hustling = True
            else:
                printslow("- Ok, per ora basta, magari dò un'occhiata più tardi.", 180, 'tommy')
                keep_hustling = False
