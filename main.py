# per creare un exe, utilizza il terminal in pycharm e scrivi pyinstaller --onefile main.py (cerca di capire se vale anche se hai più di un file, come in questo caso)
import colorama
from colorama import Fore, Back, Style
import sys, time, random
from art import titolo1, titolo2, titolo3, act1, act1_title, sansprint

colorama.init(autoreset=True)

endings = 0
timer = 0
forza = 0
soldi = 300
final = ''
glic_count = False
samuel_flag = True
agron_dialogue = True
agron_flag = True
cripi_flag = True
dialogo1_andrea = True
dead_andrea = False
party = []
dead_party = []
psi_cosa = ''
oggetti = []
game_over = False
continui = 'y'

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

# for personaggio in lista di personaggi. se personaggio == p: for l in t: sys.stdout.write(personaggi[p][0] + l)

def printslow(t, s, p):
    global lista_personaggi
    for pers in lista_personaggi:
        if pers == p:
            for l in t:
                sys.stdout.write(personaggi[p][0] + personaggi[p][1] + Back.BLACK + l)
                sys.stdout.flush()
                time.sleep(random.random() * 10.0 / (s * velocita_testo))
    print()

def finale_genocide(sans):
    if 'andrea' in sans and 'giulio' in sans and 'agron' in sans and 'samuel' in sans:
        global endings
        endings += 1
        printslow("Birds are singing, flowers are blooming...\n"
                  "On days like these, kids like you...\n"
                  "Should be burning in hell.\n"
                  " \n", 50, 'testo')
        printslow(sansprint, 450, 'testo')
        time.sleep(1.0)
        printslow(f"\nFinale Genocide - Hai sbloccato {endings} finali su 7!", 150, 'testo')
        return 'a'

def finale_soldi(money):
    global endings
    if money >= 1000:
        printslow(f"- Cazzo, ho {money} euro, mi sa che sono pronto a fare l'affare della vita!", 150, 'tommy')
        time.sleep(0.5)
        printslow("Scrolli marketplace sul cellulare con una mano, Reverb sul computer con l'altra.\n"
                  "I tuoi occhi sono indipendenti, sembri un camaleonte.\n"
                  "Dopo un po' di ricerca, lo trovi: Un ride da 80', unico, fatto di una lega di metalli mai vista,\n"
                  "con una campana gigantesca argentea con riflessi azzurri e rossi. \n"
                  "Incredibile, non avevi letteralmente mai visto una roba del genere.", 150, 'testo')
        printslow("- Ok, non ci penso nemmeno un secondo di più, questo è il piatto DELLA VITA.", 200, 'tommy')
        printslow("Noti che il venditore si trova a San Michele. Ma come hai fatto a non averlo notato prima?\n"
                  "Sali in macchina e vai. Pregusti il sustain e il ping che può avere un piatto così grande.\n"
                  "Ti immagini astri e stelle comparire con ogni bacchettata, note profonde e scrosci infiniti di metallo.",
                  150, 'testo')
        printslow("- Porcoddio che figata spaziale ahahahaha", 200, 'tommy')
        time.sleep(1.0)
        printslow(
            "Arrivi nel punto concordato col venditore. Stranamente, è una spiazzo vuoto in cima a una collina. Non c'è nessuno.",
            150, 'testo')
        printslow("- Vabbè aspettiamo un altro po', tanto non ho pagato ancora.", 150, 'tommy')
        printslow("Aspetti altri venti minuti mentre cerchi informazioni sul piatto. Non trovi letteralmente nulla.\n"
                  "Evidentemente è un progetto artigianale.\n"
                  "............\n"
                  "Dopo 30 minuti, decidi di andartene, ormai è chiaro che non verrà nessuno. Stai per salire in macchina quando vieni\n"
                  "assalito da una luce fortissima e un breve rumore, come un l'effetto Doppler.", 150, 'testo')
        printslow("- Ma che cazzo...?", 150, 'tommy')
        printslow("La luce diventa più fioca e finalmente lo vedi: è arrivato il tuo piatto.\n"
                  "Tiri fuori una bacchetta e lo colpisci fortissimo. Invece di una nota, senti però una voce:\n"
                  "- Terrestre, ti ringrazio a nome dell'universo. Accettando il mio invito,\n"
                  "hai fatto sì che io potessi liberarmi dalle maglie elettroniche di internet.\n"
                  "Forse non lo sai, ma il cosmo e internet sono strettamente collegati. Gli 'alieni', come li chiamate voi terrestri,\n"
                  "vivono nel cyberspazio.\n"
                  "Le foto di avvistamenti che ogni tanto sbucano su internet sono in realtà foto segnaletiche:\n"
                  "noi extraterrestri siamo sbadati e dimentichiamo spesso i nostri mezzi, che puntualmente ci vengono sequestrati dalle autorità.",
                  150, 'testo')
        time.sleep(1.0)
        printslow("Sei totalmente sbigottito, ma anche un po' incazzato: in fondo tu ti volevi comprà un piatto, \n"
                  "non conoscere i misteri dell'universo.\n"
                  "Non fai in tempo a lamentarti, che l'alieno ti interrompe:\n"
                  "- Non ti preoccupare terrestre, avrai ciò per cui mi hai contattato.\n"
                  "Solennemente, l'extraterrestre apre il portellone e ti lascia entrare. All'interno trovi\n"
                  "Kendrick Lamar, Thom Yorke, Jimi Hendrix, Mark Guiliana e Sergio.", 150, 'testo')
        time.sleep(1.0)
        printslow("- Ma... Ma... Voi...", 150, 'tommy')
        printslow("- Dass right my nigga, come in. Feel the power of the cosmos.\n"
                  "Kendrick ti ha chiamato 'nigga'. Senti già il ritmo nel sangue ribollire e noti un aumento di 10cm nel pene.\n"
                  "- Come on in, Tommy, let's jam!\n"
                  "Compare un drumkit che mischia vintage e moderno, mesh e sabbiato, piatti e strumenti percussivi di ogni tipo,\n"
                  "gentilmente assemblato da Jones e Guiliana. Ti spari una jam potentissima con Jimi Hendrix.\n", 150,
                  'testo')
        printslow("- Spaziale!!!!!!\n", 60, 'tommy')
        time.sleep(1.5)
        endings += 1
        printslow("Lo ricorderai come il compleanno più bello della tua vita.\n"
                  f"Ending Spaziale - Hai sbloccato {endings} finali su 7!", 150, 'testo')
        return 'a'

# generatore di tasso glicemico
# TODO: check how to connect clauses on Mac
def glicemia():
    global forza
    snacks = ["merendina", "merendina_rara", "estathe"]
    snack_counter = 0
    printslow("Stai avendo un calo di zuccheri, ti devi magnà qualcosa.", 150, 'testo')
    for i in snacks:
        if i in oggetti:
            snack_counter += 1
            if i == "merendina_rara":
                oggetti.remove("merendina_rara")
                printslow("Assorbi zuccheri e proteine dalla merendina rara. Forza + 1!", 150, 'testo')
                forza += 1
                break
            else:
                oggetti.remove(i)
                printslow("Assorbi zuccheri dalla merendina.", 150, 'testo')
                break
        else:
            pass
    if snack_counter == 0:
        printslow("Non resisti un secondo di più: svieni salutando la terra con una rullata.", 80,
                  'testo')
        return 'a'


def finale_triste():
    global endings
    endings += 1
    printslow(
        "Ormai dopo quest'ora non si farà vedere più nessuno. Sei triste, non pensavi che avresti passato il compleanno da solo.\n"
        "Vabbè, per rincuorarti un po', apri marketplace. C'è un messaggio da qualcuno che vuole comprare un tuo piatto:\n"
        "'Salve Tommaso, sono il Signor Panazzi. Sono qui con tutti gli altri per dirti che questo gioco non è una speedrun,\n"
        "quindi prenditi più tempo per esplorarlo meglio. Immaginalo come un Groundhog Day, e che ora potrai ricominciarlo da capo.\n"
        "Mi raccomando, non mollare!'", 150, 'testo')
    printslow(f"Bad Ending - Hai sbloccato {endings} finali su 7!", 150, 'testo')
    return 'a'

def finale_neutro():
    global endings
    endings += 1
    printslow("Decidi di andare coi tuoi amici a prendere una cosa.\n"
              "La serata procede bene, sei felice, ma a un tratto ricevi un messaggio:\n"
              "'Salve Tommaso, sono il Signor Panazzi. Sono qui con tutti gli altri per dirti che questo gioco non è una speedrun,\n"
              "quindi prenditi più tempo per esplorarlo meglio. Immaginalo come un Groundhog Day, e che ora potrai ricominciarlo da capo.\n"
              "Mi raccomando, non mollare!'", 150, 'testo')
    printslow(f"Neutral Ending - Hai sbloccato {endings} finali su 7!", 150, 'testo')
    return 'a'

def finale_buono():
    global endings
    endings += 1
    printslow(
        "Torni a casa per prepararti. Hai percepito che i tuoi amici hanno organizzato qualcosa, ma non hai capito bene cosa.\n"
        "gli indizi che ti hanno dato puntano al centro città, ma non sai di preciso dove. Comunque sia, ti intriga l'idea di\n"
        "risolvere un piccolo enigma.\n"
        "                                            \n"
        "Ti fai bello, ti sciacqui le palle due volte (non si sa mai) e scendi a Fabriano.\n"
        "                                            \n"
        "Arrivato al parcheggione, ti avvii verso il centro (dopo aver scritto un bel 'merdeporcoddio' su una macchina delle Poste)\n"
        "e ti ritrovi in piazza. Vuoi raggiungere i tuoi amici, ma non hai ancora capito dove cazzo siano, e nessuno risponde al telefono.\n"
        "Una merdosissima musica reggaeton ti fa girare lo sguardo. \nLE MACCHINETTE. \n"
        "Stomaco in subbuglio, salivazione tipo cane di Pavlov, flusso sanguigno aumentato, pupille dilatate.\n"
        "                                            \n"
        "Se il glucosio chiama, Tommy risponde. \n"
        "                                            \n"
        "Strabiliato da quei colori sgargianti e dagli involucri sintetici di ottima fattura, sei pronto a perderti nel marasma \n"
        "dell’indecisione davanti a cotanta scelta. \n"
        "Inserisci un euro, vai per il Bounty. La macchinetta dà errore: \n"
        "*** UF1P0K ***", 150, 'testo')
    printslow("- DIO CANISSIMO MA CHE SUCCEDE?!", 200, 'tommy')
    printslow("Hai bisogno di quello snack al cocco. Tenti di nuovo:\n"
              "*** D10C4N8 ***", 150, 'testo')
    printslow("- Non è possibile, che cazzo succede porcodio?!", 200, 'tommy')
    printslow("Sei incazzato a mille, nessuno risponde, vuoi la tua dose, cazzo. \n"
              "\n"
              "RIPETERE PROCEDURA PER CODICE DI SBLOCCO.", 150, 'testo')
    printslow("- È strano, le conosco a memoria e non ho mai visto nulla del genere. Provo ancora:", 150, 'tommy')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** WL4FY64 ***", 100, 'testo')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** K0KK0.0K ***", 100, 'testo')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** CR1ST0700 ***", 100, 'testo')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** FR4NC3S3 ***", 100, 'testo')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** PRCD10 ***", 100, 'testo')
    scelta = input(Fore.YELLOW + Back.BLACK + "Premi un tasto per inserire un codice: ")
    printslow("*** 6FR0C10 ***", 100, 'testo')
    printslow("All’ultimo codice la macchinetta trema, fa versi strani, esce acqua da sotto. \n"
              "È arrapatissima, ma è giusto così, solo tu la tocchi in quel modo, solo tu la guardi con quello sguardo di chi non desidera altro.\n"
              "L’enorme donnona di acciaio scorre fuori dalla sede, e dietro di lei scorgi un tunnel.\n"
              "                                                        \n"
              "Senti della musica, odore di canne e posacenere. Nel corridoio le pareti sono tappezzate di donne nude, \n"
              "ogni tanto capitano anche dei residui di aste della Millenium. La musica si fa più forte, arrivi a una porta.\n"
              "                                                        \n"
              "Inspiegabilmente apri la porta e ti ritrovi a Pusherland.\n"
              "Dentro trovi tutti quanti, c’è in corso una jam extra-galattica, ma nel vero senso della parola! Infatti al basso trovi \n"
              "un extraterrestre, alla batteria Palinuro (Lo Scheletro col Cazzo Duro), alla voce il sig. Panazzi, alla videocamera Kamasi Washington. \n"
              "Nella stanzetta ci sono i tuoi amici che dicono cazzate con Jimi, Kendrick, Elvin Jones e altri mostri della musica.",
              150, 'testo')
    printslow("- MA CHE PORCODDIO SUCCEDE? DIO CARO È SPAZIALE!", 200, 'tommy')
    printslow("- Visto caro Tommaso? Questo è il vero spirito di Pusherland!\n"
              "Annuncia il sig. Panazzi.\n"
              "Oggettivamente è il miglior compleanno della vita, ma non c’è compleanno senza torta.", 150, 'testo')
    scelta_finale = input(Fore.YELLOW + Back.BLACK + "Mangi la torta? 'Y' o 'N': ").lower()
    if scelta_finale == 'y':
        printslow(
            "Ovviamente non puoi rifiutare ulteriore saccarosio, già ti immagini una torta ricoperta di cioccolata al latte. Stai sbavando sulle scarpe di Andrea.\n"
            "Arriva il sig. Panazzi, leader indiscusso del mondo conosciuto. Porta una torta gigante davanti ai tuoi occhi.\n"
            "Prendi una fetta, STAMBURELLI IMPAZIENTE CON IL CUCCHIAINO, poi finalmente assaggi questa primizia cremosa.\n"
            "                                                   ", 150, 'testo')
        printslow("CIOCCOLATO FONDENTE", 30, 'testo')
        printslow(
            "Panazzi ha sbagliato, l’ha presa fondente. I muscoli del tuo viso si contraggono, smorfie mai viste. \n"
            "Le tue labbra si contorcono, stanno entrando dentro la bocca. \n"
            "Vieni completamente risucchiato all’interno di te stesso, ti trovi in un liquido arancione, senti l’odore dell’Estathè. \n"
            "SEI ALL’INTERNO DEL TUO GLUCOSIO!\n"
            "Non capisci assolutamente cosa cazzo stia succedendo, sei incazzato come una bestia per il fatto che qualche bastardo al mondo abbia inventato il gusto amaro. \n"
            "La tua potenza zuccherina sta disciogliendo tutti gli esseri viventi.", 150, 'testo')
        printslow("- TUTTI ZUCCHERO CAZZOOOOO! TUTTI ZUCCHEROOOOOOOO! \n"
                  "PERCHÉ NON VOLETE MANGIARE SOLO ROBA DOLCE? PERCHÉ NESSUNO MI CAPISCE? PERCHÉ VI PRENDETE GIOCO DI ME? AMARI MERDOSI!",
                  200, 'tommy')
        printslow("Sei completamente impazzito. Il mondo ormai è glucosio puro.\n"
                  "Dopo aver devastato l’umanità con la tua furia e aver reso tutto dolce, ti senti disgustato. \n"
                  "Senti la necessità di aria, senti qualcosa che non va.\n"
                  "                                                   \n"
                  "Miracolosamente appare una figura celestiale, stupenda. Carnagione candida e ali immense, percepisci l’armonia dei suoi meravigliosi movimenti. \n"
                  "È il sig. Ferrero, proprietario della omonima azienda, nonché padre dell’Estathè.", 150, 'testo')
        printslow("- Sig. Ferrero, dove siamo?", 150, 'tommy')
        printslow("-Questo è il mare di glucosio amico mio, siamo immersi nel brodo primordiale dello zucchero. \n"
                  "Un mondo dove non occorre più nessun altro gusto, dove ogni essere vivente è diventato un dolce. \n"
                  "Un mondo ambiguo, che non consente di percepire il confine materiale. \n"
                  "Questo è il mondo che hai desiderato, compiendo una libera scelta.", 150, 'testo')
        printslow("- Non lo so, non sono affatto sicuro...", 100, 'tommy')
        printslow(
            "- Se vuoi recuperare l’esistenza degli uomini dotati di altri gusti lo puoi fare, ma così nel mondo tornerebbe l’amaro e il sapido.",
            150, 'testo')
        printslow("Appoggi la testa sulle mani, poi dici tra te e te:", 150, 'testo')
        printslow("- Un mondo di dolcezza in cui non c'è più l'amaro.\n"
                  "Tuttavia, ho rincorso per anni questa dolcezza, ma non ho trovato altro che disgusto.", 100, 'tommy')
        time.sleep(1.0)
        printslow(
            "Decidi di fare un passo indietro, nonostante sai benissimo che qualcuno prima o poi ti tirerà un colpo basso. \n"
            "Riassorbi il glucosio primordiale all’interno di te stesso, le cose riprendono forma. Resusciti uscendo dalla tua bocca.",
            150, 'testo')
        time.sleep(1.0)
        printslow(
            "Ti ritrovi di nuovo a Pusherland, tutti gli amici con cui erano ti applaudono facendo i complimenti:", 150,
            'testo')
        printslow("- Congratulazioni!", 150, 'agron')
        printslow("- Congratulazioni!", 150, 'testo')
        printslow("- Congratulazioni!", 150, 'giulio')
        printslow("- Congratulazioni!", 150, 'andrea')
        printslow("- Congratulazioni!", 150, 'testo')
        printslow("- Congratulazioni!", 150, 'samuel')
        printslow("- Congratulazioni!", 150, 'testo')
        printslow("BRAVO TOMMY, FINALMENTE HAI IL SENSO DEL GUSTO DI UN ADULTO!\n"
                  "Ti fai coraggio, ti chini sopra la torta amara che è sul tavolo. La prendi con entrambe le mani. La mangi:",
                  150, 'testo')
        printslow("- CHE SCHIFO", 30, 'tommy')
        time.sleep(2.0)
        printslow(f"Good Ending - Hai sbloccato {endings} finali su 7!", 150, 'testo')
        return 'a'
    else:
        printslow("Sei troppo carico e quindi decidi di non mangiare la torta perché vuoi assolutamente suonare. \n"
                  "Il sig. Panazzi cerca di convincerti, ma tu persisti e non vuoi mangiare. \n"
                  "Il sig. Panazzi diventa paonazzo, tira fuori il cazzo e inizia a volare. \n"
                  "Bestemmia tutte le divinità dello scibile umano e uccide tutti i tuoi amici davanti ai tuoi occhi.",
                  150, 'testo')
        return 'a'

