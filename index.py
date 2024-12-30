from datetime import datetime
from playwright.sync_api import sync_playwright
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
        # Launch a browser (headless by default)
        browser = playwright.chromium.launch(headless=True)
        # Open a new browser context and page
        context = browser.new_context()
        page = context.new_page()
        event_glossory = []
        # Navigate to the website
        page.goto("https://www.gamesindustry.biz/events?year=2025")
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
                # THIS WORKS
                current_event_banner = (current_event.locator('div.image img').get_attribute('src') if current_event.locator('div.image').count() > 0 else 'No Image' )
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
    
