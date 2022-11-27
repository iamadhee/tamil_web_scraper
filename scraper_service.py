import warnings
import scraper_utils as utils
from pathlib import Path
import re
warnings.filterwarnings('ignore')

current_path = Path.cwd()

class Kalanjiyam:

    def __init__(self):
        self.home_url = "https://store.tamillexicon.com/"
        self.content_links = dict()
        
    def get_list_of_authors(self):
        soup = utils.make_a_soup(self.home_url)
        aside_tag = soup.find('aside', id='authors')
        author_li= aside_tag.find('ul').findAll('li')

        author_link_dict = dict()
        for li in author_li:
            a_tag = li.find('a',href=True)
            author_link_dict.update({a_tag.get_text(strip=True) : a_tag['href']})
        return author_link_dict

    def get_contents_of_author(self, author_link):
        soup = utils.make_a_soup(author_link)
        nav_tag = soup.find('section', id='list-nav-contents')
        author_contents = self.parse_ul(nav_tag)
        return(author_contents)

    def parse_ul(self, section_tag):
        ul_tag = section_tag.findAll('ul')
        for ul in ul_tag:
            if ul.ul is not None:
                self.parse_ul(ul)
            else:
                li_tag = ul.findAll('li')
                for li in li_tag:
                    if li.a:
                        self.content_links.update({li.a.get_text(strip=True):li.a['href']})
        return self.content_links

    def scrape_content_verses(self, author:str, header:str, link:str):
        soup = utils.make_a_soup(link)
        verses = soup.findAll('p',class_='verse')

        author_folder = current_path / 'kalanjiyam' / author
        if not Path.is_dir(author_folder): 
            Path.mkdir(author_folder)

        if verses:
            file_name = f'{author_folder / header}.txt'
            with open(file_name,'a') as file:
                file.write(f'{link} \n\n')

                for verse in verses:
                    verse = re.sub(r"'|\"", '', verse.get_text(strip=True))
                    file.write(f'{verse}\n')

    def scrape_kalanjiyam(self):
        author_links = self.get_list_of_authors()

        kalanjiyam_folder = current_path / 'kalanjiyam'
        if not Path.is_dir(kalanjiyam_folder): 
            Path.mkdir(kalanjiyam_folder)
        
        for author, link in author_links.items():
            self.content_links = dict()
            content_links = self.get_contents_of_author(link)

            for content_header, content_link in content_links.items():
                self.scrape_content_verses(author, content_header, content_link)


scraper = Kalanjiyam()
scraper.scrape_kalanjiyam()

        