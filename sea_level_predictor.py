import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    labels = {
        'Year': 'year',
        'CSIRO Adjusted Sea Level': 'csiro',
        'Lower Error Bound': 'lower',
        'Upper Error Bound': 'upper',
        'NOAA Adjusted Sea Level': 'noaa',
        }
    df = df.rename(columns=labels)

    dfr = df.loc[df['year'] >= 2000].reset_index()

    years_long = df['year'].append(pd.Series(range(2014, 2051)))
    years_recent = dfr['year'].append(pd.Series(range(2014, 2051)))

    # Create scatter plot.
    # Use matplotlib to create a scatter plot with "year" as the
    # x-axis and "csiro" as the y-axis.
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(1880, 2060)
    ax.scatter(x=df['year'], y=df['csiro'])

    # Create first line of best fit.
    # Use scipy.stats.linregress() to get the slope and y-intercept of
    # the line of best fit.  Plot the line of best fit over the top of
    # the scatter plot. Make the line go through the year 2050 to
    # predict the sea level rise in 2050.
    long_slope, long_int, long_r, long_p, long_error = linregress(x=df['year'], y=df['csiro'])
    ax.plot(years_long, long_slope * years_long + long_int, label='long')

    # Create second line of best fit.
    # Plot a second line of best fit using the data from the year 2000
    # through the most recent year in the dataset, going forward to
    # 2050.
    short_slope, short_int, short_r, short_p, short_error = linregress(x=dfr['year'], y=dfr['csiro'])
    ax.plot(years_recent, short_slope * years_recent + short_int, label='recent')
    # print(short_slope, short_int, short_r, short_p, short_error)

    # Add labels and title
    # The x label should be "Year."
    # The y label should be "Sea Level (inches)."
    # The title should be "Rise in Sea Level."
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    
    # Save the plot.
    fig.savefig('sea_level_plot.png')

    # Return the plot for testing.
    return plt.gca()
