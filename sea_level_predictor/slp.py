import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def import_data():
    df = pd.read_csv(r'C:\Users\Nitro\Downloads\epa-sea-level.csv')
    return df

def draw_plot():
    # Import data
    df = import_data()

    # Create scatter plot
    plt.figure(figsize=(10,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', s=10)

    # First line of best fit (all data)
    result_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = range(df['Year'].min(), 2051)
    plt.plot(years_all,
             [result_all.slope * year + result_all.intercept for year in years_all],
             'r', label='Best fit: All data')

    # Second line of best fit (from year 2000 onwards)
    df_recent = df[df['Year'] >= 2000]
    result_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = range(2000, 2051)
    plt.plot(years_recent,
             [result_recent.slope * year + result_recent.intercept for year in years_recent],
             'green', label='Best fit: From 2000')

    # Labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Save figure and return plot
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    return plt.gcf()
