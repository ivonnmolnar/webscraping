from urllib.request import urlopen
from bs4 import BeautifulSoup
import urllib.request

r = urllib.request.Request("https://www.thefactsite.com/top-100-random-funny-facts", headers= {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'})
html = urllib.request.urlopen(r)
bsObj = BeautifulSoup(html,"html.parser")

fact_headers = bsObj.findAll("h2")
facts = []

for fact in fact_headers:
    facts.append(fact.text)
