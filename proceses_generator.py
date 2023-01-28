import numpy as np
import csv


class ProcessGenerator:
    def init(self, num_processes, arrival_avg, arrival_std, execution_avg, execution_std):
        self.num_processes = num_processes
        self.arrival_avg = arrival_avg
        self.arrival_std = arrival_std
        self.execution_avg = execution_avg
        self.execution_std = execution_std

    def generate(self):
        arrivals = np.clip(np.random.uniform(self.arrival_avg, self.arrival_std, self.num_processes), 0, np.inf)   #losuje arrivals z rozkladu plaskiego
        executions = np.clip(np.random.normal(self.execution_avg, self.execution_std, self.num_processes), 0, np.inf) #losuje czas z rozkladu normalnego

        with open('processes1.csv', 'w', newline = '') as f:                   #sapisuje do pliku csv
            writer = csv.writer(f)
            writer.writerow(['arrivals', 'time'])                              #tworzy naglowki
            for index, i in enumerate(arrivals):
                writer.writerow([round(i, 2), round(executions[index], 2)])    #dodaje wiersze





pg = ProcessGenerator(100, 5, 1, 0.1,0.05) #(N, srednia arrival, odchulenie arrival, sredni czas, odchylenie czasu,

processes = pg.generate()