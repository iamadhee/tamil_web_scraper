import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup
import warnings
import yaml
warnings.filterwarnings('ignore')

headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}

config = yaml.safe_load(open('config.yaml','r'))

url = config['URL']

subject_tab = config['SUBJECT_TAB']

sub_url = url+subject_tab

page = requests.get(sub_url, verify=False,headers=headers).text

soup = BeautifulSoup(page, "html.parser")

lis = soup.findAll('li')

sub_tab_list = []
for li in lis:
    sub_tab = li.find_all('a')[0].get_text()
    sub_tab_list.append(sub_tab)

print(sub_tab_list)

count = 0 

for sub_tab in sub_tab_list:

    sub_tab = sub_tab.split(' ')
    sub_tab = '+'.join(sub_tab)

    url_to_hit = sub_url+sub_tab+'.html'

    landing_page = requests.get(url_to_hit, verify=False,headers=headers).text

    landing_soup = BeautifulSoup(landing_page, "html.parser")

    verses = landing_soup.findAll('p',class_='verse')

    if verses:

        count+=1
        with open('output.txt','a') as file:
            file.write(f'{count} - {url_to_hit} \n\n')

            for verse in verses:
                file.write(f'{verse.get_text()}\n')

            file.write('\n\n\n\n')
            


