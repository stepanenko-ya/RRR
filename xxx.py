from bs4 import BeautifulSoup





file = open("prox_adress").readlines()
print(len(file))
x = list(set(file))
print(" ".join(x))



# file = open("html").read()
# soup =BeautifulSoup(file, "html.parser")
#
# container = soup.find_all(class_="brand-products")
# for con in container:
#     f = con.find(class_='nr').get_text().strip()
#     if "SC10020" in f:
#         print(f)
#         url = con.find("a").get("href")
#         coast = con.find(class_='price').get_text().split("\xa0")[0]
#         print(url)
#         print(coast)
