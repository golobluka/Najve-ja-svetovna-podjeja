import re 
import requests, os, sys
import csv, json

def pripravi_imenik(ime_datoteke):
    '''Če še ne obstaja, pripravi prazen imenik za dano datoteko.'''
    if os.path.isfile(ime_datoteke):
            print('shranjeno že od prej!')
            return
    
    os.makedirs(ime_datoteke, exist_ok=True)

def shrani_spletno_stran(url,directory, ime_datoteke):
    '''Vsebino strani na danem naslovu shrani v datoteko z danim imenom.'''
    try:
        print('Shranjujem {} ...'.format(url), end='')
        sys.stdout.flush()
        
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        print('stran ne obstaja!')
    else:
        with open(os.path.join(directory,ime_datoteke), 'w', encoding='utf-8') as datoteka:
            datoteka.write(r.text)
            print('shranjeno!')

def zapisi_csv(slovarji, imena_polj, ime_datoteke, ime_mape):
    '''Iz seznama slovarjev ustvari CSV datoteko z glavo.'''
    pripravi_imenik(ime_datoteke)
    with open(os.path.join(ime_datoteke, ime_mape), 'w', newline='', encoding='utf-8') as csv_datoteka:
        writer = csv.DictWriter(csv_datoteka, fieldnames=imena_polj)
        writer.writeheader()
        for slovar in slovarji:
            writer.writerow(slovar)

def vrednost_stevila(string_stevila):
    ''' Pretvarja okrajšan string števila, v čisto numerično vrednost.'''
    string_stevila = string_stevila.replace(',', '')
    
    if string_stevila.count('B') == 1:
        stevilo = float(string_stevila.replace('B', '').strip()) 
    elif string_stevila.count('M') == 1:
        stevilo = float(string_stevila.replace('M', '').strip()) * 10 **(-3)

    return stevilo

def obdelaj_ime_podjetja(ime):
    ''' Funkcija obdela ime, da ustreza imenu povezave do podjetja na spletu. '''
    ime_z_malimi = ime.lower()
    ime_brez_posebnih_znakov = ime_z_malimi.replace('&amp;' , '').replace('&', '').replace('(', '').replace('é', 'e').replace('ú', 'u').replace(')' , '')
    ime_obdelani_presledki = ime_brez_posebnih_znakov.strip().replace('  ' , ' ' ).replace(' ', '-')

    return ime_obdelani_presledki
