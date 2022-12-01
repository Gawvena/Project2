from bs4 import BeautifulSoup
import requests

def main():

    url = input()
    page = requests.get(url)

    soup = BeautifulSoup.get(page.content, 'html.parser')

if __name__ == '__main__':
    main()