# in-game timer
def orologio():
    global timer
    global agron_dialogue
    global party
    global glic_count
    # orologio
    orario = 8 + (timer)
    mezza = ""
    if int(orario) >= 10 and agron_dialogue:
        agron_dialogue = False
        printslow("Ti arriva un messaggio, è Agron:", 150, 'testo')
        printslow("Oh Bro auguri!!! Ci vediamo per una birra stasera?", 150, 'agron')
        printslow("Grazie bro, sicuro! Dove?", 150, 'tommy')
        printslow("Vienimi a prendere alle 18 e decidiamo. A stasera bro", 150, 'agron')
        time.sleep(2.0)
    elif int(orario) >= 22:
        printslow("Si è fatta una certa.", 150, 'testo')
        if 'andrea' in party and 'giulio' in party and 'agron' in party and 'samuel' in party:
            return finale_buono()
        elif 'andrea' in party or 'giulio' in party or 'agron' in party or 'samuel' in party:
            return finale_neutro()
        else:
            return finale_triste()


    if orario % 1 == 0.5:
        mezza = " e mezza"

    # glicemic timer condition
    if orario % 2 == 0 and int(orario) > 8 and not glic_count:
        glic_count = True
        return glicemia()
    elif orario % 2 == 0 and int(orario) > 8 and glic_count:
        glic_count = False
        return str(int(orario)) + (mezza)
    return str(int(orario)) + (mezza)

# merendine-hoarder
def merendare():
    global oggetti
    porco = True
    while porco:
        merendinas = input(Fore.YELLOW + Back.BLACK + "Vuoi prendere un'altra merendina per dopo? 'Y' o 'N': ").lower()
        if merendinas == 'y':
            oggetti.append("merendina")
            printslow("Meglio prenderne una di riserva.", 150, 'tommy')
        else:
            printslow("Ok, basta, forse sto esagerando.", 150, 'tommy')
            porco = False

# GDR
def RPG(mod_forza):
    global oggetti
    global timer
    global party
    global dead_party
    printslow("Lo schermo, ondulante in un mélange di tinte acide, ti dà il benvenuto:", 150, 'testo')
    game_over_rpg = False
    while not game_over_rpg:
        global samuel_flag
        max_hp = 30 + (mod_forza * 3)
        current_hp_tommy = max_hp

        def cura(maxhp, currenthp):
            currenthp += int(maxhp / 4)
            if currenthp > maxhp:
                currenthp = maxhp
            return currenthp

        nome_giocatore = input(
            Fore.YELLOW + Style.BRIGHT + Back.BLACK + "Come ti chiami, eroe dell'occidente?: ").title()
        printslow(
            f"Aaaah, {nome_giocatore}, interessante. Come forse avrai capito, c'è un motivo per cui di questo synth ci sono solo 10 esemplari:\n"
            "ogniqualvolta c'è stata un'interruzione di corrente o un corto (in Polonia capitava spesso), chiunque stesse utilizzando il synth\n"
            "ne veniva istantaneamente assorbito. I maligni spiriti che lo dominano sono troppo potenti, e solo chi è versato nell'antica arte del\n"
            "'grać w gry wideo' può liberarsi. Purtroppo, nessuno per ora ci è riuscito.", 200, 'testo')
        time.sleep(0.5)
        timer += 0.5
        printslow(f"{nome_giocatore}, è tutto nelle tue mani!", 150, 'testo')
        time.sleep(0.5)
        printslow(f"Preparati a combattere contro questi abomini!", 150, 'testo')
        time.sleep(1.0)
        # action #
        nemici = {
            "Palinuro": [40, 3, 2, True, 'Osso Duro'],
            "Kamasi Washington": [80, 2, 3, True, 'Strombazzata! \nPEPEPEPEPEPEPEP-PIIIIIIIIII'],
            "Il Signor Panazzi": [70, 5, 4, True, 'Quattro Pollici in Culo']
        }
        palinuro_death = False
        extra_danno = 0
        nemici_list = ["Palinuro", "Kamasi Washington", "Il Signor Panazzi"]

        for nemico in nemici_list:
            if not palinuro_death:
                if current_hp_tommy > 0:
                    current_hp_nemico = nemici[nemico][0]
                    if nemico == "Palinuro":
                        printslow(
                            "Dalle viscere siliconiche del synth, esce fuori Palinuro, Lo Scheletro col Cazzo Duro!\n"
                            "'SKREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE\n"
                            f"'Combatti, {nome_giocatore}, o perisci,\n"
                            f"'Oppure prendilo nel culo, come preferisci!'", 150, 'testo')
                    elif nemico == "Kamasi Washington":
                        printslow(
                            "Se Palinuro era lo scheletro essiccato del synth, da qualche parte i generatori di suono \n"
                            "dovrebbero essere ancora in funzione...", 150, 'testo')
                        time.sleep(0.3)
                        printslow("Mentre ragioni, senti dei passi pesanti avvicinarsi.", 150, 'testo')
                        print("THUMP")
                        time.sleep(1.0)
                        print("THUMP")
                        time.sleep(1.0)
                        print("THUMP")
                        time.sleep(1.0)
                        printslow("Un agghiacciante barrito stride nell'aria.", 150, 'testo')
                        printslow("........", 30, 'testo')
                        printslow(f"'{nome_giocatore}, this is your time. Time to behold the power of music!'", 150,
                                  'testo')
                        time.sleep(1.0)
                        printslow("Kamasi Washington è arrivato a farti il culo!", 150, 'testo')
                    elif nemico == "Il Signor Panazzi":
                        time.sleep(1.0)
                        printslow("L'aria è gravida di silenzio. Un silenzio teso, elettrico.", 150, 'testo')
                        time.sleep(1.0)
                        printslow("Ti accingi ad andartene, quando a un tratto, una voce riempie il vuoto:", 150,
                                  'testo')
                        printslow("'Cosa credevi? Che i synth si costruissero da soli?'", 100, 'testo')
                        printslow("Ti giri: Il Signor Panazzi si staglia nell'orizzonte di catrame e cavi.", 150,
                                  'testo')
                        printslow(f"'Caro il mio {nome_giocatore}, sei arrivato lontano. I miei complimenti.'", 100,
                                  'testo')
                        printslow(
                            "Applaudendo lentamente, Il Signor Panazzi avanza. Puoi sentire da lontano il malvagio lezzo di mortadella che emana.",
                            150, 'testo')
                        printslow(
                            "'La tua ora è arrivata. Non guardare indietro, in questo mondo non c'è più nulla che sia tuo.'\n"
                            "'Con questo synth, evaderò dalla prigione spazio-temporale in cui mi trovo e finalmente trasformerò \n"
                            "l'universo nella mia personale tavola calda. Combatti, ora!'", 100, 'testo')
                    while nemici[nemico][3] and not game_over_rpg:
                        turno_tommy = input(Fore.YELLOW + Style.BRIGHT + Back.BLACK + "Cosa vuoi fare? \n"
                                                                                      "Type 'A' per attaccare,\n"
                                                                                      "Type 'M' per fare una magia,\n"
                                                                                      "Type 'S' per consumare uno snack,\n"
                                                                                      "Type 'F' per risparmiare il nemico: ").lower()
                        if turno_tommy == 'f' and nemico == 'Palinuro':
                            printslow("Lasci andare Palinuro.\n"
                                      "Lui ti guarda sbigottito, poi esclama:\n"
                                      "'Nessuno mi aveva mai lasciato andare.'\n"
                                      "'Tutti dicono Palinuro è cattivo, Palinuro fa paura, non voglio andare da Palinuro...'",
                                      100, 'testo')
                            printslow("'.........", 50, 'testo')
                            printslow("...E fanno bene, perché sono una merda!'", 200, 'testo')
                            printslow("Palinuro ti uccide con un colpo.", 150, 'testo')
                            palinuro_death = True
                            current_hp_tommy = 0
                            game_over_rpg = True
                        elif turno_tommy == 'f' and nemico == 'Kamasi Washington':
                            if current_hp_nemico <= 20:
                                printslow("'Now I see. You're the hero of light. You're my personal saviour.\n"
                                          "Thanks for sparing me, I will make the world a better place.\n"
                                          f"See you jazz cowboy!'", 150, 'testo')
                                time.sleep(0.5)
                                current_hp_tommy = cura(max_hp, current_hp_tommy)
                                printslow(f"Recuperi HP dopo la battaglia. Ora sei a {current_hp_tommy} HP", 150,
                                          'testo')
                                printslow(f"Sei salito di livello! Danno + 1", 150, 'testo')
                                extra_danno += 1
                                nemici[nemico][3] = False
                            else:
                                printslow("'The music in me is not ready to give up yet.'", 150, 'testo')
                        elif turno_tommy == 'f' and nemico == 'Il Signor Panazzi':
                            printslow("Io sono la fine e l'inizio. Io sono il pandoro che mangia se stesso. \n"
                                      "Non puoi sconfiggermi, puoi solo guardarmi mentre farcisco il mondo come un panino!",
                                      150, 'testo')
                        elif turno_tommy == 's':
                            if 'merendina' in oggetti:
                                printslow("Mangi una merendina. Recuperi 20HP!", 150, 'testo')
                                current_hp_tommy += 20
                                oggetti.remove('merendina')
                            elif 'estathe' in oggetti:
                                printslow("Bevi un estathe. Recuperi 20HP!", 150, 'testo')
                                current_hp_tommy += 20
                                oggetti.remove('estathe')
                            elif 'merendina_rara' in oggetti:
                                printslow("Mangi uno Scrofix. Yum! Recuperi 30HP e ti senti fortissimo!", 150, 'testo')
                                current_hp_tommy += 30
                                forza += 1
                                oggetti.remove('merendina_rara')
                            else:
                                printslow("Non hai snack da consumare.", 150, 'testo')
                        elif turno_tommy == 'm':
                            if psi_cosa in oggetti:
                                if nemico == 'Il Signor Panazzi':
                                    printslow(f"'{psi_cosa} non ha nessun potere su di me!'", 150, 'testo')
                                else:
                                    printslow(f"Evochi il potere della magia {psi_cosa}!\n"
                                              "****SDRSHH!****\n"
                                              f"{nemico} è sconfitto!", 150, 'testo')
                                    oggetti.remove(psi_cosa)
                                    current_hp_tommy = cura(max_hp, current_hp_tommy)
                                    printslow(f"Recuperi HP dopo la battaglia. Ora sei a {current_hp_tommy} HP", 150,
                                              'testo')
                                    printslow(f"Sei salito di livello! Danno + 1", 150, 'testo')
                                    extra_danno += 1
                                    nemici[nemico][3] = False
                            else:
                                printslow("Non conosci nessuna magia.", 150, 'testo')
                        else:
                            # attacco
                            danno = mod_forza + int(round((random.random() * 5), 2)) + extra_danno
                            current_hp_nemico -= danno
                            printslow(f"Attacchi {nemico} con tutta la tua forza.\n"
                                      f"Fai {danno} danni a {nemico}!", 150, 'testo')
                            if current_hp_nemico <= 0:
                                printslow(f"Hai sconfitto {nemico}!", 150, 'testo')
                                current_hp_tommy = cura(max_hp, current_hp_tommy)
                                printslow(f"Recuperi HP dopo la battaglia. Ora sei a {current_hp_tommy} HP", 150,
                                          'testo')
                                time.sleep(0.5)
                                printslow(f"Sei salito di livello! Danno + 1", 150, 'testo')
                                extra_danno += 1
                                nemici[nemico][3] = False
                                if nemico == "Il Signor Panazzi":
                                    # vedi se funziona cosi
                                    printslow("'Nooooooo, non può finire così!'", 80, 'testo')
                                    printslow("Le urla elettroniche del Signor Panazzi ti trapanano i timpani.", 150,
                                              'testo')
                                    time.sleep(0.5)
                                    printslow(
                                        f"{nome_giocatore}, siamo i musicisti intrappolati nel synth: Tomek, Wiesław, Zbigniew, Małgorzata e Mela.\n"
                                        "Le tue gesta sono state eroiche, e il giogo del Signor Panazzi è finalmente concluso. Ci hai liberato.\n"
                                        "Nonostante ciò, sappiamo bene che chi vorresti avere indietro non è nessuno di noi, ma il tuo amico Boldrinskyi.\n"
                                        "Per cui, eccolo qua. Noi invece continueremo a sviluppare questo synth, facendo in modo che un giorno possa portare gioia e rivoluzione.\n"
                                        "Do Zobaczenia!", 150, 'testo')
                                    time.sleep(0.5)
                                    print("SWOOOOOOOSH")
                                    time.sleep(0.5)
                                    printslow(
                                        "Con il lampo con cui tutto è iniziato, Il synth emette una fumata e ricompare Samuel.",
                                        150, 'testo')
                                    printslow("- Sa! Dio caro ma dove cazzo eri finito? m'è preso un colpo!", 150,
                                              'tommy')
                                    printslow(
                                        "- Tommy porcoddio sono finito in una pozza calda d'estathè dentro il synth, ti dice niente???",
                                        150, 'samuel')
                                    printslow("Samuel vuole fartela pagare. Ti seguirà per il resto della giornata.\n"
                                              "Samuel si unisce al party!", 150, 'testo')
                                    party.append('samuel')
                                    samuel_flag = False
                                    return samuel_flag
                                    game_over_rpg = True
                        if nemici[nemico][3] and not palinuro_death:
                            # i nemici potrebbero utilizzare sempre lo stesso calcolo per le azioni, cambiando solo l'effetto delle mosse #
                            time.sleep(0.5)
                            printslow(f"Tocca a {nemico}!", 150, 'testo')
                            time.sleep(0.5)
                            azione_nemico = ["attacco", "attacco", "attacco", "attacco", "special"]
                            turno_nemico = random.choice(azione_nemico)
                            if turno_nemico == "special":
                                if current_hp_nemico <= int(nemici[nemico][0] / 4):
                                    printslow(f"{nemico} usa il suo special, *{nemici[nemico][4]}*!", 150, 'testo')
                                    danno_nemico = (nemici[nemico][1] + int(round((random.random() * 5), 2))) * \
                                                   nemici[nemico][2]
                                    printslow(f"{nome_giocatore} riceve {danno_nemico} danni!", 150, 'testo')
                                    current_hp_tommy -= danno_nemico
                                    printslow(f"Ti sono rimasti {current_hp_tommy} HP", 150, 'testo')
                                else:
                                    printslow(f"{nemico} ti attacca!", 150, 'testo')
                                    danno_nemico = nemici[nemico][1] + int(round((random.random() * 5), 2))
                                    printslow(f"{nome_giocatore} riceve {danno_nemico} danni!", 150, 'testo')
                                    current_hp_tommy -= danno_nemico
                                    printslow(f"Ti sono rimasti {current_hp_tommy} HP", 150, 'testo')
                            else:
                                printslow(f"{nemico} ti attacca!", 150, 'testo')
                                danno_nemico = nemici[nemico][1] + int(round((random.random() * 5), 2))
                                printslow(f"{nome_giocatore} riceve {danno_nemico} danni!", 150, 'testo')
                                current_hp_tommy -= danno_nemico
                                printslow(f"Ti sono rimasti {current_hp_tommy} HP", 150, 'testo')
                            if current_hp_tommy <= 0:
                                printslow(f"Colpo fatale! {nome_giocatore} è stato sconfitto!", 150, 'testo')
                                game_over_rpg = True
        if current_hp_tommy <= 0:
            printslow("Game Over.", 40, 'testo')
            riprova = input(Fore.YELLOW + Style.BRIGHT + Back.BLACK + "Vuoi riprovare? 'Y' o 'N': ").lower()
            if riprova == 'y' and palinuro_death:
                palinuro_death = False
                time.sleep(1.0)
                game_over_rpg = False
            elif riprova == 'y':
                time.sleep(1.0)
                game_over_rpg = False
            else:
                samuel_flag = False
                printslow(
                    "Decidi di lasciare Samuel nel synth. In fondo avrebbe voluto andarsene così, tra musica e amici.",
                    150, 'testo')
                printslow("- Vabbè io ci ho provato. Ovviamente il videogioco da cui devo liberare Samuel\n"
                          "è a cazzo di difficoltà hardcore, porcoddio.", 150, 'tommy')
                printslow(f"Esci da casa di Samuel.", 150, 'testo')
                dead_party.append('samuel')
                s = finale_genocide(dead_party)
                if s == 'a':
                    return 'a'
                time.sleep(1.0)
                return samuel_flag

