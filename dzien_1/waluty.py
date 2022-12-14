"""
Czytamy z JSON
http://api.nbp.pl/api/exchangerates/rates/a/usd/2022-09-01/2022-12-01/?format=json
Wykorzystamy:
https://requests.readthedocs.io/en/latest/
"""

import requests
import matplotlib.pyplot as plt

waluta = "usd"
data_od = "2021-12-01"
data_do = "2022-12-01"
api_link = f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{data_od}/{data_do}/?format=json"

title = f""" KURS {(waluta.upper()
                    )}
        od {data_od}  do {data_do}"""
r_api = requests.get(api_link)
print(r_api)
dane = r_api.json()
#print(dane)
wartosci = []

for day in dane["rates"]:
    wartosci.append(day["mid"])

print(wartosci)
plt.title(title)
x_points = [x for x in range(len(wartosci))]
plt.plot(x_points , wartosci)
plt.grid()
plt.show()

