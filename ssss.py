import csv


el = [['64888660', '725691', 'LuminexLine', '"LuminexLine ', ' 725691 ', ' Reflektor światła dodatkowego, szt"', '', 'no such item', '', '', '\n'],['6974681', 'CT1115', 'Contitech', '"Contitech ', ' CT1115 ', ' Pasek rozrządu, szt"', '', 'https://www.czesciauto24.pl/contitech/1210493', '', '', '\n']]
file = open("czes.csv", "w")
for i in el:
    f = i[:-1]
    writer = csv.writer(file, delimiter="|")
    writer.writerow(f)
