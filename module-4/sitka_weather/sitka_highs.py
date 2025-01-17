import csv
from datetime import datetime
import sys
import os
from matplotlib import pyplot as plt

#get the current directory of the script
current_dir = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(current_dir, 'sitka_weather_2018_simple.csv')

#read the data from the CSV file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high temperatures, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        low = int(row[6])
        highs.append(high)
        lows.append(low)

#function to display the high or low temperatures
def plot_temperatures(dates, temperatures, temp_type):
    fig, ax = plt.subplots()
    color = 'red' if temp_type == 'highs' else 'blue'
    ax.plot(dates, temperatures, c=color)

    #format plot
    title = f"Daily {temp_type} temperatures - 2018"
    plt.title(title.title(), fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()

#display instructions to the user
print("Welcome to the Sitka Weather Data Viewer!")
print("You can view daily high or low temperatures for 2018.")
print("Enter 'highs' to view high temperatures, 'lows' to view low temperatures, or 'exit' to quit.")

#main program loop
while True:
    user_input = input("\nPlease enter your choice (highs, lows, exit): ").strip().lower()

    if user_input == 'highs':
        plot_temperatures(dates, highs, 'highs')
    elif user_input == 'lows':
        plot_temperatures(dates, lows, 'lows')
    elif user_input == 'exit':
        print("Thank you for using the Sitka Weather Data Viewer. Goodbye!")
        sys.exit()
    else:
        print("Invalid input. Please enter 'highs', 'lows', or 'exit'.")