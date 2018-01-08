# -*- coding: utf-8 -*-
import numpy, time

'''Labirynt_V3
nowsza wersja poprzedniego labiryntu, program wyznacza sciezke w labiryncie 
z punktu startowego "@" do punktu koncowego "$". Przebyta droge zaznacza "*" 
WAZNE: Programowi daleko do optymalnosci - nie wykorzystuje on rekurencji!'''

class Labirynt:
    def __init__(self):
        with open('labirynt6.txt') as f:
            self.lines = f.readlines()
            self.done = False
        self.tab = []
        #print self.lines
        
    def findstart(self):
        '''Funkcja znajdujaca start "@" '''
        x = self.lines[0]
        wys = ''
        szer = ''
        bl = True
        for i in range(len(x)):
            if x[i] <> ' ' and bl == True:
                wys = wys + x[i]
            if x[i] == ' ' and bl == True:
                bl = False
            if x[i] <> ' ' and bl == False:
                szer = szer + x[i]
        wys = int(wys)
        szer = int(szer)
        x = numpy.empty((szer, wys), dtype=object)
        for i in range(1,wys+1):
            for j in range(szer):
                if self.lines[i][j] == '@':
                    poczatek = [i,j]
                x[j][i-1] = str(self.lines[i][j])
        self.start = poczatek
        self.lines = x
        poczatek[0], poczatek [1] = poczatek[1], poczatek[0]
        poczatek[1] -= 1
        self.position = poczatek
        return poczatek
    
    def find_path_no_recursion(self):
        '''funkcja niewykorzystujaca rekurencji - zapamietuje wyjscia
        z kazdej pozycji i wrzuca je do listy, potem rusuje droge 
        pobierajac wspolrzedne ostatniej wolnej lokacji'''
        #print self.tab
        temp = []
        x = self.position[0]
        y = self.position[1]
        if self.lines[x+1][y] == ' ':
            temp.append(x+1)
            temp.append(y)
            self.tab.append(temp)
            temp = []
        if self.lines[x][y-1] == ' ':
            temp.append(x)
            temp.append(y-1)
            self.tab.append(temp)
            temp = []
        if self.lines[x-1][y] == ' ':
            temp.append(x-1)
            temp.append(y)
            self.tab.append(temp)
            temp = []
        if self.lines[x][y+1] == ' ':
            temp.append(x)
            temp.append(y+1)
            self.tab.append(temp)
            temp = []
            
        while len(self.tab) != 0:
            self.position = self.tab.pop()
            x = self.position[0]
            y = self.position[1]
            self.lines[x][y] = '*'
            temp = []
            if self.lines[x+1][y] == ' ':
                temp.append(x+1)
                temp.append(y)
                self.tab.append(temp)
                temp = []
            if self.lines[x][y-1] == ' ':
                temp.append(x)
                temp.append(y-1)
                self.tab.append(temp)
                temp = []
            if self.lines[x-1][y] == ' ':
                temp.append(x-1)
                temp.append(y)
                self.tab.append(temp)
                temp = []
            if self.lines[x][y+1] == ' ':
                temp.append(x)
                temp.append(y+1)
                self.tab.append(temp)
                temp = []
            if self.lines[x+1][y] == '$' or self.lines[x][y-1] == '$' or self.lines[x-1][y] == '$' or self.lines[x][y+1] == '$':
                return 'UDALO SIE ZNALEZC WYJSCIE Z LABIRYNTU',self.lines

t1 = time.time()
L1=Labirynt()
L1.findstart()
L1.find_path_no_recursion()
#L1.findpath()
print time.time() - t1
    
    

    

    
    