from bs4 import BeautifulSoup
import requests,sys
import pandas as pd
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
URL='http://www.imdb.com/chart/top/'

HEADER = { "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"}
source=requests.get(URL,headers=HEADER)

with open('saving.html', 'wb+') as f:
    f.write(source.content)
with open('saving.html', 'rb') as f:
    soup=BeautifulSoup(f.read(),'html.parser')


movies=soup.find('ul',role='presentation').find_all('li')

print(len(movies))

list=[]

for movie in movies:
    name=movie.find('h3',class_='ipc-title__text').text.split('.')[1]
    rank=name.split('.')[0]
    sec_line=movie.find('div',class_='sc-b189961a-7 btCcOY cli-title-metadata').text
    year=sec_line[0:4]
    duration=sec_line[4:10]
    Rating=sec_line[10:]
    Star_rating=movie.find('span',class_='ipc-rating-star--rating').text
    Vote_Count=movie.find('span',class_='ipc-rating-star--voteCount').text[2:-1]
    dict={'rank':rank,
          'name':name,
          
          'year':year,
          'duration':duration,
          'Rating':Rating,
          'Stars':Star_rating,
          'Votes':Vote_Count}
    list.append(dict)

#df=pd.DataFrame(list)
#df.to_csv("Top 250 MoviesIMDB.csv",index=False)

    
    