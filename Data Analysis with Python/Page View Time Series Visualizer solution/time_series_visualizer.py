# Code created by Alejandro Quiñones Gámez for freecodecamp
# time_series_visualizer

from sqlite3 import Timestamp
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('./fcc-forum-pageviews.csv', index_col=['date'], parse_dates=['date'])

# Clean data
df = df.loc[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]



def draw_line_plot():
    # Draw line plot
    fig, ax= plt.subplots(figsize=(18,5))
    
    ax = sns.lineplot(data=df, x='date', y='value', color='red')
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    
    
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy().groupby(pd.Grouper(freq='M')).mean()
    df_bar.loc[Timestamp(2016,1,1)] = 0
    df_bar.loc[Timestamp(2016,2,1)] = 0
    df_bar.loc[Timestamp(2016,3,1)] = 0
    df_bar.loc[Timestamp(2016,4,1)] = 0
    df_bar = df_bar.sort_index()
    
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).strftime('%B')
    pd.melt(df_bar, id_vars=('year', 'month'), value_vars='value')
   
    sns.set_style(style='ticks')
   
    # Draw bar plot
    fig = sns.catplot(data=df_bar, x='year', y='value', hue='month', kind='bar', legend=False)

    fig.set(xlabel='Years', ylabel='Average Page Views')
    plt.legend(title='Months')
    fig = fig.fig
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18,5))
    
    sns.boxplot(ax=ax1, data=df_box, x=df_box['year'], y=df_box['value'])
    ax1.set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')

    sns.boxplot(ax=ax2, data=df_box, x=df_box['month'], y=df_box['value'], order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    ax2.set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')  


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
