import random
import requests
from bs4 import BeautifulSoup

url = "https://projecteuler.net/problem=" + "{}".format(random.randint(1,667))

data = requests.get(url)

soup = BeautifulSoup(data.text, 'html.parser')

print(soup.find_all('div', { "class": "problem_content" })[0].text)
