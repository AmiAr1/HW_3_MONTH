import requests
from bs4 import BeautifulSoup

URL = "https://doramy.top/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="item col-lg-2 col-sm-3 col-6")
    news = []
    for item in items:
        news.append({
            'title': item.find("span").getText(),
<<<<<<< HEAD
            "link": item.find("a", class_="card-img-overlay").get("href"),
            "image": item.find('img', class_="card-img").get("src"),
            'text': item.find("a", class_="card-img-overlay").get_text()
=======
            "link":item.find("a", class_="card-img-overlay").get("href"),
            "image": item.find('img', class_="card-img").get("src"),
            'text':item.find("a",class_="card-img-overlay").get_text()

>>>>>>> fcf4af38bfc263dfead10c03931086fa6aa1198d

        })
    return news

# html = get_html(URL)
# print(get_data(html.text))



# html = get_html(URL)
# print(get_data(html.text))


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = get_data(html.text)
        return answer
    else:
        raise Exception("Error in parset")