"""_summary_
In this excercie we learned how to plot more than one line with matplotlib.
"""

from matplotlib import pyplot as plt
from load_csv import load
import numpy as np

def main():
    """_summary_
    """
    dataset = load("population_total.csv")
    plt.plot()
    spain = dataset.loc[dataset['country'] == 'Spain']
    spain_translated = []
    france = dataset.loc[dataset['country'] == 'France']
    france_translated = []
    dict = {'M':1e6, 'K':1e3}
    for i in spain.values[0]:
        if i[-1] == 'M' or i[-1] == 'K':
            spain_translated.append(int(float(i[:-1])*dict[i[-1]]))
    for i in france.values[0]:
        if i[-1] == 'M' or i[-1] == 'K':
            france_translated.append(int(float(i[:-1])*dict[i[-1]]))
    plt.plot(spain.columns[1:].astype(int), spain_translated, label='Spain')
    plt.plot(france.columns[1:].astype(int), france_translated, label='France')
    plt.title('Population projections')
    plt.xticks(range(1800, 2051, 40))
    yticks = np.arange(2e7, max(max(spain_translated), max(france_translated)), 2e7)
    print(yticks)
    plt.yticks(yticks, ["{:,.0f}M".format(pop / 1e6) for pop in yticks])
    plt.xlim(1790, 2050)
    plt.legend(loc='lower right')
    plt.xlabel('Year')
    plt.ylabel('Population')
    plt.show()


if __name__ == "__main__":
    main()