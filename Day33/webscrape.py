'''
#Challenge 1: The Direct Path (Attributes)
#Goal: Select the "Sync to FTP" button using its ID.

XPath = '//button[@id="btn_99x_sync"]'

#Challenge 2: The Text Match (Content)
#Goal: Select the table cell (td) that contains the text "inventory_raw.txt".

XPath = '//td[text()="inventory_raw.txt"]'

#Challenge 3: Using "Contains" on Text
#Goal: Select the "Daily Reports" header (h2), but pretend you only know it contains the word "Reports".

XPath = '//h2[contains(text(),"Reports")]'

#Challenge 4: Multiple Attributes
#Goal: Select the download button in the second row, specifically using the fact that it is disabled.

XPath = '//button[@class="btn-download" and @disabled]'

#Challenge 5:
#Goal: Select the Status (the td with the class status-error) but only for the row that contains "inventory_raw.txt".

XPath = '//td[text()="inventory_raw.txt"]/following-sibling::td[@class="status-error"]'
'''

from scrapy import Selector
import requests, pandas as pd, os

url = 'https://en.wikipedia.org/wiki/Web_scraping'

# Define a User-Agent so you look like a real browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36'
}

# Pass the headers into the request
response = requests.get(url, headers=headers)
html = response.text

sel = Selector(text=html)
p_selectors = sel.xpath('//div[@class="mw-content-ltr mw-parser-output"]/p[position()<=6]')
p_list = [p.xpath('string(.)').get().strip() for p in p_selectors]
clean_paragraphs = "\n\n".join(p_list)
print(clean_paragraphs)


#directory of the current .py script
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = 'output.txt'

complete_path = os.path.join(current_dir, file_name)

with open(complete_path, "w") as text_file:
    text_file.write(clean_paragraphs)
