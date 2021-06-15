import csv


def new_csv():
    with open("czes.csv") as file:
        new_lst = []
        new_czesci = open("new_czesci", "a+")
        for i in file.readlines():
            l = i.split('|')
            l[0] = int(l[0])
            new_lst.append(l)
        for t in sorted(new_lst):
            t[0] = str(t[0])
            c = "|".join(t)
            new_czesci.write(c)




def sets():
    file_first = open("czes.csv").readlines()
    f = []
    for i in file_first:
        x = i.split("|")[1:4]
        x1 = ", ".join(x)
        f.append(x1)

    file_two = open("poland.csv").readlines()
    sec = []
    for i in file_two:
        y = i.split("|")[0:3]
        y1 = ", ".join(y)
        sec.append(y1)

    first = set(f)
    two = set(sec)

    result = list(first ^ two)
    for res in result:

        print(res)



sets()