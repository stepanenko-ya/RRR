from bs4 import BeautifulSoup



#
#
# file = open("prox_adress").readlines()
# print(len(file))
# x = list(set(file))
# print(" ".join(x))

#
# #iparts#
file = open("html.html").read()
soup =BeautifulSoup(file, "html.parser")
x = 'OX 153D1'

y = 'Mahle/Knecht'
container = soup.find(class_="list_products").find_all(class_="item_in_stock")
for con in container:
    f = con.find(class_='name').find(class_="article_number").get_text().split(":")[1].strip().replace(" ", "")
    if x.replace(" ", '').upper() in f.upper():
        print(type(f))
        name = con.find(class_="name").find("a").get_text()
        # print(name)

        print("________________________________________________________________________________________________")
        brand = con.find('a').get_text()
        url = con.find('a').get('href')
        print(url)




        print(s.find("a").get("href"))
        q = s.find(class_="article_number").get_text().split(":")[1].strip().replace(" ", "")
        print(q)


            if y in brand:
                url = con.find('a').get('href')
                coast = con.find(class_='actual_price small_price').get_text().split("\xa0")[0]
                print(coast)


            url = con.find("a").get("href")
        coast = con.find(class_='price promotion').get_text().split("\xa0")[0]
        print(url)
        print(coast)
