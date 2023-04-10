import requests
import time
import openpyxl
from bs4 import BeautifulSoup
from datetime import datetime

def main():
    excel = openpyxl.Workbook()
    sheet = excel.active
    sheet.title = 'Top Events'
    sheet.append(['Event #', 'Name', 'Location', 'Time'])

    assigned_url = ''
    print()
    user_city = input("Please enter the U.S. State's name (all lowercase and no spaces) : ")
    assigned_url = "https://www.eventbrite.com/d/united-states--"+user_city+"/events--this-weekend/"
    

    last_fetch_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("\nLast fetch time:", last_fetch_time)

    try:
        req = requests.get(assigned_url)
        req.raise_for_status()

        soup = BeautifulSoup(req.text, "html.parser")

        events = soup.find('ul', class_="search-main-content__events-list").find_all('li')
        event_index = 1

        for event in events:
            event_details_html = event.find('div', class_="eds-event-card-content__content__principal")
            
            event_name_raw = event_details_html.find('div', class_="eds-event-card-content__primary-content").a.text.strip()
            event_name = event_name_raw[:len(event_name_raw)//2]
            
            event_location = event_details_html.find('div', class_="eds-event-card-content__sub-content").get_text()
            event_time = event_details_html.find('div', class_="eds-event-card-content__primary-content").find('div', class_="eds-event-card-content__sub-title eds-text-color--primary-brand eds-l-pad-bot-1 eds-l-pad-top-2 eds-text-weight--heavy eds-text-bm").get_text()

            print()
            print("Event #", event_index)
            print("\tName : ", event_name)
            print("\tLocation : ", event_location)
            print("\tTime : ", event_time)
            print()

            sheet.append([event_index, event_name, event_location, event_time])
            event_index += 1

    except Exception as e:
        print(e)

    sheet.append(['', '', '', ''])
    sheet.append(['Last fetch time:', last_fetch_time])
    excel.save('events_in_'+user_city+'.xlsx')


if __name__ == "__main__":
    while True:
        main()
        time.sleep(43200)
