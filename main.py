import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    #print(df.head())

    # Create scatter plot
    x =df['Year']
    y = df['CSIRO Adjusted Sea Level']
    fig, ax = plt.subplots(figsize = (6, 6))
    plt.scatter(x,y)

    # Create first line of best fit
    slope, intercept, r_value, p_value, stderr = linregress(x.values,y.values)
    #res = linregress(x, y)
    #get new x, y for a line plot
    x_pred = pd.Series([i for i in range(1880, 2051)])
    y_pred = slope*x_pred + intercept
    #create a line plot
    plt.plot(x_pred, y_pred, 'r')

    # Create second line of best fit
    df_forecast = df.loc[df["Year"] >= 2000]
    #new x, y for the plot
    x_forecast = df_forecast['Year']
    y_forecast = df_forecast['CSIRO Adjusted Sea Level']
    #print(df_forecast)

    #get new slope using linregress()
    res = linregress(x_forecast.values, y_forecast.values)
    x_pred2 = pd.Series([i for i in range(2000, 2051)])
    y_pred2 = res.slope*x_pred2 + res.intercept
    plt.plot(x_pred2, y_pred2, 'g')
     
    #joining all charts together
    
    fig, ax = plt.subplots(figsize = (6, 6))
    ax.scatter(x = df['Year'], y = df['CSIRO Adjusted Sea Level'])
    #plot first line graph (1880 - 2050)
    ax.plot(x_pred, y_pred, 'r')
  
    #plot second line graph (2000 - 2050)
    ax.plot(x_pred2, y_pred2, 'g')
    
    # Add labels and title
    plt.xlabel('Year', fontsize = 12)
    plt.ylabel('Sea Level (inches)', fontsize = 12)
    plt.title('Rise in Sea Level', fontsize = 12)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    #plt.show()
draw_plot(
  
)