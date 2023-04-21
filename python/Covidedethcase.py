from collections import namedtuple
import requests
from lxml import html
coviod_data=namedtuple("covid_data", "cases deaths recovered")
def covid_status(url: str = "https://www.worldometers.info/coronavirus/"):
    xpatha_str='//div[@class = "maincounter-number"]/span/text()'
    return covid_data(*html.fromstring(requests.get(url).content).xpath(xpath_str))
fmt = """\nTotal COVID-19 cases in the world: {}