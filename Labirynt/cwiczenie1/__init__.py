with open('/home/student/Pulpit/labirynt0.txt') as f:
  read_data = f.readlines()
  
print read_data

class Labirynt():
    def __init__(self):
        self.lab_str = ''
        self.lab_tab = []
        self.wyjscie = [0][0]
        temp = ''
        i = ''
        liczba = 0
        while read_data[0][liczba] != ' ':
            print read_data[0][liczba]
            temp += read_data[0][liczba]
            liczba += 1
            #print temp
        liczba += 1
        self.wysokosc = int(temp)
        temp = ''
        while read_data[0][liczba] != '\n':
            temp += read_data[0][liczba]
            liczba += 1
            #print temp
        self.szerokosc = int(temp)
        print self.szerokosc, self.wysokosc
        
        self.pozycja = [int(self.wysokosc)][int(self.szerokosc)]
        print self.szerokosc,self.wysokosc,'szer i wys'
        for i in range(0, len(read_data)):
            j = 0
            while j < len(read_data[i]):
                #print read_data[i][j]  
                self.pozycja[i][j] = read_data[i][j]                  
                self.lab_str += str(read_data[i][j])
#                 if read_data[i][j] == '$':
#                     self.wyjscie = read_data[i][j]
#                 if read_data[i][j] == '@': 
#                     self.pozycja = read_data[i][j]
#                     self.x = i
#                     self.y = j
#                 if read_data[i][j] == 'n':
#                     self.lab_str += '\n'
#                     j = 100
                j += 1
            if i >= 1:
                #print read_data[i]
                self.lab_tab.append(read_data[i])
            self.lab_tab = self.lab_tab
        print self.pozycja
        #print self.lab_str
        #print self.lab_tab
        
    def printt(self):
        print self.lab_tab

    def lewo(self):
        self.pozycja = self.pozycja[self.x-1][self.y]
        self.x = self.x - 1
        self.lab_tab[self.pozycja] = '*'
    def prawo(self):
        self.pozycja = self.pozycja[self.x+1][self.y]
        self.x = self.x + 1
        self.lab_tab[self.pozycja] = '*'
    def gora(self):
        self.pozycja = self.pozycja[self.x][self.y-1]
        self.y = self.y - 1
        self.lab_tab[self.pozycja] = '*'
    def dol(self):
        self.pozycja = self.pozycja[self.x][self.y+1]
        self.y = self.y + 1
        self.lab_tab[self.pozycja] = '*'
        
    def find(self):
        while self.wyjscie != self.pozycja:
            if self.pozycja[self.x+1][self.y] != '#' or self.pozycja[self.x+1][self.y] != '*' or self.pozycja[self.x+1][self.y] != '@':
                self.prawo()
            if self.pozycja[self.x][self.y+1] != '#' or self.pozycja[self.x][self.y+1] != '*' or self.pozycja[self.x][self.y+1] != '@':
                self.dol()
            if self.pozycja[self.x-1][self.y] != '#' or self.pozycja[self.x-1][self.y] != '*' or self.pozycja[self.x-1][self.y] != '@':
                self.lewo()
            if self.pozycja[self.x][self.y-1] != '#' or self.pozycja[self.x][self.y-1] != '*' or self.pozycja[self.x][self.y-1] != '@':
                self.gora()
            if self.pozycja[self.x+1][self.y] != '#':
                self.prawo()
            if self.pozycja[self.x][self.y+1] != '#':
                self.dol()
            if self.pozycja[self.x-1][self.y] != '#':
                self.lewo()
            if self.pozycja[self.x][self.y-1] != '#':
                self.gora()
        for i in self.lab_tab:
            print 'tu dziala?',i
        
        
        
L1 = Labirynt()
L1.printt()
# L1.find()