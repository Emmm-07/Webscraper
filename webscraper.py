from bs4 import BeautifulSoup
import requests

page_to_scrape = requests.get("https://ww3.tinyzone.org/")
soup = BeautifulSoup(page_to_scrape.text,"html.parser")

movies = soup.findAll("a",attrs={"class":"film-poster-ahref"})

print("Trending Movies of 2024:")
for movie in movies:
    print(f"{movie.get('title')} - {movie.get('href')}")            #To return only the href attribute


# quotes = soup.findAll("span",attrs={"class":"text"})
# authors = soup.findAll("small",attrs={"class":"author"})

# for quote in quotes:
#     print(quote.text)                 #To return only the text content

# for author in authors:
#     print(author.text)