from selenium import webdriver
import requests


def get_links(url):
    """Find all links on page at the given url.
       Return a list of all link addresses, as strings.
    """
    from webdriver_manager.chrome import ChromeDriverManager

    links = []
    browser = webdriver.Chrome(executable_path='/Users/supakorn/Downloads/chromedriver')
    browser.get(url)
    elements = browser.find_elements_by_tag_name("a")
    for a in elements:
        links.append(a.get_attribute('href'))
    browser.close()
    return links

def invalid_urls(urllist):
    invalidlist = []
    for url in urllist:
        r = requests.head(url)
        if r.status_code == 404:
            invalidlist.append(url)
    return invalidlist     


def main():
    hreflist = get_links("https://cpske.github.io/ISP/")
    for href in hreflist:
        print(href)
    print()
    print()
    invalidurl = invalid_urls(hreflist)        
    for invalid in invalidurl:
        print(invalid)


main()


