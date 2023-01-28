import pandas as pd
import matplotlib.pyplot as plt

class FCFS():
    def __init__(self):
        self.queue = []
        self.time = 0
        self.process = 0
        self.df = pd.read_csv('processes1.csv').sort_values('arrivals')   #posortowana ramka danych csv
        self.first_process = []
        self.wait_times = []
        self.wait_time = 0


    def start(self):
        self.first_process = self.df.iloc[0].values      #pobiera pierwszy proces z ramki danych
        self.process = self.first_process[1]             #pobiera czas wykonywania pierwszego procesu
        self.wait_times.append(0)                        #wypelnia czas oczekiwania pierwszego procesu
        # czas oczekiwania  = czas usuniecia z kolejki - dolaczenie do kolejki - dlugosc procesu

        while True:

            self.time += 0.01                        #licznik czasu przyjmijmy 0.01s
            self.time = round(self.time, 2)          #zaokragla czas do 2 liczb po przecinku
            self.process = round(self.process, 2)    #zaokragla czas wykonywania obecnego procesu do 2 liczb po przecinku

            a = self.df.loc[self.df['arrivals'] == round(self.time + self.first_process[0], 2)].values
            #a to czasy z pliku csv ktore sa rowne aktualnemu czasowi

            if len(a) == 1:                     #jesli jest jeden proces w tym czasie
                self.queue.append(list(a[0]))   #dodaje do kolejki
                self.queue[-1].append(0)        #dodaje czas oczekiwania
            elif len(a) > 1:                    #jezli jest wiecej procesow w tym samym czasie
                for i in a:
                    self.queue.append(list(i))  #dodaje do kolejki
                    self.queue[-1].append(0)    #dodaje czas oczekiwania

            for i in range(len(self.queue)):    #idzie przez kazdy proces oczekujacy w kolejce i dodaje 1
                self.queue[i][2] += 1

            if round(self.process, 2) == 0 and len(self.queue) >= 1:    #sprawdza czy wykonywany jest proces i czy jest cos w kolejce
                self.process = self.queue[0][1]                         #bierze pierwszy element z kolejki !!!!!!! w tym drugim programie bierze ostatni w tym miejscu
                self.wait_times.append(round(self.queue[0][2]/100, 2))  #dodaje jego czas oczekiwania i dodaje do listy !!!!! tutaj tez zmiana w drugim programie
                del self.queue[0]                                       #usuwa go z kolejki

            elif self.process > 0:                                      #sprawdza czy jakis proces jest wykonywany
                self.process -= 0.01                                    #jesli tak to odejmuje 0.01s





            if self.process == 0 and len(self.queue) == 0:              #przerywa petle jesli koniec
                break

            print(len(self.queue) * '--')                               #wizualizacja kolejki w konsoli

test = FCFS()
test.start()
print(test.wait_times)      #printuje liste z czasami oczekiwania
plt.plot(test.wait_times)   #tworzy wykres czasu oczekiwania
plt.show()                  #pokazuje wykres