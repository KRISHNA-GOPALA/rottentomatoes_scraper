import requests
from bs4 import BeautifulSoup
import xlwt


# Create a new Workbook
workbook = xlwt.Workbook(encoding='utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'movie_url')
table.write(0, 2, 'movie_name')
table.write(0, 3, 'movie_introduction')

line = 1
url = "https://www.rottentomatoes.com/top/bestofrt/"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
}

try:
    f = requests.get(url, headers=headers)
    soup = BeautifulSoup(f.content, 'html.parser')
    movies = soup.find('table', {'class': 'table'}).find_all('a')
    
    for num, anchor in enumerate(movies, 1):
        movie_url = 'https://www.rottentomatoes.com' + anchor['href']
        movie_f = requests.get(movie_url, headers=headers)
        movie_soup = BeautifulSoup(movie_f.content, 'html.parser')
        movie_content = movie_soup.find('div', {'class': 'movie_synopsis clamp clamp-6 js-clamp'})
        
        print(num, movie_url, '\n', 'Movie:', anchor.string.strip())
        print('Movie info:', movie_content.text.strip())
        
        table.write(line, 0, num)
        table.write(line, 1, movie_url)
        table.write(line, 2, anchor.string.strip())
        table.write(line, 3, movie_content.text.strip())
        
        line += 1

except Exception as e:
    print("An error occurred:", str(e))

workbook.save('movies_top100.xls')
