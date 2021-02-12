import os
import csv, json
import orodja
import time


STEVILO_PRENOSOV = 20
directory_companies = 'zajeti podatki posameznih podjetij'
pot_do_repozitorija = os.path.dirname(__file__) 

orodja.pripravi_imenik(directory_companies)

with open(os.path.join(pot_do_repozitorija,'zajeti_podatki','stevilo_prenesenih_podjetij.json'), 'r+', encoding='utf-8') as json_file:
    # Tukaj dostopomo do števila do sedaj prenesenih podatkov. in ga nato zvišamo za ŠTEVILO_PRENOSOV
    slovar_vsebine = json.load(json_file)[0]
    stevilo_dosedanjih_prenosov = slovar_vsebine["stevilo_dosedanjih_prenosov"]
    nov_slovar = {"stevilo_dosedanjih_prenosov": stevilo_dosedanjih_prenosov + STEVILO_PRENOSOV}
    
    json_file.seek(0)
    json_file.truncate(0)
    json.dump([nov_slovar], json_file, indent=4 , ensure_ascii=False)
    
    with open(os.path.join(pot_do_repozitorija,'urejeni_podatki', 'lestvica_podjetij.csv'), newline='', encoding='utf-8') as csv_mapa:
        bralec = csv.reader(csv_mapa)

        for vrstica in bralec:
            if vrstica[0] == 'mesto':
                pass
            elif int(vrstica[0]) > stevilo_dosedanjih_prenosov and int(vrstica[0]) <= stevilo_dosedanjih_prenosov + STEVILO_PRENOSOV:
                
                ime_datoteke = vrstica[1]
                ime_podjetja = orodja.obdelaj_ime_podjetja(vrstica[1]) #ime podjetja je treba ustrezno pretvoriti, da ustreza ključu, na internetnem naslovu.
                url = f'https://www.forbes.com/companies/{ime_podjetja}/'

                orodja.shrani_spletno_stran(url, directory_companies, ime_datoteke)

    

        
