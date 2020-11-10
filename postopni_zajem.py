import os
import csv
import orodja
import time


STEVILO_PRENOSOV = 20
directory_companies = 'zajeti podatki posameznih podjetij'

orodja.pripravi_imenik(directory_companies)

with open(os.path.join('zajeti_podatki','stevilo_prenesenih_podjetij.txt'), 'r+', encoding='utf-8') as txt_mapa:
    stevilo_dosedanjih_prenosov = int(txt_mapa.read()[-27 : -25])
    txt_mapa.write('\n' + str(STEVILO_PRENOSOV + stevilo_dosedanjih_prenosov) + ' ' + time.asctime())

    with open(os.path.join('urejeni_podatki', 'lestvica_podjetij.csv'), newline='', encoding='utf-8') as csv_mapa:
        bralec = csv.reader(csv_mapa)

        for vrstica in bralec:
            if vrstica[0] == 'mesto':
                pass
            elif int(vrstica[0]) > stevilo_dosedanjih_prenosov and int(vrstica[0]) <= stevilo_dosedanjih_prenosov + STEVILO_PRENOSOV:
                
                ime_podjetja = orodja.obdelaj_ime_podjetja(vrstica[1]) #ime podjetja je treba ustrezno pretvoriti, da ustreza ključu, na internetnem naslovu.
                url = f'https://www.forbes.com/companies/{ime_podjetja}/'

                orodja.shrani_spletno_stran(url, directory_companies, ime_datoteke)

    

        