# Percent calculator
def percentuale(num1, num2):
    return ((num1 * num2) / 100)

# minigioco compravendita
def compravendita():
    mio_piatto = []
    keep_hustling = True
    while keep_hustling:
        global final
        global soldi
        global timer
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
            Fore.MAGENTA + Back.BLACK + f"Ah! un {tipologia_chooser} {marca_chooser} {condizione_chooser} a {costo} euro! Quasi quasi...\n" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + f"Hai {soldi} euro, vuoi comprare il piatto? Y o N: ")).lower()
        if acquista == "y":
            if soldi < costo:
                printslow("- Mi sa che devo chiedere un prestito a babbo, ma mi ha già dato i soldi per i Radiohead.",
                          120, 'tommy')
                keep_hustling = False
                keep_going = input(
                    Fore.MAGENTA + Style.BRIGHT + Back.BLACK + "continuo?" + Fore.YELLOW + Style.BRIGHT + Back.BLACK + " Y o N: ").lower()
                if keep_going == "y":
                    timer += 0.5
                    if timer % 2 == 0 and int(timer) >= 2:
                        final = orologio()
                        if final == 'a':
                            another_shot = False
                            keep_hustling = False
                            keep_going = False
                            return True
                    printslow(f"Sono le {orologio()}.", 150, 'testo')
                    keep_hustling = True
            else:
                soldi = round(soldi - costo, 2)
                printslow(f"Ora hai {soldi} euro", 150, 'testo')
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
                        soldi = round(soldi + prezzo_finale, 2)
                        printslow(f"Ora hai {soldi} euro", 150, 'testo')
                        x = finale_soldi(soldi)
                        if x == 'a':
                            return True
                        timer += 0.5
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
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
                        timer += 0.5
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
                                another_shot = False
                                keep_hustling = False
                                keep_going = False
                                return True
                        final = orologio()
                        if final == 'a':
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

