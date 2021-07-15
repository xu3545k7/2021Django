import os
import django
import pandas as pd
import time
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Country , City
url="https://simpleisbetterthancomplex.com/tutorial/2020/01/19/how-to-use-chart-js-with-django.html"
raw_data = pd.read_html(url)
time.sleep(3)

data=raw_data[0]
cities = list()
for i in range(len(data)):
    temp = tuple(data['cities'].iloc[i])
    cities.append(temp)
for city in cities:
    try:
        country = Country.objects.get(country_id=city[2])
        temp=City(name=city[1],country=country,population=city[3])
        temp.save()
    except:
        pass
# print(cities)
# country_id = list(data['countries']['id'])
# country_name = list(data['countries']['name'])
# countries = zip(country_id,country_name)
# for country in countries:
#     temp = Country(name=country[1], country_id=country[0])
#     temp.save()
#     print(country)
# print("Done!")