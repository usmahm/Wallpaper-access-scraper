'''
  This is a practice script, only to be used for learning.
  Note: This will only run on Linux or Mac os, you'll need to edit the file paths to work on Windows

  @usmahm
'''

import cloudscraper
import bs4
import lxml
import os
import re
from time import sleep
from tqdm import tqdm

# Replace with a supported link, check the doc 
walpaperaccess_link = 'https://wallpaperaccess.com/4k-art'

# Replace with the path your desired folder to store the scraped images
base_folder = os.getcwd()

scrapper = cloudscraper.create_scraper()

while True:
      
    result = scrapper.get(walpaperaccess_link)

    soup = bs4.BeautifulSoup(result.text, 'lxml')

    print(soup.find('title').text, 'Access denied' not in soup.find('title').text)
    # Checks if access was denied
    if 'Access denied' in soup.find('title').text:
        print("Access denied, Trying again in 30 seconds, Please check that you have the latest version of cloudscraper")
        sleep(30)
        continue
    
    else:
        folder_name = soup.find('h1').text

        # Creates a new folder(if it doesn't exist) to write the images to
        # Change / to \\ to support file sytem on Windows
        write_folder = f'{base_folder}/{folder_name}'
        if not(os.path.isdir(write_folder)):
            os.mkdir(write_folder)

        images = soup.find_all('div', {'data-fullimg': True})

        print(f'This page has {len(images)} images.')
        print(f'Writing {len(images)} images to {write_folder}')
        print('...')

        for image in tqdm(images):
            img_part_link = image['data-fullimg']
            img_link = 'https://wallpaperaccess.com' + img_part_link

            img_name = re.search('/full/(.+)', img_part_link).group(1)

            image_result = scrapper.get(img_link)
            image_binary = image_result.content
            
            new_img_dir = f'{write_folder}/{img_name}'
            with open(new_img_dir, 'wb') as image:
                image.write(image_binary)

        print(f'Successfully written {len(images)} images to {write_folder}')
          
        break