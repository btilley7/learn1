from bs4 import BeautifulSoup as BS, Comment
import requests
import csv

targetURL = "https://theflashlist.com/articles/music/audio/tips-for-making-a-perfect-party-playlist.html"

targetFile = 'tfl-sample.html'

beginContent = "<!-- body content -->"
endContent = "<!-- end body content -->"

def webScrape(url):

    #with open(url) as fp:
        fp = requests.get(url)

        # Parse the HTML document
        soup = BS(fp.text, 'html.parser')
        
        # Find the start and end comments
        start_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content')
        end_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content end')

        # Check if both comments are found
        if not start_comment or not end_comment:
            raise ValueError("Start or end comment not found in the HTML content.")

        # Collect all siblings between the start and end comments
        content_between = []
        current = start_comment.next_sibling

        while current and current != end_comment:
            # Ignore empty strings or whitespace-only strings
            if not (isinstance(current, str) and current.strip() == ''):
                content_between.append(str(current))
            current = current.next_sibling

        # Combine the collected elements into a single string
        extracted_content = ''.join(content_between)

        print(extracted_content)

webScrape(targetURL)
