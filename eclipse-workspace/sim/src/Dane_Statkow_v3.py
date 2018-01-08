'''
Created on 8 sty 2018

@author: student
'''

# coding: utf-8

# In[8]:

#Python 2.7
#Krzysztof Skutecki
#Symulator Bitwy Ogame

import random
from random import *

class DaneStatkow(object):
    '''klasa zawierajaca wszelkie dane'''
    def __init__(self):
        '''inicjalizacja-pliki'''
        self.DaneStatkow = self.get_DaneStatkow()[1:]
        self.szybkie_dziala = self.get_szybkie_dziala()[1:]
        self.statki = self.get_skrot()

    def get_DaneStatkow(self):
        '''pobranie danych stakow'''
        DaneStatkow = []
        with open('dane_statkow.txt') as f:
            for line in f:
                statek = line.strip().split()
                for i in range(len(statek)):
                    if statek[i].isdigit():
                        statek[i] = int(statek[i])
                DaneStatkow.append(statek)
        return DaneStatkow

    def get_szybkie_dziala(self):
        '''pobranie szybkich dzial'''
        with open('szybkie_dziala.txt') as f:
            return [list(line.strip().split()) for line in f]

    def get_skrot(self):
        '''skroty statkow'''
        return [i[0] for i in self.DaneStatkow]


    
#--------------------------------------------------------------------------------------------


class Statek():
    '''Stworzenie klasy statek'''
    def __init__(self, DaneStatkow, statki, szybkie_dziala):
        '''inicjalizacja statku z parametrami'''
        self.statki = statki
        self.skrot = DaneStatkow[0]
        self.hp = DaneStatkow[2]
        self.tarcza = DaneStatkow[3]
        self.atak = DaneStatkow[4]
        self.destroy = False
        self.DaneStatkow = DaneStatkow
        self.szybkie_dziala = szybkie_dziala

    def __str__(self):
        '''podstawowy opis statku'''
        return "{}  hp: {}  tarcza: {}  atak: {}".format(self.skrot, self.hp, self.tarcza, self.atak)

    def shoot(self, other):
        '''funkcja obslugujaca strzelanie statku'''
        if self.atak > (other.tarcza * 0.01):
            if (other.tarcza - self.atak) > 0:
                other.tarcza -= self.atak
            else:
                other.tarcza = 0
                temp = self.atak - other.tarcza
                other.hp -= temp
                
            if (other.hp / float(other.DaneStatkow[2])) < 0.7:
                x = random()
                chance = 1 - ((other.hp) / float(other.DaneStatkow[2]))
                if x < chance:
                    other.hp = 0

            if self.fastguns(other):
                return True
            return False

    def fastguns(self, other):
        '''funkcja obslugujaca szybkie dziala'''
        L = self.szybkie_dziala[self.statki.index(other.skrot) + 1]
        chance = 1 - 1/float(L)
        return (chance > random())


#-------------------------------------------------------------------------------------------------------

