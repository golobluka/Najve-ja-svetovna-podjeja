import re, os
import orodja
import csv

imena_polj = ['ime', 'panoga', 'leto_ustanovitve', 'stevilo_zaposlenih']

vzorec = (
    r'>Industry.*?value\">(?P<panoga>.*?)</span>'
    r'.*?Founded.*?value\">(?P<leto_ustanovitve>.*?)</span>'
    r'.*?Employees.*?value\">(?P<stevilo_zaposlenih>.*?)</span>'
)

#### Pomožni funkciji ####

def pretvori_zapis(stevilo):
    return stevilo.replace(',', '')

def preberi_podatke_podjetja(ime_podjetja):
    naslov = os.path.join('zajeti podatki posameznih podjetij', ime_podjetja)
    if os.path.isfile(naslov):
        with open(os.path.join('zajeti podatki posameznih podjetij', ime_podjetja ), 'r', encoding='utf-8') as spletna_stran_pdjetja:
            vsebina = spletna_stran_pdjetja.read()

            for ponovitev in re.finditer(vzorec, vsebina):
                return ponovitev.groupdict()
    else: 
        return None

#### main ####

with open(os.path.join('urejeni_podatki', 'lestvica_podjetij.csv'), 'r', newline='', encoding='utf-8') as mapa_z_imeni_podjetij:
    bralec = csv.reader(mapa_z_imeni_podjetij)
    seznam_slovarjev_podjetij = []
    seznam_vseh_podjetij = []

    for vrstica in bralec:
        if vrstica[0] == 'mesto':
            pass
        else:
            slovar_podjetja = preberi_podatke_podjetja(vrstica[1])
            if slovar_podjetja:
                slovar_podjetja["stevilo_zaposlenih"] = pretvori_zapis(slovar_podjetja["stevilo_zaposlenih"])
                slovar_podjetja['ime'] = vrstica[1]
                seznam_slovarjev_podjetij.append(slovar_podjetja)
            seznam_vseh_podjetij.append(slovar_podjetja)

    orodja.zapisi_csv(seznam_slovarjev_podjetij, imena_polj, 'urejeni_podatki','lestvica_podjetij_2.csv')
    print(seznam_vseh_podjetij)



    
    
        