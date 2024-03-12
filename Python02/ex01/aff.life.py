"""_summary_
    In this module we learned how to make a graph with matplotlib.
    Thanks to matplotlib we can visualize dataframes.
"""

from matplotlib import pyplot as plt
from load_csv import load

def main():
    """_summary_
    """
    dataset = load("life_expectancy_years.csv")
    plt.plot()
    # x = dataset[]
    spain = dataset.loc[dataset['country'] == 'Spain']
    plt.plot(spain.columns[1:], spain.values[0][1:], label='Spain')
    plt.title('Spain Life expectancy Projections')
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.xticks(range(0, len(spain.columns[1:]), 40))
    plt.show()

if __name__ == "__main__":
    main()