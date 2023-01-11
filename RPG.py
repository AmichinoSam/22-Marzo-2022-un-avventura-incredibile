from colorama import Fore, Back, Style
import time, random
from Finali import finale_genocide
from printing import printslow
import GlVar

# GDR
def RPG(mod_forza):
    printslow("Lo schermo, ondulante in un mélange di tinte acide, ti dà il benvenuto:", 150, 'testo')
    game_over_rpg = False
    while not game_over_rpg:
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
        GlVar.timer += 0.5
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
                            if 'merendina' in GlVar.oggetti:
                                printslow("Mangi una merendina. Recuperi 20HP!", 150, 'testo')
                                current_hp_tommy += 20
                                GlVar.oggetti.remove('merendina')
                            elif 'estathe' in GlVar.oggetti:
                                printslow("Bevi un estathe. Recuperi 20HP!", 150, 'testo')
                                current_hp_tommy += 20
                                GlVar.oggetti.remove('estathe')
                            elif 'merendina_rara' in GlVar.oggetti:
                                printslow("Mangi uno Scrofix. Yum! Recuperi 30HP e ti senti fortissimo!", 150, 'testo')
                                current_hp_tommy += 30
                                GlVar.forza += 1
                                GlVar.oggetti.remove('merendina_rara')
                            else:
                                printslow("Non hai snack da consumare.", 150, 'testo')
                        elif turno_tommy == 'm':
                            if GlVar.psi_cosa in GlVar.oggetti:
                                if nemico == 'Il Signor Panazzi':
                                    printslow(f"'{GlVar.psi_cosa} non ha nessun potere su di me!'", 150, 'testo')
                                else:
                                    printslow(f"Evochi il potere della magia {GlVar.psi_cosa}!\n"
                                              "****SDRSHH!****\n"
                                              f"{nemico} è sconfitto!", 150, 'testo')
                                    GlVar.oggetti.remove(GlVar.psi_cosa)
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
                                    GlVar.party.append('samuel')
                                    GlVar.samuel_flag = False
                                    return GlVar.samuel_flag
                                    game_over_rpg = True
                        if nemici[nemico][3] and not palinuro_death:
                            # i nemici potrebbero utilizzare sempre lo stesso calcolo per le azioni, cambiando solo l'effetto delle mosse #
                            time.sleep(0.5)
                            printslow(f"Tocca a {nemico}!", 150, 'testo')
                            time.sleep(0.5)
                            azione_nemico = ["attacco", "attacco", "attacco", "attacco", "special"]
                            turno_nemico = random.choice(azione_nemico)
                            if turno_nemico == "special" and current_hp_nemico <= int(nemici[nemico][0] / 4):
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
                GlVar.samuel_flag = False
                printslow(
                    "Decidi di lasciare Samuel nel synth. In fondo avrebbe voluto andarsene così, tra musica e amici.",
                    150, 'testo')
                printslow("- Vabbè io ci ho provato. Ovviamente il videogioco da cui devo liberare Samuel\n"
                          "è a cazzo di difficoltà hardcore, porcoddio.", 150, 'tommy')
                printslow(f"Esci da casa di Samuel.", 150, 'testo')
                GlVar.dead_party.append('samuel')
                s = finale_genocide(GlVar.dead_party)
                if s == 'a':
                    return 'a'
                time.sleep(1.0)
                return GlVar.samuel_flag