import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

FOLDER_SAVE_DATA = 'data'


class CrawlUrl():

    # init method or constructor
    def __init__(self, url):
        self.url = url

    def main(self):
        if not os.path.exists(FOLDER_SAVE_DATA):
            os.mkdir(FOLDER_SAVE_DATA)
        self.crawl()
        self.write_data()
        print(str(datetime.now()) + ' ~ Done')

    def crawl(self):
        source_code = requests.get(self.url)
        soup = BeautifulSoup(source_code.text, "html.parser")
        set_of_urls = set()

        for tag in soup.findAll('a'):
            link_href = tag.get('href')
            if link_href is not None:
                if not link_href.startswith("http"):
                    link_href = self.url + link_href
                set_of_urls.add(link_href + '\n')

        print(str(datetime.now()) + ' ~ Crawled count links:', len(set_of_urls))

        # Sort links
        set_of_urls = sorted(set_of_urls)
        self.crawled_urls = set_of_urls

    def write_data(self):
        try:
            now = datetime.now()
            dt_string = now.strftime("%Y%m%d_%H%M%S")
            file_name = FOLDER_SAVE_DATA + '/' + \
                self.url.replace('://', '_').replace('.', '_') + \
                '_' + dt_string + '.txt'
            print(str(now) + ' ~ Start write file: ' + file_name)
            file_save = open(file_name, "w", encoding='utf-8')
            file_save.writelines(self.crawled_urls)
            file_save.close()
        except Exception as e:
            print(e)

    def test(self):
        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%Y%m%d_%H%M%S")
        print("date and time =", dt_string)

# obj = CrawlUrl('https://freemediatools.com')
# obj.main()
# obj.test()
