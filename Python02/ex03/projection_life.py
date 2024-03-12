"""_summary_
In this excercice we learned how to use matplotlib scatter.
Thanks to scatter we can visualize the relation of 2 dataframes values.
Every point in this graph represents a country.
"""

from matplotlib import pyplot as plt
from load_csv import load

def main():
    """_summary_
    """
    exp_data = load("life_expectancy_years.csv")
    in_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    plt.scatter( in_data['1900'], exp_data['1900'])
    plt.xscale('log')
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title('1900')
    plt.show()

if __name__ == "__main__":
    main()