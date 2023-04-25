# Code created by Alejandro Quiñones Gámez for freecodecamp
# sea_level_predictor

from select import select
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv', usecols=['Year', 'CSIRO Adjusted Sea Level'])

    # Create scatter plot
    plt.figure(1, figsize=(18,5))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    df_complete = df.copy()
    reg = linregress(x=df_complete['Year'], y=df_complete['CSIRO Adjusted Sea Level'])
    for year in range(df_complete['Year'].max()+1, 2051):
        df_complete = df_complete.append({'Year': year, 'CSIRO Adjusted Sea Level': reg.intercept + reg.slope * year}, ignore_index=True)
    print(df_complete)
    plt.plot(df_complete['Year'], reg.intercept + reg.slope * df_complete['Year'], c='g', label='complete_regression')
    

    # Create second line of best fit
    df_21th_century=df.loc[(df['Year'] > 1999)]
    new_reg = linregress(x=df_21th_century['Year'], y=df_21th_century['CSIRO Adjusted Sea Level'])
    for year in range(df_21th_century['Year'].max()+1, 2051):
        df_21th_century = df_21th_century.append({'Year': year, 'CSIRO Adjusted Sea Level': new_reg.intercept + new_reg.slope * year}, ignore_index=True)
    print(df_21th_century)
    plt.plot(df_21th_century['Year'], new_reg.intercept + new_reg.slope * df_21th_century['Year'], c='r', label='21th_century_regression')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    xticks = [float(i) for i in range (1850, 2076, 25)]
    plt.xticks(xticks)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()