class Symulator(DaneStatkow):
    '''Klasa korzystajaca z klasy Statek i DaneStatkow obslugujaca symulator wlasciwy'''
    
    def __init__(self):
        '''inicjalizacja - stworzenie floty1 i floty2'''
        DaneStatkow.__init__(self)
        self.koniec_bitwy = False
        
        self.flota1 = []
        with open('flota_1.txt') as f:
            for i in f:
                elem = i.strip().split()
                if len(elem) == 2 and elem[1].isdigit():
                    if int(elem[1]) != 0:
                        self.flota1.append(elem)
        #print self.flota1, " Flota 1"
        self.Instancja(self.flota1)
        
        self.flota2 = []
        with open('flota_2.txt') as f:
            for i in f:
                elem = i.strip().split()
                if len(elem) == 2 and elem[1].isdigit():
                    if int(elem[1]) != 0:
                        self.flota2.append(elem)
        #print self.flota2, " Flota 2"
        self.Instancja(self.flota2)
        
    def stan_floty(self, flota):
        '''wypisanie stanu floty'''
        for type in flota:
            for i in type:
                print(i)

    def Instancja(self, flota):
        '''Stworzenie instancji statku'''
        for i in range(len(flota)):
            for j in range(int(flota[i][1])):
                statki = (self.DaneStatkow[self.statki.index(flota[i][0])])
                szybkie_dziala = (self.szybkie_dziala[self.statki.index(flota[i][0])])
                flota[i].append(Statek(statki, self.statki, szybkie_dziala))
        return flota
    
    def czyszczenie(self, flota, numer_floty):
        '''Czyszczenie zniszczonych statkow'''
        count = 0
        for i in flota:
            L = []
            for k in i:
                if type(k).__name__ == 'instance':
                    if k.hp > 0:
                        k.tarcza = k.DaneStatkow[3]
                        L.append(k)
            flota[count] = i[:2] + L
            count += 1;

        if len(flota) <= 1 and len(flota[0]) == 2:
            return True
        else:
            temp = []
            for i in range(len(flota)):
                if len(flota[i]) != 2:
                    temp.append(flota[i])
            flota = temp
            if numer_floty == 1:
                self.flota1 = flota
            else:
                self.flota2 = flota
            return False

    def start(self):
        '''rozpoczecie walki (max 6 rund)
        co runde zniszczone statki sa usuwane
        mozliwy overkill'''
        runda = 0
        while (runda != 5):
           
            for i in self.flota1:
                for k in i:
                    if type(k).__name__ == 'instance':
                        while (True): 
                            Max = 0
                            SzansaTrafienia = [[100, 99]]
                            for i in self.flota2:
                                Max += len(i[2:])
                            Max *= 1.0
                            x = 0
                            for i in self.flota2:
                                SzansaTrafienia.append([((len(i[2:]))/Max)*100, x])
                                x +=1 
                                
                            SzansaTrafienia.append([0,99])
                            SzansaTrafienia = sorted(SzansaTrafienia, key=lambda SzansaTrafienia: SzansaTrafienia[0])
                            x = randint(0, 100)
                            if len(SzansaTrafienia) == 3:
                                WylosowanyStatek = 0
                            else:
                                for i in range(1, len(SzansaTrafienia)-1):
                                    if x > SzansaTrafienia[i-1][0] and x < SzansaTrafienia[i][0]:
                                        WylosowanyStatek = SzansaTrafienia[i][1]
                                        break
                            wrog = self.flota2[WylosowanyStatek]
                            x = randint(2, len(wrog)-1)
                            WylosowanyStatek = wrog[x]
                            attackResult = k.shoot(WylosowanyStatek)
                            if not attackResult:
                                break
                                
            for i in self.flota2:
                for k in i:
                    if type(k).__name__ == 'instance':
                        while (True):
                            Max = 0
                            SzansaTrafienia = [[100, 99]]
                            for i in self.flota1:
                                #print len(i)
                                Max += len(i[2:])
                            Max *= 1.0
                            x = 0
                            for i in self.flota1:
                                SzansaTrafienia.append([((len(i[2:]))/Max)*100, x])
                                x +=1 
                                
                            SzansaTrafienia.append([0,99])
                            SzansaTrafienia = sorted(SzansaTrafienia, key=lambda SzansaTrafienia: SzansaTrafienia[0])
                            x = randint(0, 100)
                            if len(SzansaTrafienia) == 3:
                                WylosowanyStatek = 0
                            else:
                                for i in range(1, len(SzansaTrafienia)-1):
                                    if x > SzansaTrafienia[i-1][0] and x < SzansaTrafienia[i][0]:
                                        WylosowanyStatek = SzansaTrafienia[i][1]
                                        break
                            wrog = self.flota1[WylosowanyStatek]
                            x = randint(2, len(wrog)-1)
                            WylosowanyStatek = wrog[x]
                            if not k.shoot(WylosowanyStatek):
                                break
            '''                    
            #self.stan_floty(self.flota1)
            #self.stan_floty(self.flota2)
            for i in self.flota1:
                print(i[0], len(i[2:]))
            for i in self.flota2:
                print(i[0], len(i[2:]))
            print "Before czyszczenie"
            for i in self.flota1:
                print(i[0], len(i[2:]))
            for i in self.flota2:
                print(i[0], len(i[2:]))
            print "After czyszczenie"
            '''
            self.czyszczenie(self.flota1, 1)
            self.czyszczenie(self.flota2, 2)
            
            
            runda += 1
            self.wynik(runda)
            if self.koniec_bitwy == True:
                break

    def wynik(self, runda):
        '''Wywolanie na ekran podsumowania kazdej rundy z bitwy'''
        print ('=======================') 
        print("||      RUNDA {}      ||").format(runda)
        print ('=======================') 
        print("Flota PIERWSZA: ")
        if len(self.flota1) <= 1 and len(self.flota1[0]) == 2:
            print("ZNISZCZONA!!!")
            self.koniec_bitwy = True
        else:
            for i in self.flota1:
                print(i[0], len(i[2:]))
        print ('---------------------')
        print("Flota DRUGA: ")
        if len(self.flota2) <= 1 and len(self.flota2[0]) == 2:
            print("ZNISZCZONA!!!")
            self.koniec_bitwy = True
        else:
            for i in self.flota2:
                print(i[0], len(i[2:]))
        print ('\n\n')
        






S = Symulator()
S.start()


# In[ ]:




# In[ ]:


