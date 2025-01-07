from datetime import datetime
from playwright.sync_api import sync_playwright
import random

# /////////////------THIS ALLOWS US TO GET BY THE CURRENT ITS ONLY HALF FINISH ---------//////
# def scrape_by_month():
#     with sync_playwright() as playwright:
#         # Launch a browser (headless by default)
#         browser = playwright.chromium.launch(headless=True)
#         # Open a new browser context and page
#         context = browser.new_context()
#         page = context.new_page()
#         # TODO; WILLH HAVE TO UPDATE THIS AFTER DECEMBER ENDS
#         current_year = datetime.now().year + 1
#         current_month = ' January'
#         # Navigate to the website
#         page.goto("https://www.gamesindustry.biz/events?year=2025")
#         # have to target month class and get all children buy 
#         article_parent_element = page.locator('div.months')
#         article_month_header = article_parent_element.locator('div.month :first-child')
#         print(article_month_header.text_content())
        
#         # check if the current year matches and month
#         # if current year adn month matches then we continue
#         # if str(current_year + ) in article_header:
#         #     print("Year Matches")
#         #     # get access to element by class and then get children
#         #     eventsParentElement = page.locator('')
#         #     return 
#         # return print("Did not match")
#         # Extract and print the page title
#         # title = page.title()

#         # print(f"Page title: {title}")

#         # Close the browser
#         browser.close()
# /////////////------THIS ALLOWS US TO GET BY THE CURRENT ITS ONLY HALF FINISH ---------//////
def scrape_months():
    with sync_playwright() as playwright:
        random_images = [
                'https://images.unsplash.com/photo-1593508512255-86ab42a8e620?q=80&w=2078&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1575291786213-f932b9d57c25?q=80&w=1964&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1554410637-1a8267402b57?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1493711662062-fa541adb3fc8?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1640968418417-8bb0f5467417?q=80&w=1932&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1652197881268-d625ad54402b?q=80&w=2835&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1651612448880-2f1bc9145f8e?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1643966398552-0bb0bf0c78cf?q=80&w=2832&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1642444616393-df04dcb1492c?q=80&w=2807&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1619253790960-83acb6df8cc3?q=80&w=2787&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1597840900616-664e930c29df?q=80&w=2825&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1531594896955-305cf81269f1?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D',
                'https://images.unsplash.com/photo-1700154636736-cb5f4c3751b3?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D'
        ]
        # Launch a browser (headless by default)
        browser = playwright.chromium.launch(headless=True)
        # Open a new browser context and page
        context = browser.new_context()
        page = context.new_page()
        event_glossory = []
        current_year = datetime.now().year
        # Navigate to the website
        page.goto(f"https://www.gamesindustry.biz/events?year={current_year}")
        # have to target month classes and get all children with class
        event_elements = page.locator('div.month')
        # print(event_elements)
        length_of_element = event_elements.count()
        for index in range(length_of_element):
            current_element = event_elements.nth(index)
            # THIS WORKS
            month_title = current_element.locator("div.section_title").text_content()
            # print(month_title.inner_html())
            parent_events = current_element.locator('.events')
            # THIS WORKS BUT ITS NOT PERFECT
            current_events = parent_events.locator('.event.summary')
            current_events_lenght = current_events.count()   
            # current_event_title = current_event.locator('p.name')
            for event_index in range(current_events_lenght):
                current_event = current_events.nth(event_index)
                # THIS WORKS
                current_event_title = current_event.locator('p.name').text_content() 
                if current_event.locator('div.image').count() > 0:
                    random_index = random.randint(0, len(random_images) - 1)
                    selected_random_image = random_images.pop(random_index)
                    current_event_banner = (current_event.locator('div.image img').get_attribute('src') if current_event.locator('div.image').count() > 0 else selected_random_image)
                # current_event_banner = (current_event.locator('div.image img').get_attribute('src') if current_event.locator('div.image').count() > 0 else  "selected_random_image")
                current_event_date = current_event.locator('p.dates').text_content()
                current_event_location =  ( current_event.locator('p.location').text_content() if current_event.locator('p.location').count() > 0 else "N/A" )
                current_event_description = current_event.locator('p.description').text_content()
                current_event_link = (current_event.locator('a.button').get_attribute('href') if current_event.locator('a.button').count() > 0 else "N/A")
            event_dictonary = {
                "title":month_title.strip(),
                "event_title":current_event_title.strip(),
                "date":current_event_date.strip(),
                "location":current_event_location.strip(),
                "description":current_event_description.strip(),
                "link":current_event_link.strip(),
                "image":current_event_banner.strip()
            }
            # print(event_dictonary)
            event_glossory.append(event_dictonary.copy())
        browser.close()
        return event_glossory


if __name__ == "__main__":
    # scrape_title()
    events = scrape_months()
    print(events)
    
