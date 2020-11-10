import re, os
import orodja

file_name = "Spletna stran.html"
directory = 'zajeti_podatki'
directory_companies = 'podatki posameznih podjetij'



vzorec = (
r'<td class="rank">#(?P<mesto>\d+).*\n'
r'.*?exit_trigger_set">(?P<ime>.*?)</a>.*\n'
r'<td>(?P<drzava>.*)?</td>\n'
r'<td>\$(?P<prodaja>.*)?</td>\n'
r'<td>\$(?P<profit>.*)?</td>\n'
r'<td>\$(?P<premozenska_vrednost>.*)?</td>\n'
r'<td>\$(?P<trzna_cena>.*)?</td>'
)



with open(os.path.join(directory, file_name) , 'r', encoding='utf-8') as spletna_stran:
    vsebina = spletna_stran.read()
    seznam_podjetij = [] 
    
    for podjetje in re.finditer(vzorec, vsebina):
        slovar_podjetja = {}
        for polje in podjetje.groupdict().keys():
            if  polje in ['prodaja', 'profit', 'premozenska_vrednost', 'trzna_cena']:            # Nekatere številske vrednosti moramo predelati, tako da bodo brez okrajšav, to naredi funkcija vrednost_stevila.
                slovar_podjetja[polje] = str(orodja.vrednost_stevila(podjetje.group(polje)))
            else:
                slovar_podjetja[polje] = podjetje.group(polje)
        seznam_podjetij.append(slovar_podjetja)
    
    imena_polj = ['mesto', 'ime', 'drzava', 'prodaja', 'profit', 'premozenska_vrednost', 'trzna_cena']
    orodja.zapisi_csv(seznam_podjetij, imena_polj, 'urejeni_podatki','lestvica_podjetij.csv')
    
        
        


    


    ######   To je stara koda   #######

    # orodja.pripravi_imenik(directory_companies) 
    # for podjetje in re.finditer(vzorec, vsebina):
    #     ime_podjetja = podjetje.group('ime').lower().replace('&' , '').strip().replace(' ', '-')
    #     ime_datoteke = podjetje.group('ime')

    #     url = f'https://www.forbes.com/companies/{ime_podjetja}/'

    #     orodja.shrani_spletno_stran(url, directory_companies, ime_datoteke)

