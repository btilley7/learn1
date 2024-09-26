from bs4 import BeautifulSoup as BS, Comment
import requests
import csv

targetFile = 'tfl-sample.html'

beginContent = "<!-- body content -->"
endContent = "<!-- end body content -->"

def webScrape(url):
    with open(url) as fp:
        # Parse the HTML document
        soup = BS(fp, 'html.parser')
        
        # Find the start and end comments
        start_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content')
        end_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content end')

        # Check if both comments are found
        if not start_comment or not end_comment:
            raise ValueError("Start or end comment not found in the HTML content.")

        # Collect all elements between the start and end comments
        content_between = []
        for element in start_comment.next_elements:
            if element == end_comment:
                break
            content_between.append(str(element))

        # Combine the collected elements into a single string
        #extracted_content = ''.join(content_between)

        #print(extracted_content)
        
        print(start_comment)

#webScrape("tfl-sample.html")


def webScrape(url):
    with open(url) as fp:
        # Parse the HTML document
        soup = BS(fp, 'html.parser')
        
        # Find the start and end comments
        start_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content')
        end_comment = soup.find(string=lambda text: isinstance(text, Comment) and text.strip() == 'body content end')

        # Check if both comments are found
        if not start_comment or not end_comment:
            raise ValueError("Start or end comment not found in the HTML content.")

        # Collect all elements between the start and end comments
        content_between = []
        for element in start_comment.next_elements:
            if element == end_comment:
                break
            content_between.append(str(element))

        # Combine the collected elements into a single string
        #extracted_content = ''.join(content_between)

        #print(extracted_content)
        
        print(start_comment)

webScrape("tfl-sample.html")
