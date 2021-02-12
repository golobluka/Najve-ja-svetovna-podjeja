# V tej mapi sem prvič pobral podatke, in preko teh podatkov nato dostopal do spletnih strani posameznih podjetij (v postopni_zajem) in nato še te uradil v csv zapis (cvs_generator_2).

import re, os
import orodja

file_name = "Spletna stran.html"
directory = 'zajeti_podatki'
directory_companies = 'podatki posameznih podjetij'
imena_polj = ['mesto', 'ime', 'drzava', 'prodaja_B', 'profit_B', 'premozenska_vrednost_B', 'trzna_cena_B']


vzorec = (
r'<td class="rank">#(?P<mesto>\d+).*\n'
r'.*?exit_trigger_set">(?P<ime>.*?)</a>.*\n'
r'<td>(?P<drzava>.*)?</td>\n'
r'<td>\$(?P<prodaja_B>.*)?</td>\n'
r'<td>\$(?P<profit_B>.*)?</td>\n'
r'<td>\$(?P<premozenska_vrednost_B>.*)?</td>\n'
r'<td>\$(?P<trzna_cena_B>.*)?</td>'
)

with open(os.path.join(directory, file_name) , 'r', encoding='utf-8') as spletna_stran:
    vsebina = spletna_stran.read()
    seznam_podjetij = [] 
    
    for podjetje in re.finditer(vzorec, vsebina):
        slovar_podjetja = {}
        for polje in podjetje.groupdict().keys():
            if  polje in ['prodaja_B', 'profit_B', 'premozenska_vrednost_B', 'trzna_cena_B']:            # Nekatere številske vrednosti moramo predelati, tako da bodo brez okrajšav, to naredi funkcija vrednost_stevila.
                slovar_podjetja[polje] = str(orodja.vrednost_stevila(podjetje.group(polje)))
            else:
                slovar_podjetja[polje] = podjetje.group(polje)
        seznam_podjetij.append(slovar_podjetja)
    
    orodja.zapisi_csv(seznam_podjetij, imena_polj, 'urejeni_podatki','lestvica_podjetij.csv')
    
        


    ######   To je stara koda   #######

    # orodja.pripravi_imenik(directory_companies) 
    # for podjetje in re.finditer(vzorec, vsebina):
    #     ime_podjetja = podjetje.group('ime').lower().replace('&' , '').strip().replace(' ', '-')
    #     ime_datoteke = podjetje.group('ime')

    #     url = f'https://www.forbes.com/companies/{ime_podjetja}/'

    #     orodja.shrani_spletno_stran(url, directory_companies, ime_datoteke)

