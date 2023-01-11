# per creare un exe, utilizza il terminal in pycharm e scrivi pyinstaller --onefile main.py (cerca di capire se vale anche se hai più di un file, come in questo caso)
import colorama
from colorama import Fore, Back, Style
import GlVar
from Finali import finale_triste, finale_soldi, finale_neutro, finale_buono, finale_genocide
import sys, time, random
from art import titolo1, titolo2, titolo3, act1, act1_title, sansprint
from Compravendita import compravendita
from printing import printslow
from Orologio import orologio
from RPG import RPG

colorama.init(autoreset=True)
GlVar.init()

# merendine-hoarder
def merendare():
    porco = True
    while porco:
        merendinas = input(Fore.YELLOW + Back.BLACK + "Vuoi prendere un'altra merendina per dopo? 'Y' o 'N': ").lower()
        if merendinas == 'y':
            GlVar.oggetti.append("merendina")
            printslow("Meglio prenderne una di riserva.", 150, 'tommy')
        else:
            printslow("Ok, basta, forse sto esagerando.", 150, 'tommy')
            porco = False

while not GlVar.game_over:
    GlVar.timer = 0
    GlVar.forza = 0
    GlVar.soldi = 300
    GlVar.final = ''
    GlVar.glic_count = False
    GlVar.samuel_flag = True
    GlVar.agron_dialogue = True
    GlVar.agron_flag = True
    GlVar.cripi_flag = True
    GlVar.dialogo1_andrea = True
    GlVar.dead_andrea = False
    GlVar.party = []
    GlVar.dead_party = []
    GlVar.psi_cosa = ''
    GlVar.oggetti = []
    GlVar.game_over = False
    GlVar.continui = 'y'
    while GlVar.continui == 'y':
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
            GlVar.timer += 0.5
            GlVar.forza += 1
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
          GlVar.timer += 0.5
          GlVar.forza += 1
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
              GlVar.game_over = True
              GlVar.continui = 'n'
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
            if GlVar.timer >= 2 and fine_giulio == '0':
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
                  GlVar.oggetti.append("sigarette")
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
                if 'sigarette' in GlVar.oggetti:
                  offri = input(Fore.MAGENTA + Back.BLACK + "Giulio è di fretta, magari si rilasserà se facciamo due chiacchiere con una sigaretta." + Fore.YELLOW + Back.BLACK + " \nOffri una sigaretta? 'Y' o 'N': ").lower()
                  if offri == 'y':
                    GlVar.timer += 0.5
                    GlVar.oggetti.remove('sigarette')
                    printslow("- Ci fumiamo una sigaretta?", 150, 'tommy')
                    if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                        GlVar.final = orologio()
                        if GlVar.final == 'a':
                            part_end = True
                            collepaganello = False
                            GlVar.game_over = True
                            GlVar.continui = 'n'
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
                          GlVar.timer += 0.5
                          jamcounter += 1
                          if GlVar.forza >= 5:
                            GlVar.endings += 1
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
                                      f"Finale Jam forzuta - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
                            part_end = True
                            jamming = False
                            collepaganello = False
                            GlVar.game_over = True
                            GlVar.continui = 'n'
                            continue
                          elif jamcounter > 3:
                            if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                GlVar.final = orologio()
                                if GlVar.final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  GlVar.game_over = True
                                  GlVar.continui = 'n'
                                  continue
                            printslow(f"- porcoddio Tommà sono le {orologio()}, è tardissimo. Devo andà.", 180, 'giulio')
                            printslow("Nooooooo, non puoi lasciare Giulio andarsene così! Decidi di sparare un'ultima potentissima rullata:\n"
                                      "TUTUTUTUTUTUTU'STRAK'STRAK'CRSH'CRSH'TUPATUPATUPATUPATUPATUPATU-", 100, 'testo')
                            printslow("Con l'ultimo colpo potentissimo sul ride, raggiungi un livello di db improponibile:\n"
                                      "ti giri a controllare Giulio e noti che gli è esplosa la testa.", 150, 'testo')
                            time.sleep(1.0)
                            printslow("- Vabbè sono sicuro che se ne sarebbe voluto andare così, tra musica e amici. Bella Givil.", 150, 'tommy')
                            GlVar.dead_party.append('giulio')
                            s = finale_genocide(dead_party)
                            if s == 'a':
                                part_end = True
                                jamming = False
                                collepaganello = False
                                GlVar.game_over = True
                                GlVar.continui = 'n'
                                continue
                            printslow("Seppelisci il cadavere, o meglio i pezzetti, nel parcheggio del Colle, sperando che le coppiette che ci si vanno a infrattare\n"
                                      "vengano colpite dalla maledizione Giulio.", 150, 'testo')
                            GlVar.timer += 0.5
                            fine_giulio = '1'
                            jam_o_studio = 'l'
                            jamming = False
                          else:
                            jams = ["JAM INCAZZATISSIMAAAAAAAAAAAA \nSDREEEEENG CRSH CRSH SKRGNEEEEEE PZFFSFZPZPKZ", "J a m - M e g a - R e l a x\nDum dum duuummmm, chks chks chks ding, tatatapu-dummmm", "Jam psichedelica\npiropiropiro sleeeemb sleeeemb strakatum-ts, strakatum-tssss"]
                            printslow(f"Fate una {random.choice(jams)}\nForza + 1!\n", 80, 'testo')
                            GlVar.forza += 1
                            if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                GlVar.final = orologio()
                                if GlVar.final == 'a':
                                    part_end = True
                                    collepaganello = False
                                    GlVar.game_over = True
                                    GlVar.continui = 'n'
                                    continue
                            printslow(f"Sono le {orologio()}.", 150, 'testo')
                            ancora_jam = input(Fore.YELLOW + Back.BLACK + "Fate un'altra jam? 'Y' o 'N': ").lower()
                            if ancora_jam == 'n':
                              jamming = False
                              if jamcounter > 1 and jamcounter < 4:
                                printslow("- Cazzo, m'ha proprio gustato jammare, ci voleva porcoddio!", 150, 'giulio')
                                printslow("- Daje Givil, è stato SPAZIALE", 150, 'tommy')
                                printslow("Giulio si è unito al party!", 80, 'testo')
                                GlVar.party.append('giulio')
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
                          GlVar.timer += 0.5
                          GlVar.forza += 1
                          printslow("Resti a suonare la batteria. Quanto cazzo sei bravo! Forza + 1!", 150, 'testo')
                          if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                              GlVar.final = orologio()
                              if GlVar.final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  GlVar.game_over = True
                                  GlVar.continui = 'n'
                                  continue
                          printslow(f"Sono le {orologio()}", 150, 'testo')
                          jam_o_studio = input(Fore.YELLOW + Back.BLACK + "Type 'B' per restare da nonno a suonare la batteria\n"
                                                                          "Type 'C' per tornare a casa: ").lower()
                    elif bivio_collepaganello == 'p':
                      GlVar.timer += 0.5
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
                        GlVar.timer += 1
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                part_end = True
                                collepaganello = False
                                GlVar.game_over = True
                                GlVar.continui = 'n'
                                continue
                        printslow(f"Sono le {orologio()}", 150, 'testo')
                      elif bivio_spianata == 'p':
                        GlVar.timer += 0.5
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                part_end = True
                                collepaganello = False
                                GlVar.game_over = True
                                GlVar.continui = 'n'
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
                          GlVar.timer += 0.5
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
                          if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                              GlVar.final = orologio()
                              if GlVar.final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  GlVar.game_over = True
                                  GlVar.continui = 'n'
                                  continue
                          printslow(f"Sono le {orologio()}", 150, 'testo')
                          printslow("Dopo questa esperienza, tu e Giulio vi sentite legati per la vita. Giulio si unisce al party!", 150, 'testo')
                          GlVar.party.append('giulio')
                          fine_giulio = '2'
                          time.sleep(1.0)
                          printslow("Passando vicino al cespuglio di Tarek, notate che gli è caduto il portafogli.\n"
                                    "Dentro ci sono 200 euro.", 150, 'testo')
                          GlVar.soldi += 200
                          s = finale_soldi(GlVar.soldi)
                          if s == 'a':
                              Part_end = True
                              collepaganello = False
                              GlVar.game_over = True
                              GlVar.continui = 'n'
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
                                  GlVar.game_over = True
                                  GlVar.continui = 'n'
                                  continue
                          printslow("Dopo questa scarica di adrenalina, decidete di tornare a Collepaganello.", 150, 'testo')
                          GlVar.timer += 0.5
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
                          GlVar.timer += 0.5
                          GlVar.party.append('giulio')
                          fine_giulio = '2'
                          printslow("Dopo questa bonding experience, Giulio si unisce al party! \n"
                                    "decidete di tornare a Collepaganello.", 150, 'testo')
                          if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                              GlVar.final = orologio()
                              if GlVar.final == 'a':
                                  part_end = True
                                  collepaganello = False
                                  GlVar.game_over = True
                                  GlVar.continui = 'n'
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
                        GlVar.timer += 2
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                part_end = True
                                collepaganello = False
                                GlVar.game_over = True
                                GlVar.continui = 'n'
                                continue
                        printslow(f"Sono le {orologio()}", 150, 'testo')
                        printslow("Arrivati all'eremo, un potente rombo ti trapana i timpani, seguito da una voce solenne che declama:\n"
                                  "'O tu, che la padronanza del ritmo alleni,'\n"
                                  "'O tu, che la montagna aspra temi,'\n"
                                  "'O tu, dai livelli glicemici osceni,'\n"
                                  "'Dimmi, qual è la cosa che preferisci o a cui aneli?", 100, 'testo')
                        GlVar.psi_cosa = str("PSI " + input(Fore.YELLOW + Back.BLACK + "Scrivi la cosa che più ti piace o desideri: ")).title()
                        printslow("'E sia, che il potere di evocare il tuo più profondo desiderio ti sia concesso'", 150, 'testo')
                        printslow(f"Hai appreso {GlVar.psi_cosa}!", 80, 'testo')
                        GlVar.oggetti.append(GlVar.psi_cosa)
                        printslow("\n- Giù, non ti immagini che cazzo m'è appena successo...", 80, 'tommy')
                        printslow("- Ti sei pisciato sulle scarpe Tommà", 150, 'giulio')
                        printslow("Ti guardi i piedi. Hai le scarpe fradice.", 150, 'testo')
                        printslow("- Porca madonna.", 150, 'tommy')
                        printslow("- Tornamo a casa va', tanto ormai la giornata di lavoro è andata a schifìo.", 150, 'giulio')
                        GlVar.party.append('giulio')
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
              GlVar.timer += 0.5
              GlVar.forza += 1
              printslow("Ti metti a suonare la batteria. Quanto cazzo sei bravo! Forza + 1!", 150, 'testo')
              if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                  GlVar.final = orologio()
                  if GlVar.final == 'a':
                      jam_o_studio = False
                      part_end = True
                      collepaganello = False
                      GlVar.game_over = True
                      GlVar.continui = 'n'
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
              if 'mutandine' in GlVar.oggetti:
                GlVar.oggetti.remove('mutandine')
              printslow("E via col nostro caro vizietto. Sali in camera.", 150, 'testo')
              time.sleep(1.0)
              printslow("Ritrovi in un cassetto delle mutandine.\n"
                        "Immagini siano di Kiernan Shipka.", 150, 'testo')
              time.sleep(2.0)
              printslow("Sborri in due secondi netti.", 150, 'testo')
              printslow("U O O O O O O O O O O O R G H H G G H G H", 30, 'tommy')
              GlVar.forza += 1
              GlVar.timer += 0.5
              printslow("Ti riprendi dopo un riposino aftersex.", 150, 'testo')
              if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                  GlVar.final = orologio()
                  if GlVar.final == 'a':
                      part_end = True
                      collepaganello = False
                      GlVar.game_over = True
                      GlVar.continui = 'n'
                      continue
              printslow(f"Sono le {orologio()}", 150, 'testo')
              GlVar.oggetti.append('mutandine')
            elif cose_casa == 's':
              if 'occhiali' not in GlVar.oggetti:
                printslow("Ti avvicini lussurioso alla Switch. Sul mobiletto all'ingresso, noti un paio di occhiale da sole funky.", 150, 'testo')
                occhiali = input(Fore.YELLOW + Back.BLACK + "Provi gli occhiali? 'Y' o 'N': ").lower()
                if occhiali == 'y':
                  GlVar.oggetti.append('occhiali')
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
                  GlVar.timer += 2
                  if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                      GlVar.final = orologio()
                      if GlVar.final == 'a':
                          part_end = True
                          collepaganello = False
                          GlVar.game_over = True
                          GlVar.continui = 'n'
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
                  GlVar.game_over = True
                  GlVar.continui = 'n'
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
            if GlVar.samuel_flag:
              printslow("Vai verso San Giuseppe. \nC'è poco da fare: il Piano è il quartiere migliore di Fabriano.", 150, 'testo')
              printslow("- Se Sergio fosse di Fabriano, vivrebbe qui in quanto tra le persone migliori che conosco.", 150, 'tommy')
              time.sleep(0.5)
              printslow("Arrivi sotto casa di Samuel. Negli ultimi mesi è diventato ancora più elettronico, chissà se parlerà in codice binario ormai?", 150, 'testo')
              estathe = input(Fore.YELLOW + Back.BLACK + "Noti un estathè incastrato tra i sedili, vuoi prenderlo? 'Y' o 'N': ").lower()
              if estathe == 'y':
                GlVar.oggetti.append("estathe")
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
                GlVar.timer += 0.5
                r = RPG(GlVar.forza)
                if r:
                    GlVar.game_over = True
                    GlVar.continui = 'n'
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
                GlVar.timer += 2
                printslow(f"Apri gli occhi. Sono le {orologio()}.", 150, 'testo')
                printslow("- Merda.", 150, 'tommy')
                GlVar.samuel_flag = False
            else:
              printslow("- Che torno a fare?", 150, 'tommy')
            if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                GlVar.final = orologio()
                if GlVar.final == 'a':
                    Fabriano = False
                    GlVar.game_over = True
                    GlVar.continui = 'n'
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
                        if GlVar.soldi < 50:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            GlVar.timer += 0.5
                            GlVar.soldi -= 50
                            GlVar.oggetti.append('estathe')
                            printslow(f"Hai comprato un estathè, Sei rimasto con {GlVar.soldi}€.\n"
                                      f"La macchinetta segna le {orologio()}.", 200, 'testo')
                    elif acquisto_snack == 's' or acquisto_snack == 'b':
                        if GlVar.soldi < 100:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            GlVar.timer += 0.5
                            GlVar.soldi -= 100
                            GlVar.oggetti.append('merendina')
                            printslow(f"Hai comprato una fonte esagerata di zuccheri. Sei rimasto con {GlVar.soldi}€.\n"
                                      f"La macchinetta segna le {orologio()}.", 200, 'testo')
                    macchinetta = input(Fore.YELLOW + Back.BLACK + "Vuoi continuare a fare acquisti? 'Y' o 'N': ").lower()
            else:
                printslow("- No, non è il momento di merendare.", 150, 'tommy')
                offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi aprire marketplace magari? 'Y' o 'N': ").lower()
                if offerte == 'y':
                    s = compravendita()
                    if s:
                        Fabriano = False
                        GlVar.game_over = True
                        GlVar.continui = 'n'
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
                if GlVar.timer >= 6 and GlVar.cripi_flag:
                    GlVar.cripi_flag = False
                    printslow("Tra le nuove leve del Bar Mario c'è Cripi, che attacca a bere alle 14:00. Oggi è particolarmente unto,\n"
                              "e il sole gli riflette addosso.", 150, 'testo')
                    if 'occhiali' in GlVar.oggetti:
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
                        GlVar.timer += 0.5
                        GlVar.oggetti.append('pergamena')
                        printslow("Ti infili al bagno del Bar Mario per lavare via la pezza che ti ritrovi in mano. Piangi lacrime amare, e tu odi\n"
                                  "l'amaro. Al terzo strato di sudiciume che togli, noti che oltre ai pantaloni hai qualcos'altro in mano:\n"
                                  "sembrerebbe la carta d'identità di Diego.", 150, 'testo')
                        printslow("- Ma che cazzo...", 100, 'tommy')
                        if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                            GlVar.final = orologio()
                            if GlVar.final == 'a':
                                Fabriano = False
                                GlVar.game_over = True
                                GlVar.continui = 'n'
                                continue
                        printslow("Il documento è illeggibile: è ricoperto da capo a piedi da numeri e nomi di ragazze. Sembrerebbe che Cripi\n"
                                  "abbia utilizzato la carta d'identità come una sorta di pergamena su cui scrivere i suoi appunti.\n"
                                  "Decidi di tenerla, magari tra quei numeri c'è qualche baldracca buona.\n"
                                  f"Esci dal bagno. Sono le {orologio()}.", 150, 'testo')
                    elif GlVar.psi_cosa in GlVar.oggetti:
                        printslow("Non te la senti di affrontare Cripi e le sue manate sul culo. Appena si gira verso di te,\n"
                                  "chiami il potere di San Silvestro:\n", 150, 'testo')
                        printslow(f"- {GlVar.psi_cosa}!", 200, 'tommy')
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
                        GlVar.timer += 0.5
                        GlVar.oggetti.append('pergamena')
                    else:
                        printslow("Accecato dal riverbero, ti avvicini a guardia abbassata. Cripi ti nota e ti si fionda contro.\n"
                                  "Vuole cercare di prenderti il culo. Fai uno scatto all'ultimo mentre ti monta il terrore.", 150, 'tommy')
                        attacco_culo = random.randint(0, 100)
                        if attacco_culo > 10+(GlVar.forza*10):
                            printslow("- Nooooooooooooo!", 100, 'tommy')
                            printslow("Urli, mentre Cripi stringe la presa sulle tua chiappe di marshmallow.\n"
                                      "Sei umiliato, ti senti sporco e ti viene da piangere.\n"
                                      "Barcolli all'indietro, non riesci a stare in piedi.\n"
                                      "Mentre la vista ti si offusca, dedichi un ultimo messaggio mentale al mondo:", 150, 'testo')
                            printslow("- Vorrei... C-Chiavare... Mi-Mi-Misato...", 30, 'tommy')
                            printslow("Chiudi gli occhi. Sei stato sconfitto. Game over.", 150, 'testo')
                            GlVar.game_over = True
                            GlVar.continui = 'n'
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
                            GlVar.oggetti.append('pergamena')
                printslow("Entri dentro cercando di non farti vedere. Pare abbia funzionato.", 150, 'testo')
                macchinetta = 'y'
                while macchinetta == 'y':
                    acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Cosa vuoi? prenditi una mezz'oretta per selezionare.\n"
                                                                      "(E) Estathè:  100€\n"
                                                                      "(V) Vodka:    300€\n"
                                                                      "(N) Niente\n"
                                                                      "Scrivi l'iniziale di ciò che vuoi comprare: ").lower()
                    if acquisto_snack == 'v':
                        if GlVar.soldi < 300:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            GlVar.timer += 0.5
                            GlVar.soldi -= 300
                            GlVar.oggetti.append('vodka')
                            if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                GlVar.final = orologio()
                                if GlVar.final == 'a':
                                    macchinetta = 'False'
                                    Fabriano = False
                                    GlVar.game_over = True
                                    GlVar.continui = 'n'
                                    continue
                            printslow(f"Hai comprato una vodka, Sei rimasto con {GlVar.soldi}€.\n"
                                          f"L'orologio segna le {orologio()}.", 200, 'testo')
                    elif acquisto_snack == 'e':
                        if GlVar.soldi < 100:
                            printslow("Non te lo puoi permettere, stronzo.\n", 200, 'testo')
                        else:
                            GlVar.timer += 0.5
                            GlVar.soldi -= 100
                            GlVar.oggetti.append('estathe')
                            printslow(f"Hai comprato un estathè, Sei rimasto con {GlVar.soldi}€.\n"
                                      f"L'orologio segna le {orologio()}.", 200, 'testo')
                    macchinetta = input(Fore.YELLOW + Back.BLACK + "Vuoi continuare a fare acquisti? 'Y' o 'N': ").lower()
                printslow("Sembra che non ci sia nient'altro da fare, qua. Torni alla macchina.", 150, 'testo')
                GlVar.timer += 0.5
                if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                    GlVar.final = orologio()
                    if GlVar.final == 'a':
                        macchinetta = 'False'
                        Fabriano = False
                        GlVar.game_over = True
                        GlVar.continui = 'n'
                        continue
                printslow(f"Sono le {orologio()}", 150, 'testo')
            else:
                printslow("Vai verso il public passando per la cattedrale, evitando così la marmaglia del Bar Mario.\n"
                          "Ti affascina sempre la zona di San Venanzio, a lei sono legati ricordi dolceamari.\n"
                          "scendi in piazza.", 150, 'testo')
                printslow("- Ah ma oggi è martedì, il Public è chiuso. So' un coglione.", 150, 'tommy')
                if GlVar.forza >= 5 and 'andrea' in GlVar.party and GlVar.timer >= 10:
                    GlVar.endings += 1
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
                              f"Finale Albero delle Sbronze - Hai scoperto un finale! Ora sei a {GlVar.endings} su 7!", 150, 'testo')
                    GlVar.game_over = True
                    GlVar.continui = 'n'
                    Fabriano = False
                    continue

                printslow("Torni in macchina incazzato. Un'ora buttata.", 150, 'testo')
                GlVar.timer += 1
                if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                    GlVar.final = orologio()
                    if GlVar.final == 'a':
                        Fabriano = False
                        GlVar.game_over = True
                        GlVar.continui = 'n'
                        continue
                printslow(f"Sono le {orologio()}", 150, 'testo')

            hub2 = input(Fore.YELLOW + Back.BLACK + "Type 'S' se vuoi andare da Samuel,\n"
                                                    "Type 'P' se vuoi andare verso la Pisana,\n"
                                                    "Type 'B' se vuoi andare al Borgo: ").lower()

          elif hub2 == 'p':

              def hub2switcher():
                  GlVar.game_over = True
                  GlVar.continui = 'n'
                  global hub_piazzale
                  global Fabriano
                  hub_piazzale = False
                  Fabriano = False

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
                              if GlVar.soldi < 150:
                                  printslow("Il dottore ti guarda male. \n'- Non te lo puoi permettere, stronzo.'", 200, 'testo')
                                  macchinetta = False
                              else:
                                  GlVar.soldi -= 150
                                  GlVar.oggetti.append('merendina_rara')
                                  printslow(f"Hai comprato uno Scrofix, Sei rimasto con {GlVar.soldi}€.", 150, 'testo')
                                  acquisto_snack = input(Fore.YELLOW + Back.BLACK + "Vuoi comprarne un'altro? 'Y' o 'N': ").lower()
                          elif acquisto_snack != 'y':
                              macchinetta = False
                  elif piazzale == 'm':
                      s = compravendita()
                      if s:
                          hub2switcher()
                          continue
                  elif piazzale == 'a':
                      printslow("Decidi di suonare a casa di Agron.", 150, 'testo')
                      printslow("BZZZZZZZZZZZZ", 60, 'testo')
                      if GlVar.timer >= 10 and GlVar.agron_flag:
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
                              GlVar.agron_flag = False
                              GlVar.timer += 0.5
                              printslow("Fai ascoltare il passaggio che ti carica, ma ovviamente non ti puoi fermare lì.\n"
                                        "Parti con una megarullata che mischia 3/4, 5/8 e 11/16: inascoltabile, letteralmente una tortura di Guantanamo.\n"
                                        "Agron ti guarda, lo vedi male, sta impallidendo. Cerchi di caricarlo facendo dei gesti ritmici con la mano, ma è troppo tardi:\n"
                                        "Agron spalanca la portiera, vomita e infine torna a casa.", 150, 'testo')
                              time.sleep(1.0)
                              if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                  GlVar.final = orologio()
                                  if GlVar.final == 'a':
                                      hub2switcher()
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
                                  GlVar.timer += 0.5
                                  GlVar.agron_flag = False
                                  printslow("Dopo aver scelto canzoni tristi e essere andato nei peggiori bar di fabriano, Agron è malinconico e tu ti sei rovinato il compleanno. Riporti a casa il tuo amico colorato.\n"
                                            "Appena uscito dalla macchina, la iella delle canzoni che hai scelto lo fa investire da tre macchine di fila.\n"
                                            "Guardi ciò che rimane di Agron (ovvero una striscia rosso-bruna lunga tutto Piazzale Matteotti) e sospiri: ", 150, 'testo')
                                  printslow("- Vabbè sono sicuro che se ne sarebbe voluto andare così, tra musica triste e amici. Ciao Ag.", 150, 'tommy')
                                  if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                      GlVar.final = orologio()
                                      if GlVar.final == 'a':
                                          hub2switcher()
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                                  GlVar.dead_party.append('agron')
                                  s = finale_genocide(GlVar.dead_party)
                                  if s == 'a':
                                      hub2switcher()
                                      continue
                              else:
                                  GlVar.agron_flag = False
                                  printslow("Cazzo che bomba di serata! La musica è stata fighissima e già siete mezzi brilli.\n"
                                            "Carichissimo, ti prepari: il party sta per iniziare!\n"
                                            "                                             \n"
                                            "Agron si unisce al party!", 150, 'testo')
                                  GlVar.party.append('agron')
                                  GlVar.timer += 0.5
                                  if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                      GlVar.final = orologio()
                                      if GlVar.final == 'a':
                                          hub2switcher()
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                      else:
                        printslow("Non risponde nessuno.", 150, 'testo')
                        if GlVar.timer < 10:
                            if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                GlVar.final = orologio()
                                if GlVar.final == 'a':
                                    hub2switcher()
                                    continue
                            printslow(f"- In effetti è presto, sono le {orologio()}, perché sono qua? \n"
                                      "- Forse perché so' un coglione!", 150, 'tommy')
                            offerte = input(Fore.YELLOW + Back.BLACK + "Vuoi ammazzare il tempo aprendo marketplace? 'Y' o 'N': ").lower()
                            if offerte == 'y':
                                s = compravendita()
                                if s:
                                    hub2switcher()
                                    continue
                  else:
                      printslow("Vai da Piazzale Matteotti al centro.", 150, 'testo')
                      if GlVar.timer >= 8 and GlVar.dialogo1_andrea and not GlVar.dead_andrea:
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
                              GlVar.dead_party.append('andrea')
                              s = finale_genocide(GlVar.dead_party)
                              if s == 'a':
                                  hub2switcher()
                                  continue
                              GlVar.dead_andrea = True
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
                              GlVar.dialogo1_andrea = False
                      elif GlVar.timer >= 8 and not GlVar.dialogo1_andrea and quest_andrea:
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
                              elif domanda_mago == 'd' and 'estathe' in GlVar.oggetti and 'vodka' in GlVar.oggetti and 'mutandine' in GlVar.oggetti:
                                  quest_andrea = False
                                  GlVar.timer += 0.5
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
                                  GlVar.party.append('andrea')
                                  time.sleep(1.0)
                                  printslow("Andrea, il Mago del Crespuscolo, si unisce al party!", 100, 'testo')
                                  if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                      GlVar.final = orologio()
                                      if GlVar.final == 'a':
                                          hub2switcher()
                                          continue
                                  printslow(f"Sono le {orologio()} mentre ti avvii verso il Centro.", 150, 'testo')
                              elif domanda_mago == 'd' and 'estathe' not in GlVar.oggetti and 'vodka' not in GlVar.oggetti and 'mutandine' not in GlVar.oggetti:
                                  printslow("- Torna quando avrai trovato tutti gli ingredienti, giovane padawan.", 100, 'andrea')
                              elif domanda_mago == 'p' and 'pergamena' in GlVar.oggetti:
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
                                  if GlVar.timer % 2 == 0 and int(GlVar.timer) >= 2:
                                      GlVar.final = orologio()
                                      if GlVar.final == 'a':
                                          hub2switcher()
                                          continue
                                  printslow(f"Sono le {orologio()}", 150, 'testo')
                                  GlVar.party.append('andrea')
                                  quest_andrea = False
                              elif domanda_mago == 'p' and 'pergamena' not in GlVar.oggetti:
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
              for i in range(0, 10):
                  printslow("Porcoddio coglione che cazzo vai al Borgo?\n"
                            "Ti ho chiesto se vuoi andare AL BORGO, non a Pusherland.\n"
                            "Porcoddio mi fai bestemmià. Ti meriti un cazzo di Game Over.", 2000, 'testo')
              GlVar.game_over = True
              GlVar.continui = 'n'
              Fabriano = False
              continue
    GlVar.continui = input("Game Over, vuoi ricominciare? 'Y' o 'N': ").lower()
    if GlVar.continui == 'y':
        GlVar.game_over = False
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