while not game_over:
    timer = 0
    forza = 0
    soldi = 300
    final = ''
    glic_count = False
    samuel_flag = True
    agron_dialogue = True
    agron_flag = True
    cripi_flag = True
    dialogo1_andrea = True
    dead_andrea = False
    party = []
    dead_party = []
    psi_cosa = ''
    oggetti = []
    game_over = False
    continui = 'y'
    while continui == 'y':
        salta_intro = input(Fore.YELLOW + Style.BRIGHT + Back.BLACK + "salta intro? 'y' o 'n': ").lower()
        if salta_intro == 'n':
          printslow(titolo1, 450, 'testo')
          printslow(titolo2, 600, 'testo')
          printslow(titolo3, 600, 'testo')
          # ACT 1 - Risveglio
          printslow("\nSono le 8. Questa storia inizia nel centro Italia.", 50, 'testo')
          printslow("\nNelle Marche, morbida regione lambita da monti e mare, oggi è una splendida giornata. \n"
                    "In particolare, c'è un bel sole a Collepaganello, frazioncina di Fabriano a 475mt. s.l.m. \n"
                    "Gli uccellini cinguettano, i primi odori della primavera volteggiano nell'aria. \n"
                    "Il camion della monnezza si ferma per il suo consueto giro. Uno dei netturbini biascica un 'porcoddio' mentre apre un bidone. \n"
                    "Il dolce suono di quella voce catarrosa sveglia Tommy, che stiracchiandosi pensa:", 150, 'testo')
        ##############################################
        ######## COMMMENT DA QUA PER TESTARE #########
        ##############################################
        part_end = False
        orologio()
        printslow(f"- Aaaaah, che bella dormita! \n- Cazzo ma sono le 8, ho un botto di tempo oggi! Quasi quasi...", 80, 'tommy')
        choice1 = input(Fore.YELLOW + Back.BLACK + "Type 'c' per fare colazione, type 'm' per masturbarti: ").lower()
        if choice1 == "m":
            timer += 0.5
            forza += 1
            printslow("- Quasi quasi mi sparo una sega!\nVediamo un po'...", 100, 'tommy')
            printslow("-Pornhub-", 80, 'testo')
            printslow("'Colate di sborra'", 80, 'testo')
            printslow("'Sborra su broccoli'", 80, 'testo')
            printslow("'Bounty ripieni di sborra'", 80, 'testo')
            printslow("'A E S T H E T I C - F U C K'", 80, 'testo')
            printslow("'Lesbian Twix'", 120, 'testo')
            printslow("'Elvin Jones rapes a drumkit'", 80, 'testo')
            printslow("'Mark Guiliana senza mutande'", 80, 'testo')
            printslow("\n- S-S-S-\n", 50, 'tommy')
            printslow("- SBORROOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO", 120, 'tommy')
            printslow("\n     ", 50, 'testo')
            printslow("Ti senti rinvigorito. Forza + 1", 200, 'testo')
            printslow(f"{orologio()}", 150, 'testo')
        printslow("- Sono pronto per la colazione.", 200, 'tommy')
        printslow("Ti incammini verso la cucina. Nell'altra stanza, Filippo dorme.", 150, 'testo')
        printslow("'Il mio bro :)'", 150, 'tommy')
        printslow("pensi, mentre tendi la mano come a volerlo accarezzare.\n"
                  "Al piano di sotto non c'è nessuno. Sul tavolo, attorniata da merendine di varie fogge e colori, c'è la moka pronta col caffè. Dici tra te e te: ", 150, 'testo')
        printslow("- No, il caffè è troppo amaro per la mia baby-bocca.", 150, 'tommy')
        printslow("Stai per prendere la tua merendina preferita, l'Orcociok, quando pensi: ", 150, 'testo')
        printslow("Oggi compio 26 anni, forse è il momento di darci un taglio con questa merda.", 150, 'tommy')
        choice2 = input(Fore.YELLOW + Back.BLACK + "Type 'm' se vuoi comunque mangiare la merendina, \nType 's' se vuoi chiamare Samuel: ").lower()
        if choice2 == "s":
          timer += 0.5
          forza += 1
          printslow("- Sì, da oggi si cambia, mo chiamo Samuel e mi faccio consigliare una colazione sana.", 130, 'tommy')
          printslow("*il telefono s q u i l l a*", 80, 'testo')
          printslow("-      ", 30, 'samuel')
          printslow("- Pronto.", 80, 'samuel')
          printslow("- Sam sono Tommaso, ti ho svegliato?", 130, 'tommy')
          printslow("-   ", 30, 'samuel')
          printslow("- No. Dimmi.", 100, 'samuel')
          printslow("- Ti dò una buona notizia: ti ho chiamato perché vorrei che mi consigliassi una colazione sana!", 130, 'tommy')
          printslow("- Oh Madonna Tommy, questa sì che è una notizia! Come mai questo cambio repentino? Hai sognato di nuovo che studiare jazz ti faceva scopare?", 130, 'samuel')
          printslow("- ahah no, COGLIONE, oggi è il mio compleanno e volevo cambiare un po' le mie abitudini. Dai aiutami.", 130, 'tommy')
          printslow("- Mi hai ninjato sugli auguri! Buon compleanno Tommasiello. Va bene, ti aiuto.", 130, 'samuel')
          printslow("- Grazie! Dai, spara.", 130, 'tommy')
          printslow("- Ok, il mio consiglio per una colazione sana è prendere quello che mangi di solito e-", 130, 'samuel')
          printslow("- Ma come? Volevo fare qualcosa di nuovo!", 200, 'tommy')
          printslow("- Lasciami finire. Devi prendere quello che mangi di solito ma mangiarlo in una maniera diversa. Di solito come la fai colazione?", 130, 'samuel')
          printslow("- Mah, seduto, mangio una merendina sorseggiando un estathè.", 130, 'tommy')
          printslow("- Ok, oggi la farai in piedi, merendando una mangina e estatheando un sorsè. Tutto chiaro?", 130, 'samuel')
          printslow("- Ma che vuol dire? come si fa a estatheare un s-", 130, 'tommy')
          printslow("- Bene, ciao Tommy torno a dormire.", 200, 'samuel')
          printslow("*tuuu-tuuu-tuuu*", 30, 'testo')
          printslow("- Ma che cazzo...", 100, 'tommy')
          printslow("\nProvi a merendare la mangina e a estatheare il sorsè.\n", 130, 'testo')
          printslow("........\n", 40, 'testo')
          printslow("Ti sbrodoli tutto ma ti senti rinvigorito. Forza + 1", 180, 'testo')
          printslow(f"Sono le {orologio()}.", 150, 'testo')
        else:
          printslow("- Ma chi prendo in giro? Sono o non sono il king degli snack?", 150, 'tommy')
          printslow("Ingurgiti l'Orcociok e reciti la pubblicità:\n", 130, 'testo')
          printslow("'Orcociok,\nOrcociok\nOrco-Dio che buono-ciok!'\n", 100, 'tommy')

        merendare()

        printslow("Corroborato dagli zuccheri, sei pronto a iniziare la giornata. Guardi il telefono.", 150, 'testo')
        printslow("- Potrei dare un'occhiata al marketplace, magari trovo un'offerta.", 150, 'tommy')
        offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi aprire marketplace? 'Y' o 'N': ").lower()
        if offerte == 'y':
          s = compravendita()
          if s:
              game_over = True
              continui = 'n'
              continue
        else:
          printslow("- Magari dopo.\n", 150, 'tommy')

        # ACT 2 - Hub Collepaganello
        # printslow(act1, 900, 'testo')
        # printslow(act1_title, 1600, 'testo')
        collepaganello = True
        fine_giulio = '0'
        while collepaganello:
          printslow("Sei indeciso sul da farsi, la giornata sembra gravida di possibilità.", 150, 'testo')
          hub1 = input(Fore.YELLOW + Back.BLACK + "Type: \n"
                                                  "'G' se vuoi andare da Giulio, \n"
                                                  "'F' se vuoi scendere a Fabriano,\n"
                                                  "'B' se vuoi andare da nonno a suonare la batteria, \n"
                                                  "'C' se vuoi restare a casa: ").lower()
          ############# Giulio's route ###############
          if hub1 == 'g':
            if timer >= 2 and fine_giulio == '0':
              printslow("Giulio è già andato al lavoro.", 150, 'testo')
            else:
              if fine_giulio == '1':
                printslow("Sono già andato da Givil.", 150, 'tommy')
              elif fine_giulio == '2':
                printslow("Giulio è già con me.", 150, 'tommy')
              else:
                printslow("- Vediamo che fa il vecchio Givil.", 150, 'tommy')
                siga = input(Fore.MAGENTA + Back.BLACK + "Mi porto le sigarette?" + Fore.YELLOW + Back.BLACK + " 'Y' o 'N': ").lower()
                if siga == 'y':
                  oggetti.append("sigarette")
                else:
                  printslow("- Facciamo senza, oggi mi sento frizzante!", 150, 'tommy')
                printslow("Ti incammini verso casa di Giulio. \nLa giornata è così entusiasmante che ti metti a tamburellare in aria e ti fai i complimenti da solo per come stai tenendo il groove.\nSei carico a pallettoni. Dopo la terza air-rullata e la quindicesima roteazione cammellare della lingua, sei davanti casa di Giulio.", 150, 'testo')
                porta = input(Fore.YELLOW + Back.BLACK + "Vuoi suonare il campanello? 'Y' o 'N': ").lower()
                if porta == 'y':
                  printslow("Suoni il campanello. \nMafalda abbaia spaventata.", 150, 'testo')
                  printslow("- Oh ma', e apri porcoddio", 150, 'giulio')
                  printslow("senti berciare. Caro vecchio Giulio, prima o poi così l'ammazzerai a Mara!\nSenti Giulio avvicinarsi: ", 150, 'testo')
                  printslow("- Porcoddio manco la porta sa aprì.", 150, 'giulio')
                  printslow("Appena apre la porta, è stupito di vederti: ", 150, 'testo')
                  printslow("- Oh Bombo! auguri! Ma che ci fai qui a quest'ora? Mi stavo preparando per il lavoro.", 150, 'giulio')
                  printslow("- Ma niente, sono uscito e ho detto 'mo vado a rompere le palle a Givil'. Sei di fretta?", 150, 'tommy')
                  printslow("- Eh, mi sto preparando perché entro le dieci vorrei partire", 150, 'giulio')
                else:
                  printslow("Decidi di non suonare. Dopo poco, senti Giulio bestemmiare e ti prepari a fargli una sorpresa. \nAppena apre la porta di casa, gli urli un 'Woo! Uigaraaa, uiuoouu'.", 150, 'testo')
                  printslow("- Porcoddio Tommà ma sei scemo? M'hai fatto prende un colpo!", 150, 'giulio')
                  printslow("Ridi sguaiatamente. Prima o poi così l'ammazzerai, a Giulio!", 150, 'testo')
                  printslow("- Oh Bombo! auguri! Ma che ci fai qui a quest'ora? Mi stavo preparando per il lavoro.", 150, 'giulio')
                  printslow("- Ma niente, sono uscito e ho detto 'mo vado a rompere le palle a Givil'. Sei di fretta?", 150, 'tommy')
                  printslow("- Eh, mi sto preparando perché entro le dieci vorrei partire", 150, 'giulio')
                if 'sigarette' in oggetti:
                  offri = input(Fore.MAGENTA + Back.BLACK + "Giulio è di fretta, magari si rilasserà se facciamo due chiacchiere con una sigaretta." + Fore.YELLOW + Back.BLACK + " \nOffri una sigaretta? 'Y' o 'N': ").lower()
                  if offri == 'y':
                    timer += 0.5
                    oggetti.remove('sigarette')
                    printslow("- Ci fumiamo una sigaretta?", 150, 'tommy')
                    if timer % 2 == 0 and int(timer) >= 2:
                        final = orologio()
                        if final == 'a':
                            part_end = True
                            collepaganello = False
                            game_over = True
                            continui = 'n'
                            continue
                    printslow(f"- No Tom, devo andare a lavoro. E poi porcoddio sono le {orologio()} e c’ho le madonne.", 150, 'giulio')
                    printslow("- Dai dio caro Givil, famoce na sigaretta alle panchine, due minuti e via!", 150, 'tommy')
                    printslow("Giulio tentenna, poi col sorriso sotto il baffo dice:", 150, 'testo')
                    printslow("- Via, facciamoci questa sigaretta. Ho appena preso il caffè poi, vedrai se non mi cago addosso!", 150, 'giulio')
                    printslow("Andate alla panchina. \nChe bello, Giulio è lì con te! Per fargli capire quanto apprezzi la sua compagnia, \n"
                              "decidi di mettere un video di batteria al massimo volume dal cellulare, piazzandoglielo ben bene dentro l'orecchio."
                              "\nGiulio è chiaramente entusiasta, difatti bestemmia in ordine alfabetico i santi di 4 calendari diversi.\n"
                              "Approfitti della situazione per fare una proposta:", 150, 'testo')
                    bivio_collepaganello = input(Fore.YELLOW + Back.BLACK + "Type 'J' per convincerlo a jammare da nonno.\n"
                                                                            "Type 'P' per proporre una passeggiata sul monte: ").lower()
                    # jamming
                    if bivio_collepaganello == 'j':
                      printslow("- Mi dai un passaggio a casa di nonno? Devo lasciare delle cose.", 150, 'tommy')
                      printslow("- Ma certo Dio camper", 150, 'giulio')
                      printslow("Ti freghi le mani mentalmente. Il tuo piano per intrappolare Giulio nella musica sta andando bene. "
                                "\nArrivati di fronte a casa di nonno, decidi di premere l'acceleratore:", 150, 'testo')
                      printslow("- Givil dio caro non ti immagini che cazzo de piatto me so comprato, entri a vederlo?", 150, 'tommy')
                      printslow("- Non vorrei fare tardi sinceramente.", 100, 'giulio')
                      jam_o_studio = input(Fore.YELLOW + Back.BLACK + "Type 'I' per insistere\nType 'L' per lasciarlo andare: ").lower()
                      if jam_o_studio == 'i':
                        printslow("- Dai ma che te frega, giusto 5 minuti!", 150, 'tommy')
                        printslow("- Mi piacerebbe ma dopo faccio tardi al lavoro.", 150, 'giulio')
                        printslow("- Dai marescialle è pure il compleanno mio, non rompe sempre i coglioni co sto lavoro! \n"
                                  "Ma famo una jam, che c’è pure il basso tuo qui, suonamo 20min e basta!", 150, 'tommy')
                        jamming = True
                        jamcounter = 0
                        while jamming:
                          timer += 0.5
                          jamcounter += 1
                          if forza >= 5:
                            endings += 1
                            printslow("Ti senti particolarmente carico. Giulio è con te, hai fatto una bella colazione, studi come un matto tutti i giorni\n"
                                      "e i piatti che hai sulla batteria sono quelli definitivi (per ora).\n"
                                      "Date queste circostanze, cominci a fare il cazzone, e oltre a rullare in maniere scriteriate, cominci a fare i trick con le bacchette,\n"
                                      "roteandole in aria prima e dopo ogni colpo. Data la forza che hai stamattina, ti risulta particolarmente facile, quindi lo fai sempre più velocemente,\n"
                                      "aggiungendo giri su giri come se fossi un motore. Le bacchette vorticano, tu suoni e urli, sembri una macchina della musica.\n"
                                      "All'apice della jam lasci posto per un assolo di Giulio mentre tieni la cassa in quarti e fai le facce. Le bacchette roteano,\n"
                                      "roteano,\n"
                                      "roteano,\n"
                                      "roteano sempre di più\n"
                                      "e roteano e roteano e roteano e tu chiudi gli occhi e ti impegni tantissimo nella roteazione\n"
                                      "                                            \n"
                                      "finché a un tratto non ti sollevi da terra, esci dalla finestra aperta e ti allontani verso l'orizzonte come un elicottero musicale.\n"
                                      "                                            \n"
                                      "La ricorderanno come la tecnica dell'Elitch-cottero.\n"
                                      "\n"
                                      f"Finale Jam forzuta - Hai sbloccato {endings} finali su 7!", 150, 'testo')
                            part_end = True
                            jamming = False
                            collepaganello = False
                            game_over = True
                            continui = 'n'
                            continue
                          elif jamcounter > 3:
                            if timer % 2 == 0 and int(timer) >= 2:
                                final = orologio()
                                if final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  game_over = True
                                  continui = 'n'
                                  continue
                            printslow(f"- porcoddio Tommà sono le {orologio()}, è tardissimo. Devo andà.", 180, 'giulio')
                            printslow("Nooooooo, non puoi lasciare Giulio andarsene così! Decidi di sparare un'ultima potentissima rullata:\n"
                                      "TUTUTUTUTUTUTU'STRAK'STRAK'CRSH'CRSH'TUPATUPATUPATUPATUPATUPATU-", 100, 'testo')
                            printslow("Con l'ultimo colpo potentissimo sul ride, raggiungi un livello di db improponibile:\n"
                                      "ti giri a controllare Giulio e noti che gli è esplosa la testa.", 150, 'testo')
                            time.sleep(1.0)
                            printslow("- Vabbè sono sicuro che se ne sarebbe voluto andare così, tra musica e amici. Bella Givil.", 150, 'tommy')
                            dead_party.append('giulio')
                            s = finale_genocide(dead_party)
                            if s == 'a':
                                part_end = True
                                jamming = False
                                collepaganello = False
                                game_over = True
                                continui = 'n'
                                continue
                            printslow("Seppelisci il cadavere, o meglio i pezzetti, nel parcheggio del Colle, sperando che le coppiette che ci si vanno a infrattare\n"
                                      "vengano colpite dalla maledizione Giulio.", 150, 'testo')
                            timer += 0.5
                            fine_giulio = '1'
                            jam_o_studio = 'l'
                            jamming = False
                          else:
                            jams = ["JAM INCAZZATISSIMAAAAAAAAAAAA \nSDREEEEENG CRSH CRSH SKRGNEEEEEE PZFFSFZPZPKZ", "J a m - M e g a - R e l a x\nDum dum duuummmm, chks chks chks ding, tatatapu-dummmm", "Jam psichedelica\npiropiropiro sleeeemb sleeeemb strakatum-ts, strakatum-tssss"]
                            printslow(f"Fate una {random.choice(jams)}\nForza + 1!\n", 80, 'testo')
                            forza += 1
                            if timer % 2 == 0 and int(timer) >= 2:
                                final = orologio()
                                if final == 'a':
                                    part_end = True
                                    collepaganello = False
                                    game_over = True
                                    continui = 'n'
                                    continue
                            printslow(f"Sono le {orologio()}.", 150, 'testo')
                            ancora_jam = input(Fore.YELLOW + Back.BLACK + "Fate un'altra jam? 'Y' o 'N': ").lower()
                            if ancora_jam == 'n':
                              jamming = False
                              if jamcounter > 1 and jamcounter < 4:
                                printslow("- Cazzo, m'ha proprio gustato jammare, ci voleva porcoddio!", 150, 'giulio')
                                printslow("- Daje Givil, è stato SPAZIALE", 150, 'tommy')
                                printslow("Giulio si è unito al party!", 80, 'testo')
                                party.append('giulio')
                                fine_giulio = '2'
                              else:
                                fine_giulio = '1'
                                printslow("- Nonno Peroni, mi sono molto divertito, ma ci starrebbe questo lavoro che devo fare e devo andare via.", 150, 'giulio')
                                printslow("- Va bene Marescialle, la saluto", 150, 'tommy')
                                printslow("Giulio esce e va all'avventura. Chissà dove lo porteranno le sue stampanti \n"
                                          "con sistema a getto d'inchiostro a colori a modulo continuo ColorStream 8000?\nTorni a casa.", 150, 'testo')
                      elif jam_o_studio == "l":
                        fine_giulio = '1'
                        printslow("Forse è il caso di lasciarlo andare", 150, 'tommy')
                        printslow("Giulio esce e va all'avventura. Chissà dove lo porteranno le sue stampanti \n"
                                  "con sistema a getto d'inchiostro a colori a modulo continuo ColorStream 8000?", 150, 'testo')
                        jam_o_studio = input(Fore.YELLOW + Back.BLACK + "Type 'B' per restare da nonno a suonare la batteria\nType 'C' per tornare a casa: ").lower()
                        while jam_o_studio == 'b':
                          timer += 0.5
                          forza += 1
                          printslow("Resti a suonare la batteria. Quanto cazzo sei bravo! Forza + 1!", 150, 'testo')
                          if timer % 2 == 0 and int(timer) >= 2:
                              final = orologio()
                              if final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  game_over = True
                                  continui = 'n'
                                  continue
                          printslow(f"Sono le {orologio()}", 150, 'testo')
                          jam_o_studio = input(Fore.YELLOW + Back.BLACK + "Type 'B' per restare da nonno a suonare la batteria\n"
                                                                          "Type 'C' per tornare a casa: ").lower()
                    elif bivio_collepaganello == 'p':
                      timer += 0.5
                      printslow("- Andamo ai monticelli Givil?", 150, 'tommy')
                      printslow("- Va bene, magari come dice Samuel mi fa bene fare movimento la mattina, madonna merendina!", 150, 'giulio')
                      printslow("Vi incamminate verso la spianata. \n"
                                "Giulio ormai ha derubricato gli impegni lavorativi e ti propone di comprare un kit di microfoni fatti come dio comanda, \n"
                                "perché porcodio suoni benissimo, ma sentire la roba registrata con il cellulare è una tortura.\n"
                                "Arrivati alla spianata, bisogna decidere che percorso prendere.", 150, 'testo')
                      bivio_spianata = input(Fore.YELLOW + Back.BLACK + "Type 'C' per andare alla croce,\n"
                                                                        "Type 'P' per la panchina panoramica,\n"
                                                                        "Type 'E' per arrivare all'eremo: ").lower()
                      if bivio_spianata == 'c':
                        printslow("Carichi visto il bel tempo primaverile e la tangibile voglia di fica fresca che c’è nell’aria, \n"
                                  "decidete di straziare i vostri polmoni con la pettata della croce.", 150, 'testo')
                        printslow("- Dio canissimo me devo fa minimo 8 docce adesso.", 150, 'giulio')
                        printslow("- Cazzo sei il re delle docce, è giusto così!", 150,'tommy')
                        printslow("Arrivati in cima alla croce, vi sedete per terra, casa di nonno Mario è in primo piano e Fabriano rumoreggia ai suoi piedi. \n"
                                  "Alla vista dei primi fiori delle ginestre che colorano la vallata, decidi di mettere della musica, musica triste ovviamente. \n"
                                  "Partono gli Smiths, intro di chitarra, “Punctured bicycle on a hillside desolate, Will nature make a man of me yet?”, \n"
                                  "parte il capolavoro. \n"
                                  "Neanche Sergio, che è una delle persone migliori che conosci potrebbe creare qualcosa di così emozionante (forse giusto un CHALSTON).\n"
                                  "Ormai siete carichi di tristezza, una tristezza bella.", 150, 'testo')
                        time.sleep(1.0)
                        printslow("Giulio rompe il silenzio con un 'porcoddio' sincerissimo, propone inoltre \n"
                                  "di tornare a casa perché siete zuppi di sudore e lui deve andare a lavorare.", 150, 'testo')
                        fine_giulio = '1'
                        timer += 1
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
                                part_end = True
                                collepaganello = False
                                game_over = True
                                continui = 'n'
                                continue
                        printslow(f"Sono le {orologio()}", 150, 'testo')
                      elif bivio_spianata == 'p':
                        timer += 0.5
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
                                part_end = True
                                collepaganello = False
                                game_over = True
                                continui = 'n'
                                continue
                        printslow(f"Sono le {orologio()}", 150, 'testo')
                        printslow("Vi incamminate per il dedalo di stradine che portano alla panchina panoramica, sede incontrastata di:\n"
                                  "1) Chiacchierate emozionanti\n"
                                  "2) Sigarette\n"
                                  "3) Erezioni malcelate\n", 150, 'testo')
                        printslow("- Dio caro Givil quanto cazzo è bella la natura? Incredibile, dà frutti senza volere niente in cambio, è l'archetipo della bontà.", 150, 'tommy')
                        printslow("- Disse quello che tocca il cibo solo se è confezionato.", 150, 'giulio')
                        time.sleep(0.5)
                        printslow("Mentre camminate, sentite un rumore. Sembra provenire da un cespuglio. \n"
                                  "Tu e Giulio vi fate cauti, cosa potrebbe essere?", 150, 'testo')
                        soldi_o_panca = input(Fore.YELLOW + Back.BLACK + "Type 'S' se vuoi avvicinarti al rumore,\nType 'P' per proseguire: ").lower()
                        if soldi_o_panca == 's':
                          timer += 0.5
                          printslow("- Damo un'occhiata Givil, magari è uno scoiattolo.", 120, 'tommy')
                          printslow("- Sì Tommà, lo scoiattolo degli appennini. Tornamo indietro, che è un cinghiale!", 150, 'giulio')
                          printslow("Sei intimorito ma anche eccitato, come quando ti sei portato a casa le mutandine di quella ragazza.\n"
                                    "Ad un certo punto, noti un movimento dietro dei cespugli.", 150, 'testo')
                          printslow("- PORCODDIO Tommà gimo via!", 150, 'giulio')
                          printslow("- No Givil, today is the day I live!", 150, 'tommy')
                          printslow("Con un tonfo, cade a terra rovinosamente Tarek, nascosto dietro il cespuglio.", 150, 'testo')
                          printslow("'Una sigaretta, il mio regno per una sigaretta'\n"
                                    "Dice Tarek, evidentemente provato dall'assenza di tabacco.\n"
                                    "Non avendo altre sigarette con te, ti arrangi: prendi una pigna, ne accendi la cima e gliela passi.\n"
                                    "Tarek fuma contento e se ne va.", 150, 'testo')
                          printslow("- ahahahah ma che cazzo è successo", 150, 'tommy')
                          printslow("- Non lo so Bombo, però per un attimo me so cagato addosso ahah", 150, 'giulio')
                          if timer % 2 == 0 and int(timer) >= 2:
                              final = orologio()
                              if final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  game_over = True
                                  continui = 'n'
                                  continue
                          printslow(f"Sono le {orologio()}", 150, 'testo')
                          printslow("Dopo questa esperienza, tu e Giulio vi sentite legati per la vita. Giulio si unisce al party!", 150, 'testo')
                          party.append('giulio')
                          fine_giulio = '2'
                          time.sleep(1.0)
                          printslow("Passando vicino al cespuglio di Tarek, notate che gli è caduto il portafogli.\n"
                                    "Dentro ci sono 200 euro.", 150, 'testo')
                          soldi += 200
                          s = finale_soldi(soldi)
                          if s == 'a':
                              Part_end = True
                              collepaganello = False
                              game_over = True
                              continui = 'n'
                              continue
                          printslow("- Questi sono per le 14000 sigarette che mi ha scroccato, porcoddio", 180, 'tommy')
                          printslow("Pensi, mentre intaschi il maltolto.", 150, 'testo')
                          printslow("- Ora che ho trovato questi soldi, potrei dare un'occhiata al marketplace.", 150, 'tommy')
                          offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi aprire marketplace? 'Y' o 'N': ").lower()
                          if offerte == 'y':
                              s = compravendita()
                              if s:
                                  part_end = True
                                  collepaganello = False
                                  game_over = True
                                  continui = 'n'
                                  continue
                          printslow("Dopo questa scarica di adrenalina, decidete di tornare a Collepaganello.", 150, 'testo')
                          timer += 0.5
                        else:
                          printslow("Decidete di non indagare oltre e andate verso la panchina.\n"
                                    "Sei intimorito ma anche eccitato, come quando ti sei portato a casa le mutandine di quella ragazza.\n"
                                    "Dopo un po', apri Instagram", 150, 'testo')
                          printslow("- No Dio caro lo voglio", 150, 'tommy')
                          printslow("- Tommà porcoddio c’hai 37 piatti dio cane", 150, 'giulio')
                          printslow("- Sì Giù, ma questo è un Istanbul da 28”, martellato direttamente con la testa del figlio dell’artigiano turco! \n"
                                    "In pratica i turchi hanno una testa perfetta per far risuonare i piatti... Cazzo mesà me lo compro", 150, 'tommy')
                          printslow("- Tommy ma che cazzo ce fai co n'altro ride?", 150, 'giulio')
                          printslow("- Ma è che lo cercavo proprio così, questo poi è ultra mega iper raro", 150, 'tommy')
                          printslow("Dici mentre mandi il bonifico per direttissima. \n"
                                    "Torci la lingua pregustando le bacchettate che darai a quella delizia.", 150, 'tommy')
                          time.sleep(0.5)
                          printslow("Dopo una mezz'ora, arrivate al punto panoramico.\n"
                                    "Alla panchina, come sempre, c’è gente, tra cui due discretissime tope che ti salutano.", 150, 'testo')
                          printslow("- Famme fa' 'na sigaretta va', che a polmoni aperti fa più male... Ma chi erano quelle due?", 120, 'giulio')
                          printslow("- Quelle erano rispettivamente Groove e Armonia: il musicista vero è colui che fa dei threesome con loro.", 150, 'tommy')
                          printslow(".........", 30, 'testo')
                          printslow("- Tommy sei un coglione.", 150, 'giulio')
                          timer += 0.5
                          party.append('giulio')
                          fine_giulio = '2'
                          printslow("Dopo questa bonding experience, Giulio si unisce al party! \n"
                                    "decidete di tornare a Collepaganello.", 150, 'testo')
                          if timer % 2 == 0 and int(timer) >= 2:
                              final = orologio()
                              if final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  game_over = True
                                  continui = 'n'
                                  continue
                          printslow(f"Sono le {orologio()}", 150, 'testo')
                      else:
                        printslow("Vi incamminate verso l'eremo dalla spianata, dove i vecchi hanno appena iniziato una violentissima partita a bocce \n"
                                  "carica di bestemmie e frasi fatte.", 150, 'testo')
                        printslow("- Tommy ma sei sicuro di andare all’eremo? Guarda che sono almeno 5km dio serpe", 150, 'giulio')
                        printslow("- Giù, fidate, l’ho fatta mille volte e ci vuole pochissimo, è uno dei posti più belli della vita.", 150, 'tommy')
                        printslow("- Eh lo so che San Silvestro è bello, ma porco quel dio è una faticata.", 150, 'giulio')
                        printslow("- Ma dai che ce fa bene, lassù c’è un’atmosfera ispiratrice, vedrai che torni a Colle più rilassato.", 150, 'tommy')
                        printslow("Vi incamminate. Giulio non è convinto della scelta ma ti segue.", 150, 'testo')
                        printslow("- Mannaggia a quel tamarro del papa, ma perché t’ho dato retta!", 150, 'giulio')
                        time.sleep(1.5)
                        timer += 2
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
                                part_end = True
                                collepaganello = False
                                game_over = True
                                continui = 'n'
                                continue
                        printslow(f"Sono le {orologio()}", 150, 'testo')
                        printslow("Arrivati all'eremo, un potente rombo ti trapana i timpani, seguito da una voce solenne che declama:\n"
                                  "'O tu, che la padronanza del ritmo alleni,'\n"
                                  "'O tu, che la montagna aspra temi,'\n"
                                  "'O tu, dai livelli glicemici osceni,'\n"
                                  "'Dimmi, qual è la cosa che preferisci o a cui aneli?", 100, 'testo')
                        psi_cosa = str("PSI " + input(Fore.YELLOW + Back.BLACK + "Scrivi la cosa che più ti piace o desideri: ")).title()
                        printslow("'E sia, che il potere di evocare il tuo più profondo desiderio ti sia concesso'", 150, 'testo')
                        printslow(f"Hai appreso {psi_cosa}!", 80, 'testo')
                        oggetti.append(psi_cosa)
                        printslow("\n- Giù, non ti immagini che cazzo m'è appena successo...", 80, 'tommy')
                        printslow("- Ti sei pisciato sulle scarpe Tommà", 150, 'giulio')
                        printslow("Ti guardi i piedi. Hai le scarpe fradice.", 150, 'testo')
                        printslow("- Porca madonna.", 150, 'tommy')
                        printslow("- Tornamo a casa va', tanto ormai la giornata di lavoro è andata a schifìo.", 150, 'giulio')
                        party.append('giulio')
                        fine_giulio = '2'
                        printslow("Ti sei pisciato sulle scarpe, ma Giulio si è unito al party!", 200, 'testo')
                        printslow(f"Tornate a Collepaganello.", 150, 'testo')
                  else:
                    printslow("Forse è il caso di lasciarlo andare", 150, 'tommy')
                    fine_giulio = '1'
                else:
                  printslow("Forse è il caso di lasciarlo andare", 150, 'tommy')
                  fine_giulio = '1'
          # batteria da nonno
          elif hub1 == 'b':
            jam_o_studio = 'b'
            printslow("Mi sa che vado a suonare un po'", 150, 'tommy')
            printslow("Ti incammini verso casa di nonno. Per la strada, fischietti e air-rulli, riarrangiando mentalmente Soria Moria in versione funk.\n"
                      "Bomba! Pensi, immaginando l'armonizzazione delle voci fatta da Jacob Collier e Jacob Collier e Jacob Collier e Jacob Collier e...\n"
                      "Nel pieno dell'estasi, non ti sei reso nemmeno conto di essere arrivato.", 150, 'testo')
            printslow("Al lavoro!", 150, 'tommy')
            while jam_o_studio == 'b':
              timer += 0.5
              forza += 1
              printslow("Ti metti a suonare la batteria. Quanto cazzo sei bravo! Forza + 1!", 150, 'testo')
              if timer % 2 == 0 and int(timer) >= 2:
                  final = orologio()
                  if final == 'a':
                      jam_o_studio = False
                      part_end = True
                      collepaganello = False
                      game_over = True
                      continui = 'n'
                      continue
              printslow(f"Sono le {orologio()}.", 150, 'testo')
              jam_o_studio = input(Fore.YELLOW + Back.BLACK + "Type 'B' per restare da nonno a suonare la batteria\nType 'C' per tornare a casa: ").lower()
          elif hub1 == 'c':
            printslow("- Ma no, resto a casa ancora un po'.", 150, 'tommy')
            printslow("Ti guardi intorno. Le opzioni qua sono tre, fondamentalmente.", 150, 'testo')
            cose_casa = input(Fore.YELLOW + Back.BLACK + "Type 'M' per masturbarti,\n"
                                                         "Type 'S' per giocare alla switch,\n"
                                                         "Type 'E' per uscire: ").lower()
            if cose_casa == 'm':
              if 'mutandine' in oggetti:
                oggetti.remove('mutandine')
              printslow("E via col nostro caro vizietto. Sali in camera.", 150, 'testo')
              time.sleep(1.0)
              printslow("Ritrovi in un cassetto delle mutandine.\n"
                        "Immagini siano di Kiernan Shipka.", 150, 'testo')
              time.sleep(2.0)
              printslow("Sborri in due secondi netti.", 150, 'testo')
              printslow("U O O O O O O O O O O O R G H H G G H G H", 30, 'tommy')
              forza += 1
              timer += 0.5
              printslow("Ti riprendi dopo un riposino aftersex.", 150, 'testo')
              if timer % 2 == 0 and int(timer) >= 2:
                  final = orologio()
                  if final == 'a':
                      part_end = True
                      collepaganello = False
                      game_over = True
                      continui = 'n'
                      continue
              printslow(f"Sono le {orologio()}", 150, 'testo')
              oggetti.append('mutandine')
            elif cose_casa == 's':
              if 'occhiali' not in oggetti:
                printslow("Ti avvicini lussurioso alla Switch. Sul mobiletto all'ingresso, noti un paio di occhiale da sole funky.", 150, 'testo')
                occhiali = input(Fore.YELLOW + Back.BLACK + "Provi gli occhiali? 'Y' o 'N': ").lower()
                if occhiali == 'y':
                  oggetti.append('occhiali')
                  printslow("Afferri gli occhiali.", 150, 'testo')
                  printslow("- woo, che figo!", 150, 'tommy')
                  printslow("Ti spari un doppio gesto della pistola allo specchio, fai due pose e ti riavvicini alla switch.", 150, 'testo')
                  printslow("- Merda ma ora non ci vedo un cazzo. Vorrei giocare a Owl Boy, ma dovrei rinunciare allo $wag.", 150, 'tommy')
                  time.sleep(2.0)
                  printslow("- Fanculo, mi tengo lo $wag!", 150, 'tommy')
                  printslow("Ti spari una jam mentale con diverse rullate e cantanti rap afroamericani che poliritmano 'borghiddio'.\n"
                            "Che bomba di giornata.\n", 150, 'testo')
                else:
                  printslow("- Tempo di grindare emozioni.", 150, 'tommy')
                  timer += 2
                  if timer % 2 == 0 and int(timer) >= 2:
                      final = orologio()
                      if final == 'a':
                          part_end = True
                          collepaganello = False
                          game_over = True
                          continui = 'n'
                          continue
                  printslow("Il vortice di feels dei tuoi giochi preferiti (Celeste, Undertale, My Little Pony Friendship is Magic)\n"
                                "ti inebria e ti porta in una dimensione magica, morbida, familiare.\n"
                                "Potresti rimanere incollato allo schermo per ore, giorni, settimane, mesi...\n"
                                f"Ti guardi il Casio: sono le {orologio()}", 150, 'testo')
                  printslow("- Merda ho giocato per due ore.", 150, 'tommy')
                  time.sleep(2.0)
                  printslow("- Ok devo uscire per forza.", 150, 'tommy')
              else:
                printslow("Hai gli occhiali. Sei figo ma non ci vedi un cazzo. Non puoi giocà alla Switch.", 150, 'testo')
            else:
              printslow("Ok, credo di aver fatto tutto a casa. Facciamo mente locale:", 150, 'tommy')
              offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi aprire marketplace? 'Y' o 'N': ").lower()
              if offerte == 'y':
                s = compravendita()
                if s:
                  part_end = True
                  collepaganello = False
                  game_over = True
                  continui = 'n'
                  continue
              else:
                printslow("- Magari dopo.\n", 150, 'tommy')
              merendare()
          else:
            collepaganello = False
        if part_end:
            continue

        # si va a Fabriano
        printslow("- Mi sa che scendo a Fabriano.", 150, 'tommy')
        printslow("Prendi la Marco-car. Puzza di Polonia.", 150, 'testo')
        printslow("- Cazzo mi manca Samuel, quasi quasi lo vado a trovare, ora che è tornato!", 150, 'tommy')
        printslow("Scendi la strada di Collepaganello. Dalla collina, svetta casa di nonno.", 150, 'testo')
        printslow("- Alla fine è sempre la casa più figa del Colle, quella di nonno.", 150, 'tommy')
        time.sleep(1.5)
        Fabriano = True
        printslow("Arrivi in fondo alla via. La rotatoria dei giardini ti dà tre possibilità:", 150, 'testo')
        # ACT 3 - Good kid, F.A.A.B.riano city
        hub2 = input(Fore.YELLOW + Back.BLACK + "Type 'S' se vuoi andare da Samuel,\n"
                                                "Type 'C' se vuoi andare in centro, \n"
                                                "Type 'P' se vuoi andare verso la Pisana,\n"
                                                "Type 'B' se vuoi andare al Borgo: ").lower()
        while Fabriano:
          if hub2 == 's':
            if samuel_flag:
              printslow("Vai verso San Giuseppe. \nC'è poco da fare: il Piano è il quartiere migliore di Fabriano.", 150, 'testo')
              printslow("- Se Sergio fosse di Fabriano, vivrebbe qui in quanto tra le persone migliori che conosco.", 150, 'tommy')
              time.sleep(0.5)
              printslow("Arrivi sotto casa di Samuel. Negli ultimi mesi è diventato ancora più elettronico, chissà se parlerà in codice binario ormai?", 150, 'testo')
              estathe = input(Fore.YELLOW + Back.BLACK + "Noti un estathè incastrato tra i sedili, vuoi prenderlo? 'Y' o 'N': ").lower()
              if estathe == 'y':
                oggetti.append("estathe")
                printslow("- Wow, ma c'è ancora del liquido!", 150, 'tommy')
                printslow("Suggi l'estathè come se fosse della manna. Era scaduto e aperto da 3 mesi. Spaziale!\n"
                          "Suoni il campanello. Samuel risponde subito:", 150, 'testo')
                printslow("- Chi è?", 150, 'samuel')
                nome_citofono = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi rispondere?: ").title()
                time.sleep(0.5)
                printslow(f"- Sono {nome_citofono}, apri.", 150, 'tommy')
                printslow(f"- Non conosco nessun {nome_citofono}.", 150, 'samuel')
                printslow("- Sa so Tommaso. Posso salire?", 150, 'tommy')
                printslow("- Non conosco nessun Tommaso.", 150, 'samuel')
                printslow("Samuel ti chiude il citofono in faccia", 150, 'testo')
                printslow("- Porcoddio che stronzo guarda.", 150, 'tommy')
                time.sleep(0.5)
                printslow("Dopo poco, il portone si apre.", 150, 'testo')
                time.sleep(0.5)
                print("BZZZZZZZ")
                printslow("gli zuccheri antichi dell'estathè ti danno la forza di salire le scale. \n"
                          "Qualsiasi altra persona si sarebbe cagata addosso a questo punto.", 150, 'testo')
                printslow("- Madonna ma perché non li vendono già scaduti?", 150, 'tommy')
                printslow("Pensi, mentre arrivi sul pianerottolo.", 150, 'testo')
                time.sleep(0.5)
                printslow("Samuel ti apre tutto eccitato.", 150, 'testo')
                printslow("- Auguri Brasnio! Guarda che c'è qua: ", 150, 'samuel')
                printslow("Samuel ti indica un accrocco con manopole e una sorta di tastiera sul tavolo. L'oggetto è lurido.", 150, 'testo')
                printslow("- Sarebbe un synth?", 150, 'tommy')
                printslow("- Yesssss, è un Żurek-łomza-szczepienia-żubr, un synth polacco degli anni 80. \n"
                          "L'ho trovato in uno scantinato a Bydgoszcz, non ci potevo credere!", 150, 'samuel')
                printslow("Hai capito metà delle parole ma l'eccitazione di Samuel è palpabile.", 150, 'testo')
                printslow("- Bomba! Ma come funziona? Me lo fai sentire?", 150, 'tommy')
                printslow("- Yeah, lo stavo giusto collegando al televisore. Assurdamente, il motore audio ha bisogno di un cavo RGB per funzionare.\n"
                          "A quanto pare, il synth dovrebbe essere capace di creare delle grafiche che si modificano col suono.", 150, 'samuel')
                printslow("- Madonna ma che figata! Ma cazzo stavano avanti i polacchi!", 150, 'tommy')
                printslow("- La cosa che mi sconvolge è che ce ne sono tipo 10 esemplari, perché era un progetto troppo costoso e\n"
                          "praticamente l'hanno solo testato in qualche conservatorio. Mi stupisce che l'abbia trovato. Gratis, per giunta.", 150, 'samuel')
                printslow("- Che cazzo di ebreo ahahah", 150, 'tommy')
                time.sleep(1.0)
                printslow("Armeggiate un po' coi cavi e finalmente riuscite ad accendere il synth.\n"
                          "Un terribile rumore di elettricità riempie l'aria.", 150, 'testo')
                printslow("- Ah merda, devo attaccare quest'altro adattatore, aspetta un attimo e non toccare nulla.", 150, 'samuel')
                printslow("- Sisi, tranquillo!", 150, 'tommy')
                printslow("Suggi rilassato i rimasugli dell'estathè, reggendolo dalla cannuccia coi denti, mentre air rulli.\n"
                          "Al secondo paradiddle la cannuccia si sfila e l'estathè cade sul synth, donandogli un odore zuccheroso artificiale.", 150, 'testo')
                printslow("- Merda!", 150, 'tommy')
                printslow("Pensi, mentre senti che il synth comincia a friggere.\n"
                          "Non fai in tempo ad asciugarlo che arriva Samuel.\n"
                          "Sembra non aver notato nulla.", 150, 'testo')
                printslow("- Madonna Tommy, ma che è st'odore di chimico? è scaduto l'estathè?", 150, 'samuel')
                printslow("Non fai in tempo a rispondere: Samuel infila l'adattatore e sparisce in un lampo elettronico.", 150, 'testo')
                time.sleep(0.5)
                printslow("Subito dopo, il synth comincia a mandare segnali video. Sembra ti stia invitando a giocare.", 150, 'testo')
                timer += 0.5
                r = RPG(forza)
                if r:
                    game_over = True
                    continui = 'n'
                    Fabriano = False
                    continue
              else:
                printslow("Suoni il campanello. Samuel risponde subito:", 150, 'testo')
                printslow("- Chi è?", 150, 'samuel')
                nome_citofono = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi rispondere?: ").title()
                time.sleep(0.5)
                printslow(f"- Sono {nome_citofono}, apri.", 150, 'tommy')
                printslow(f"- Non conosco nessun {nome_citofono}.", 150, 'samuel')
                printslow("- Sa so Tommaso. Posso salire?", 150, 'tommy')
                printslow("- Non conosco nessun Tommaso.", 150, 'samuel')
                printslow("Samuel ti chiude il citofono in faccia", 150, 'testo')
                printslow("- Porcoddio che stronzo guarda.", 150, 'tommy')
                time.sleep(0.5)
                printslow("Dopo poco, il portone si apre.", 150, 'testo')
                time.sleep(0.5)
                print("BZZZZZZZ")
                printslow("Avresti dovuto bere quell'estathè per avere la forza di salire le scale. \n"
                          "Arranchi.", 150, 'testo')
                printslow("- Madonna ma perché non ho preso l'estathè?", 150, 'tommy')
                printslow("Pensi, mentre arrivi sul pianerottolo.", 150, 'testo')
                time.sleep(0.5)
                printslow("Samuel ti apre tutto eccitato.", 150, 'testo')
                printslow("- Auguri Frissip! Guarda che c'è qua: ", 150, 'samuel')
                printslow("Samuel ti indica un accrocco con manopole e una sorta di tastiera sul tavolo. L'oggetto è lurido.", 150, 'testo')
                printslow("- Sarebbe un synth?", 150, 'tommy')
                printslow("- Yesssss, è un Żurek-łomza-szczepienia-żubr, un synth polacco degli anni 80. \n"
                          "L'ho trovato in uno scantinato a Bydgoszcz, non ci potevo credere!", 150, 'samuel')
                printslow("Hai capito metà delle parole ma l'eccitazione di Samuel è palpabile.", 150, 'testo')
                printslow("- Bomba! Ma come funziona? Me lo fai sentire?", 150, 'tommy')
                printslow("- Yeah, lo stavo giusto collegando al televisore. Assurdamente, il motore audio ha bisogno di un cavo RGB per funzionare.\n"
                          "A quanto pare, il synth dovrebbe essere capace di creare delle grafiche che si modificano col suono.", 150, 'samuel')
                printslow("- Madonna ma che figata! Ma cazzo stavano avanti i polacchi!", 150, 'tommy')
                printslow("- La cosa che mi sconvolge è che ce ne sono tipo 10 esemplari, perché era un progetto troppo costoso e\n"
                          "praticamente l'hanno solo testato in qualche conservatorio. Mi stupisce che l'abbia trovato. Gratis, per giunta.", 150, 'samuel')
                printslow("- Che cazzo di ebreo ahahah", 150, 'tommy')
                time.sleep(1.0)
                printslow("Armeggiate un po' coi cavi e finalmente riuscite ad accendere il synth.\n"
                          "Un terribile rumore di elettricità riempie l'aria.", 150, 'testo')
                printslow("- Ah merda, devo attaccare quest'altro adattatore, aspetta un attimo e non toccare nulla.", 150, 'samuel')
                printslow("- Sisi, tranquillo!", 150, 'tommy')
                printslow("Samuel torna e attacca l'ennesimo cavo. Il synth sembra funzionare. Toccate qualche manopola e siete nello spazio:\n"
                          "Suoni e rumori mai sentiti si mischiano a grafiche psichedeliche e spaventose, una sorta di brutalismo allucinogeno.\n"
                          "Non pensavate che potesse esistere una roba del genere, e invece...", 100, 'testo')
                stop = input(Fore.YELLOW + Back.BLACK + "Premi un tasto qualsiasi quando vuoi stoppare la musica.")
                time.sleep(1.0)
                printslow("- Madonna che cazzo di trip.", 80, 'samuel')
                printslow("- Ma che cazzo abbiamo fatto? Giuro so sconvolto.", 80, 'tommy')
                printslow("- Penso che dovrò stare a letto il resto del giorno per riprendermi. Dio porco che botta.", 80, 'samuel')
                printslow("Ti alzi barcollando ed esci da casa di Samuel. Sei totalmente rincoglionito.\n"
                          "Appena entri in macchina, ti addormenti di colpo.", 150, 'testo')
                time.sleep(2.0)
                timer += 2
                printslow(f"Apri gli occhi. Sono le {orologio()}.", 150, 'testo')
                printslow("- Merda.", 150, 'tommy')
                samuel_flag = False
            else:
              printslow("- Che torno a fare?", 150, 'tommy')
            if timer % 2 == 0 and int(timer) >= 2:
                final = orologio()
                if final == 'a':
                    Fabriano = False
                    game_over = True
                    continui = 'n'
                    continue
            printslow(f"Sei sotto casa di Samuel, sono le {orologio()}. Dove vuoi andare?", 150, 'testo')
            hub2 = input(Fore.YELLOW + Back.BLACK + "Type 'C' se vuoi andare in centro, \n"
                                                    "Type 'P' se vuoi andare verso la Pisana,\n"
                                                    "Type 'B' se vuoi andare al Borgo: ").lower()
          elif hub2 == 'c':
            printslow("Ti dirigi al parcheggione. Oggi c'è la ZTL e non puoi raggiungere la piazza con la macchina.\n"
                      "Trovi posto a fianco a una macchina delle poste, che sfregi fantasiosamente con la chiave.", 150, 'testo')
            printslow("B r u t t i S t r o n z i", 50, 'testo')
            printslow("Sei davanti al Bar Centrale. Senti un brivido sulla schiena: del reggaeton fortissimo pompa dalle casse\n"
                      "della macchinetta delle merendine. La odi, ma la ami, anche.", 150, 'testo')
            macchinetta = input(Fore.YELLOW + Back.BLACK + "Vuoi comprare qualcosa alla macchinetta? 'Y' o 'N': ").lower()
            if macchinetta == 'y':
                while macchinetta == 'y':
                    acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Cosa prendi? prenditi una mezz'oretta per selezionare.\n"
                                                                      "(E) Estathè:  50€\n"
                                                                      "(S) Snickers: 100€\n"
                                                                      "(B) Bounty:   100€\n"
                                                                      "Scrivi l'iniziale di ciò che vuoi comprare: ").lower()
                    if acquisto_snack == 'e':
                        if soldi < 50:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            timer += 0.5
                            soldi -= 50
                            oggetti.append('estathe')
                            printslow(f"Hai comprato un estathè, Sei rimasto con {soldi}€.\n"
                                      f"La macchinetta segna le {orologio()}.", 200, 'testo')
                    elif acquisto_snack == 's' or acquisto_snack == 'b':
                        if soldi < 100:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            timer += 0.5
                            soldi -= 100
                            oggetti.append('merendina')
                            printslow(f"Hai comprato una fonte esagerata di zuccheri. Sei rimasto con {soldi}€.\n"
                                      f"La macchinetta segna le {orologio()}.", 200, 'testo')
                    macchinetta = input(Fore.YELLOW + Back.BLACK + "Vuoi continuare a fare acquisti? 'Y' o 'N': ").lower()
            else:
                printslow("- No, non è il momento di merendare.", 150, 'tommy')
                offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi aprire marketplace magari? 'Y' o 'N': ").lower()
                if offerte == 'y':
                    s = compravendita()
                    if s:
                        Fabriano = False
                        game_over = True
                        continui = 'n'
                        continue
            printslow("Ti allontani dolorosamente dal dispensatore di gioia e saccarosio.", 150, 'testo')
            bivio_centro = input(Fore.YELLOW + Back.BLACK + "Type 'M' per andare al Bar Mario,\n"
                                                            "Type 'P' per andare al Public: ").lower()
            if bivio_centro == 'm':
                printslow("Continui per il Bar Mario. Benché tu odi profondamente quel posto, in fondo speri anche di incontrare qualcuno.\n"
                          "                            \n"
                          "Il chiacchiericcio e il biascichìo dei vari tossici e alcolisti che ronzano intorno al bar ti stordisce, \n"
                          "la voce a trombetta di Tommy Fogna ti provoca un'irrefrenabile voglia di buttarlo in un pogo dei Meshuggah, \n"
                          "mentre le risate di Claudio ti fanno venire da piangere. La tristezza di queste esistenze ti abbatte.", 150, 'testo')
                if timer >= 6 and cripi_flag:
                    cripi_flag = False
                    printslow("Tra le nuove leve del Bar Mario c'è Cripi, che attacca a bere alle 14:00. Oggi è particolarmente unto,\n"
                              "e il sole gli riflette addosso.", 150, 'testo')
                    if 'occhiali' in oggetti:
                        printslow("Per ovviare al problema, ti metti gli occhiali e ti avvicini baldanzoso. Non riuscendo a sfruttare\n"
                                  "l'effetto sorpresa del riflesso, Cripi non è abbastanza rapido nell'allungarti una mano sul culo.\n"
                                  "In tutta risposta, prendendolo in contropiede, riesci a toccargli il culo tu, umiliandolo profondamente.", 150, 'testo')
                        printslow("- Bella Die, c'hai le chiappe d'oro, me le vendi?", 150, 'tommy')
                        printslow("Sghignazzi beffardo. Stavolta non è riuscito a toccarti il culo. \n"
                                  "Ma il riso si trasforma ben presto in terrore, quando ti accorgi che la mano ti è rimasta\n"
                                  "letteralmente incollata al culo di Cripi.", 150, 'testo')
                        printslow("- Die ma che cazzo c'hai sul culo?", 150, 'tommy')
                        printslow("Cripi serafico ti spiega la sua filosofia sui pantaloni:\n"
                                  "'- Oh Tommà ma i pantaloni bisogna lavarli solo se sono sporchi sporchi, non è che solo perché mi sono seduto\n"
                                  "per terra mentre lavoravo al maneggio, allora sono da cambiare.'\n"
                                  "La tua mano è letteralmente incollata a un misto di sterco e peli di cavallo, Diego deve aver pensato di\n"
                                  "essersi messo i suoi pantaloni da cowboy, oggi.\n"
                                  "Stai andando nel panico, sudi e iperventili. In un ultimo sforzo disperato, tiri via la mano e senti uno strappo:\n"
                                  "hai letteralmente portato via un pezzo dei pantaloni di Cripi, che ora ha una chiappa all'aria.", 150, 'testo')
                        time.sleep(1.5)
                        timer += 0.5
                        oggetti.append('pergamena')
                        printslow("Ti infili al bagno del Bar Mario per lavare via la pezza che ti ritrovi in mano. Piangi lacrime amare, e tu odi\n"
                                  "l'amaro. Al terzo strato di sudiciume che togli, noti che oltre ai pantaloni hai qualcos'altro in mano:\n"
                                  "sembrerebbe la carta d'identità di Diego.", 150, 'testo')
                        printslow("- Ma che cazzo...", 100, 'tommy')
                        if timer % 2 == 0 and int(timer) >= 2:
                            final = orologio()
                            if final == 'a':
                                Fabriano = False
                                game_over = True
                                continui = 'n'
                                continue
                        printslow("Il documento è illeggibile: è ricoperto da capo a piedi da numeri e nomi di ragazze. Sembrerebbe che Cripi\n"
                                  "abbia utilizzato la carta d'identità come una sorta di pergamena su cui scrivere i suoi appunti.\n"
                                  "Decidi di tenerla, magari tra quei numeri c'è qualche baldracca buona.\n"
                                  f"Esci dal bagno. Sono le {orologio()}.", 150, 'testo')
                    elif psi_cosa in oggetti:
                        printslow("Non te la senti di affrontare Cripi e le sue manate sul culo. Appena si gira verso di te,\n"
                                  "chiami il potere di San Silvestro:\n", 150, 'testo')
                        printslow(f"- {psi_cosa}!", 200, 'tommy')
                        printslow("Urli, e il potere risuona in te: \n"
                                  "dalle mani, una concrezione di sborra e zucchero si cristallizza, andando a scagliarsi contro tutti i presenti al Bar Mario.\n"
                                  "                                                          \n"
                                  "Sono tutti intrappolati nella tua forza generativa. Sei sbigottito dall'effetto della magia. Ti senti un po' Shinji.", 150, 'testo')
                        printslow("- Grazie San Silvestro, grazie Misato. Questa era per te.", 150, 'tommy')
                        time.sleep(1.0)
                        printslow("Avvicinandoti al Bar, noti qualcosa a terra: sembrerebbe la carta d'identità di Diego.", 150, 'testo')
                        printslow("- Ma che cazzo...", 100, 'tommy')
                        printslow("Il documento è illeggibile: è ricoperto da capo a piedi da numeri e nomi di ragazze. Sembrerebbe che Cripi\n"
                                  "abbia utilizzato la carta d'identità come una sorta di pergamena su cui scrivere i suoi appunti.\n"
                                  "Decidi di tenerla, magari tra quei numeri c'è qualche baldracca buona.", 150, 'testo')
                        timer += 0.5
                        oggetti.append('pergamena')
                    else:
                        printslow("Accecato dal riverbero, ti avvicini a guardia abbassata. Cripi ti nota e ti si fionda contro.\n"
                                  "Vuole cercare di prenderti il culo. Fai uno scatto all'ultimo mentre ti monta il terrore.", 150, 'tommy')
                        attacco_culo = random.randint(0, 100)
                        if attacco_culo > 10+(forza*10):
                            printslow("- Nooooooooooooo!", 100, 'tommy')
                            printslow("Urli, mentre Cripi stringe la presa sulle tua chiappe di marshmallow.\n"
                                      "Sei umiliato, ti senti sporco e ti viene da piangere.\n"
                                      "Barcolli all'indietro, non riesci a stare in piedi.\n"
                                      "Mentre la vista ti si offusca, dedichi un ultimo messaggio mentale al mondo:", 150, 'testo')
                            printslow("- Vorrei... C-Chiavare... Mi-Mi-Misato...", 30, 'tommy')
                            printslow("Chiudi gli occhi. Sei stato sconfitto. Game over.", 150, 'testo')
                            game_over = True
                            continui = 'n'
                            Fabriano = False
                            continue
                        else:
                            printslow("Con un colpo di mano, superi l'assalto di Cripi e sfrutti il rimpallo per tirargli uno schiaffo sul culo.\n"
                                      "Il colpo rapido, a contatto col culo appiccicoso di Diego, ti lascia in mano un pezzo di carta.\n"
                                      "sembrerebbe la carta d'identità di Diego.", 150, 'testo')
                            printslow("- Ma che cazzo...", 100, 'tommy')
                            printslow("Il documento è illeggibile: è ricoperto da capo a piedi da numeri e nomi di ragazze. Sembrerebbe che Cripi\n"
                                      "abbia utilizzato la carta d'identità come una sorta di pergamena su cui scrivere i suoi appunti.\n"
                                      "Decidi di tenerla, magari tra quei numeri c'è qualche baldracca buona.", 150, 'testo')
                            printslow("- Bella Die, vado a spararmi una bevuta", 200, 'tommy')
                            printslow("Dici velocemente, appropinquandoti al bar. Ti sei salvato, brutto furbone.", 150, 'testo')
                            oggetti.append('pergamena')
                printslow("Entri dentro cercando di non farti vedere. Pare abbia funzionato.", 150, 'testo')
                macchinetta = 'y'
                while macchinetta == 'y':
                    acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi? prenditi una mezz'oretta per selezionare.\n"
                                                                      "(E) Estathè:  100€\n"
                                                                      "(V) Vodka:    300€\n"
                                                                      "(N) Niente\n"
                                                                      "Scrivi l'iniziale di ciò che vuoi comprare: ").lower()
                    if acquisto_snack == 'v':
                        if soldi < 300:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            timer += 0.5
                            soldi -= 300
                            oggetti.append('vodka')
                            if timer % 2 == 0 and int(timer) >= 2:
                                final = orologio()
                                if final == 'a':
                                    macchinetta = 'False'
                                    Fabriano = False
                                    game_over = True
                                    continui = 'n'
                                    continue
                            printslow(f"Hai comprato una vodka, Sei rimasto con {soldi}€.\n"
                                          f"L'orologio segna le {orologio()}.", 200, 'testo')
                    elif acquisto_snack == 'e':
                        if soldi < 100:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            timer += 0.5
                            soldi -= 100
                            oggetti.append('estathe')
                            printslow(f"Hai comprato un estathè, Sei rimasto con {soldi}€.\n"
                                      f"L'orologio segna le {orologio()}.", 200, 'testo')
                    macchinetta = input(Fore.YELLOW + Back.BLACK + "Vuoi continuare a fare acquisti? 'Y' o 'N': ").lower()
                printslow("Sembra che non ci sia nient'altro da fare, qua. Torni alla macchina.", 150, 'testo')
                timer += 0.5
                if timer % 2 == 0 and int(timer) >= 2:
                    final = orologio()
                    if final == 'a':
                        macchinetta = 'False'
                        Fabriano = False
                        game_over = True
                        continui = 'n'
                        continue
                printslow(f"Sono le {orologio()}", 150, 'testo')
            else:
                printslow("Vai verso il public passando per la cattedrale, evitando così la marmaglia del Bar Mario.\n"
                          "Ti affascina sempre la zona di San Venanzio, a lei sono legati ricordi dolceamari.\n"
                          "scendi in piazza.", 150, 'testo')
                printslow("- Ah ma oggi è martedì, il Public è chiuso. So' un coglione.", 150, 'tommy')
                if forza >= 5 and 'andrea' in party and timer >= 10:
                    endings += 1
                    printslow("- No te preocupes, amigo, tengo les chiavis", 150, 'andrea')
                    printslow("Andrea schiava il portone e ti invita per un drink.", 150, 'testo')
                    printslow("- Bomba! mi prepari un drink spaziale? Posso vedere il menù?", 150, 'tommy')
                    printslow("Il Mago Andrea ti guarda di traverso: non è disposto ad aspettare una mezz'ora per poi doverti servire un estathè.\n"
                              "Ci pensa un attimo e poi ti dice:", 150, 'testo')
                    printslow("- Tommy ti fidi di me?", 150, 'andrea')
                    printslow("- Sì signor capitano!", 150, 'tommy')
                    printslow("- Allora tieniti forte che mo ti sbudello, ma con classe.", 150, 'andrea')
                    printslow("Il Mago Andrea comincia a mescolare liquidi e triturare solidi. L'odore è nauseabondo, poi paradisiaco,\n"
                              "poi afrodisiaco.", 150, 'testo')
                    printslow("- Andrè ma che è?", 150, 'tommy')
                    printslow("- Questo, caro mio, è un distillato di sapori unico, questo è il drink degli dèi,\n"
                              "questo è ciò di cui i sogni sono fatti, è l'espressione massima che un liquido può raggiungere:\n"
                              "assomigliare da vicino al sapore della fica.", 150, 'andrea')
                    printslow("Chiudi gli occhi e assapori. Tutto, dalla consistenza alla dolcezza, dal tocco salino\n"
                              "all'inebriante retrogusto tossico, ti riporta al caldo momento della pressione delle labbra su una fica.\n", 150, 'testo')
                    printslow("- Minchia, è incredibile", 150, 'tommy')
                    printslow("Pensi, mentre ingurgiti il succo d'amore. Appena lo finisci, ne vuoi subito un'altro.", 150, 'testo')
                    printslow("- Andrè porcoddio ci voglio morì co sta roba", 200, 'tommy')
                    printslow("Dici, mentre tracanni il secondo drink.", 150, 'testo')
                    time.sleep(1.5)
                    printslow("Ti prende la parlantina alticcia e intavoli una conversazione su quanto ping ha il tavolino del bar.\n"
                              "Il Mago Andrea non ti ascolta più da una mezz'ora ormai, e trinca un bel Melissa Juice.\n"
                              "Risentito, per attirare l'attenzione urli un 'Uigaraaaa' fragoroso.\n"
                              "                                                   \n"
                              "Niente, sei invisibile. Sentendo una forza dentro mai sentita prima, data un po' dai drinks e un po'\n"
                              "dal fatto che oggi hai fatto movimento, dai un pugno fortissimo al bancone.", 150, 'testo')
                    printslow("- Porcoddio Andr-", 150, 'tommy')
                    printslow("Non fai in tempo a finire la frase che il bancone, risuonando per via del tuo pugno, esplode in mille pezzi.\n"
                              "Chiudi gli occhi spaventato.\n"
                              "                            \n"
                              "Poco dopo, noti che il bancone si è ricostituito sotto forma di albero millenario.\n"
                              "Sei incredulo e spaventato. L'albero ti parla.\n"
                              "'Maestro della forza lubrica, il tuo pugno/pugnetta mi ha chiamato,\n"
                              "quindi io ho risposto. Tu sei il cavaliere decisivo nella corte di Arsù,\n"
                              "paladino della Tavola di Sbronza. Il mio potere a te va, e con sè,\n"
                              "il contraltare del tuo io meccanico, la Big Machine: d'ora in poi, oltre a Big Machine,\n"
                              "Potrai evocare anche Legno Marcio, il ciocco accioccato.", 150, 'testo')
                    printslow("- Eh?", 150, 'tommy')
                    printslow("Dopo queste parole, il vecchio tronco ti tocca e senti che parte del tuo sangue si trasforma in alcol.\n"
                              "Diventi ubriaco in una maniera profonda, complessa e importante. Le leggi che governano i rapporti umani\n"
                              "ti sono tutte note, e le riscrivi semplicemente pensandole. Il buon costume è per te ormai un ricordo lontano,\n"
                              "i vestiti solo una maglia che costringe il tuo corpo chr vibra.", 150, 'testo')
                    printslow("- So liberoooooooooo", 200, 'tommy')
                    printslow("Esclami, mentre ti senti librare nell'aria.\n"
                              "                                    \n"
                              "                                    \n"
                              "                                    \n"
                              "Ti ritrovano la mattina dopo completamente nudo in piazza bassa, nascosto dietro il camion\n"
                              "del porchettaro, coperto solo da dei rami. Secondo il racconto di alcuni passanti, ieri sera\n"
                              "sei salito su un albero e hai provato a saltare, dicendo di aver sentito la chiamata del Cielo Daoista.\n"
                              "Ne è risultata una caduta rovinosa dalla quale ti hanno salvato i rami di un albero.\n"
                              "Ti guardi addosso. \n"
                              "La corteccia ti fa l'occhiolino.\n"
                              "\n"
                              ";)\n"
                              "\n"
                              f"Finale Albero delle Sbronze - Hai scoperto un finale! Ora sei a {endings} su 7!", 150, 'testo')
                    game_over = True
                    continui = 'n'
                    Fabriano = False
                    continue

                printslow("Torni in macchina incazzato. Un'ora buttata.", 150, 'testo')
                timer += 1
                if timer % 2 == 0 and int(timer) >= 2:
                    final = orologio()
                    if final == 'a':
                        Fabriano = False
                        game_over = True
                        continui = 'n'
                        continue
                printslow(f"Sono le {orologio()}", 150, 'testo')

            hub2 = input(Fore.YELLOW + Back.BLACK + "Type 'S' se vuoi andare da Samuel,\n"
                                                    "Type 'P' se vuoi andare verso la Pisana,\n"
                                                    "Type 'B' se vuoi andare al Borgo: ").lower()

          elif hub2 == 'p':
              printslow("Prendi per la Pisana.\n"
                        "Arrivi in Piazzale Matteotti.", 150, 'testo')
              hub_piazzale = True
              while hub_piazzale:
                  piazzale = input(Fore.YELLOW + Back.BLACK + "Type 'F' per andare in farmacia,\n"
                                                              "Type 'A' per suonare da Agron,\n"
                                                              "Type 'C' per andare in centro,\n"
                                                              "Type 'M' per aprire il marketplace: ").lower()
                  if piazzale == 'f':
                      printslow("Entri in farmacia sperando di trovare qualche snack particolare e sano. Le tue aspettative non vengono deluse,\n"
                                "noti una bella confezione di 'Scrofix' appena arrivati.", 150, 'testo')
                      printslow("- Oltre ad essere incredibilmente buoni, sono il cibo più sano della vita", 150, 'tommy')
                      macchinetta = True
                      acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Vuoi comprare uno Scrofix? Costa 150€. 'Y' o 'N': ").lower()
                      while macchinetta:
                          if acquisto_snack == 'y':
                              if soldi < 150:
                                  printslow("Il dottore ti guarda male. \n'- Non te lo puoi permettere, stronzo.'", 200, 'testo')
                                  macchinetta = False
                              else:
                                  soldi -= 150
                                  oggetti.append('merendina_rara')
                                  printslow(f"Hai comprato uno Scrofix, Sei rimasto con {soldi}€.", 150, 'testo')
                                  acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Vuoi comprarne un'altro? 'Y' o 'N': ").lower()
                          elif acquisto_snack != 'y':
                              macchinetta = False
                  elif piazzale == 'm':
                      s = compravendita()
                      if s:
                          game_over = True
                          continui = 'n'
                          hub_piazzale = False
                          Fabriano = False
                          continue
                  elif piazzale == 'a':
                      printslow("Decidi di suonare a casa di Agron.", 150, 'testo')
                      printslow("BZZZZZZZZZZZZ", 60, 'testo')
                      if timer >= 10 and agron_flag:
                          # Agron route
                          printslow("Raggiungi Agron sotto casa alle 18 come concordato, ovviamente non è sceso, decidi di chiamarlo:", 150, 'testo')
                          printslow("- Oh Ag, sto qui sotto, scendi?", 150, 'tommy')
                          printslow("- Ah stai qui sotto? Arrivo subito", 150, 'agron')
                          printslow("Ovviamente passano 15min, Agron si starà sicuramente depilando le palle senza aver controllato l’orario. \n"
                                    "Decidi di mandargli un audio su whatsapp:", 150, 'testo')
                          printslow("- oooooohhhh porcodeddiooooo fa freddoooo dio negro!", 250, 'tommy')
                          printslow("Nel mentre che aspetti stai ascoltando mezza discografia di Kanye e pensi a quanto sia bello \n"
                                    "che lo schiavismo ci abbia portato questa musica.\n"
                                    "Finalmente scende Agron tutto pulito e profumato.", 150, 'testo')
                          printslow("- Dove andiamo?", 150, 'tommy')
                          printslow("- Boh pensavo a un aperitivo tranquillo.", 150, 'agron')
                          printslow("Prima di ripartire, colleghi il cellulare alle casse. Anzi, prefersci di no perché dal cellulare si sente meglio,\n"
                                    "dato che il tuo cellulare ha una qualità audio suprema.", 150, 'testo')
                          printslow("- Bro senti che cazzo di groove che ho trovato oggi", 150, 'tommy')
                          printslow("Spari a tutto volume 15min di video registrato malissimo in cui suoni cose difficilissime. Una scarica di rumore bianco.", 150, 'testo')
                          printslow("- Ma che bomba bro fighissimo!", 150, 'agron')
                          printslow("Sei carico, Agron è sempre una sicurezza per quel che riguarda il ritmo.", 150, 'testo')
                          printslow("- Comunque bro me so innamorato completamente de questa su instagram, guarda che fica porcoddio!", 150, 'tommy')
                          printslow("Per sbaglio, con un movimento sbadato, rispondi alla storia della tipa con un emoji che piange e un coltello.\n"
                                    "Agron scioglie l'imbarazzo:", 150, 'testo')
                          printslow("- Ascoltiamo della musica che carica?", 150, 'agron')
                          printslow("- Si aspetta un attimo, senti qui sto passaggio che faccio!", 150, 'tommy')
                          infierisci = input(Fore.YELLOW + Back.BLACK + "Vuoi infierire facendogli ascoltare un'altra rullata? 'Y' o 'N': ").lower()
                          if infierisci == 'y':
                              agron_flag = False
                              timer += 0.5
                              printslow("Fai ascoltare il passaggio che ti carica, ma ovviamente non ti puoi fermare lì.\n"
                                        "Parti con una megarullata che mischia 3/4, 5/8 e 11/16: inascoltabile, letteralmente una tortura di Guantanamo.\n"
                                        "Agron ti guarda, lo vedi male, sta impallidendo. Cerchi di caricarlo facendo dei gesti ritmici con la mano, ma è troppo tardi:\n"
                                        "Agron spalanca la portiera, vomita e infine torna a casa.", 150, 'testo')
                              time.sleep(1.0)
                              if timer % 2 == 0 and int(timer) >= 2:
                                  final = orologio()
                                  if final == 'a':
                                      Fabriano = False
                                      hub_piazzale = False
                                      game_over = True
                                      continui = 'n'
                                      continue
                              printslow(f"Sono le {orologio()}", 150, 'testo')
                          else:
                              time.sleep(1.0)
                              triste = 0
                              carica = 0
                              printslow("Decidi di graziarlo e di dargli la possibilità di scegliere della musica.", 150, 'testo')
                              printslow("- Mettiamo la musica da una playlist che ho fatto ieri, si chiama 'Banane & Negroni'.", 150, 'agron')
                              canzone_1 = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi mettere?\n"
                                                                           "(C) Carissa - Sun Kil Moon\n"
                                                                           "(P) Passionfruit - Drake\n"
                                                                           "Scegli con l'iniziale: ").lower()
                              if canzone_1 == 'c':
                                  triste += 1
                                  printslow("Mettete su Carissa.\n"
                                            "                                                  \n"
                                            "'Oh Carissa, when I first saw you, you were a lovely child'\n"
                                            "'And the last time I saw you, you were fifteen and pregnant and running wild'\n"
                                            "............\n"
                                            "'Carissa was thirty-five, raised kids since she was fifteen years old and suddenly died'\n"
                                            "'Next to an old river, fire pit, oh there's gotta be more than that to it'\n"
                                            "Canticchi col buon Sun Kil Moon mentre ti dirigi verso il Bar Mario.", 150, 'testo')
                                  printslow("- Ma perchè siamo venuti al Bar Mario? Me fa schifo...\n"
                                            "poi dopo che ho sentito sto pezzo m’è passata la voglia de fa tutto... Andiamo da un’altra parte!", 150, 'agron')
                              else:
                                  carica += 1
                                  printslow("Mettete su Passionfruit.\n"
                                            "                                                  \n"
                                            "'Hold on, hold on, fuck that, fuck that shit'\n"
                                            "'Hold on, I got to start this motherfuckin record over again'\n"
                                            "............\n"
                                            "'Passionate from miles away'\n"
                                            "'Passive with the things you say'\n"
                                            "'Passin' up on my old ways'\n"
                                            "I can't blame you, no, no'\n"
                                            "Canticchi con lo scuretto Drake mentre ti dirigi verso il Bar Mario.", 150, 'testo')
                                  printslow("- Ooh dopo Drake ce voleva proprio un bel drink da Otello! Facciamo una bevuta e andiamo in giro?", 150, 'agron')
                              printslow("Dopo la prima tappa, riprendete la macchina.", 150, 'testo')
                              canzone_3 = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi mettere?\n"
                                                                           "(P) Pyramid Song - Radiohead\n"
                                                                           "(S) Still D.R.E. - Snoop Dogg and Dr. Dre\n"
                                                                           "Scegli con l'iniziale: ").lower()
                              if canzone_3 == 'p':
                                  triste += 1
                                  printslow("Mettete su Pyramid Song.\n"
                                            "                                                  \n"
                                            "'I jumped in the river and what did I see?'\n"
                                            "'Black-eyed angels swam with me'\n"
                                            "............\n"
                                            "'There was nothing to fear and nothing to doubt'\n"
                                            "'There was nothing to fear and nothing to doubt'\n"
                                            "Biascichi con l'attempato Thom Yorke mentre ti dirigi verso il Time Out.", 150, 'testo')
                                  printslow("Pyramid Song ti ha dato una sensazione di tristezza fresca, difficile da spiegare, \n"
                                            "ma è la sensazione che hai dopo che fai la doccia dopo un duro allenamento. \n"
                                            "Saresti pronto per una bevuta malinconica ma invece entri al Time Out. \n"
                                            "Musica di merda, smandrappate cafonissime, drink di merda...", 150, 'testo')
                                  printslow("- Ma che è sto zozzo? Agron, ti va di jire da un'atru varre?", 150, 'tommy')
                              else:
                                  carica += 1
                                  printslow("Mettete su Still D.R.E.\n"
                                            "                                                  \n"
                                            "'Yeah, nigga'\n"
                                            "'I'm still fucking with you'\n"
                                            "'Still waters run deep'\n"
                                            "'Still Snoop Dogg and D-R-E, '99 nigga'\n"
                                            "............\n"
                                            "'No stress, no seeds, no stems, no sticks!'\n"
                                            "'Some of that real sticky-icky-icky'\n"
                                            "'Ooh wee! Put it in the air!'\n"
                                            "'Well, you's a fool, D-R, ha-ha'\n"
                                            "Sborri con questi calibri 35 afroamericani mentre ti dirigi verso il prossimo bar.", 150, 'testo')
                                  printslow("Siete vestiti benissimo, si percepisce la figaggine a distanza di km, quintali di $wag. \n"
                                            "Prendi un Appletini, voli verso galassie infinite di zucchero e alcool. Ma il giro continua!", 150, 'testo')
                              printslow("Dopo la seconda tappa, riprendete la macchina.", 150, 'testo')
                              canzone_2 = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi mettere?\n"
                                                                           "(G) Gold Digger - Kanye West\n"
                                                                           "(S) Soria Moria - Mount Eerie\n"
                                                                           "Scegli con l'iniziale: ").lower()
                              if canzone_2 == 'g':
                                  carica += 1
                                  printslow("Mettete su Gold Digger.\n"
                                            "                                                  \n"
                                            "'Now, I ain't sayin' she a gold digger'\n"
                                            "'But she ain't messin' with no broke niggas'\n"
                                            "............\n"
                                            "'Get down girl, go 'head, get down'\n"
                                            "'Get down girl, go 'head, get down'\n"
                                            "Rappi col pazzo Ye mentre ti dirigi verso il Wooden.", 150, 'testo')
                                  printslow("Dopo Gold Digger entrate al Wooden e ordinate un cocktail buonissimo. \n"
                                            "Parte una base hip hop, Agron sfodera un freestyle:\n", 150, 'testo')
                                  printslow("- Tommy klan, con lo swing affiliato, colpo di stato, il reggaeton è da sfigato! \n"
                                            "In the Ypsilon, too fast for polizia, show me paletta and disappear, Santa Maria!", 150, 'agron')
                              else:
                                  triste += 1
                                  printslow("Mettete su Soria Moria.\n"
                                            "                                                  \n"
                                            "'Slow pulsing, red tower lights'\n"
                                            "'Across a distance, refuge in the dust'\n"
                                            "............\n"
                                            "'I'm an arrow now'\n"
                                            "'Mid-air'\n"
                                            "Piagnucoli con Mr. Elverum mentre ti dirigi verso il prossimo bar.", 150, 'testo')
                                  printslow("Andate al Centrale perchè devi comprare le cartine. Non ne sei felice. \n"
                                            "Agron si è pure fermato a fare due chiacchiere con un tamarro, quindi adesso \n"
                                            "ti devi per forza pocciare tutta la discografia di Giusy Ferreri che mandano a tutto volume. \n"
                                            "Bestemmi dentro.", 150, 'testo')
                              printslow("Dopo la terza tappa, riprendete la macchina.", 150, 'testo')
                              canzone_4 = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi mettere?\n"
                                                                           "(D) Dagger - Slowdive\n"
                                                                           "(B) The Blacker The Berry - Kendrick Lamar\n"
                                                                           "Scegli con l'iniziale: ").lower()
                              if canzone_4 == 'b':
                                  carica += 1
                                  printslow("Mettete su The Blacker The Berry.\n"
                                            "                                                  \n"
                                            "'I'm the biggest hypocrite of 2015'\n"
                                            "'Once I finish this, witnesses will convey just what I mean'\n"
                                            "............\n"
                                            "'How you no see the whip, left scars pon' me back'\n"
                                            "'But now we have a big whip parked pon' the block'\n"
                                            "'All them say we doomed from the start, cah' we black'\n"
                                            "'Remember this, every race start from the block, just remember that'\n"
                                            "Rappi a cannone mentre ti dirigi verso lo Sverso.", 150, 'testo')
                                  printslow("Scendi dalla macchina e ancora ti senti blacker and blacker, è tutto uno YO, BRO, NIGGA, BITCH.", 150, 'testo')
                                  printslow("- Ag, ma se dopo continuassimo a bere?", 150, 'tommy')
                              else:
                                  triste += 1
                                  printslow("Mettete su Dagger.\n"
                                            "                                                  \n"
                                            "'The sunshine girl is sleeping'\n"
                                            "'She falls and dreams alone'\n"
                                            "'And me I am her dagger'\n"
                                            "'Too numb to feel her pain'\n"
                                            "............\n"
                                            "'I thought I heard you whisper'\n"
                                            "'It happens all the time'\n"
                                            "Declami con gli Slowdive mentre ti dirigi verso il Bogart.", 150, 'testo')
                                  printslow("Dopo questa mattonata anni ‘90, entri al Bogart per comprare un Estathè. Guardi il prezzo: 1200€!", 150, 'testo')
                                  printslow("- MA PORCODDIO! ANDAMO VIA DIO CANE!", 200, 'tommy')
                              printslow("Dopo la quarta tappa, riprendete la macchina.", 150, 'testo')
                              canzone_5 = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi mettere?\n"
                                                                           "(P) Pink + White - Frank Ocean\n"
                                                                           "(K) Katy Song - Red House Painters\n"
                                                                           "Scegli con l'iniziale: ").lower()
                              if canzone_5 == 'p':
                                  carica += 1
                                  printslow("Mettete su Pink + White.\n"
                                            "                                                  \n"
                                            "'That's the way everyday goes'\n"
                                            "'Every time we've no control'\n"
                                            "............\n"
                                            "'Running out the melpomene, nicotine'\n"
                                            "'Stealing granny cigs (Take it easy)'\n"
                                            "'Gimme something sweet'\n"
                                            "'Bitch, I might like immortality'\n"
                                            "'This is life, life immortality'\n"
                                            "Ti sbrodoli con quel figo di Frank Ocean mentre ti dirigi verso il bar dell'Angoletto.", 150, 'testo')
                                  printslow("Marius è il solito antipatico, però la piazza è bellissima e il bar è calmo. \n"
                                            "Proprio quello che cercavi! Essendo rilassato, prendi il tuo solito barattolo di miele con aggiunta di tisana. \n"
                                            "Berrai altro alcool dopo, tanto sei già ubriaco!", 150, 'testo')
                              else:
                                  triste += 1
                                  printslow("Mettete su Katy Song.\n"
                                            "                                                  \n"
                                            "'Some escape some door to open'\n"
                                            "'This path seems the blackest but I'\n"
                                            "'Guess it's the soonest'\n"
                                            "............\n"
                                            "'Empty and bothered'\n"
                                            "'Watching the water'\n"
                                            "'Quiet in the corner'\n"
                                            "'Numb and falling through'\n"
                                            "'Without you what does my life amount to'\n"
                                            "Ti sfregni con i Red House Painters mentre ti dirigi verso il Bar Nuovo.", 150, 'testo')
                                  printslow("Arrivate al Bar Nuovo, ti avevano detto che dopo la ristrutturazione era migliorato. \n"
                                            "Invece no, è solo nuovo e pulito, ma per assurdo molto più squallido, tu invece volevi il vero bar nuovo, quello vecchio. Quello del PITBULL! \n"
                                            "Vi sciacquate subito dalle palle.", 150, 'testo')
                                  printslow("- MA PORCODDIO! ANDAMO VIA DIO CANE!", 200, 'tommy')
                              if triste > carica:
                                  timer += 0.5
                                  agron_flag = False
                                  printslow("Dopo aver scelto canzoni tristi e essere andato nei peggiori bar di fabriano, Agron è malinconico e tu ti sei rovinato il compleanno. Riporti a casa il tuo amico colorato.\n"
                                            "Appena uscito dalla macchina, la iella delle canzoni che hai scelto lo fa investire da tre macchine di fila.\n"
                                            "Guardi ciò che rimane di Agron (ovvero una striscia rosso-bruna lunga tutto Piazzale Matteotti) e sospiri: ", 150, 'testo')
                                  printslow("- Vabbè sono sicuro che se ne sarebbe voluto andare così, tra musica triste e amici. Ciao Ag.", 150, 'tommy')
                                  if timer % 2 == 0 and int(timer) >= 2:
                                      final = orologio()
                                      if final == 'a':
                                          Fabriano = False
                                          hub_piazzale = False
                                          game_over = True
                                          continui = 'n'
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                                  dead_party.append('agron')
                                  s = finale_genocide(dead_party)
                                  if s == 'a':
                                      game_over = True
                                      continui = 'n'
                                      hub_piazzale = False
                                      Fabriano = False
                                      continue
                              else:
                                  agron_flag = False
                                  printslow("Cazzo che bomba di serata! La musica è stata fighissima e già siete mezzi brilli.\n"
                                            "Carichissimo, ti prepari: il party sta per iniziare!\n"
                                            "                                             \n"
                                            "Agron si unisce al party!", 150, 'testo')
                                  party.append('agron')
                                  timer += 0.5
                                  if timer % 2 == 0 and int(timer) >= 2:
                                      final = orologio()
                                      if final == 'a':
                                          Fabriano = False
                                          hub_piazzale = False
                                          game_over = True
                                          continui = 'n'
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                      else:
                        printslow("Non risponde nessuno.", 150, 'testo')
                        if timer < 10:
                            if timer % 2 == 0 and int(timer) >= 2:
                                final = orologio()
                                if final == 'a':
                                    Fabriano = False
                                    hub_piazzale = False
                                    game_over = True
                                    continui = 'n'
                                    continue
                            printslow(f"- In effetti è presto, sono le {orologio()}, perché sono qua? \n"
                                      "- Forse perché so' un coglione!", 150, 'tommy')
                            offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi ammazzare il tempo aprendo marketplace? 'Y' o 'N': ").lower()
                            if offerte == 'y':
                                s = compravendita()
                                if s:
                                    game_over = True
                                    continui = 'n'
                                    hub_piazzale = False
                                    Fabriano = False
                                    continue
                  else:
                      printslow("Vai da Piazzale Matteotti al centro.", 150, 'testo')
                      if timer >= 8 and dialogo1_andrea and not dead_andrea:
                          quest_andrea = True
                          printslow("Mentre giri verso il centro, noti un losco figuro.", 150, 'testo')
                          printslow("- Ma è Andrea!", 150, 'tommy')
                          nome_andrea = input(Fore.YELLOW + Back.BLACK + "Come vuoi chiamare Andrea? Scrivi la lettera tra parentesi.\n"
                                                                         "(C) 'Capo'\n"
                                                                         "(D) 'Dr. Millennium'\n"
                                                                         "(A) 'Andry'\n"
                                                                         "(T) 'Threesoman': ").lower()
                          def nomignolo(l):
                              lettere = ['c', 'd', 't']
                              nomi = ['Capo', 'Dr. Millennium', 'Threesome']
                              return nomi[lettere.index(l)]
                          if nome_andrea == 'a':
                              printslow("- Andry!", 150, 'tommy')
                              printslow("Gridi sagace. La figura si gira verso di te e ti guarda negli occhi.\n"
                                        "nel giro di due secondi, la faccia gli diventa totalmente rossa e, prima di riuscire a maledirti,\n"
                                        "esplode sorda in una fontana di pezzi di carne e cervella.", 150, 'testo')
                              time.sleep(1.5)
                              printslow("- Vabbè sono sicuro che se ne sarebbe voluto andare così, tra soprannomi divertenti e amici.", 150, 'tommy')
                              dead_party.append('andrea')
                              s = finale_genocide(dead_party)
                              if s == 'a':
                                  game_over = True
                                  continui = 'n'
                                  hub_piazzale = False
                                  Fabriano = False
                                  continue
                              dead_andrea = True
                              quest_andrea = False
                          elif nome_andrea != 's':
                              printslow(f"- {nomignolo(nome_andrea)}!", 150, 'tommy')
                              printslow("La figura incappucciata si gira verso di te e ti intima di fermarti. Scendi divertito.", 150, 'testo')
                              printslow("- Oh Andrè ma che ci fai da queste parti?", 150, 'tommy')
                              printslow("- Il silenzio è d'oro, giovane padawan.", 100, 'andrea')
                              printslow("Non capisci di cosa Andrea stia parlando. Decidi di sorvolare.", 150, 'testo')
                              printslow("- Oh ma serata Mario Party stasera? Eh dai che ti faccio il culo!", 150, 'tommy')
                              printslow("Andrea ti guarda con uno sguardo misto tra noia e disprezzo.", 150, 'testo')
                              printslow("- Tommy, tu mi hai incontrato per un solo motivo: perché lo volevi.\n"
                                        "Il Mago del Crepuscolo si palesa solo a chi lo evoca. Dimmi cosa ti turba.", 100, 'andrea')
                              printslow("- Andrè ma chi è il Mago del Crepuscolo? Stai uscendo di nuovo con Andrea Mori per caso?", 150, 'tommy')
                              printslow("- Non so di cosa tu stia parlando. Il Mago del Crepuscolo sono io, e tu mi hai evocato perché\n"
                                        "hai bisogno della mia saggezza. Per cui dimmi, cosa vuoi sapere?", 100, 'andrea')
                              printslow("Senti uno strano potere ipnotico provenire dal Mago del Cre- cioè, da Andrea.", 150, 'testo')
                              printslow("- In effetti c'è qualcosa che vorrei sapere. Ogni tanto mi chiedo come si fa a scopare le tipe\n"
                                        "senza conseguenze. Non voglio starci sotto, voglio solo jazzare quà e là.", 150, 'tommy')
                              printslow("Il Mago del Crepuscolo si fa grave:", 150, 'testo')
                              printslow("- Questa domanda... Questa domanda è la domanda definitiva, la domanda che accomuna uomini e dèi\n"
                                        "sin dall'antica Grecia. Ma come in tutte le storie mitiche, per ricevere una risposta, c'è \n"
                                        "una prova da superare.", 100, 'andrea')
                              printslow("- Sono disposto a tutto.", 150, 'tommy')
                              printslow("Il Mago del Crepuscolo accenna un sorriso. Poi, lentamente, ti espone la prova.", 150, 'testo')
                              printslow("- Ebbene giovane adepto, questa è la prova. Dovrai recuperare degli artefatti che ho perso dopo una notte\n"
                                        "di esperimenti sulle mie pozioni.", 100, 'andrea')
                              printslow("- Per pozioni intendi drink? Mago, ti sei ubriacato?", 150, 'tommy')
                              printslow("- La strada della magia è incomprensibile per i non iniziati. Taci, mezzuomo!", 100, 'andrea')
                              printslow("Il Mago ringhia. Decidi di ascoltare.", 150, 'testo')
                              printslow("- Dicevo, stavo lavorando al drink definitivo, il Piçka e Shipkës. Un sorso è abbastanza per abbassare le difese\n"
                                        "di qualsiasi uomo e renderlo schiavo della Dea Vagina. Ho bisogno che tu mi porti questi tre ingredienti per prepararlo:\n"
                                        "- 1 Liquido estivo zuccherino\n"
                                        "- 1 Distillato di distruzione dell'Est\n"
                                        "- 1 Contenitore di donna\n"
                                        "Una volta che li avrai, torna da me e condividerò con te i miei poteri.", 100, 'andrea')
                              printslow("- Va bene Mago, mi avvio alla ricerca degli artefatti.", 150, 'tommy')
                              printslow("- In culo alla figa, giovane Padawan", 100, 'andrea')
                              dialogo1_andrea = False
                      elif timer >= 8 and not dialogo1_andrea and quest_andrea:
                          mago = input(Fore.YELLOW + Back.BLACK + "Vedi il Mago. Vuoi fermarti? 'Y' o 'N': ").lower()
                          andrea = True
                          saggezza = 'y'
                          if mago == 'y' and andrea:
                              printslow("- Dimmi, giovane Padawan, cosa desideri?", 100, 'andrea')
                              domanda_mago = input(Fore.YELLOW + Back.BLACK + "Type 'S' per chiedere saggezza\n"
                                                                              "Type 'D' per donare gli artefatti\n"
                                                                              "Type 'P' se sei in possesso di un importante documento,\n"
                                                                              "Type 'A' per andartene: ").lower()
                              if domanda_mago == 's':
                                  while saggezza == 'y':
                                      saggezze = ["- Il vero Saggio della fica non ne parla perché è impegnato a leccarla",
                                                  "- Le donne sono come i gatti, vogliono le coccole",
                                                  "- Le donne c'hanno voglia quanto noi, forse di più",
                                                  "- Porta sempre con te un tubetto di vaselina, non sai mai quando potrebbe servirti",
                                                  "- Devi entrare nell'ottica che la drum n bass è una musica frattale",
                                                  "- Perché spendere 400 euro per un kit di base buono, quando con la stessa cifra\n"
                                                  "puoi prendere una Millennium full optional di merda?"]
                                      printslow("- Mago, donami un po' della tua saggezza.", 150, 'tommy')
                                      printslow("- Ecco a te:\n"
                                                f"{random.choice(saggezze)}", 100, 'andrea')
                                      saggezza = input(Fore.YELLOW + Back.BLACK + "Vuoi un'altra perla di saggezza? 'Y' o 'N': ").lower()
                              elif domanda_mago == 'd' and 'estathe' in oggetti and 'vodka' in oggetti and 'mutandine' in oggetti:
                                  quest_andrea = False
                                  timer += 0.5
                                  printslow("- Ho portato gli artefatti, Mago.", 150, 'tommy')
                                  printslow("Dici con tono solenne.\n"
                                            "Il mago osserva i tre oggetti, poi con calma declama:", 150, 'testo')
                                  printslow("- Locus Pregnum,\n"
                                            "- Batteria Millennium\n"
                                            "- Chiappe di Scarlet\n"
                                            "- E degli Autechre Basscadet\n"
                                            "- Per il potere donatomi da David Bowie\n"
                                            "- Piçka e Shipkës, pronto a scatenarti!", 100, 'andrea')
                                  printslow("Il Mago mesce la sua pozione con agili gesti, mentre la incanta con le sue parole.\n"
                                            "                                                          \n"
                                            "Dopo poco, il mago assaggia il Piçka e Shipkës.", 150, 'testo')
                                  printslow("- Così dolce... e eccitante... e matto... è proprio un Piçka e Shipkës.\n"
                                            "Tommy, ti sei mostrato all'altezza del compito, e per questo riceverai i miei poteri.\n"
                                            "All'avventura!", 100, 'andrea')
                                  party.append('andrea')
                                  time.sleep(1.0)
                                  printslow("Andrea, il Mago del Crespuscolo, si unisce al party!", 100, 'testo')
                                  if timer % 2 == 0 and int(timer) >= 2:
                                      final = orologio()
                                      if final == 'a':
                                          Fabriano = False
                                          hub_piazzale = False
                                          game_over = True
                                          continui = 'n'
                                          continue
                                  printslow(f"Sono le {orologio()} mentre ti avvii verso il Centro.", 150, 'testo')
                              elif domanda_mago == 'd' and 'estathe' not in oggetti and 'vodka' not in oggetti and 'mutandine' not in oggetti:
                                  printslow("- Torna quando avrai trovato tutti gli ingredienti, giovane padawan.", 100, 'andrea')
                              elif domanda_mago == 'p' and 'pergamena' in oggetti:
                                  printslow("Il Mago ti guarda e esclama:", 150, 'testo')
                                  printslow("- Tu... Tu... Tu sei in possesso delle pergamene!", 100, 'andrea')
                                  printslow("- Pergamene? Che pergamene?", 150, 'tommy')
                                  printslow("- Le Pergamene del Mar Morto di Fica! Dai qua!", 100, 'andrea')
                                  printslow("Il Mago indica la tua tasca. Qualcosa sembra brillare. Tiri fuori il documento d'identità di Cripi e lo porgi al Mago.", 150, 'testo')
                                  printslow("- Sì, sono loro! Le antiche pergamene! Veloce, tira fuori il cellulare!", 150, 'andrea')
                                  printslow("Prendi il telefono e ti prepari ad ascoltare le indicazioni del Mago.", 150, 'testo')
                                  printslow("- Chiamiamo le smandrappe, Capo? Ehm, volevo dire Mago?", 150, 'tommy')
                                  printslow("- No, per prima cosa devi utilizzare la calcolatrice per sommare tutti i numeri che vedi scritti sulla pergamena, \n"
                                            "poi chiamare il numero che ne risulta. Questa è l'antica profezia delle Pergamene.", 100, 'andrea')
                                  printslow("Cominci a sommare i numeri di telefono delle tipe scritti sul documento.\n"
                                            "                                            \n"
                                            "Dopo un po' sei quasi alla fine, manca giusto l'ultimo numero.", 150, 'testo')
                                  printslow("- 3769577048 + 3200119921... Porta 6969696969!", 150, 'tommy')
                                  printslow("Il Mago fa una risatina. Decidi di chiamare."
                                            "                                                  \n"
                                            "tuuuuuuuuu                                      \n"
                                            "tuuuuuuuuu                                      \n"
                                            "- Lei ha chiamato il numero proibito. \n"
                                            "Da stanotte a mezzanotte, il suo cazzo verrà succhiato magicamente ogni mattina.\n"
                                            "Cordiali saluti, si goda le palle finché ce le ha.\n"
                                            "tuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", 150, 'testo')
                                  printslow("- Ma che cazzo...\n"
                                            "\n", 150, 'tommy')
                                  printslow("Hai appena beccato una maledizione venerea!\n"
                                            "                                           \n"
                                            "...In compenso Andrea, Il Mago del Crepuscolo, si unisce al party!", 150, 'testo')
                                  if timer % 2 == 0 and int(timer) >= 2:
                                      final = orologio()
                                      if final == 'a':
                                          Fabriano = False
                                          hub_piazzale = False
                                          game_over = True
                                          continui = 'n'
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                                  party.append('andrea')
                                  quest_andrea = False
                              elif domanda_mago == 'p' and 'pergamena' not in oggetti:
                                  printslow("Non hai nessun documento importante con te.", 100, 'testo')
                          else:
                              printslow("Saluti ossequiosamente il Mago e ti avvii verso il Centro.", 150, 'testo')
                              andrea = False
                              hub2 = 'c'
                              hub_piazzale = False
                      else:
                          hub2 = 'c'
                          hub_piazzale = False

          elif hub2 == 'b':
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                      "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                      "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
            game_over = True
            continui = 'n'
            Fabriano = False
            continue
    continui = input("Game Over, vuoi ricominciare? 'Y' o 'N': ").lower()
    if continui == 'y':
        game_over = False
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
    else:
        printslow("Hey Tommy, I'm Mario! Thank you so much for to playing my game!", 80, 'testo')