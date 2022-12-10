from bs4 import BeautifulSoup
import requests
from controller_scraper import *

def main():
    app = QApplication([])
    window = Controller()
    window.show()
    app.exec_()


    # url = input()
    # page = requests.get(url)
    #
    # soup = BeautifulSoup.get(page.content, 'html.parser')

if __name__ == '__main__':
    main()
