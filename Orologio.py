import GlVar
from Finali import finale_buono, finale_triste, finale_neutro
from printing import printslow
import time

GlVar.timer = 0

def glicemia():
    snacks = ["merendina", "merendina_rara", "estathe"]
    snack_counter = 0
    printslow("Stai avendo un calo di zuccheri, ti devi magnà qualcosa.", 150, 'testo')
    for i in snacks:
        if i in GlVar.oggetti:
            snack_counter += 1
            if i == "merendina_rara":
                GlVar.oggetti.remove("merendina_rara")
                printslow("Assorbi zuccheri e proteine dalla merendina rara. Forza + 1!", 150, 'testo')
                GlVar.forza += 1
                break
            else:
                GlVar.oggetti.remove(i)
                printslow("Assorbi zuccheri dalla merendina.", 150, 'testo')
                break
        else:
            pass
    if snack_counter == 0:
        printslow("Non resisti un secondo di più: svieni salutando la terra con una rullata.", 80,
                  'testo')
        return 'a'

def orologio():
    # orologio
    orario = 8 + GlVar.timer
    mezza = ""
    if int(orario) >= 10 and GlVar.agron_dialogue:
        GlVar.agron_dialogue = False
        printslow("Ti arriva un messaggio, è Agron:", 150, 'testo')
        printslow("Oh Bro auguri!!! Ci vediamo per una birra stasera?", 150, 'agron')
        printslow("Grazie bro, sicuro! Dove?", 150, 'tommy')
        printslow("Vienimi a prendere alle 18 e decidiamo. A stasera bro", 150, 'agron')
        time.sleep(2.0)
    elif 'andrea' in GlVar.party and 'giulio' in GlVar.party and 'agron' in GlVar.party and 'samuel' in GlVar.party and GlVar.timer % 2 == 0:
            return finale_buono()
    elif int(orario) >= 22:
        printslow("Si è fatta una certa.", 150, 'testo')
        if 'andrea' in GlVar.party or 'giulio' in GlVar.party or 'agron' in GlVar.party or 'samuel' in GlVar.party:
            return finale_neutro()
        else:
            return finale_triste()


    if orario % 1 == 0.5:
        mezza = " e mezza"

    # glicemic timer condition
    if orario % 2 == 0 and int(orario) > 8 and not GlVar.glic_count:
        GlVar.glic_count = True
        return glicemia()
    elif orario % 2 == 0 and int(orario) > 8 and GlVar.glic_count:
        GlVar.glic_count = False
        return str(int(orario)) + (mezza)
    return str(int(orario)) + (mezza)

