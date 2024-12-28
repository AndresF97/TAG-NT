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
        print(event_elements)
        length_of_element = event_elements.count()
        for index in range(length_of_element):
            current_element = event_elements.nth(index)
            current_title = current_element.locator("div.section_title")
            print(current_title.inner_html())
        
        # check if the current year matches and month
        # if current year adn month matches then we continue
        # if str(current_year + ) in article_header:
        #     print("Year Matches")
        #     # get access to element by class and then get children
        #     eventsParentElement = page.locator('')
        #     return 
        # return print("Did not match")
        # Extract and print the page title
        # title = page.title()

        # print(f"Page title: {title}")

        # Close the browser
        browser.close()


if __name__ == "__main__":
    # scrape_title()
    scrape_months()
