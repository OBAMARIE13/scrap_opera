import requests
from bs4 import BeautifulSoup



def scrap_nom(current_page=None):

    def get_detail(detail_url):
        detail = ""
        reponse = requests.get(detail_url, headers=headers)
        if reponse.ok:
            soup = BeautifulSoup(reponse.text, "html.parser")
            detail = soup.find('section', {'id': 'block-system-main'})
        return detail

    if current_page:
        url = f"https://news.un.org/fr/features?page={current_page}"
    else:
        url = "https://news.un.org/fr/features"

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    reponse = requests.get(url, headers=headers) 
    bloc = []

    if reponse.ok:

        soup = BeautifulSoup(reponse.text, "html.parser")
        section = soup.find('section', {'id': 'block-system-main'})

        contents = list(section.findAll('div', {'class': 'views-row'}))

        if len(contents) == 0: return

        for content in contents:
            dic = {}

            title_ = content.find('h1', {'class': 'story-title'})
            title_a = title_.find('a')
            picture = content.find('img', {'class': 'img-responsive'})
            date_publication_ = content.find('span', {'class': 'date-display-single'})
            category_ = content.find('div', {'class': 'topics'})

            dic['title'] = title_.text
            dic['link_detail'] = "https://news.un.org" + title_a['href']
            dic['src_picture'] = picture['src']
            dic['date_publication'] = date_publication_.text
            dic['category'] = category_.text

            dic['description'] = get_detail(dic['link_detail'])
            
            bloc.append(dic)
        
        current_page = (current_page + 1) if current_page else 1

        scrap_nom(current_page=current_page)
            

if __name__ == '__main__':
    scrap_nom()