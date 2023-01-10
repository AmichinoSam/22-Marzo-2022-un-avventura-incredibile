import time
import colorama
from colorama import Fore, Back, Style
from printing import printslow
import GlVar

def finale_genocide(sans):
    if 'andrea' in sans and 'giulio' in sans and 'agron' in sans and 'samuel' in sans:
        GlVar.endings += 1
        printslow("Birds are singing, flowers are blooming...\n"
                  "On days like these, kids like you...\n"
                  "Should be burning in hell.\n"
                  " \n", 50, 'testo')
        printslow(sansprint, 450, 'testo')
        time.sleep(1.0)
        printslow(f"\nFinale Genocide - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
        return 'a'

def finale_soldi(money):
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
        GlVar.endings += 1
        printslow("Lo ricorderai come il compleanno più bello della tua vita.\n"
                  f"Ending Spaziale - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
        return 'a'

def finale_triste():
    GlVar.endings += 1
    printslow(
        "Ormai dopo quest'ora non si farà vedere più nessuno. Sei triste, non pensavi che avresti passato il compleanno da solo.\n"
        "Vabbè, per rincuorarti un po', apri marketplace. C'è un messaggio da qualcuno che vuole comprare un tuo piatto:\n"
        "'Salve Tommaso, sono il Signor Panazzi. Sono qui con tutti gli altri per dirti che questo gioco non è una speedrun,\n"
        "quindi prenditi più tempo per esplorarlo meglio. Immaginalo come un Groundhog Day, e che ora potrai ricominciarlo da capo.\n"
        "Mi raccomando, non mollare!'", 150, 'testo')
    printslow(f"Bad Ending - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
    return 'a'

def finale_neutro():
    GlVar.endings += 1
    printslow("Decidi di andare coi tuoi amici a prendere una cosa.\n"
              "La serata procede bene, sei felice, ma a un tratto ricevi un messaggio:\n"
              "'Salve Tommaso, sono il Signor Panazzi. Sono qui con tutti gli altri per dirti che questo gioco non è una speedrun,\n"
              "quindi prenditi più tempo per esplorarlo meglio. Immaginalo come un Groundhog Day, e che ora potrai ricominciarlo da capo.\n"
              "Mi raccomando, non mollare!'", 150, 'testo')
    printslow(f"Neutral Ending - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
    return 'a'

def finale_buono():
    GlVar.endings += 1
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
        printslow(f"Good Ending - Hai sbloccato {GlVar.endings} finali su 7!", 150, 'testo')
        return 'a'
    else:
        printslow("Sei troppo carico e quindi decidi di non mangiare la torta perché vuoi assolutamente suonare. \n"
                  "Il sig. Panazzi cerca di convincerti, ma tu persisti e non vuoi mangiare. \n"
                  "Il sig. Panazzi diventa paonazzo, tira fuori il cazzo e inizia a volare. \n"
                  "Bestemmia tutte le divinità dello scibile umano e uccide tutti i tuoi amici davanti ai tuoi occhi.",
                  150, 'testo')
        return 'a'
