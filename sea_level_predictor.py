import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    
    fig, ax = plt.subplots()
    ax.scatter(x, y)

    # Create first line of best fit
    lobf = linregress(x, y)

    x_2050 = np.append(x.min(), 2050)

    # ax.plot(x, lobf.intercept + lobf.slope*x, 'r')
    ax.plot(x_2050, lobf.intercept + lobf.slope*x_2050, 'r')


    # Create second line of best fit
    df_2000 = df[df['Year'] >= 2000]
    
    lobf_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    
    x_2000_2050 = np.append(2000, 2050)

    ax.plot(x_2000_2050, lobf_2000.intercept + lobf_2000.slope*x_2000_2050, 'r--')


    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()