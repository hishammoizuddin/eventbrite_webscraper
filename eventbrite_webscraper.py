"""
Eventbrite Webscraper Script
Author: Mohammed Hisham Moizuddin

This script scrapes information about upcoming weekend events in a specified U.S. state from Eventbrite,
prints it on the console, and stores it in an Excel sheet.
"""

import requests
import time
import openpyxl
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    # Create a new Excel workbook and set the active sheet's title
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'Top Events'
    sheet.append(['Event #', 'Name', 'Location', 'Time'])

    # Prompt user for the U.S. state's name
    print()
    user_input = input("Please enter the U.S. State's name: ")
    user_city = user_input.lower().replace(' ', '')
    assigned_url = "https://www.eventbrite.com/d/united-states--"+user_city+"/events--this-weekend/"

    # Get the current time as the last fetch time
    last_fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nLast fetch time:", last_fetch_time)

    try:
        # Send a GET request to the specified URL
        req = requests.get(assigned_url)
        req.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(req.text, "html.parser")

        # Find all event list items
        events = soup.find('ul', class_="search-main-content__events-list").find_all('li')
        event_index = 1

        # Iterate through the events and extract relevant information
        for event in events:
            event_details_html = event.find('div', class_="eds-event-card-content__content__principal")
            
            event_name_raw = event_details_html.find('div', class_="eds-event-card-content__primary-content").a.text.strip()
            event_name = event_name_raw[:len(event_name_raw)//2]
            
            event_location = event_details_html.find('div', class_="eds-event-card-content__sub-content").get_text()
            event_time = event_details_html.find('div', class_="eds-event-card-content__primary-content").find('div', class_="eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm").get_text()

            # Print the event details to the console
            print()
            print("Event #", event_index)
            print("\tName : ", event_name)
            print("\tLocation : ", event_location)
            print("\tTime : ", event_time)
            print()

            # Append the event details to the Excel sheet
            sheet.append([event_index, event_name, event_location, event_time])
            event_index += 1

    except Exception as e:
        print(e)

    # Append the last fetch time to the Excel sheet
    sheet.append(['', '', '', ''])
    sheet.append(['Last fetch time:', last_fetch_time])
    
    # Save the Excel file with the events information
    excel.save('events_in_'+user_city+'.xlsx')

# Continuously run the main function every 12 hours (43200 seconds)
if __name__ == "__main__":
    while True:
        main()
        time.sleep(43200)
