import requests
from bs4 import BeautifulSoup as bs
import random

# wiki page you want to start on
start_point = "https://en.wikipedia.org/wiki/Portal:Society"  # we_live_in_a_society.jpg


def scrape_wikipage(url):
    # sends a http request
    # creates a new response object
    response = requests.get(url=url)

    # check for HTTP 200 OK success, indicating the request succeded
    print("Recieved:", response.status_code)
    if response.status_code == 200:
        print("Success")

        # parse our response's html with BeautifulSoup, bs object
        soup = bs(response.content, "html.parser")

        scrape_title(soup)
        link = random_link(soup)

    # infinite scrape
    scrape_wikipage("https://en.wikipedia.org" + link["href"])


# prints the webpage title
def scrape_title(soup):
    print("Grabbing Title")
    # grab our title by element id, firstHeading
    title = soup.find(id="firstHeading")

    # verify
    print("Title:", title.string)


# grab a random link to scrape
def random_link(soup):
    print("Grabbing Random Link")

    # finds all links within a body tag bodyContent
    all_links = soup.find(id="bodyContent").find_all("a")

    # first link we grab will be random
    random.shuffle(all_links)

    for link in all_links:
        # is it a wiki link?
        if link["href"].find("/wiki") == -1:
            # if not skip
            continue

        # stop on the first found link
        scraped_link = link
        break

    print("Link:", scraped_link)
    return scraped_link


scrape_wikipage(start_point)
