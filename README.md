# Eventbrite Webscraper

This Python script scrapes information about upcoming weekend events in a specified city from Eventbrite, prints the information to the console, and stores the data in an Excel file.

## Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

##  Installation

1. Clone this repository to your local machine

2. Change to the `eventbrite_webscraper` directory:
cd eventbrite_webscraper

3. Install the required packages using `pip`:
pip install requests beautifulsoup4 openpyxl


## Usage

Run the script using Python:
python eventbrite_webscraper.py


The script will prompt you to enter a city name (in lowercase and without spaces). After you provide the city name, the script will start scraping the Eventbrite website for upcoming weekend events in the specified city. It will print the event information on the console and store the data in an Excel file named `events_in_<city>.xlsx`.

The scraper will continue to run every 12 hours to fetch updated event information.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.





