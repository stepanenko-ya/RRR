from bs4 import BeautifulSoup
from selenium import webdriver
import time
from fake_useragent import UserAgent
from proxy import proxy_list
import random
from selenium.webdriver.common.keys import Keys
import csv
from multiprocessing import Pool

ua = UserAgent()

URL = "https://www.iparts.pl/znajdz/?idCar=&query="


def finder():
    with open('p.csv') as file:
        poland_items = [i.split("|") for i in file.readlines()]
    return poland_items


def iparts(findr):
    for el in findr:
        hunter_list = el[1:3]
        vendor = hunter_list[0]
        hunter_derty = " ".join(hunter_list)
        hunter = hunter_derty.replace(" ", "+").replace("/", "%")
        finder_url = URL + hunter
        print(finder_url)
        # del i[6:]
        x = True
        while x:
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-agent={ua.random}")
            options.add_argument("--disable-blink-features=AutomationControlled")
            # options.add_argument("--headless")
            options.add_argument(f"--proxy-server={random.choice(proxy_list)}")
            driver = webdriver.Chrome(options=options)

            try:
                driver.get(finder_url)

                items = driver.find_element_by_id('SklepKatalog').find_elements_by_class_name("produkt")

                for item in items:
                    name = item.find_element_by_class_name("nazwa").find_element_by_tag_name("a")
                    print(name)
                time.sleep(8)
            except Exception as ex:
                print(ex)
            else:
                x = False
            finally:
                driver.close()
                driver.quit()


#         with open("html.html") as html:
#
#             result_file = open("RESULT", "a+")
#             file = html.read()
#             try:
#                 soup = BeautifulSoup(file, "html.parser")
#                 items = soup.find(id="SklepKatalog").find_all(class_="produkt middle-12")
#                 link = '___'
#                 price = '___'
#                 if len(items) == 0:
#                     link = "product is out of stock"
#                     price = "0"
#                 else:
#                     for item in items:
#                         name_item = item.find(class_="nazwa naglowek").get_text().strip()
#                         if vendor in name_item:
#                             if hunter_list[1].upper() in name_item.upper():
#                                 url = item.find(class_="nazwa naglowek").find("a").get("href")
#                                 result_url = 'https://www.iparts.pl' + url
#                                 cena = item.find(class_="cena").find("b").get_text()
#                                 price = cena
#                                 link = result_url
#             except Exception as ex:
#                 print(ex)
#             else:
#
#
#                 i.append(link)
#                 i.append(price)
#                 print(i)

if __name__ == "__main__":
    findr = finder()
    iparts(findr)
