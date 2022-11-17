import numpy as np
import matplotlib.pyplot as plt
from functions import Connection, Message, clearStr


class Chart_MainWindow(object):
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent



    def points(self): #megjelenítendő pontok meghatározása
        con, cur = Connection()
        if con is not None:
            good_points = 'select pont from eredmenyek where nev = %s and kontinens = %s'
            cur.execute(good_points, (self.name, self.continent))
            result_pass = cur.fetchall()
            str_points = clearStr(str(result_pass))
            list_points = []
            list_points.append(str_points.split(' '))
            list_points = list_points[0]
            return list_points
        else:
            Message("HIBAÜZENET", "Adatbázis kapcsolati hiba! Ellenőrizd az internetelérésed!")





    def makeChart(self): #diagram elkészítése

        continents_array = {"afrika":"afrikai", "azsia":"ázsiai", "del-amerika":"dél-amerikai", "eszek-amerika":"észak-amerikai", "europa":"európai", "anktartisz":"anktartiszi", "ausztralia":"ausztráliai"}

        range_points = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        frequency_points = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        list_point = self.points()
        if list_point is not None:
            for p in range(len(list_point)):
                point = int(list_point[p])
                frequency_points[point] += 1

            x = np.arange(len(range_points))
            y = np.arange(max(frequency_points)+2)
            width = 0.50

            fig, ax = plt.subplots()
            series = ax.bar(x, frequency_points, width, color = 'yellow')

            ax.set_ylabel("Elért pontok gyakorisága")
            ax.set_xlabel("Elért pontok")

            ax.set_title("Eddigi " + continents_array[self.continent] + " pontjaid")
            ax.set_xticks(x)
            ax.set_yticks(y)
            ax.set_xticklabels(range_points)
            ax.bar_label(series)

            ax.tick_params(axis="both", which="major", labelsize=10)

            fig.tight_layout()

            plt.show()

if __name__ == "__main__":
    chart = Chart_MainWindow()
    chart.makeChart()




