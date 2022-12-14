"""
Czytamy z JSON
http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-09-01/2022-12-01/?format=json
Wykorzystamy:
https://requests.readthedocs.io/en/latest/
"""

import requests
import matplotlib.pyplot as plt

wal = ("usd", "chf", "gbp")
od = "2021-12-01"
do = "2022-12-01"

#print(dane)
wartosci2 = []




def get_curr(waluta, data_od, data_do):
    wartosci = []
    api_link = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data_od}/{data_do}/?format=json"
    r_api = requests.get(api_link)
    print(r_api)
    dane = r_api.json()
    for day in dane["rates"]:
        wartosci.append(day["mid"])
    return wartosci


title = f""" KURS {(wal)}
        od {od}  do {do}"""
for waluta in wal:
    get_curr(wal, od, do)


print(wartosci2)
plt.title(title)

x_points = [x for x in range(len(wartosci2))]
plt.plot(x_points, wartosci2)
plt.grid()
plt.show()

