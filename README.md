# Eventbrite Webscraper

This is an automated Python script (utilizing BeautifulSoup, Requests, and Openpyxl python libraries) to efficiently scrape and compile data on upcoming weekend events from Eventbrite for any specified U.S. state. The script provides real-time event information, including event name, location, and time, displayed in the console and stored in a well-structured Excel sheet with regular updates every 12 hours.

## Prerequisites

Make sure you have Python 3.x installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

##  Installation

1. Clone this repository to your local machine

`git clone https://github.com/<your_github_username>/eventbrite_webscraper.git`

Replace `<your_github_username>` with your actual GitHub username.

2. Change to the `eventbrite_webscraper` directory:

`cd eventbrite_webscraper`

3. Install the required packages using `pip`:

`pip install requests beautifulsoup4 openpyxl`


## Usage

Run the script using Python:

`python eventbrite_webscraper.py`


The script will prompt you to enter a city name. After you provide the city name, the script will start scraping the Eventbrite website for upcoming weekend events in the specified city. It will print the event information on the console and store the data in an Excel file named `events_in_<city>.xlsx`.

<img src="https://user-images.githubusercontent.com/78191578/230825563-f10053c6-1fca-41a9-a352-d0859ea7c265.gif" width=60% height=60%>

#### The scraper will continue to run every 12 hours to fetch updated event information.

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

