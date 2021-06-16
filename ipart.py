from bs4 import BeautifulSoup
from selenium import webdriver
import time
from fake_useragent import UserAgent
from proxy import proxy_list
import random
from selenium.webdriver.common.keys import Keys
import csv

ua = UserAgent()

URL = "https://www.iparts.pl/znajdz/?idCar=&query="


def writer(*args):
    result = "|".join(*args)
    with open("RESULT", "a+") as file:
        file.write(result + "\n")


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
        print(">>>>>>>>>>>>>>>", finder_url)
        del el[6:]
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
                iter_items = iter(items)
                link = None
                price = None

                for item in iter_items:
                # for item in items:
                    time.sleep(8)
                    # -------------------------------------------------------------------------------------------
                    """make function"""
                    name_item = item.find_element_by_class_name("nazwa").find_element_by_tag_name("a").text
                    if vendor in name_item.strip():
                        if hunter_list[1].upper() in name_item.upper():
                            item.find_element_by_class_name("nazwa").find_element_by_tag_name("a").click()
                            time.sleep(8)
                            elements = driver.find_element_by_css_selector('span[itemprop="mpn"]').text.replace(" ", "")
                            if vendor.replace(" ", "") == elements:
                                result_url = driver.current_url
                                print(driver.current_url)
                                link = result_url
                                el.append(link)
                                writer(el)
                                break
                            else:
                                driver.back()
                                print("должно взять следующую карточку")
                                # if not link:
                                #     el.append("item is out")
                                #     el.append("0")
                    # -------------------------------------------------------------------------------------------------
                    else:
                        nastepna = driver.find_element_by_class_name("button-and-number-pager")
                        if nastepna:
                            nastepna.click()
                        else:
                            el.append("item is out")
                            el.append("0")
                            writer(el)
            except Exception as ex:
               print(ex)
            else:
                x = False
            finally:
                driver.close()
                driver.quit()


if __name__ == "__main__":
    findr = finder()
    iparts(findr)



