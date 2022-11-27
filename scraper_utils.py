from bs4 import BeautifulSoup
import requests


headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}



def make_a_soup(url:str, verify=False):
    headers = {'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:10.0) Gecko/20100101 Firefox/10.0"}
    page = requests.get(url, verify=verify,headers=headers).text
    soup = BeautifulSoup(page, "html.parser")
    return soup